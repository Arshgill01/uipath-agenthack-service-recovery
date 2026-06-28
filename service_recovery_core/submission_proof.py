from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


CORE_EXPECTED = {
    "E-002": {
        "case_id": "CASE-BG-MISSING",
        "recommended_next_stage": "closure_candidate",
        "decision": "override_recommendation",
        "to_stage": "verify_telemetry",
        "block_reason": "missing_authoritative_signal",
    },
    "E-004": {
        "case_id": "CASE-BG-CONTRA",
        "recommended_next_stage": "closure_candidate",
        "decision": "require_human_review",
        "to_stage": "human_review",
        "block_reason": "source_contradiction",
    },
}

REQUIRED_ARTIFACTS = (
    "action_payload_E002.json",
    "action_payload_E004.json",
    "service_recovery_audit_bundle_E002.json",
    "service_recovery_audit_bundle_E004.json",
    "evidence_packet_E002.html",
    "evidence_packet_E002_desktop.png",
    "evidence_packet_E004.html",
    "evidence_packet_E004_desktop.png",
    "demo_proof_manifest.json",
    "proof_index.html",
    "llm_interpreter_E003_live.json",
    "llm_interpreter_E003_adversarial_live.json",
    "evidence_packet_E003_adversarial_live.html",
    "evidence_packet_E003_adversarial_desktop.png",
    "evidence_packet_E003_adversarial_mobile.png",
    "policy_improvement_E008.json",
)

REQUIRED_DOC_CLAIMS = {
    "README.md": (
        "UiPath AgentHack Maestro Case",
        "Codex as the coding agent",
        "scripts/run_submission_check.sh",
    ),
    "docs/submission/SUBMISSION_BRIEF.md": (
        "Primary track: UiPath Maestro Case",
        "Coding-agent bonus: Codex",
        "not automated Test Cloud execution",
        "Native Maestro Case history is not claimed",
    ),
    "docs/submission/TRACK_SELECTION_DECISION.md": (
        "Decision: submit the project under **UiPath Maestro Case**",
        "Test Manager validation is manual representation",
        "Codex was used as the coding agent",
    ),
    "docs/submission/CODING_AGENT_PROOF_LOG.md": (
        "Coding agent used: Codex",
        "scripts/run_submission_check.sh",
        "UiPath remains the runtime orchestration and governance layer",
    ),
    "docs/product/FEEDBACK_SURVEY_COPY_READY.md": (
        "Add a Maestro Case human-review readiness and preflight path",
        "Automated Test Cloud execution",
        "Generated Action Center UI is final-demo ready",
        "Native Case history alone passes the domain audit gate",
    ),
    "docs/product/FEEDBACK_AWARD_APPENDIX.md": (
        "Maestro Case human-review readiness/preflight",
        "Do not claim automated Test Cloud execution",
        "Do not claim generated Action Center UI is final-demo ready",
        "Do not claim native Case history alone passes",
    ),
    "docs/validation/ACTION_CENTER_UI_REPAIR_ASSESSMENT.md": (
        "fresh package `1.0.6` Case Instance then created task `4333536`",
        "Action Center runtime still rendered `Unnamed String 1:`",
        "custom evidence packet as the judge-facing surface",
    ),
    "docs/validation/artifacts/2026-06-27/product_feedback_action_binding_probe.md": (
        "Existing read-only evidence confirms the proof-critical fields are present",
        "fresh runtime recheck task `4333536` used `SystemName`",
        "custom evidence packet/Data Fabric/bucket audit surfaces",
    ),
}


def verify_submission_proof(repo_root: Path, artifact_dir: Path | None = None) -> list[str]:
    root = repo_root.resolve()
    artifacts = _resolve_path(root, artifact_dir or Path("docs/demo/artifacts"))

    errors: list[str] = []
    errors.extend(_verify_required_files(root, artifacts))
    errors.extend(_verify_doc_claims(root))
    errors.extend(_verify_demo_manifest(root, artifacts))
    errors.extend(_verify_core_demo_artifacts(artifacts))
    errors.extend(_verify_proof_index_html(artifacts / "proof_index.html"))
    errors.extend(_verify_llm_artifact(artifacts / "llm_interpreter_E003_live.json", adversarial=False))
    errors.extend(_verify_llm_artifact(artifacts / "llm_interpreter_E003_adversarial_live.json", adversarial=True))
    errors.extend(_verify_policy_improvement_artifact(artifacts / "policy_improvement_E008.json"))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify final local submission proof artifacts and claim docs.")
    parser.add_argument("--repo-root", default=".", help="Repository root. Defaults to the current directory.")
    parser.add_argument(
        "--artifact-dir",
        default="docs/demo/artifacts",
        help="Demo artifact directory, relative to repo root unless absolute.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root)
    artifact_dir = Path(args.artifact_dir)
    errors = verify_submission_proof(repo_root, artifact_dir)
    if errors:
        print(json.dumps({"status": "failed", "errors": errors}, indent=2, sort_keys=True))
        return 1

    print(
        json.dumps(
            {
                "status": "passed",
                "artifact_dir": str(_resolve_path(repo_root.resolve(), artifact_dir)),
                "checked_artifacts": len(REQUIRED_ARTIFACTS),
                "checked_claim_docs": len(REQUIRED_DOC_CLAIMS),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def _verify_required_files(repo_root: Path, artifact_dir: Path) -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_DOC_CLAIMS:
        path = repo_root / relative_path
        if not path.exists():
            errors.append(f"missing required proof doc: {relative_path}")
    for artifact_name in REQUIRED_ARTIFACTS:
        path = artifact_dir / artifact_name
        if not path.exists():
            errors.append(f"missing required proof artifact: {path}")
        elif path.suffix.lower() == ".png" and path.stat().st_size <= 1024:
            errors.append(f"proof screenshot appears empty or truncated: {path}")
    return errors


def _verify_doc_claims(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for relative_path, required_strings in REQUIRED_DOC_CLAIMS.items():
        path = repo_root / relative_path
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        for required in required_strings:
            if required not in content:
                errors.append(f"{relative_path}: missing required claim string {required!r}")
    return errors


def _verify_demo_manifest(repo_root: Path, artifact_dir: Path) -> list[str]:
    manifest_path = artifact_dir / "demo_proof_manifest.json"
    if not manifest_path.exists():
        return []

    errors: list[str] = []
    manifest = _read_json(manifest_path)
    if manifest.get("artifact_type") != "service-recovery-demo-proof-manifest":
        errors.append("demo_proof_manifest.json: unexpected artifact_type")

    scenarios = manifest.get("scenarios")
    if not isinstance(scenarios, list):
        return errors + ["demo_proof_manifest.json: scenarios must be a list"]

    observed_ids = [scenario.get("scenario_id") for scenario in scenarios]
    expected_ids = list(CORE_EXPECTED)
    if observed_ids != expected_ids:
        errors.append(f"demo_proof_manifest.json: expected scenarios {expected_ids}, observed {observed_ids}")

    for scenario in scenarios:
        scenario_id = scenario.get("scenario_id")
        expected = CORE_EXPECTED.get(scenario_id)
        if not expected:
            continue
        for key, expected_value in expected.items():
            observed = scenario.get(key)
            if observed != expected_value:
                errors.append(
                    f"demo_proof_manifest.json: {scenario_id} expected {key}={expected_value}, observed {observed}"
                )
        for path_key in ("payload_path", "audit_bundle_path", "evidence_packet_html_path"):
            value = scenario.get(path_key)
            if not isinstance(value, str):
                errors.append(f"demo_proof_manifest.json: {scenario_id} missing {path_key}")
                continue
            if not _manifest_path(repo_root, value).exists():
                errors.append(f"demo_proof_manifest.json: {scenario_id} missing referenced {path_key}: {value}")
    return errors


def _verify_core_demo_artifacts(artifact_dir: Path) -> list[str]:
    errors: list[str] = []
    for scenario_id, expected in CORE_EXPECTED.items():
        compact_id = scenario_id.replace("-", "")
        payload_path = artifact_dir / f"action_payload_{compact_id}.json"
        audit_path = artifact_dir / f"service_recovery_audit_bundle_{compact_id}.json"
        html_path = artifact_dir / f"evidence_packet_{compact_id}.html"

        if payload_path.exists():
            payload = _read_json(payload_path)
            errors.extend(_verify_action_payload(payload_path.name, expected, payload))
        if audit_path.exists():
            audit_bundle = _read_json(audit_path)
            errors.extend(_verify_audit_bundle(audit_path.name, expected, audit_bundle))
        if html_path.exists():
            html = html_path.read_text(encoding="utf-8")
            errors.extend(_verify_evidence_packet_html(html_path.name, expected, html))
    return errors


def _verify_action_payload(prefix: str, expected: dict[str, str], payload: dict[str, Any]) -> list[str]:
    try:
        raw_agent = json.loads(payload["RawAgentRecommendation"])
        policy = json.loads(payload["PolicyDecisionJson"])
    except (KeyError, TypeError, json.JSONDecodeError) as error:
        return [f"{prefix}: failed to parse Action Center proof payload: {error}"]

    checks = {
        "raw_agent.case_id": raw_agent.get("case_id") == expected["case_id"],
        "raw_agent.recommended_next_stage": raw_agent.get("recommended_next_stage")
        == expected["recommended_next_stage"],
        "policy.links_to_raw_agent": policy.get("links_to") == raw_agent.get("event_id"),
        "policy.decision": policy.get("decision") == expected["decision"],
        "policy.from_recommended_stage": policy.get("from_recommended_stage")
        == expected["recommended_next_stage"],
        "policy.to_stage": policy.get("to_stage") == expected["to_stage"],
        "policy.block_reason": policy.get("block_reason") == expected["block_reason"],
    }
    return _failed_checks(prefix, checks)


def _verify_audit_bundle(prefix: str, expected: dict[str, str], audit_bundle: dict[str, Any]) -> list[str]:
    agent = audit_bundle.get("agent_interpretation_event", {})
    policy = audit_bundle.get("policy_decision_event", {})
    reviewer_packet = audit_bundle.get("reviewer_packet", {})
    evidence_state = audit_bundle.get("evidence_state", {})
    checks = {
        "case_id": audit_bundle.get("case_id") == expected["case_id"],
        "audit_contract_version": audit_bundle.get("audit_contract_version") == "service-recovery-audit-v1",
        "agent.recommended_next_stage": agent.get("recommended_next_stage") == expected["recommended_next_stage"],
        "policy.links_to_agent": policy.get("links_to") == agent.get("event_id"),
        "policy.decision": policy.get("decision") == expected["decision"],
        "policy.to_stage": policy.get("to_stage") == expected["to_stage"],
        "policy.block_reason": policy.get("block_reason") == expected["block_reason"],
        "evidence_state.block_reason": evidence_state.get("closure_block_reason") == expected["block_reason"],
        "reviewer_packet.rendering_status": reviewer_packet.get("rendering_status") == "structured_packet_ready",
        "reviewer_packet.raw_agent_recommendation": isinstance(
            reviewer_packet.get("raw_agent_recommendation"), dict
        ),
        "reviewer_packet.policy_decision": isinstance(reviewer_packet.get("policy_decision"), dict),
    }
    return _failed_checks(prefix, checks)


def _verify_evidence_packet_html(prefix: str, expected: dict[str, str], html: str) -> list[str]:
    required_strings = (
        "UiPath platform role",
        "generated Action Center page hid or mislabeled proof-critical fields",
        "Raw Agent Interpretation Event",
        "Linked Policy Decision Event",
        expected["recommended_next_stage"],
        expected["decision"],
        expected["to_stage"],
        expected["block_reason"],
    )
    return [f"{prefix}: missing evidence-packet proof string {value!r}" for value in required_strings if value not in html]


def _verify_llm_artifact(path: Path, *, adversarial: bool) -> list[str]:
    if not path.exists():
        return []

    errors: list[str] = []
    result = _read_json(path)
    prefix = path.name
    agent = result.get("agent_interpretation_event", {})
    policy = result.get("policy_decision_event", {})
    validation = result.get("agent_validation", {})

    expected_policy = {
        "decision": "require_human_review" if adversarial else "override_recommendation",
        "to_stage": "human_review" if adversarial else "verify_telemetry",
        "reason_code": "high_interpretation_disagreement" if adversarial else "stale_authoritative_signal",
    }
    checks = {
        "scenario_id": result.get("scenario_id") == "E-003",
        "agent_validation.valid": validation.get("valid") is True,
        "agent.recommended_next_stage": agent.get("recommended_next_stage") == "closure_candidate",
        "policy.agent_event_id": policy.get("agent_event_id") == agent.get("event_id"),
        "policy.closure_allowed": policy.get("closure_allowed") is False,
        "policy.decision": policy.get("decision") == expected_policy["decision"],
        "policy.to_stage": policy.get("to_stage") == expected_policy["to_stage"],
        "policy.reason_code": expected_policy["reason_code"] in policy.get("reason_codes", []),
    }
    errors.extend(_failed_checks(prefix, checks))

    if adversarial:
        disagreement = agent.get("adversarial_interpretation", {}).get("disagreement", {})
        threshold = disagreement.get("threshold")
        score = disagreement.get("disagreement_score")
        checks = {
            "disagreement.stage_match": disagreement.get("stage_match") is False,
            "disagreement.advocate_recommendation": disagreement.get("advocate_recommendation") == "closure_candidate",
            "disagreement.skeptic_recommendation": disagreement.get("skeptic_recommendation") == "verify_telemetry",
            "disagreement.score_crosses_threshold": isinstance(score, (int, float))
            and isinstance(threshold, (int, float))
            and score >= threshold,
        }
        errors.extend(_failed_checks(prefix, checks))
    return errors


def _verify_policy_improvement_artifact(path: Path) -> list[str]:
    if not path.exists():
        return []

    artifact = _read_json(path)
    checks = {
        "artifact_type": artifact.get("artifact_type") == "policy_improvement_case",
        "source_scenario_id": artifact.get("source_scenario_id") == "E-008",
        "approval_status": artifact.get("approval_status") == "pending_human_approval",
        "promotion_status": artifact.get("promotion_status") == "not_promoted",
        "active_case_policy_version_action": artifact.get("active_case_policy_version_action")
        == "active_cases_remain_pinned_until_explicit_migration_event",
        "current_interpretation_policy": artifact.get("current_policy_version", {}).get("interpretation_policy_version")
        == "ip-v1",
        "current_decision_policy": artifact.get("current_policy_version", {}).get("decision_policy_version") == "dp-v1",
        "proposed_interpretation_policy": artifact.get("proposed_next_version", {}).get(
            "interpretation_policy_version"
        )
        == "ip-v2-proposed",
        "decision_policy_not_promoted": artifact.get("proposed_next_version", {}).get("decision_policy_version")
        == "dp-v1",
        "forbids_auto_promote": "auto_promote_policy" in artifact.get("forbidden_actions", []),
    }
    return _failed_checks(path.name, checks)


def _verify_proof_index_html(path: Path) -> list[str]:
    if not path.exists():
        return []

    content = path.read_text(encoding="utf-8")
    checks = {
        "title": "Judge-facing proof index" in content,
        "claim_boundary": "Claim boundaries" in content,
        "support_not_replacement": "not a replacement for UiPath Maestro Case" in content,
        "missing_telemetry": "E-002" in content and "missing_authoritative_signal" in content,
        "contradiction": "E-004" in content and "source_contradiction" in content,
        "llm_adversarial": "E-003" in content and "high_interpretation_disagreement" in content,
        "learning_loop": "E-008" in content and "pending_human_approval" in content and "not_promoted" in content,
    }
    return _failed_checks(path.name, checks)


def _failed_checks(prefix: str, checks: dict[str, bool]) -> list[str]:
    return [f"{prefix}: failed proof check {name}" for name, passed in checks.items() if not passed]


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_path(repo_root: Path, path: Path) -> Path:
    return path if path.is_absolute() else repo_root / path


def _manifest_path(repo_root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else repo_root / path


if __name__ == "__main__":
    raise SystemExit(main())
