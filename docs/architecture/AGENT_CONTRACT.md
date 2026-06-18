# Agent Contract

The agent converts ambiguous unstructured evidence into structured signals. It does not decide closure or mutate policy.

## Output Schema

```json
{
  "failure_category": "activation_failure | billing_hold | inventory_mismatch | dispatch_dependency | telemetry_gap | customer_premises_issue | unclassified",
  "category_confidence": 0.0,
  "interpretation_rationale_codes": [
    "mentions_access_blocker | mentions_device_mismatch | mentions_signal_absent | mentions_billing_hold | mentions_customer_pressure | mentions_system_timeout | none"
  ],
  "extracted_claims": [
    {
      "claim_type": "customer_reported_symptom | technician_observation | support_note_claim | device_identifier | appointment_update | pressure_to_bypass",
      "value": "...",
      "source": "customer_message | technician_note | support_note",
      "timestamp": "..."
    }
  ],
  "recommended_next_stage": "verify_telemetry | retry_activation | dispatch_followup | inventory_reconciliation | billing_review | human_exception_review | closure_candidate",
  "recommendation_confidence": 0.0,
  "closure_block_reason_code": "none | missing_authoritative_signal | stale_authoritative_signal | source_contradiction | low_category_confidence | low_recommendation_confidence | high_impact_exception | invalid_agent_output",
  "audit_explanation": "generated once and logged for this stage-transition event"
}
```

## Rules

- Output must validate against closed enums.
- Policy must never parse `audit_explanation`.
- `extracted_claims` never override structured authoritative evidence.
- Claims can inform failure category, urgency, audit explanation, and recommended route.
- `category_confidence` and `recommendation_confidence` are separate.
- Low category confidence means the failure type is unclear.
- Low recommendation confidence means the next action is unclear.
- Either confidence issue can block closure.

## Confidence Validation

- `category_confidence >= 0.75` requires at least one non-`none` rationale code.
- `category_confidence >= 0.90` requires two independent rationale codes or one high-specificity code.
- `failure_category: unclassified` requires `category_confidence <= 0.40`.
- `interpretation_rationale_codes: ["none"]` requires low confidence or `unclassified`.
- Category/rationale conflicts invalidate output.
- Confidence must be capped if rationale codes lack supporting extracted claims.

## Invalid Output Examples

- `failure_category: unclassified` with `category_confidence: 0.95`.
- `recommended_next_stage: closure_candidate` with non-`none` block reason.
- `recommended_next_stage: closure_candidate` with low recommendation confidence.
- `failure_category: billing_hold` with only `mentions_device_mismatch`.
- Bad enum, missing required field, impossible confidence value.

## Operational Meaning

The agent is useful when it:

- turns notes/messages into structured, valid, evidence-backed signals,
- classifies failure mode better than generic retry,
- prepares useful human handoff packets,
- produces stable explanations tied to events,
- improves route selection without weakening policy.

The agent is failing when it:

- emits invalid schema,
- outputs unsupported high confidence,
- repeatedly returns `unclassified` despite sufficient signal,
- recommends unsafe closure,
- ignores adversarial pressure markers,
- produces inconsistent explanations for the same event.
