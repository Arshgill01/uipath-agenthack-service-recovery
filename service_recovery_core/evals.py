from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from service_recovery_core.agent_validator import validate_agent_interpretation
from service_recovery_core.audit_bundle import build_case_audit_bundle
from service_recovery_core.data_fabric_record import build_data_fabric_record
from service_recovery_core.evidence_packet_view import render_evidence_packet_html
from service_recovery_core.fixtures import load_scenarios
from service_recovery_core.policy import decide_policy
from service_recovery_core.state_machine import apply_policy_decision
from service_recovery_core.uipath_payload import build_action_center_payload


def run_eval_suite() -> dict[str, Any]:
    scenario_results = []
    for scenario in load_scenarios().values():
        agent_validation = validate_agent_interpretation(scenario["agent_interpretation"])
        policy_decision = decide_policy(
            scenario["case"],
            scenario["evidence"],
            scenario["agent_interpretation"],
        )
        transition = apply_policy_decision(
            scenario["case"],
            scenario["agent_interpretation"],
            policy_decision,
            event_id=f"PDE-{scenario['scenario_id']}",
        )

        expected = scenario["expected"]
        assertions = [
            agent_validation["valid"] == expected["agent_valid"],
            policy_decision["decision"] == expected["policy_decision"],
            policy_decision["to_stage"] == expected["target_stage"],
            policy_decision["derived_evidence_state"] == expected["derived_evidence_state"],
            set(expected["reason_codes"]).issubset(set(policy_decision["reason_codes"])),
        ]
        if "closure_allowed" in expected:
            assertions.append(policy_decision["closure_allowed"] == expected["closure_allowed"])
        if "failure_category" in expected:
            assertions.append(scenario["agent_interpretation"]["failure_category"] == expected["failure_category"])
        if scenario["scenario_id"] == "E-009":
            assertions.extend(_override_persistence_assertions(transition))

        passed = all(assertions)
        scenario_results.append(
            {
                "scenario_id": scenario["scenario_id"],
                "passed": passed,
                "agent_valid": agent_validation["valid"],
                "agent_errors": agent_validation["errors"],
                "policy_decision": policy_decision,
                "policy_event": transition["policy_event"],
                "usefulness_incident": _usefulness_incident(scenario, policy_decision),
            }
        )

    total = len(scenario_results)
    passed_count = sum(1 for result in scenario_results if result["passed"])
    return {
        "summary": {
            "total": total,
            "passed": passed_count,
            "failed": total - passed_count,
            "schema_validity_rate": _rate(result["agent_valid"] for result in scenario_results),
            "eval_pass_rate": passed_count / total if total else 0,
            "policy_version": "dp-v1",
        },
        "results": scenario_results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=None, help="Optional JSON output path.")
    parser.add_argument(
        "--uipath-payload-scenario",
        default=None,
        help="Optional scenario ID to export as generated Action Center input payload.",
    )
    parser.add_argument(
        "--audit-bundle-scenario",
        default=None,
        help="Optional scenario ID to export as the custom one-query case audit bundle.",
    )
    parser.add_argument(
        "--evidence-packet-html-scenario",
        default=None,
        help="Optional scenario ID to export as a static reviewer evidence-packet HTML file.",
    )
    parser.add_argument(
        "--data-fabric-record-scenario",
        default=None,
        help="Optional scenario ID to export as a Data Fabric audit record body.",
    )
    parser.add_argument(
        "--llm-result-evidence-packet",
        default=None,
        help="Optional governed LLM demo result JSON to export as a static reviewer evidence-packet HTML file.",
    )
    args = parser.parse_args()
    if args.uipath_payload_scenario:
        payload = build_uipath_payload(args.uipath_payload_scenario)
        rendered_payload = json.dumps(payload, indent=2, sort_keys=True)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rendered_payload + "\n", encoding="utf-8")
        print(rendered_payload)
        return 0
    if args.audit_bundle_scenario:
        bundle = build_audit_bundle(args.audit_bundle_scenario)
        rendered_bundle = json.dumps(bundle, indent=2, sort_keys=True)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rendered_bundle + "\n", encoding="utf-8")
        print(rendered_bundle)
        return 0
    if args.evidence_packet_html_scenario:
        html = build_evidence_packet_html(args.evidence_packet_html_scenario)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(html, encoding="utf-8")
        print(html)
        return 0
    if args.data_fabric_record_scenario:
        if args.output and args.output.endswith(".csv"):
            import csv
            record = build_audit_record(args.data_fabric_record_scenario, for_csv=True)
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(record.keys()))
                writer.writeheader()
                writer.writerow(record)
            print(f"Exported Data Fabric CSV record to {args.output}")
            return 0
        else:
            record = build_audit_record(args.data_fabric_record_scenario, for_csv=False)
            rendered_record = json.dumps(record, indent=2, sort_keys=True)
            if args.output:
                output_path = Path(args.output)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(rendered_record + "\n", encoding="utf-8")
            print(rendered_record)
            return 0
    if args.llm_result_evidence_packet:
        html = build_llm_result_evidence_packet_html(Path(args.llm_result_evidence_packet))
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(html, encoding="utf-8")
        print(html)
        return 0

    results = run_eval_suite()
    rendered = json.dumps(results, indent=2, sort_keys=True)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if results["summary"]["failed"] == 0 else 1


def build_uipath_payload(scenario_id: str) -> dict[str, str]:
    scenario, transition = _scenario_transition(scenario_id)
    return build_action_center_payload(scenario["case"], scenario["evidence"], transition)


def build_audit_bundle(scenario_id: str) -> dict[str, Any]:
    scenario, transition = _scenario_transition(scenario_id)
    return build_case_audit_bundle(scenario["case"], scenario["evidence"], transition)


def build_evidence_packet_html(scenario_id: str) -> str:
    return render_evidence_packet_html(build_audit_bundle(scenario_id))


def build_audit_record(scenario_id: str, for_csv: bool = False) -> dict[str, Any]:
    live_refs = {
        "E-002": {
            "source_case_instance_key": "3af41e1d-8b04-4eba-aa5e-a95c5c673730",
            "source_task_id": "4300080",
            "package_version": "1.0.4",
        },
        "E-004": {
            "source_case_instance_key": "60e52ca5-6891-45b4-9e98-e1b08a984f06",
            "source_task_id": "4300219",
            "package_version": "1.0.5",
        },
    }
    return build_data_fabric_record(
        build_audit_bundle(scenario_id),
        scenario_id=scenario_id,
        for_csv=for_csv,
        **live_refs.get(scenario_id, {}),
    )


def build_llm_result_evidence_packet_html(result_path: Path) -> str:
    result = json.loads(result_path.read_text(encoding="utf-8"))
    scenario_id = result["scenario_id"]
    scenario = load_scenarios()[scenario_id]
    transition = apply_policy_decision(
        scenario["case"],
        result["agent_interpretation_event"],
        result["policy_decision_event"],
        event_id=f"PDE-LLM-{scenario_id}",
    )
    return render_evidence_packet_html(build_case_audit_bundle(scenario["case"], scenario["evidence"], transition))


def _scenario_transition(scenario_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    scenarios = load_scenarios()
    if scenario_id not in scenarios:
        raise KeyError(f"unknown scenario_id: {scenario_id}")
    scenario = scenarios[scenario_id]
    policy_decision = decide_policy(
        scenario["case"],
        scenario["evidence"],
        scenario["agent_interpretation"],
    )
    transition = apply_policy_decision(
        scenario["case"],
        scenario["agent_interpretation"],
        policy_decision,
        event_id=f"PDE-{scenario_id}",
    )
    return scenario, transition


def _override_persistence_assertions(transition: dict[str, Any]) -> list[bool]:
    agent_event = transition["agent_event"]
    policy_event = transition["policy_event"]
    return [
        agent_event["recommended_next_stage"] == "closure_candidate",
        policy_event["agent_event_id"] == agent_event["event_id"],
        policy_event["decision"] == "override_recommendation",
        policy_event["from_recommended_stage"] == "closure_candidate",
        policy_event["to_stage"] == "verify_telemetry",
        "missing_authoritative_signal" in policy_event["reason_codes"],
    ]


def _usefulness_incident(scenario: dict[str, Any], policy_decision: dict[str, Any]) -> dict[str, Any] | None:
    if scenario["scenario_id"] != "E-008":
        return None
    return {
        "incident_type": "agent_usefulness_degradation",
        "trigger": "low_confidence_despite_sufficient_signal",
        "sample_case_ids": [scenario["case"]["case_id"]],
        "reason_codes": policy_decision["reason_codes"],
        "recommended_owner_action": "review_interpretation_policy_or_input_quality",
    }


def _rate(values: Any) -> float:
    materialized = list(values)
    if not materialized:
        return 0
    return sum(1 for value in materialized if value) / len(materialized)


if __name__ == "__main__":
    raise SystemExit(main())
