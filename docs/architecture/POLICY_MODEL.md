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

## Versioning

Separate policy families:

- Interpretation policy: schema, prompts, rationale codes, examples, confidence validation.
- Decision policy: source authority, TTLs, closure eligibility, human approval rules, SLA thresholds.

Rules:

- Active cases stay pinned to the policy versions they started with.
- New cases use latest approved versions.
- Migration requires explicit audit event.
- Decision policy changes require stricter approval than interpretation policy changes.
