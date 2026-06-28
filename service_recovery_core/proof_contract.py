from __future__ import annotations

CORE_DEMO_SCENARIOS = ("E-002", "E-004")

CORE_DEMO_EXPECTED_PROOF = {
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
