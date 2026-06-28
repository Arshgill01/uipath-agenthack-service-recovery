import json
import tempfile
import unittest
from pathlib import Path

from service_recovery_core.demo_proof import build_demo_proof_artifacts
from service_recovery_core.evals import build_policy_improvement_artifact_for_scenario
from service_recovery_core.proof_index import build_proof_index, verify_proof_index


REPO_ROOT = Path(__file__).resolve().parents[1]


class ProofIndexTests(unittest.TestCase):
    def test_builds_judge_facing_index_from_existing_artifacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_dir = Path(temp_dir)
            build_demo_proof_artifacts(artifact_dir)
            _write_required_support_artifacts(artifact_dir)

            index = build_proof_index(artifact_dir)
            errors = verify_proof_index(artifact_dir)
            html = (artifact_dir / "proof_index.html").read_text(encoding="utf-8")

            self.assertEqual(errors, [])
            self.assertEqual([beat["scenario_id"] for beat in index["beats"]], ["E-002", "E-004", "E-003", "E-008"])
            self.assertIn("Judge-facing proof index", html)
            self.assertIn("Claim boundaries", html)
            self.assertIn("judge-readable support surface", html)
            self.assertIn("not a replacement for UiPath Maestro Case", html)
            self.assertIn("closure_candidate", html)
            self.assertIn("verify_telemetry", html)
            self.assertIn("human_review", html)
            self.assertIn("pending_human_approval", html)
            self.assertIn("not_promoted", html)

    def test_verifier_reports_missing_source_artifact(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_dir = Path(temp_dir)
            build_demo_proof_artifacts(artifact_dir)
            _write_required_support_artifacts(artifact_dir)
            build_proof_index(artifact_dir)
            (artifact_dir / "policy_improvement_E008.json").unlink()

            errors = verify_proof_index(artifact_dir)

            self.assertIn("missing source artifact", errors[0])
            self.assertIn("policy_improvement_E008.json", errors[0])


def _write_required_support_artifacts(artifact_dir: Path) -> None:
    source = REPO_ROOT / "docs/demo/artifacts/llm_interpreter_E003_adversarial_live.json"
    (artifact_dir / source.name).write_bytes(source.read_bytes())
    (artifact_dir / "evidence_packet_E003_adversarial_live.html").write_text(
        "<!doctype html><title>E-003</title>",
        encoding="utf-8",
    )
    artifact = build_policy_improvement_artifact_for_scenario("E-008")
    (artifact_dir / "policy_improvement_E008.json").write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    unittest.main()
