from __future__ import annotations

import json
from typing import Any


def build_action_center_payload(
    case: dict[str, Any],
    evidence: list[dict[str, Any]],
    transition: dict[str, Any],
) -> dict[str, str]:
    """Build the generated Action app input payload for a UiPath human review task."""
    evidence_packet = {
        "case_id": case["case_id"],
        "service_id": case["service_id"],
        "business_state": _business_state(evidence),
        "derived_evidence_state": transition["case"]["derived_evidence_state"],
        "evidence_signals": evidence,
        "closure_block_reason": _primary_block_reason(transition["policy_event"]),
        "recommended_options": _recommended_options(transition["policy_event"]),
    }
    agent_event = _agent_interpretation_event(case, transition["agent_event"])
    policy_event = _policy_decision_event(transition["policy_event"])

    return {
        "Content": _content_summary(evidence_packet, policy_event),
        "EvidencePacketJson": _dumps(evidence_packet),
        "RawAgentRecommendation": _dumps(agent_event),
        "PolicyDecisionJson": _dumps(policy_event),
        "Comment": "",
    }


def _agent_interpretation_event(case: dict[str, Any], agent_event: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_type": "AgentInterpretationEvent",
        "event_id": agent_event["event_id"],
        "case_id": case["case_id"],
        "interpretation_policy_version": case["interpretation_policy_version"],
        "recommended_next_stage": agent_event["recommended_next_stage"],
        "confidence": agent_event["recommendation_confidence"],
        "failure_category": agent_event["failure_category"],
        "rationale": agent_event["audit_explanation"],
        "urgency": agent_event.get("urgency"),
        "customer_impact_summary": agent_event.get("customer_impact_summary"),
        "evidence_gaps": agent_event.get("evidence_gaps", []),
        "recommended_actions": agent_event.get("recommended_actions", []),
        "reviewer_questions": agent_event.get("reviewer_questions", []),
        "operator_note": agent_event.get("operator_note"),
    }


def _policy_decision_event(policy_event: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_type": "PolicyDecisionEvent",
        "event_id": policy_event["event_id"],
        "case_id": policy_event["case_id"],
        "links_to": policy_event["agent_event_id"],
        "decision_policy_version": policy_event["decision_policy_version"],
        "decision": policy_event["decision"],
        "from_recommended_stage": policy_event["from_recommended_stage"],
        "to_stage": policy_event["to_stage"],
        "block_reason": _primary_block_reason(policy_event),
        "reason_codes": policy_event["reason_codes"],
        "allowed_actions": _recommended_options(policy_event),
    }


def _business_state(evidence: list[dict[str, Any]]) -> str:
    material_business = [
        signal
        for signal in evidence
        if signal["field"] in {"crm_order_status", "billing_status", "inventory_assignment", "dispatch_status"}
    ]
    if material_business and all(signal["freshness_status"] == "fresh" for signal in material_business):
        return "green"
    return "needs_review"


def _primary_block_reason(policy_event: dict[str, Any]) -> str:
    return policy_event["reason_codes"][0] if policy_event["reason_codes"] else "none"


def _recommended_options(policy_event: dict[str, Any]) -> list[str]:
    if policy_event["to_stage"] == "verify_telemetry":
        return ["retry_telemetry", "request_evidence", "human_review"]
    if policy_event["to_stage"] == "human_review":
        return ["human_review", "request_evidence", "open_investigation"]
    if policy_event["to_stage"] == "closure_candidate":
        return ["approve_closure", "request_evidence"]
    return ["request_evidence", "human_review"]


def _content_summary(evidence_packet: dict[str, Any], policy_event: dict[str, Any]) -> str:
    if policy_event["block_reason"] == "source_contradiction":
        return (
            "Service recovery exception review required: CRM/order/billing/support notes are green, "
            "but fresh authoritative telemetry contradicts the business state. "
            "Do not close; open human exception review."
        )
    if evidence_packet["business_state"] == "green" and policy_event["block_reason"] != "none":
        return (
            "Service recovery verification required: CRM/order/billing/support notes are green, "
            f"but closure is blocked by {policy_event['block_reason']}. "
            "Do not close until authoritative evidence satisfies policy."
        )
    return "Service recovery review required: inspect evidence, agent recommendation, and policy decision."


def _dumps(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))
