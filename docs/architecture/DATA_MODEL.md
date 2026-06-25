# Provisional Data Model

This model is provisional until hard platform gates are validated.

## Case

```json
{
  "case_id": "CASE-1001",
  "customer_id": "C-42",
  "service_id": "SVC-900",
  "case_stage": "intake | evidence_verification | retry_with_sla | exception_investigation | human_review | remediation | closure_candidate | closed",
  "severity": "normal | elevated | critical",
  "sla_deadline": "timestamp",
  "interpretation_policy_version": "ip-v1",
  "decision_policy_version": "dp-v1",
  "derived_evidence_state": "confirmed_aligned | missing_pending | contradicting | authoritative_unavailable_or_stale",
  "case_process_package_key": "PackageKey visible on live case instance",
  "case_process_package_version": "1.0.2",
  "case_process_auto_update": false
}
```

Package metadata is operational audit metadata, not business evidence. It pins which Case package executed the workflow and must not be used by the LLM or policy as a reason to close or reroute service recovery.

## Evidence Signal

```json
{
  "case_id": "CASE-1001",
  "field": "service_live_status | crm_order_status | billing_status | inventory_assignment | dispatch_status",
  "source": "crm | billing | network_telemetry | inventory | dispatch | customer_message | support_note",
  "value": "...",
  "authoritative": true,
  "freshness_status": "fresh | stale | unavailable",
  "ttl_seconds": 300,
  "observed_at": "timestamp"
}
```

## Agent Interpretation Event

```json
{
  "case_id": "CASE-1001",
  "event_id": "AIE-1",
  "input_refs": ["customer_message_1", "tech_note_1"],
  "failure_category": "activation_failure | billing_hold | inventory_mismatch | dispatch_dependency | telemetry_gap | customer_premises_issue | unclassified",
  "category_confidence": 0.0,
  "interpretation_rationale_codes": ["mentions_access_blocker"],
  "recommended_next_stage": "verify_telemetry | retry_activation | dispatch_followup | inventory_reconciliation | billing_review | human_exception_review | closure_candidate",
  "recommendation_confidence": 0.0,
  "closure_block_reason_code": "none | missing_authoritative_signal | stale_authoritative_signal | source_contradiction | low_category_confidence | low_recommendation_confidence | high_impact_exception | invalid_agent_output",
  "audit_explanation": "generated once",
  "valid_schema": true
}
```

## Policy Decision Event

```json
{
  "case_id": "CASE-1001",
  "event_id": "PDE-1",
  "agent_event_id": "AIE-1",
  "decision": "accept_recommendation | override_recommendation | block_closure | require_human_review",
  "from_recommended_stage": "closure_candidate",
  "to_stage": "verify_telemetry",
  "reason_codes": ["missing_authoritative_signal"],
  "decision_policy_version": "dp-v1",
  "created_at": "timestamp"
}
```

## Human Review Event

```json
{
  "case_id": "CASE-1001",
  "task_key": "Action Center task key",
  "reviewer_role": "network_ops | dispatch_coordinator | service_manager",
  "decision": "approve_remediation | reject | request_more_evidence | close_after_confirmation",
  "comment": "...",
  "evidence_packet_ref": "EP-1",
  "structured_task_output": {
    "action": "approve | reject | request_more_evidence",
    "comment": "...",
    "raw_output_ref": "UiPath AppTask output payload"
  },
  "created_at": "timestamp"
}
```

## Human Evidence Packet Payload

```json
{
  "case_id": "CASE-1001",
  "evidence_packet_ref": "EP-1",
  "evidence_signals": ["evidence-signal-ref"],
  "raw_agent_recommendation": {
    "agent_event_id": "AIE-1",
    "recommended_next_stage": "closure_candidate",
    "recommendation_confidence": 0.91
  },
  "policy_decision": {
    "policy_event_id": "PDE-1",
    "decision": "block_closure",
    "to_stage": "retry_with_sla",
    "reason_codes": ["missing_authoritative_signal"]
  },
  "rendering_status": "rendered | persisted_but_mislabeled | failed"
}
```

The raw agent recommendation and final policy decision are separate fields because the demo and audit trail must show the policy boundary. Package `1.0.3` proved persistence for both fields in Action Center task `4295299`, but the generated Action Center page rendered `PolicyDecisionJson` as `Unnamed String 1`; use `persisted_but_mislabeled` until the reviewer page is repaired.

## Package / Migration Event

```json
{
  "case_id": "CASE-1001",
  "event_id": "PME-1",
  "event_type": "case_started | package_pinned | package_migration_requested | package_migrated | app_binding_repaired",
  "package_key": "PackageKey visible on live case instance",
  "from_package_version": "1.0.0",
  "to_package_version": "1.0.2",
  "auto_update": false,
  "reason": "explicit validation/deployment action",
  "created_at": "timestamp"
}
```

Active cases remain on their starting Case package and policy versions unless a `package_migrated` event and corresponding policy migration event are explicitly recorded.

## Policy Improvement Case

```json
{
  "improvement_case_id": "PIC-1",
  "trigger": "agent_usefulness_degradation | repeated_policy_override | eval_failure | invalid_schema_rate",
  "affected_policy_type": "interpretation | decision",
  "proposed_change_type": "rationale_code | prompt_schema | routing_rule | ttl_review | closure_rule",
  "proposed_diff": {},
  "eval_result_ref": "EVAL-1",
  "approval_status": "proposed | eval_passed | approved | rejected | promoted",
  "new_policy_version": "ip-v2"
}
```

## Eval Scenario / Result

```json
{
  "scenario_id": "EVAL-001",
  "case_fixture": {},
  "expected_failure_category": "dispatch_dependency",
  "expected_policy_decision": "block_closure",
  "expected_stage": "human_exception_review",
  "actual_result": {},
  "passed": true
}
```
