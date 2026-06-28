from __future__ import annotations

import argparse
import copy
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
                "policy_improvement_artifact": build_policy_improvement_artifact(
                    scenario,
                    policy_decision,
                    passed,
                ),
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
        "--data-fabric-field-style",
        choices=["snake", "pascal"],
        default="snake",
        help="Field naming style for Data Fabric record export.",
    )
    parser.add_argument(
        "--llm-result-evidence-packet",
        default=None,
        help="Optional governed LLM demo result JSON to export as a static reviewer evidence-packet HTML file.",
    )
    parser.add_argument(
        "--policy-improvement-artifact-scenario",
        default=None,
        help="Optional scenario ID to export as a governed policy-improvement artifact JSON file.",
    )
    parser.add_argument(
        "--policy-boundary-report",
        action="store_true",
        help="Export a deterministic hardening report for source authority, override persistence, fixture discipline, and confidence guardrails.",
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
            record = build_audit_record(
                args.data_fabric_record_scenario,
                for_csv=True,
                field_style=args.data_fabric_field_style,
            )
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(record.keys()))
                writer.writeheader()
                writer.writerow(record)
            print(f"Exported Data Fabric CSV record to {args.output}")
            return 0
        else:
            record = build_audit_record(
                args.data_fabric_record_scenario,
                for_csv=False,
                field_style=args.data_fabric_field_style,
            )
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
    if args.policy_improvement_artifact_scenario:
        artifact = build_policy_improvement_artifact_for_scenario(args.policy_improvement_artifact_scenario)
        rendered_artifact = json.dumps(artifact, indent=2, sort_keys=True)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rendered_artifact + "\n", encoding="utf-8")
        print(rendered_artifact)
        return 0
    if args.policy_boundary_report:
        report = build_policy_boundary_report()
        rendered_report = json.dumps(report, indent=2, sort_keys=True)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rendered_report + "\n", encoding="utf-8")
        print(rendered_report)
        return 0 if report["summary"]["failed"] == 0 else 1

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


def build_audit_record(scenario_id: str, for_csv: bool = False, field_style: str = "snake") -> dict[str, Any]:
    live_refs = {
        "E-002": {
            "source_case_instance_key": "3af41e1d-8b04-4eba-aa5e-a95c5c673730",
            "source_task_id": "4300080",
            "package_version": "1.0.4",
        },
        "E-004": {
            "source_case_instance_key": "9fc6fece-55ed-4fb2-b11a-6c96f7a3314e",
            "source_task_id": "4328396",
            "package_version": "1.0.6",
        },
    }
    return build_data_fabric_record(
        build_audit_bundle(scenario_id),
        scenario_id=scenario_id,
        for_csv=for_csv,
        field_style=field_style,
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


def build_policy_improvement_artifact_for_scenario(scenario_id: str) -> dict[str, Any]:
    scenarios = load_scenarios()
    if scenario_id not in scenarios:
        raise KeyError(f"unknown scenario_id: {scenario_id}")
    scenario = scenarios[scenario_id]
    policy_decision = decide_policy(
        scenario["case"],
        scenario["evidence"],
        scenario["agent_interpretation"],
    )
    expected = scenario["expected"]
    passed = (
        policy_decision["decision"] == expected["policy_decision"]
        and policy_decision["to_stage"] == expected["target_stage"]
        and set(expected["reason_codes"]).issubset(set(policy_decision["reason_codes"]))
    )
    return build_policy_improvement_artifact(scenario, policy_decision, passed)


def build_policy_improvement_artifact(
    scenario: dict[str, Any],
    policy_decision: dict[str, Any],
    eval_passed: bool,
) -> dict[str, Any] | None:
    incident = _usefulness_incident(scenario, policy_decision)
    if incident is None:
        return None

    current_decision_version = scenario["case"]["decision_policy_version"]
    current_interpretation_version = scenario["case"]["interpretation_policy_version"]
    return {
        "artifact_type": "policy_improvement_case",
        "artifact_id": f"PIC-{scenario['scenario_id']}",
        "source_scenario_id": scenario["scenario_id"],
        "trigger": incident["trigger"],
        "sample_case_ids": incident["sample_case_ids"],
        "proposed_change_type": "new_eval_scenario_and_interpretation_policy_review",
        "proposed_diff_summary": [
            "Add an eval guard for low-confidence unclassified output when authoritative evidence is otherwise sufficient.",
            "Review interpretation prompts or classification hints so the agent does not stay unclassified on fully aligned service recovery evidence.",
            "Keep deterministic closure policy unchanged until human approval and regression validation.",
        ],
        "eval_result": {
            "scenario_id": scenario["scenario_id"],
            "passed": eval_passed,
            "policy_decision": policy_decision["decision"],
            "final_route": policy_decision["to_stage"],
            "reason_codes": policy_decision["reason_codes"],
        },
        "approval_status": "pending_human_approval",
        "promotion_status": "not_promoted",
        "current_policy_version": {
            "interpretation_policy_version": current_interpretation_version,
            "decision_policy_version": current_decision_version,
        },
        "proposed_next_version": {
            "interpretation_policy_version": "ip-v2-proposed",
            "decision_policy_version": current_decision_version,
        },
        "active_case_policy_version_action": "active_cases_remain_pinned_until_explicit_migration_event",
        "forbidden_actions": [
            "auto_promote_policy",
            "weaken_closure_requirements_without_approval",
            "let_agent_override_authoritative_evidence",
        ],
    }


def build_policy_boundary_report() -> dict[str, Any]:
    scenarios = load_scenarios()
    checks: list[dict[str, Any]] = []
    focused_ids = ["E-002", "E-003", "E-004", "E-009"]

    _add_policy_boundary_check(
        checks,
        "fixture_discipline.business_green_shared_fields",
        focused_ids,
        "E-002/E-003/E-004/E-009 keep CRM, billing, inventory, and dispatch identical.",
        _business_green_shared_fields_match(scenarios),
        {
            "shared_fields": ["crm_order_status", "billing_status", "inventory_assignment", "dispatch_status"],
            "baseline_scenario_id": "E-002",
        },
    )
    _add_policy_boundary_check(
        checks,
        "fixture_discipline.telemetry_is_only_material_variant",
        focused_ids,
        "The focused business-green variants only change authoritative service telemetry shape.",
        _business_green_telemetry_variants_match(scenarios),
        {
            "E-002": _service_live_signal(scenarios["E-002"]),
            "E-003": _service_live_signal(scenarios["E-003"]),
            "E-004": _service_live_signal(scenarios["E-004"]),
            "E-009": _service_live_signal(scenarios["E-009"]),
        },
    )

    source_authority_expectations = {
        "E-002": ("missing_pending", "verify_telemetry", "missing_authoritative_signal"),
        "E-003": ("authoritative_unavailable_or_stale", "verify_telemetry", "stale_authoritative_signal"),
        "E-004": ("contradicting", "human_review", "source_contradiction"),
        "E-009": ("missing_pending", "verify_telemetry", "missing_authoritative_signal"),
    }
    for scenario_id, (state, stage, reason) in source_authority_expectations.items():
        decision = decide_policy(
            scenarios[scenario_id]["case"],
            scenarios[scenario_id]["evidence"],
            scenarios[scenario_id]["agent_interpretation"],
        )
        _add_policy_boundary_check(
            checks,
            f"source_authority.{scenario_id}",
            [scenario_id],
            "Supporting notes and green business systems do not override authoritative telemetry state.",
            (
                not decision["closure_allowed"]
                and decision["derived_evidence_state"] == state
                and decision["to_stage"] == stage
                and reason in decision["reason_codes"]
            ),
            {
                "closure_allowed": decision["closure_allowed"],
                "derived_evidence_state": decision["derived_evidence_state"],
                "to_stage": decision["to_stage"],
                "reason_codes": decision["reason_codes"],
            },
        )

    for scenario_id in focused_ids:
        scenario, transition = _scenario_transition(scenario_id)
        expected_stage = source_authority_expectations[scenario_id][1]
        _add_policy_boundary_check(
            checks,
            f"override_persistence.{scenario_id}",
            [scenario_id],
            "Raw closure recommendation is preserved separately and linked to the policy decision.",
            (
                transition["agent_event"]["recommended_next_stage"] == "closure_candidate"
                and transition["policy_event"]["agent_event_id"] == transition["agent_event"]["event_id"]
                and transition["policy_event"]["from_recommended_stage"] == "closure_candidate"
                and transition["policy_event"]["to_stage"] == expected_stage
                and transition["policy_event"]["decision_policy_version"] == scenario["case"]["decision_policy_version"]
            ),
            {
                "agent_event_id": transition["agent_event"]["event_id"],
                "agent_recommended_next_stage": transition["agent_event"]["recommended_next_stage"],
                "policy_agent_event_id": transition["policy_event"]["agent_event_id"],
                "policy_decision": transition["policy_event"]["decision"],
                "policy_to_stage": transition["policy_event"]["to_stage"],
            },
        )

    high_confidence_stale = copy.deepcopy(scenarios["E-003"])
    high_confidence_stale["agent_interpretation"]["recommendation_confidence"] = 0.99
    decision = decide_policy(
        high_confidence_stale["case"],
        high_confidence_stale["evidence"],
        high_confidence_stale["agent_interpretation"],
    )
    _add_policy_boundary_check(
        checks,
        "confidence_calibration.high_confidence_stale_telemetry",
        ["E-003"],
        "High recommendation confidence cannot overcome stale authoritative telemetry.",
        (
            not decision["closure_allowed"]
            and decision["decision"] == "override_recommendation"
            and decision["to_stage"] == "verify_telemetry"
            and "stale_authoritative_signal" in decision["reason_codes"]
        ),
        {
            "mutated_recommendation_confidence": high_confidence_stale["agent_interpretation"]["recommendation_confidence"],
            "closure_allowed": decision["closure_allowed"],
            "decision": decision["decision"],
            "to_stage": decision["to_stage"],
            "reason_codes": decision["reason_codes"],
        },
    )

    passed = sum(1 for check in checks if check["passed"])
    return {
        "artifact_type": "policy_boundary_eval_report",
        "artifact_version": "policy-boundary-v1",
        "focused_scenario_ids": focused_ids,
        "summary": {
            "total_checks": len(checks),
            "passed": passed,
            "failed": len(checks) - passed,
            "decision_policy_version": "dp-v1",
            "interpretation_policy_version": "ip-v1",
        },
        "checks": checks,
    }


def _add_policy_boundary_check(
    checks: list[dict[str, Any]],
    check_id: str,
    scenario_ids: list[str],
    assertion: str,
    passed: bool,
    observed: dict[str, Any],
) -> None:
    checks.append(
        {
            "check_id": check_id,
            "scenario_ids": scenario_ids,
            "assertion": assertion,
            "passed": passed,
            "observed": observed,
        }
    )


def _business_green_shared_fields_match(scenarios: dict[str, dict[str, Any]]) -> bool:
    baseline = _evidence_by_field(scenarios["E-002"]["evidence"])
    for scenario_id in ("E-003", "E-004", "E-009"):
        variant = _evidence_by_field(scenarios[scenario_id]["evidence"])
        for field in ("crm_order_status", "billing_status", "inventory_assignment", "dispatch_status"):
            if variant[field] != baseline[field]:
                return False
    return True


def _business_green_telemetry_variants_match(scenarios: dict[str, dict[str, Any]]) -> bool:
    service_live = {scenario_id: _service_live_signal(scenarios[scenario_id]) for scenario_id in ("E-002", "E-003", "E-004", "E-009")}
    return (
        service_live["E-002"] == service_live["E-009"]
        and service_live["E-002"] == {
            "source": "support_note",
            "value": "resolved",
            "authoritative": False,
            "freshness_status": "fresh",
        }
        and service_live["E-003"] == {
            "source": "network_telemetry",
            "value": "live",
            "authoritative": True,
            "freshness_status": "stale",
        }
        and service_live["E-004"] == {
            "source": "network_telemetry",
            "value": "not_live",
            "authoritative": True,
            "freshness_status": "fresh",
        }
    )


def _service_live_signal(scenario: dict[str, Any]) -> dict[str, Any]:
    return _evidence_by_field(scenario["evidence"])["service_live_status"]


def _evidence_by_field(evidence: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        signal["field"]: {
            "source": signal["source"],
            "value": signal["value"],
            "authoritative": signal["authoritative"],
            "freshness_status": signal["freshness_status"],
        }
        for signal in evidence
    }


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
