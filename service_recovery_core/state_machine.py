from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

ALLOWED_TRANSITIONS = {
    "intake": {"evidence_verification", "retry_with_sla", "human_review", "remediation", "closure_candidate"},
    "evidence_verification": {"retry_with_sla", "human_review", "closure_candidate"},
    "retry_with_sla": {"evidence_verification", "human_review", "closure_candidate"},
    "human_review": {"exception_investigation", "remediation", "evidence_verification", "closure_candidate"},
    "exception_investigation": {"human_review", "remediation", "evidence_verification"},
    "remediation": {"evidence_verification", "closure_candidate"},
    "closure_candidate": {"closed", "evidence_verification", "human_review"},
    "closed": set(),
}

POLICY_STAGE_TO_CASE_STAGE = {
    "verify_telemetry": "evidence_verification",
    "retry_activation": "retry_with_sla",
    "dispatch_followup": "remediation",
    "inventory_reconciliation": "remediation",
    "billing_review": "remediation",
    "human_exception_review": "human_review",
    "human_review": "human_review",
    "closure_candidate": "closure_candidate",
}


def apply_policy_decision(
    case: dict[str, Any],
    agent_event: dict[str, Any],
    policy_decision: dict[str, Any],
    *,
    event_id: str = "PDE-1",
) -> dict[str, Any]:
    next_stage = POLICY_STAGE_TO_CASE_STAGE.get(policy_decision["to_stage"], policy_decision["to_stage"])
    current_stage = case["case_stage"]
    if next_stage not in ALLOWED_TRANSITIONS[current_stage]:
        raise ValueError(f"transition {current_stage} -> {next_stage} is not allowed")

    updated_case = dict(case)
    updated_case["case_stage"] = next_stage
    updated_case["severity"] = policy_decision["severity"]
    updated_case["derived_evidence_state"] = policy_decision["derived_evidence_state"]

    policy_event = {
        "case_id": case["case_id"],
        "event_id": event_id,
        "agent_event_id": agent_event["event_id"],
        "decision": policy_decision["decision"],
        "from_recommended_stage": policy_decision["from_recommended_stage"],
        "to_stage": policy_decision["to_stage"],
        "reason_codes": policy_decision["reason_codes"],
        "decision_policy_version": policy_decision["decision_policy_version"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    return {
        "case": updated_case,
        "agent_event": dict(agent_event),
        "policy_event": policy_event,
    }
