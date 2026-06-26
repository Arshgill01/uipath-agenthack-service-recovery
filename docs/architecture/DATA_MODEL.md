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

## Case Audit Bundle

Native Maestro Case state is useful for package/job/stage/task order, but live validation showed that the domain audit must be carried explicitly. The implementation now has a reproducible `service-recovery-audit-v1` bundle generated from the same scenario, policy, and transition outputs that feed UiPath Action Center.

Generate examples with:

```bash
python -m service_recovery_core.evals --audit-bundle-scenario E-002 --output eval_results/audit_bundle_E002.json
python -m service_recovery_core.evals --audit-bundle-scenario E-004 --output eval_results/audit_bundle_E004.json
```

Bundle shape:

```json
{
  "case_id": "CASE-BG-MISSING",
  "service_id": "SVC-BG-1",
  "audit_contract_version": "service-recovery-audit-v1",
  "case_instance": {
    "case_stage": "intake",
    "severity": "normal",
    "sla_deadline": "timestamp",
    "case_process_package_key": "optional UiPath PackageKey",
    "case_process_package_version": "optional UiPath package version",
    "case_process_auto_update": false
  },
  "policy_versions": {
    "interpretation_policy_version": "ip-v1",
    "decision_policy_version": "dp-v1"
  },
  "evidence_state": {
    "business_state": "green",
    "derived_evidence_state": "missing_pending",
    "closure_block_reason": "missing_authoritative_signal"
  },
  "agent_interpretation_event": {},
  "policy_decision_event": {},
  "human_review_event": {},
  "reviewer_packet": {
    "content": "reviewer summary",
    "evidence_table": [],
    "raw_agent_recommendation": {},
    "policy_decision": {},
    "block_reason": "missing_authoritative_signal",
    "recommended_options": [],
    "rendering_status": "structured_packet_ready"
  },
  "events": [
    {"event_type": "EvidenceStateEvent", "sort_order": 10},
    {"event_type": "AgentInterpretationEvent", "sort_order": 20},
    {"event_type": "PolicyDecisionEvent", "sort_order": 30},
    {"event_type": "HumanReviewEvent", "sort_order": 40}
  ]
}
```

This is the fallback answer for G-001: if a single native Case query/view cannot reconstruct the domain proof beat, store this bundle as custom audit state/events in the Case payload, Data Fabric/Data Service, or another UiPath-accessible artifact. It preserves the exact fields the hard gate requires: evidence state, active policy versions, raw agent recommendation, policy decision, closure block reason, human action, and event order.

## Data Fabric Audit Entity

`docs/architecture/data_fabric/service_recovery_audit_bundle_v2_entity.json` defines the live-validated `ServiceRecoveryAuditBundleV2` entity for storing `service-recovery-audit-v1` in UiPath Data Fabric.

First-class query fields:

- `CaseId`
- `ServiceId`
- `ScenarioId`
- `AuditContractVersion`
- `BusinessState`
- `DerivedEvidenceState`
- `ClosureBlockReason`
- `InterpretationPolicyVersion`
- `DecisionPolicyVersion`
- `SourceCaseInstanceKey`
- `SourceTaskId`
- `PackageVersion`
- `CreatedAt`

JSON payload fields:

- `RawAgentEventJson`
- `PolicyDecisionEventJson`
- `ReviewerPacketJson`
- `AuditBundleJson`

`python -m service_recovery_core.evals --data-fabric-record-scenario <ID> --data-fabric-field-style pascal` emits the matching record body. Live entity creation and record insertion require explicit approval because they mutate the UiPath tenant schema/data.

Live validation note from 2026-06-26:

- Probe entity `DataFabricPascalProbe` proved that PascalCase custom fields insert and query back through `uip df records insert/query`.
- Entity creation succeeded: `ServiceRecoveryAuditBundleV2`, ID `35e8f6c7-4671-f111-ac9a-002248a16d28`.
- JSON insert succeeded for E-004 record `F9D838CE-4671-F111-AC9A-0022489A9A06`.
- Query by `CaseId = CASE-BG-CONTRA` returned the first-class domain fields, including `InterpretationPolicyVersion = ip-v1`, `DecisionPolicyVersion = dp-v1`, `ClosureBlockReason = source_contradiction`, `SourceCaseInstanceKey = 9fc6fece-55ed-4fb2-b11a-6c96f7a3314e`, `SourceTaskId = 4328396`, and `PackageVersion = 1.0.6`.
- Record get returned parseable `RawAgentEventJson`, `PolicyDecisionEventJson`, and `AuditBundleJson`; parsed readback proved raw recommendation `closure_candidate`, policy decision `require_human_review`, link `PDE-E-004 -> AIE-E004`, `from_recommended_stage = closure_candidate`, `to_stage = human_review`, and `block_reason = source_contradiction`.

Legacy validation note from 2026-06-25:

- Entity creation succeeded after user approval: `ServiceRecoveryAuditBundle`, ID `328ef8b6-ab70-f111-ac9a-002248a16d28`.
- Schema readback by ID succeeded and returned the expected fields.
- Name-based `entities get ServiceRecoveryAuditBundle` failed; use the entity ID for CLI operations.
- Direct JSON record insertion with snake_case field names failed. `records insert` rejected file, inline object, minimal object, wrapper object, field-ID keyed object, and array payloads with required `case_id` reported missing. CSV import created E-004 record `DA42769C-33B7-4701-A266-019F032AF376` in entity `328ef8b6-ab70-f111-ac9a-002248a16d28`, but follow-up CLI readback returned only system fields and did not prove the custom payload values.

## Orchestrator Bucket Audit Artifact

Because native Case history does not currently reconstruct the domain proof beat by itself, Data Fabric V2 and Orchestrator storage buckets are the validated UiPath-hosted full-payload audit paths.

Live validation note from 2026-06-25:

- Bucket `service-recovery-audit-validation` was created in org `keepingitlowkey`, tenant `DefaultTenant`.
- Bucket key: `dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb`.
- Uploaded path: `audit/service_recovery_audit_bundle_E004.json`.
- Source artifact: `docs/validation/artifacts/2026-06-25/service_recovery_audit_bundle_E004.json`.
- Manifest: `docs/validation/artifacts/2026-06-25/orchestrator_bucket_audit_artifact_E004_manifest.json`.
- Downloaded copy: `eval_results/downloaded_audit_bundle_E004.json`.
- SHA-256: `3d02852775cb8e6a3c3c451553a22c5c5afe38848853f48e9f4f5a506b83a05e`.
- Upload, list, download, and byte-compare all succeeded.

Use this bucket-backed artifact as the durable UiPath-accessible fallback when Data Fabric CSV import is not part of the demo path. It is not native Case history; it is explicit custom audit state stored on a UiPath platform surface.

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
