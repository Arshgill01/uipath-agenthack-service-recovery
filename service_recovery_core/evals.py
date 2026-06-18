from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from service_recovery_core.agent_validator import validate_agent_interpretation
from service_recovery_core.fixtures import load_scenarios
from service_recovery_core.policy import decide_policy
from service_recovery_core.state_machine import apply_policy_decision


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
    args = parser.parse_args()
    results = run_eval_suite()
    rendered = json.dumps(results, indent=2, sort_keys=True)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if results["summary"]["failed"] == 0 else 1


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
