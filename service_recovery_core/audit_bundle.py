from __future__ import annotations

import json
from typing import Any

from service_recovery_core.uipath_payload import build_action_center_payload


def build_case_audit_bundle(
    case: dict[str, Any],
    evidence: list[dict[str, Any]],
    transition: dict[str, Any],
    *,
    case_instance: dict[str, Any] | None = None,
    human_review: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build the one-query domain audit shape required when native Case history is not enough."""
    action_payload = build_action_center_payload(case, evidence, transition)
    evidence_packet = _loads(action_payload["EvidencePacketJson"])
    agent_event = _loads(action_payload["RawAgentRecommendation"])
    policy_event = _loads(action_payload["PolicyDecisionJson"])
    human_event = _human_review_event(case["case_id"], human_review)

    events = [
        {
            "event_type": "EvidenceStateEvent",
            "event_id": f"ESE-{case['case_id']}",
            "case_id": case["case_id"],
            "derived_evidence_state": evidence_packet["derived_evidence_state"],
            "business_state": evidence_packet["business_state"],
            "closure_block_reason": evidence_packet["closure_block_reason"],
            "evidence_signal_count": len(evidence_packet["evidence_signals"]),
            "sort_order": 10,
        },
        dict(agent_event, sort_order=20),
        dict(policy_event, sort_order=30),
        dict(human_event, sort_order=40),
    ]

    return {
        "case_id": case["case_id"],
        "service_id": case["service_id"],
        "audit_contract_version": "service-recovery-audit-v1",
        "case_instance": _case_instance(case, case_instance),
        "policy_versions": {
            "interpretation_policy_version": agent_event["interpretation_policy_version"],
            "decision_policy_version": policy_event["decision_policy_version"],
        },
        "evidence_state": {
            "business_state": evidence_packet["business_state"],
            "derived_evidence_state": evidence_packet["derived_evidence_state"],
            "closure_block_reason": evidence_packet["closure_block_reason"],
        },
        "agent_interpretation_event": agent_event,
        "policy_decision_event": policy_event,
        "human_review_event": human_event,
        "reviewer_packet": {
            "content": action_payload["Content"],
            "evidence_table": evidence_packet["evidence_signals"],
            "raw_agent_recommendation": agent_event,
            "policy_decision": policy_event,
            "block_reason": evidence_packet["closure_block_reason"],
            "recommended_options": evidence_packet["recommended_options"],
            "closure_readiness_checklist": evidence_packet["closure_readiness_checklist"],
            "reviewer_questions": evidence_packet["reviewer_questions"],
            "rendering_status": "structured_packet_ready",
        },
        "events": sorted(events, key=lambda event: event["sort_order"]),
    }


def _case_instance(case: dict[str, Any], case_instance: dict[str, Any] | None) -> dict[str, Any]:
    default_instance = {
        "case_stage": case["case_stage"],
        "severity": case["severity"],
        "sla_deadline": case["sla_deadline"],
        "case_process_package_key": case.get("case_process_package_key"),
        "case_process_package_version": case.get("case_process_package_version"),
        "case_process_auto_update": case.get("case_process_auto_update"),
    }
    if not case_instance:
        return default_instance
    merged = dict(default_instance)
    merged.update(case_instance)
    return merged


def _human_review_event(case_id: str, human_review: dict[str, Any] | None) -> dict[str, Any]:
    if human_review:
        event = dict(human_review)
        event.setdefault("event_type", "HumanReviewEvent")
        event.setdefault("case_id", case_id)
        return event
    return {
        "event_type": "HumanReviewEvent",
        "event_id": f"HRE-{case_id}-PENDING",
        "case_id": case_id,
        "task_key": None,
        "decision": "pending",
        "comment": "",
        "structured_task_output": None,
    }


def _loads(payload: str) -> dict[str, Any]:
    return json.loads(payload)
