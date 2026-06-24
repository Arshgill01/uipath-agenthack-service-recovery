# Next Demo Architecture Plan

Status: planning artifact for the next implementation wave after G-001 through G-004 are PASS/PARTIAL with documented implications. Do not treat this as approval to start broad implementation before the hard gates are resolved or explicitly waived.

## Product Shape

Build a concrete telecom service recovery Case, not a generic AI governance product.

The real submission should first prove one narrow governed recovery loop:

1. A Maestro Case instance receives the canonical "business systems green" fixture.
2. A structured Agent Interpretation Event records the raw recommendation.
3. A deterministic Policy Decision Event links to the agent event and decides the route.
4. Maestro Case moves the work to the correct stage.
5. A human reviewer sees the exception packet when policy requires review.
6. The case audit can reconstruct the event chain without manual log archaeology.

Everything else should stay local/provisional until that loop works end to end.

## Highest-Leverage Build First

Build first:

- Maestro Case stages for `intake`, `evidence_verification`, `retry_with_sla`, `exception_investigation`, `human_review`, `remediation`, `closure_candidate`, and `closed`.
- Simulated CRM/order, billing, network telemetry, inventory, dispatch, and support-note evidence calls through the lightest UiPath-supported path.
- First-class `Agent Interpretation Event` and `Policy Decision Event` records with `agent_event_id` linkage.
- Case fields for `interpretation_policy_version`, `decision_policy_version`, `derived_evidence_state`, `severity`, `case_stage`, and closure block reason.
- One human evidence packet for the contradiction route.
- One eval/policy-improvement artifact that proves the system improves under human approval, not self-mutation.

Keep local/provisional:

- Telecom system adapters beyond simple simulated responses.
- Full metrics dashboard; show calculated business-impact numbers in the demo/deck instead.
- Full Test Cloud integration if it cannot be validated quickly; keep the local eval harness and map it honestly to Test Cloud intent.
- Broad failure taxonomy beyond the minimum scenarios in `docs/validation/EVAL_PLAN.md`.
- Production-style policy management UI.

Show live:

- 2A missing/stale authoritative evidence causing policy override from `closure_candidate` to verification/retry.
- 2B contradicting authoritative evidence causing elevated human review.
- The linked raw Agent Interpretation Event and Policy Decision Event.
- The human evidence packet if G-003 proves a readable packet path.
- Case stage/severity/SLA movement if G-005/G-006 make it legible.

Narrate honestly:

- Simulated telecom systems.
- Any Test Cloud mapping that remains a local eval harness.
- Any fallback audit store or custom packet used because native Maestro/Action Center surfaces were insufficient.

Do not show as if live:

- Production telecom integrations.
- Automatic policy promotion.
- Closure from agent recommendation alone.
- Generic governance dashboards detached from the service-recovery case.

## Stage Model

| Stage | Demo responsibility | Implementation priority |
| --- | --- | --- |
| `intake` | Create the case with customer, service, order, SLA, and policy versions. | Required for first live run. |
| `evidence_verification` | Collect business-system and authoritative evidence. | Required for 2A/2B. |
| `retry_with_sla` | Show missing/stale telemetry is recoverable verification work, not a high-impact contradiction. | Required for 2A. |
| `exception_investigation` | Show contradiction is more severe than missing evidence. | Required for 2B. |
| `human_review` | Present the evidence packet and capture structured reviewer outcome. | Required if G-003 path is viable; otherwise use custom packet fallback. |
| `remediation` | Represent approved action after review. | Keep minimal. |
| `closure_candidate` | Show policy closure check, not agent closure authority. | Required for the override proof. |
| `closed` | Terminal only after fresh authoritative confirmation. | Demo only if closure criteria are satisfied. |

## Data And Event Model

The demo should make these records visible or reconstructable:

- `Case`: `case_id`, `customer_id`, `service_id`, `case_stage`, `severity`, `sla_deadline`, `interpretation_policy_version`, `decision_policy_version`, `derived_evidence_state`.
- `Evidence Signal`: `field`, `source`, `value`, `authoritative`, `freshness_status`, `ttl_seconds`, `observed_at`.
- `Agent Interpretation Event`: `event_id`, `input_refs`, `failure_category`, confidence fields, rationale codes, `recommended_next_stage`, `closure_block_reason_code`, `audit_explanation`, `valid_schema`.
- `Policy Decision Event`: `event_id`, `agent_event_id`, `decision`, `from_recommended_stage`, `to_stage`, `reason_codes`, `decision_policy_version`, `created_at`.
- `Human Review Event`: reviewer role, decision, comment, evidence packet reference, timestamp.
- `Policy Improvement Case`: trigger, proposed diff, eval result reference, approval status, new policy version when promoted.

The `Agent Interpretation Event` and `Policy Decision Event` must remain separate first-class artifacts. The policy event links to the agent event; it does not overwrite it.

## Human Evidence Packet

The packet should fit one reviewer screen and include:

- Case identity: customer, service, order, current stage, severity, SLA.
- Evidence table: CRM/order, billing, network telemetry, inventory/device assignment, dispatch, support/tech note.
- Freshness indicators and TTL for authoritative signals.
- Raw Agent Interpretation Event summary, including recommendation and confidence.
- Policy Decision Event summary, including override/block reason and policy version.
- Derived evidence state and source-authority explanation.
- Recommended reviewer actions: approve remediation, reject, request more evidence, close after confirmation.
- Structured reviewer outputs: decision enum, comment, optional requested evidence, reviewer role, timestamp.

If Action Center renders this generically or hides the agent/policy boundary, use a Case App/custom packet for the demo while still recording the Action Center limitation as product feedback.

## Demo Proof Sequence

1. Start with the canonical green business fixture: CRM/order active, billing clear, support note resolved.
2. Run 2A by making authoritative network telemetry missing or stale.
3. Show the agent recommends `closure_candidate`.
4. Show policy creates a linked decision that overrides to `verify_telemetry` or `retry_with_sla` with `missing_authoritative_signal` or `stale_authoritative_signal`.
5. Reset to the same green business fixture and run 2B with only fresh authoritative telemetry or inventory changed to contradiction.
6. Show severity escalation and route to `exception_investigation` or `human_review`.
7. Show the evidence packet and structured reviewer outcome.
8. Show one unstructured note route change, such as device mismatch or access blocker.
9. Show eval results and a policy improvement case that requires human approval before promotion.

## Decision Points Before Implementation

Action Center versus Case App/custom packet:

- Use Action Center as the review surface only if G-003 proves the required evidence table, agent output, policy decision, block reason, recommended actions, and structured return are readable.
- Use Case App/custom packet if Action Center technically works but hides the packet structure or weakens the demo.
- If both work, prefer the surface that best shows the reviewer decision and linked event boundary in one screen.

Native Case state versus explicit audit store:

- Use native Case state/history only if G-001 proves one-view or one-query reconstruction of evidence state, policy versions, raw recommendation, policy decision, closure block, human action, and timestamps.
- Add Data Fabric/Data Service or explicit custom audit events if reconstruction requires manual log archaeology.

Native version fields versus explicit metadata:

- Use native fields only if G-002 proves active cases persist interpretation and decision policy versions without silent changes.
- Otherwise store versions as explicit case metadata and emit migration events.

Raw recommendation visibility:

- Use native event/timeline UI if G-004 proves raw recommendation is visible before final policy decision.
- Otherwise make the Agent Interpretation Event and Policy Decision Event visible through the custom audit view or packet, while keeping them linked in persisted data.

## Platform Facts Still Needed

Before broad implementation, validate:

- Whether a live Maestro Case instance can be published/debugged and reconstructed for G-001.
- Whether policy versions can be pinned on active cases for G-002.
- Whether `Human action placeholder` or `Create new Action app` can render and return the full evidence packet for G-003.
- Whether raw agent recommendation and policy override can be shown separately in the same run for G-004.
- Whether policy output can drive distinct 2A and 2B Case routes for G-005.
- Whether Case App/Case instances can make severity, SLA, stage, and block reason legible for G-006.
- Whether Test Manager/Test Cloud can host or reference the local eval scenarios for G-007.
- Whether UiPath CLI/skills can provide a visible coding-agent lifecycle proof for G-008.

## Stop Rule

If any hard gate fails, stop and update `docs/decisions/DECISIONS.md` with the chosen fallback before building. The fallback may still be competitive if it is honest: Maestro Case remains the lifecycle backbone, explicit events preserve the agent/policy boundary, and the custom surface exists only to make evidence and review legible.
