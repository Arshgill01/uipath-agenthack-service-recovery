# Demo Storyboard

This is a north-star storyboard, not video work. Update after product exists.

## Five-Minute Flow

### 0:00-0:30 Problem

Telecom service case is marked resolved in business systems, but customer still lacks service. Wrong closure creates repeat calls, SLA breaches, churn, service credits, and audit gaps.

### 0:30-1:15 Architecture

Show:

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

Show stages.

### 1:15-2:15 Missing/Stale Evidence + Policy Override

Show:

- CRM/order/billing/support note green.
- Agent recommends `closure_candidate`.
- Network telemetry missing/stale.
- Policy rejects recommendation.
- Case routes to verification/retry.
- SLA clock continues.
- Audit event logged.

This should be the most deliberate staged moment. The screen must show a before/after boundary:

- `Agent Interpretation Event`: `recommended_next_stage: closure_candidate`.
- `Policy Decision Event`: `decision: override_recommendation`, `from_recommended_stage: closure_candidate`, `to_stage: verify_telemetry`.
- `closure_block_reason_code: missing_authoritative_signal` or `stale_authoritative_signal`.

Do not rely on narration. The raw agent recommendation and policy override must both be visible.

### 2:15-3:15 Contradiction + Escalation

Show:

- Same canonical green business fixture as the prior beat, with only telemetry/inventory changed.
- Fresh telemetry or inventory contradicts.
- Severity escalates.
- Human evidence packet appears.
- Route is visibly more serious than missing evidence.

The viewer should understand that 2A and 2B start from the same business-system state. The distinction is the authoritative signal:

- missing/stale authoritative signal -> controlled retry/verification,
- contradicting authoritative signal -> elevated exception/human review.

### 3:15-4:00 Unstructured Evidence Changes Route

Show:

- Technician note reveals access blocker, device mismatch, or customer-premises issue.
- Agent converts note to structured signal.
- Policy routes to correct remediation path.

### 4:00-4:35 Eval + Learning Loop Artifact

Show:

- eval scenario list,
- missing telemetry,
- contradiction,
- adversarial pressure,
- invalid schema,
- policy improvement case with proposed diff,
- eval result,
- approval/version state.

### 4:35-5:00 Business Impact

Close with:

- MTTR,
- SLA breach reduction,
- fewer wrongful closures,
- fewer repeat contacts,
- audit completeness,
- why UiPath specifically.

## Demo Constraints

- Spend less than 30 seconds explaining telecom.
- Do not demo every failure type.
- Do not rely on narration for the override. Show it.
- Do not hide behind dashboards; show case movement and evidence.
- Do not author 2A and 2B as unrelated examples. They must be fixture variants.
