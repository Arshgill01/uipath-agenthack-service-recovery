from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from service_recovery_core.evals import build_audit_bundle, build_evidence_packet_html, build_uipath_payload


CORE_SCENARIOS = ("E-002", "E-004")

EXPECTED_PROOF = {
    "E-002": {
        "case_id": "CASE-BG-MISSING",
        "recommended_next_stage": "closure_candidate",
        "decision": "override_recommendation",
        "to_stage": "verify_telemetry",
        "block_reason": "missing_authoritative_signal",
        "agent_event_id": "AIE-E002",
    },
    "E-004": {
        "case_id": "CASE-BG-CONTRA",
        "recommended_next_stage": "closure_candidate",
        "decision": "require_human_review",
        "to_stage": "human_review",
        "block_reason": "source_contradiction",
        "agent_event_id": "AIE-E004",
    },
}


def build_demo_proof_artifacts(
    output_dir: Path,
    *,
    scenario_ids: tuple[str, ...] = CORE_SCENARIOS,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    scenarios = []
    for scenario_id in scenario_ids:
        scenarios.append(_write_scenario_artifacts(output_dir, scenario_id))

    manifest = {
        "artifact_type": "service-recovery-demo-proof-manifest",
        "scenarios": scenarios,
    }
    _write_json(output_dir / "demo_proof_manifest.json", manifest)
    return manifest


def verify_demo_proof_artifacts(output_dir: Path, *, scenario_ids: tuple[str, ...] = CORE_SCENARIOS) -> list[str]:
    errors: list[str] = []
    for scenario_id in scenario_ids:
        expected = EXPECTED_PROOF[scenario_id]
        audit_path = output_dir / f"service_recovery_audit_bundle_{scenario_id.replace('-', '')}.json"
        payload_path = output_dir / f"action_payload_{scenario_id.replace('-', '')}.json"
        html_path = output_dir / f"evidence_packet_{scenario_id.replace('-', '')}.html"

        if not audit_path.exists():
            errors.append(f"{scenario_id}: missing audit bundle {audit_path}")
            continue
        if not payload_path.exists():
            errors.append(f"{scenario_id}: missing Action Center payload {payload_path}")
            continue
        if not html_path.exists():
            errors.append(f"{scenario_id}: missing evidence packet HTML {html_path}")
            continue

        audit_bundle = json.loads(audit_path.read_text(encoding="utf-8"))
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
        raw_agent = json.loads(payload["RawAgentRecommendation"])
        policy_decision = json.loads(payload["PolicyDecisionJson"])
        html = html_path.read_text(encoding="utf-8")

        errors.extend(_verify_audit_bundle(scenario_id, expected, audit_bundle))
        errors.extend(_verify_payload(scenario_id, expected, raw_agent, policy_decision))
        errors.extend(_verify_html(scenario_id, expected, html))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate and verify the demo-safe 2A/2B proof artifacts.")
    parser.add_argument(
        "--output-dir",
        default="docs/demo/artifacts",
        help="Directory for generated payload, audit bundle, HTML packet, and manifest artifacts.",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Verify existing artifacts without regenerating them.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if not args.verify_only:
        manifest = build_demo_proof_artifacts(output_dir)
        print(json.dumps(manifest, indent=2, sort_keys=True))

    errors = verify_demo_proof_artifacts(output_dir)
    if errors:
        print(json.dumps({"status": "failed", "errors": errors}, indent=2, sort_keys=True))
        return 1

    print(json.dumps({"status": "passed", "verified_scenarios": list(CORE_SCENARIOS)}, indent=2, sort_keys=True))
    return 0


def _write_scenario_artifacts(output_dir: Path, scenario_id: str) -> dict[str, Any]:
    compact_id = scenario_id.replace("-", "")
    payload = build_uipath_payload(scenario_id)
    audit_bundle = build_audit_bundle(scenario_id)
    html = build_evidence_packet_html(scenario_id)

    payload_path = output_dir / f"action_payload_{compact_id}.json"
    audit_path = output_dir / f"service_recovery_audit_bundle_{compact_id}.json"
    html_path = output_dir / f"evidence_packet_{compact_id}.html"

    _write_json(payload_path, payload)
    _write_json(audit_path, audit_bundle)
    html_path.write_text(html, encoding="utf-8")

    expected = EXPECTED_PROOF[scenario_id]
    return {
        "scenario_id": scenario_id,
        "case_id": expected["case_id"],
        "payload_path": str(payload_path),
        "audit_bundle_path": str(audit_path),
        "evidence_packet_html_path": str(html_path),
        "recommended_next_stage": expected["recommended_next_stage"],
        "decision": expected["decision"],
        "to_stage": expected["to_stage"],
        "block_reason": expected["block_reason"],
    }


def _verify_audit_bundle(scenario_id: str, expected: dict[str, str], audit_bundle: dict[str, Any]) -> list[str]:
    raw_agent = audit_bundle["agent_interpretation_event"]
    policy_decision = audit_bundle["policy_decision_event"]
    checks = {
        "case_id": audit_bundle["case_id"],
        "agent_event_id": raw_agent["event_id"],
        "recommended_next_stage": raw_agent["recommended_next_stage"],
        "policy_links_to": policy_decision["links_to"],
        "decision": policy_decision["decision"],
        "from_recommended_stage": policy_decision["from_recommended_stage"],
        "to_stage": policy_decision["to_stage"],
        "block_reason": policy_decision["block_reason"],
    }
    return _expected_errors(scenario_id, expected, checks)


def _verify_payload(
    scenario_id: str,
    expected: dict[str, str],
    raw_agent: dict[str, Any],
    policy_decision: dict[str, Any],
) -> list[str]:
    checks = {
        "case_id": raw_agent["case_id"],
        "agent_event_id": raw_agent["event_id"],
        "recommended_next_stage": raw_agent["recommended_next_stage"],
        "policy_links_to": policy_decision["links_to"],
        "decision": policy_decision["decision"],
        "from_recommended_stage": policy_decision["from_recommended_stage"],
        "to_stage": policy_decision["to_stage"],
        "block_reason": policy_decision["block_reason"],
    }
    return _expected_errors(scenario_id, expected, checks)


def _verify_html(scenario_id: str, expected: dict[str, str], html: str) -> list[str]:
    missing = [
        value
        for value in (
            expected["case_id"],
            expected["agent_event_id"],
            expected["recommended_next_stage"],
            expected["decision"],
            expected["to_stage"],
            expected["block_reason"],
            "Raw agent interpretation",
            "Final policy decision",
        )
        if value not in html
    ]
    return [f"{scenario_id}: evidence packet HTML missing {value}" for value in missing]


def _expected_errors(scenario_id: str, expected: dict[str, str], checks: dict[str, str]) -> list[str]:
    expected_checks = {
        "case_id": expected["case_id"],
        "agent_event_id": expected["agent_event_id"],
        "recommended_next_stage": expected["recommended_next_stage"],
        "policy_links_to": expected["agent_event_id"],
        "decision": expected["decision"],
        "from_recommended_stage": expected["recommended_next_stage"],
        "to_stage": expected["to_stage"],
        "block_reason": expected["block_reason"],
    }
    return [
        f"{scenario_id}: expected {name}={expected_value}, observed {checks.get(name)}"
        for name, expected_value in expected_checks.items()
        if checks.get(name) != expected_value
    ]


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
