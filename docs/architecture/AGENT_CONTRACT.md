# Agent Contract

The agent converts ambiguous unstructured evidence into structured signals and a useful triage recommendation package. It does not mutate policy, and its recommendation is not final until policy decides.

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
  "closure_block_reason_code": "none | missing_authoritative_signal | stale_authoritative_signal | source_contradiction | low_category_confidence | low_recommendation_confidence | high_impact_exception | high_interpretation_disagreement | invalid_agent_output",
  "audit_explanation": "generated once and logged for this stage-transition event",
  "urgency": "low | normal | high | critical",
  "customer_impact_summary": "business impact and customer-risk summary",
  "evidence_gaps": ["specific evidence still needed"],
  "recommended_actions": ["operator or reviewer actions the agent recommends"],
  "reviewer_questions": ["questions for human exception review"],
  "operator_note": "short operational note for the case owner"
}
```

## Optional Adversarial Interpretation

The Gemini-backed demo path can run two structured interpretations over the same notes:

- resolution advocate: strongest honest case for closure or recovery,
- closure skeptic: strongest honest case against premature closure.

Both calls must independently satisfy the same agent contract above. The synthesized Agent Interpretation Event preserves the advocate's raw recommendation and stores the full advocate/skeptic trace under `adversarial_interpretation`.

Policy receives only the structured disagreement metadata, not prose:

```json
{
  "disagreement_score": 0.826,
  "threshold": 0.6,
  "stage_match": false,
  "confidence_delta": 0.42,
  "claim_overlap_ratio": 0.0,
  "advocate_recommendation": "closure_candidate",
  "skeptic_recommendation": "human_exception_review",
  "unique_skeptic_gaps": ["confirm upstream signal stability"]
}
```

If the score crosses threshold, policy may add `high_interpretation_disagreement` and route to human review. This does not relax validation: a `closure_candidate` still requires `recommendation_confidence >= 0.75` and `closure_block_reason_code: none`.

## Rules

- Output must validate against closed enums.
- Policy must never parse `audit_explanation`.
- `extracted_claims` never override structured authoritative evidence.
- Claims can inform failure category, urgency, audit explanation, and recommended route.
- The agent may recommend closure, retry, investigation, or human review; policy may accept, override, downgrade, or escalate that recommendation.
- The triage package is useful to humans and operators, but does not override authoritative structured evidence.
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
- identifies customer impact, urgency, evidence gaps, remediation actions, and reviewer questions,
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
