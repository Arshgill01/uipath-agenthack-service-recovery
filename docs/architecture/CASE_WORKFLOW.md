# Maestro Case Workflow

## Stages

| Stage | Purpose | Entry triggers | Exit conditions |
| --- | --- | --- | --- |
| `intake` | Create case from customer/support/order event. | New failed activation/restoration signal. | Case has identifiers and initial context. |
| `evidence_verification` | Query systems and collect unstructured notes/messages. | Intake complete or new evidence requested. | Evidence state derived. |
| `retry_with_sla` | Automated verification/retry when evidence is missing/stale but not contradicting. | `missing_pending` or stale authoritative signal. | Fresh evidence arrives, retry succeeds/fails, SLA threshold reached. |
| `exception_investigation` | Investigate contradicting sources or severe inconsistencies. | `contradicting` evidence state. | Human review packet prepared or contradiction resolved. |
| `human_review` | Human evaluates high-impact exception or risky remediation. | Contradiction, invalid agent output, low confidence with impact, risky action. | Human approves/rejects/requests evidence. |
| `remediation` | Execute allowed remediation path. | Approved or policy-allowed remediation. | Fresh authoritative evidence confirms state or failure returns to verification. |
| `closure_candidate` | Final closure check. | All closure criteria satisfied. | Closed or rejected by policy. |
| `closed` | Case complete with audit trail. | Closure approved by policy. | Terminal. |

## Core Transition 2A: Missing/Stale Evidence

Setup:

- CRM/order: active/resolved.
- Billing: clear.
- Support note: resolved.
- Network telemetry: missing or stale.
- Agent recommendation: `closure_candidate`.

Policy result:

- Override recommendation.
- Block closure.
- Route to `retry_with_sla` or `evidence_verification`.
- Reason: `missing_authoritative_signal` or `stale_authoritative_signal`.

Demo requirement:

- Show raw recommendation first.
- Show policy rejection/downgrade.
- Show SLA clock continuing.

## Core Transition 2B: Contradicting Evidence

Setup:

- CRM/order: active.
- Billing: clear.
- Network telemetry: fresh `not_live`, or inventory/device mismatch.

Policy result:

- Escalate severity.
- Route to `exception_investigation` or `human_review`.
- Reason: `source_contradiction`.

Demo requirement:

- Must feel visually and tonally more serious than 2A.
- Use severity badge, human queue, and evidence packet.

## Unstructured Evidence Route Change

The agent must materially affect routing by interpreting free text into structured signals.

Example signals:

- `dispatch_dependency`: technician note says building junction/MDF access blocked.
- `inventory_mismatch`: note says ONT/router serial does not match order.
- `customer_premises_issue`: node signal present but CPE offline.

Policy still decides whether the recommended route is allowed.

## Reviewer Closure Readiness

For blocked closure and human-review routes, the packet now shows a deterministic closure-readiness checklist before the reviewer can treat the case as closable:

- fresh authoritative telemetry confirms `service_live_status=live`,
- no unresolved source contradiction remains,
- billing is clear,
- inventory assignment matches the order,
- required human review is complete when the case is in `human_review`,
- advocate/skeptic interpretation disagreement is resolved when policy raised `high_interpretation_disagreement`.

This is the judge-visible handoff: Maestro routes the case, policy explains the blocked closure criteria, and the human owns unresolved exception questions. The LLM may contribute reviewer questions and skeptic-only gaps, but policy still owns the checklist and closure gate.
