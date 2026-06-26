CASE_STAGES = {
    "intake",
    "evidence_verification",
    "retry_with_sla",
    "exception_investigation",
    "human_review",
    "remediation",
    "closure_candidate",
    "closed",
}

SEVERITIES = {"normal", "elevated", "critical"}

EVIDENCE_STATES = {
    "confirmed_aligned",
    "missing_pending",
    "contradicting",
    "authoritative_unavailable_or_stale",
}

EVIDENCE_FIELDS = {
    "service_live_status",
    "crm_order_status",
    "billing_status",
    "inventory_assignment",
    "dispatch_status",
}

SOURCES = {
    "crm",
    "billing",
    "network_telemetry",
    "inventory",
    "dispatch",
    "customer_message",
    "support_note",
    "technician_note",
}

FRESHNESS_STATUSES = {"fresh", "stale", "unavailable"}

FAILURE_CATEGORIES = {
    "activation_failure",
    "billing_hold",
    "inventory_mismatch",
    "dispatch_dependency",
    "telemetry_gap",
    "customer_premises_issue",
    "unclassified",
}

RATIONALE_CODES = {
    "mentions_access_blocker",
    "mentions_device_mismatch",
    "mentions_signal_absent",
    "mentions_billing_hold",
    "mentions_customer_pressure",
    "mentions_system_timeout",
    "none",
}

CLAIM_TYPES = {
    "customer_reported_symptom",
    "technician_observation",
    "support_note_claim",
    "device_identifier",
    "appointment_update",
    "pressure_to_bypass",
}

CLAIM_SOURCES = {"customer_message", "technician_note", "support_note"}

RECOMMENDED_STAGES = {
    "verify_telemetry",
    "retry_activation",
    "dispatch_followup",
    "inventory_reconciliation",
    "billing_review",
    "human_exception_review",
    "closure_candidate",
}

BLOCK_REASONS = {
    "none",
    "missing_authoritative_signal",
    "stale_authoritative_signal",
    "source_contradiction",
    "low_category_confidence",
    "low_recommendation_confidence",
    "high_interpretation_disagreement",
    "high_impact_exception",
    "invalid_agent_output",
}

POLICY_DECISIONS = {
    "accept_recommendation",
    "override_recommendation",
    "block_closure",
    "require_human_review",
}
