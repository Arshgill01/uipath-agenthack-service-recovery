# Policy Model

Decision policy is deterministic. It consumes authoritative evidence, agent structured signals, current case state, and policy versions.

## Source Authority

| Field | Authoritative source | Supporting sources | Notes |
| --- | --- | --- | --- |
| `service_live_status` | Network telemetry | Support notes, customer report | Fresh telemetry wins over CRM/support text. |
| `crm_order_status` | CRM/order system | Support notes | CRM/order owns order lifecycle, not live service truth. |
| `billing_status` | Billing system | CRM | Billing owns holds/overdue state. |
| `inventory_assignment` | Inventory/activation system | Technician notes | Device/service assignment must match order. |
| `dispatch_status` | Dispatch system | Technician notes | Dispatch owns appointment/access state. |
| `customer_pressure` | Agent extraction | Customer/support messages | Informs urgency/risk; never truth state. |

## Evidence Reconciliation

Policy derives:

```json
{
  "derived_evidence_state": "confirmed_aligned | missing_pending | contradicting | authoritative_unavailable_or_stale",
  "closure_allowed": false,
  "reason_codes": ["missing_authoritative_signal"],
  "target_stage": "verify_telemetry",
  "severity": "normal | elevated | critical"
}
```

## Closure Eligibility

Closure requires:

- fresh authoritative network telemetry confirming service live,
- no unresolved contradiction across material fields,
- no active billing hold,
- inventory/device assignment aligned,
- no unresolved human-review requirement,
- valid agent output or agent output not required for closure,
- audit explanation logged for latest stage transition.

No single source owns closure eligibility. It is a derived decision.

## Policy Override

Policy can:

- accept agent recommendation,
- downgrade agent recommendation,
- block closure,
- route to safer stage,
- require human review,
- mark agent output invalid.

The demo must show at least one override.

## Reviewer Handoff

When closure is blocked or routed to human review, the reviewer packet carries a deterministic closure-readiness checklist. The checklist answers what must be true before closure, using structured evidence and policy reason codes rather than agent prose.

Current checklist criteria:

- fresh authoritative telemetry confirms service is live,
- no unresolved source contradiction remains,
- billing has no active hold,
- inventory assignment matches the order,
- required human review has resolved the exception when the route is `human_review`,
- advocate/skeptic disagreement is resolved when `high_interpretation_disagreement` is present.

Policy also emits route-specific reviewer questions. For example, missing telemetry asks which authoritative retry/source will produce `service_live_status`; contradiction asks why business systems show active while fresh authoritative service evidence disagrees; high interpretation disagreement asks which interpretation is supported by authoritative evidence and which skeptic-only gap must be resolved. These questions guide the human; they do not grant the agent closure authority.

## Interpretation Disagreement

Policy can consume a structured `interpretation_disagreement` object produced by the optional advocate/skeptic LLM path. Policy does not parse either LLM's prose explanations.

If `disagreement_score >= 0.60`, policy adds reason code `high_interpretation_disagreement`, sets severity to `elevated`, and routes to `human_review`.

This is a separate safety signal from stale telemetry or source contradiction:

- missing/stale authoritative evidence still routes to verification/retry,
- fresh authoritative contradiction still routes to elevated human exception review,
- high advocate/skeptic disagreement routes to human review because the same unstructured evidence produced materially different structured recommendations.

The agent validator is unchanged. Adversarial mode may preserve a raw advocate `closure_candidate`, but it must remain valid under the normal closure-candidate confidence and block-reason rules.

## Versioning

Separate policy families:

- Interpretation policy: schema, prompts, rationale codes, examples, confidence validation.
- Decision policy: source authority, TTLs, closure eligibility, human approval rules, SLA thresholds.

Rules:

- Active cases stay pinned to the policy versions they started with.
- New cases use latest approved versions.
- Migration requires explicit audit event.
- Decision policy changes require stricter approval than interpretation policy changes.
