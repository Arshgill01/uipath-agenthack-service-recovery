from __future__ import annotations

import json
from typing import Any


def build_action_center_payload(
    case: dict[str, Any],
    evidence: list[dict[str, Any]],
    transition: dict[str, Any],
) -> dict[str, str]:
    """Build the generated Action app input payload for a UiPath human review task."""
    agent_event = _agent_interpretation_event(case, transition["agent_event"])
    policy_event = _policy_decision_event(transition["policy_event"])
    closure_checklist = _closure_readiness_checklist(evidence, policy_event)
    reviewer_questions = _reviewer_questions(policy_event, agent_event, closure_checklist)
    policy_event["closure_readiness_checklist"] = closure_checklist
    policy_event["reviewer_questions"] = reviewer_questions

    evidence_packet = {
        "case_id": case["case_id"],
        "service_id": case["service_id"],
        "business_state": _business_state(evidence),
        "derived_evidence_state": transition["case"]["derived_evidence_state"],
        "evidence_signals": evidence,
        "closure_block_reason": _primary_block_reason(transition["policy_event"]),
        "recommended_options": _recommended_options(transition["policy_event"]),
        "closure_readiness_checklist": closure_checklist,
        "reviewer_questions": reviewer_questions,
    }

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
        "adversarial_interpretation": agent_event.get("adversarial_interpretation"),
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


def _closure_readiness_checklist(evidence: list[dict[str, Any]], policy_event: dict[str, Any]) -> list[dict[str, Any]]:
    by_field = {signal["field"]: signal for signal in evidence if signal["authoritative"]}
    reason_codes = set(policy_event["reason_codes"])

    network = by_field.get("service_live_status")
    billing = by_field.get("billing_status")
    inventory = by_field.get("inventory_assignment")

    checklist = [
        _check(
            "Fresh authoritative telemetry confirms service is live",
            network is not None and network["freshness_status"] == "fresh" and network["value"] == "live",
            _signal_summary(network) if network else "No authoritative network telemetry signal is present.",
        ),
        _check(
            "No unresolved source contradiction remains",
            "source_contradiction" not in reason_codes,
            "Policy reason source_contradiction is present."
            if "source_contradiction" in reason_codes
            else "No fresh authoritative contradiction was derived.",
        ),
        _check(
            "Billing has no active hold",
            billing is not None and billing["freshness_status"] == "fresh" and billing["value"] != "hold",
            _signal_summary(billing) if billing else "No authoritative billing signal is present.",
        ),
        _check(
            "Inventory assignment matches the order",
            inventory is not None and inventory["freshness_status"] == "fresh" and inventory["value"] == "assigned_match",
            _signal_summary(inventory) if inventory else "No authoritative inventory signal is present.",
        ),
    ]
    if policy_event["to_stage"] == "human_review":
        checklist.append(
            _check(
                "Required human review has resolved the exception",
                False,
                f"Case is routed to human_review for {policy_event['block_reason']}.",
            )
        )
    if "high_interpretation_disagreement" in reason_codes:
        checklist.append(
            _check(
                "Advocate/skeptic interpretation disagreement is resolved",
                False,
                "Policy received high_interpretation_disagreement as structured input.",
            )
        )
    return checklist


def _reviewer_questions(
    policy_event: dict[str, Any],
    agent_event: dict[str, Any],
    closure_checklist: list[dict[str, Any]],
) -> list[str]:
    questions = list(agent_event.get("reviewer_questions", []))
    reason_codes = set(policy_event["reason_codes"])

    if "missing_authoritative_signal" in reason_codes:
        questions.append("Which authoritative telemetry retry or source will produce service_live_status before closure?")
    if "stale_authoritative_signal" in reason_codes:
        questions.append("Can network operations refresh telemetry and confirm observed_at is inside the required TTL?")
    if "source_contradiction" in reason_codes:
        questions.append("Why do business systems show active while fresh authoritative service evidence disagrees?")
    if "invalid_agent_output" in reason_codes:
        questions.append("What schema or confidence issue made the agent output invalid before routing continues?")
    if "high_interpretation_disagreement" in reason_codes:
        questions.append("Which interpretation is supported by authoritative evidence, and which gap must be resolved before closure?")
        questions.extend(_skeptic_gap_questions(agent_event))
    if any(item["status"] == "blocked" for item in closure_checklist):
        questions.append("Which blocked closure criteria now have fresh authoritative evidence?")
    return _dedupe(questions)


def _skeptic_gap_questions(agent_event: dict[str, Any]) -> list[str]:
    adversarial = agent_event.get("adversarial_interpretation")
    if not isinstance(adversarial, dict):
        return []
    disagreement = adversarial.get("disagreement")
    if not isinstance(disagreement, dict):
        return []
    return [
        f"Resolve skeptic-only gap before closure: {str(gap).strip().rstrip('.')}."
        for gap in disagreement.get("unique_skeptic_gaps", [])
        if str(gap).strip()
    ]


def _check(criterion: str, passed: bool, evidence: str) -> dict[str, Any]:
    return {
        "criterion": criterion,
        "status": "satisfied" if passed else "blocked",
        "evidence": evidence,
        "required_to_close": True,
    }


def _signal_summary(signal: dict[str, Any] | None) -> str:
    if not signal:
        return "No signal is present."
    return (
        f"{signal['source']} {signal['field']}={signal['value']} "
        f"freshness={signal['freshness_status']} observed_at={signal['observed_at']}"
    )


def _dedupe(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def _content_summary(evidence_packet: dict[str, Any], policy_event: dict[str, Any]) -> str:
    if "high_interpretation_disagreement" in policy_event["reason_codes"]:
        return (
            "Service recovery ambiguity review required: two valid structured interpretations diverged on "
            "the same evidence. Resolve the disagreement and blocked closure checklist before closure."
        )
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
