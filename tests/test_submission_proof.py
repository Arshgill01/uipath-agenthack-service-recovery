import copy
import json
import tempfile
import unittest
from pathlib import Path

from service_recovery_core.submission_proof import CLAIM_BOUNDARY_DOCS, REQUIRED_DOC_CLAIMS, verify_submission_proof


REPO_ROOT = Path(__file__).resolve().parents[1]


class SubmissionProofTests(unittest.TestCase):
    def test_current_submission_proof_contract_passes(self):
        errors = verify_submission_proof(REPO_ROOT)

        self.assertEqual(errors, [])

    def test_reports_policy_improvement_auto_promotion(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_dir = Path(temp_dir)
            _copy_required_artifacts(artifact_dir)
            artifact_path = artifact_dir / "policy_improvement_E008.json"
            artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
            artifact["promotion_status"] = "promoted"
            artifact["forbidden_actions"] = [
                action for action in artifact["forbidden_actions"] if action != "auto_promote_policy"
            ]
            artifact_path.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")

            errors = verify_submission_proof(REPO_ROOT, artifact_dir)

            self.assertIn("policy_improvement_E008.json: failed proof check promotion_status", errors)
            self.assertIn("policy_improvement_E008.json: failed proof check forbids_auto_promote", errors)

    def test_reports_adversarial_route_drift(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_dir = Path(temp_dir)
            _copy_required_artifacts(artifact_dir)
            artifact_path = artifact_dir / "llm_interpreter_E003_adversarial_live.json"
            artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
            mutated = copy.deepcopy(artifact)
            mutated["policy_decision_event"]["to_stage"] = "verify_telemetry"
            mutated["policy_decision_event"]["reason_codes"] = ["stale_authoritative_signal"]
            artifact_path.write_text(json.dumps(mutated, indent=2, sort_keys=True) + "\n", encoding="utf-8")

            errors = verify_submission_proof(REPO_ROOT, artifact_dir)

            self.assertIn("llm_interpreter_E003_adversarial_live.json: failed proof check policy.to_stage", errors)
            self.assertIn(
                "llm_interpreter_E003_adversarial_live.json: failed proof check policy.reason_code",
                errors,
            )

    def test_reports_action_payload_policy_link_drift(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_dir = Path(temp_dir)
            _copy_required_artifacts(artifact_dir)
            artifact_path = artifact_dir / "action_payload_E004.json"
            payload = json.loads(artifact_path.read_text(encoding="utf-8"))
            policy = json.loads(payload["PolicyDecisionJson"])
            policy["links_to"] = "AIE-UNLINKED"
            payload["PolicyDecisionJson"] = json.dumps(policy, sort_keys=True, separators=(",", ":"))
            artifact_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

            errors = verify_submission_proof(REPO_ROOT, artifact_dir)

            self.assertIn("action_payload_E004.json: failed proof check policy.links_to_raw_agent", errors)

    def test_reports_custom_packet_caveat_drift(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_dir = Path(temp_dir)
            _copy_required_artifacts(artifact_dir)
            artifact_path = artifact_dir / "evidence_packet_E002.html"
            html = artifact_path.read_text(encoding="utf-8")
            artifact_path.write_text(
                html.replace("generated Action Center page hid or mislabeled proof-critical fields", ""),
                encoding="utf-8",
            )

            errors = verify_submission_proof(REPO_ROOT, artifact_dir)

            self.assertIn(
                "evidence_packet_E002.html: missing evidence-packet proof string "
                "'generated Action Center page hid or mislabeled proof-critical fields'",
                errors,
            )

    def test_reports_automated_test_cloud_overclaim(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = _copy_required_proof_tree(Path(temp_dir))
            readme_path = repo_root / "README.md"
            readme_path.write_text(
                readme_path.read_text(encoding="utf-8")
                + "\nAutomated Test Cloud execution passed for E-001 through E-009.\n",
                encoding="utf-8",
            )

            errors = verify_submission_proof(repo_root, repo_root / "docs/demo/artifacts")

            self.assertTrue(
                any(
                    error.startswith("README.md:")
                    and "forbidden overclaim automated_test_cloud_execution" in error
                    for error in errors
                ),
                errors,
            )

    def test_reports_llm_closure_authority_overclaim(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = _copy_required_proof_tree(Path(temp_dir))
            brief_path = repo_root / "docs/submission/SUBMISSION_BRIEF.md"
            brief_path.write_text(
                brief_path.read_text(encoding="utf-8").replace(
                    "## Evidence Links\n",
                    "## Evidence Links\n\nGemini owns final closure for the telecom recovery case.\n",
                    1,
                ),
                encoding="utf-8",
            )

            errors = verify_submission_proof(repo_root, repo_root / "docs/demo/artifacts")

            self.assertTrue(
                any(
                    error.startswith(
                        "docs/submission/SUBMISSION_BRIEF.md:"
                    )
                    and "forbidden overclaim llm_or_codex_closure_authority" in error
                    for error in errors
                ),
                errors,
            )

    def test_do_not_claim_sections_do_not_trip_overclaim_scanner(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = _copy_required_proof_tree(Path(temp_dir))
            checklist_path = repo_root / "docs/submission/READINESS_CHECKLIST.md"
            checklist_path.write_text(
                checklist_path.read_text(encoding="utf-8")
                + "\n## Do Not Claim\n\n- Automated Test Cloud execution passed.\n",
                encoding="utf-8",
            )

            errors = verify_submission_proof(repo_root, repo_root / "docs/demo/artifacts")

            self.assertEqual(errors, [])


def _copy_required_artifacts(target_dir: Path) -> None:
    source_dir = REPO_ROOT / "docs/demo/artifacts"
    target_dir.mkdir(parents=True, exist_ok=True)
    for source_path in source_dir.iterdir():
        if source_path.is_file():
            target_path = target_dir / source_path.name
            target_path.write_bytes(source_path.read_bytes())


def _copy_required_proof_tree(target_root: Path) -> Path:
    source_artifacts = REPO_ROOT / "docs/demo/artifacts"
    target_artifacts = target_root / "docs/demo/artifacts"
    target_artifacts.mkdir(parents=True, exist_ok=True)
    for source_path in source_artifacts.iterdir():
        if source_path.is_file():
            (target_artifacts / source_path.name).write_bytes(source_path.read_bytes())

    for relative_path in sorted(set(REQUIRED_DOC_CLAIMS) | set(CLAIM_BOUNDARY_DOCS)):
        source_path = REPO_ROOT / relative_path
        target_path = target_root / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(source_path.read_bytes())

    return target_root


if __name__ == "__main__":
    unittest.main()
