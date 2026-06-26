from __future__ import annotations

from collections import defaultdict
from typing import Any

from service_recovery_core.agent_validator import validate_agent_interpretation
from service_recovery_core.enums import EVIDENCE_STATES
from service_recovery_core.schemas import AUTHORITATIVE_SOURCE_BY_FIELD, ValidationError, validate_evidence_signal

MATERIAL_FIELDS = {
    "service_live_status",
    "crm_order_status",
    "billing_status",
    "inventory_assignment",
}


def decide_policy(
    case: dict[str, Any],
    evidence: list[dict[str, Any]],
    agent_event: dict[str, Any],
    interpretation_disagreement: dict[str, Any] | None = None,
) -> dict[str, Any]:
    agent_validation = validate_agent_interpretation(agent_event)
    reconciliation = reconcile_evidence(evidence)
    reason_codes = list(reconciliation["reason_codes"])
    high_disagreement = _is_high_interpretation_disagreement(interpretation_disagreement)

    if not agent_validation["valid"]:
        reason_codes.append("invalid_agent_output")
    else:
        if agent_event["closure_block_reason_code"] != "none":
            reason_codes.append(agent_event["closure_block_reason_code"])
        if agent_event["category_confidence"] < 0.50:
            reason_codes.append("low_category_confidence")
        if agent_event["recommendation_confidence"] < 0.50:
            reason_codes.append("low_recommendation_confidence")
    if high_disagreement:
        reason_codes.append("high_interpretation_disagreement")

    closure_allowed = (
        reconciliation["derived_evidence_state"] == "confirmed_aligned"
        and not reason_codes
        and agent_event["recommended_next_stage"] == "closure_candidate"
    )
    if "invalid_agent_output" in reason_codes:
        decision = "override_recommendation"
        target_stage = "verify_telemetry"
    elif high_disagreement:
        decision = "require_human_review"
        target_stage = "human_review"
    elif "low_category_confidence" in reason_codes or "low_recommendation_confidence" in reason_codes:
        decision = "block_closure"
        target_stage = "verify_telemetry"
    elif closure_allowed and agent_event["recommended_next_stage"] == "closure_candidate":
        decision = "accept_recommendation"
        target_stage = "closure_candidate"
    elif reconciliation["derived_evidence_state"] == "confirmed_aligned" and not reason_codes:
        decision = "accept_recommendation"
        target_stage = agent_event["recommended_next_stage"]
    elif reconciliation["derived_evidence_state"] == "contradicting":
        decision = "require_human_review"
        target_stage = "human_review"
    elif agent_event["recommended_next_stage"] == "closure_candidate":
        decision = "override_recommendation"
        target_stage = reconciliation["target_stage"]
    elif reconciliation["derived_evidence_state"] == "confirmed_aligned":
        decision = "accept_recommendation"
        target_stage = agent_event["recommended_next_stage"]
    else:
        decision = "block_closure" if reason_codes else "accept_recommendation"
        target_stage = reconciliation["target_stage"]

    return {
        "case_id": case["case_id"],
        "agent_event_id": agent_event.get("event_id"),
        "decision": decision,
        "from_recommended_stage": agent_event.get("recommended_next_stage"),
        "to_stage": target_stage,
        "derived_evidence_state": reconciliation["derived_evidence_state"],
        "closure_allowed": closure_allowed,
        "reason_codes": _dedupe(reason_codes),
        "decision_policy_version": case["decision_policy_version"],
        "severity": "elevated" if high_disagreement else reconciliation["severity"],
    }


def reconcile_evidence(evidence: list[dict[str, Any]]) -> dict[str, Any]:
    by_field: dict[str, list[dict[str, Any]]] = defaultdict(list)
    reason_codes: list[str] = []

    for signal in evidence:
        validate_evidence_signal(signal)
        by_field[signal["field"]].append(signal)

    authoritative_by_field = {}
    for field in MATERIAL_FIELDS:
        source = AUTHORITATIVE_SOURCE_BY_FIELD[field]
        matching = [
            signal
            for signal in by_field.get(field, [])
            if signal["authoritative"] and signal["source"] == source
        ]
        if not matching:
            reason_codes.append("missing_authoritative_signal")
            continue
        authoritative_by_field[field] = matching[0]
        if matching[0]["freshness_status"] == "unavailable":
            reason_codes.append("missing_authoritative_signal")
        elif matching[0]["freshness_status"] == "stale":
            reason_codes.append("stale_authoritative_signal")

    contradiction = _find_contradiction(by_field, authoritative_by_field)
    if contradiction:
        reason_codes.append("source_contradiction")

    if contradiction:
        state = "contradicting"
        target_stage = "human_review"
        severity = "elevated"
    elif "stale_authoritative_signal" in reason_codes:
        state = "authoritative_unavailable_or_stale"
        target_stage = "verify_telemetry"
        severity = "normal"
    elif "missing_authoritative_signal" in reason_codes:
        state = "missing_pending"
        target_stage = "verify_telemetry"
        severity = "normal"
    else:
        state = "confirmed_aligned"
        target_stage = "closure_candidate"
        severity = "normal"

    if state not in EVIDENCE_STATES:
        raise ValidationError(f"invalid derived state: {state}")

    return {
        "derived_evidence_state": state,
        "closure_allowed": state == "confirmed_aligned",
        "reason_codes": _dedupe(reason_codes),
        "target_stage": target_stage,
        "severity": severity,
    }


def _find_contradiction(
    by_field: dict[str, list[dict[str, Any]]],
    authoritative_by_field: dict[str, dict[str, Any]],
) -> bool:
    network = authoritative_by_field.get("service_live_status")
    crm = authoritative_by_field.get("crm_order_status")
    inventory = authoritative_by_field.get("inventory_assignment")
    billing = authoritative_by_field.get("billing_status")

    if network and network["freshness_status"] == "fresh" and network["value"] != "live":
        if crm and crm["value"] in {"active", "completed"}:
            return True

    if inventory and inventory["freshness_status"] == "fresh" and inventory["value"] != "assigned_match":
        return True

    if billing and billing["freshness_status"] == "fresh" and billing["value"] == "hold":
        return True

    for field, signals in by_field.items():
        authoritative = authoritative_by_field.get(field)
        if not authoritative or authoritative["freshness_status"] != "fresh":
            continue
        for signal in signals:
            if signal["authoritative"]:
                continue
            if signal["freshness_status"] == "fresh" and signal["value"] != authoritative["value"]:
                return True
    return False


def _dedupe(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def _is_high_interpretation_disagreement(disagreement: dict[str, Any] | None) -> bool:
    if not disagreement:
        return False
    score = disagreement.get("disagreement_score")
    return isinstance(score, (int, float)) and not isinstance(score, bool) and score >= 0.60
