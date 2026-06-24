# Hard Gate Next Validation Runbook

Date: 2026-06-25

Scope: next live UiPath validation run for G-001 through G-004 only. Do not start broad implementation during this run.

Observed starting state:

- UiPath org: `keepingitlowkey`.
- Tenant: `DefaultTenant`.
- Action Center is enabled and opens as `Inbox - Action Center`.
- Studio Web solution `Maestro BPMN` exists.
- Maestro Case project exists with `Case plan`.
- `Human action (placeholder)` is inserted under `Stage 1`.
- No live case instance has proven runtime audit reconstruction, active-case policy version pinning, structured evidence-packet review/return, or raw recommendation visibility before policy override.

Architecture boundary:

- Agent output is structured and advisory.
- Policy decides allowed actions and must not parse prose.
- LLM output cannot close cases, override policy, override source-of-truth hierarchy, or mutate production policy.
- Closure requires fresh authoritative telemetry.
- Raw agent recommendation and final policy decision must persist as separate linked events.
- Active cases stay pinned to interpretation and decision policy versions unless explicitly migrated.

## Validation Fixture

Use one telecom service-recovery validation case family for the live run. Label all fields as validation data.

Minimal case fields to model or enter:

- `case_id`: platform-generated, expected prefix `CASE`.
- `customer_id`: `VAL-CUST-001`.
- `service_id`: `VAL-BB-001`.
- `crm_order_status`: `active`.
- `billing_status`: `clear`.
- `support_note_summary`: `Customer account marked resolved; customer reports service is still not usable.`
- `network_telemetry_status`: `missing` for the G-001/G-002/G-004 override path.
- `derived_evidence_state`: `missing_pending`.
- `interpretation_policy_version`: `interp-2026-06-25-a`.
- `decision_policy_version`: `decision-2026-06-25-a`.
- `agent_recommended_next_stage`: `closure_candidate`.
- `agent_closure_block_reason_code`: `none`.
- `policy_decision`: `override_recommendation`.
- `policy_target_stage`: `verify_telemetry`.
- `policy_closure_block_reason_code`: `missing_authoritative_signal`.
- `audit_explanation`: generated once for this stage-transition event.

If G-003 reaches a human review task, use the same case family but switch only the authoritative evidence condition for the evidence packet:

- `network_telemetry_status`: `fresh_not_live` or equivalent.
- `derived_evidence_state`: `contradicting`.
- `policy_target_stage`: `human_review` or `exception_investigation`.
- `policy_closure_block_reason_code`: `source_contradiction`.

Do not author unrelated demo data for missing/stale and contradiction paths.

## Evidence Capture

Create a timestamped artifact folder before platform interaction:

```sh
mkdir -p docs/validation/artifacts/2026-06-25-hard-gates
```

Capture screenshots or screen recordings with descriptive names:

- `g001-case-start-state.png`
- `g001-case-history-or-query.png`
- `g002-policy-version-fields-before-transition.png`
- `g002-policy-version-fields-after-transition.png`
- `g002-policy-migration-event-or-gap.png`
- `g003-action-app-config.png`
- `g003-action-center-packet.png`
- `g003-action-center-structured-return.png`
- `g004-agent-recommendation-before-policy.png`
- `g004-policy-override-after-agent.png`

Record exact URLs only if they contain no secrets. Do not store cookies, tokens, MFA codes, or credentials.

After the run, append results to:

- `docs/validation/VALIDATION_RESULTS.md`
- `docs/logs/BUILD_LOG.md`
- `docs/logs/RISK_REGISTER.md` if risk likelihood/status changes
- `docs/decisions/DECISIONS.md` only for material architecture decisions
- `docs/product/PRODUCT_FEEDBACK_AWARD.md` only for concrete UiPath product feedback

## Required Loop

For each gate:

1. Observe the current platform state.
2. Plan the smallest next action.
3. Act once.
4. Evaluate against the pass condition.
5. Reflect on architecture impact.
6. Log result and evidence path.

Stop instead of improvising if the next step would require broad implementation or unknown platform schema edits.

## G-003 First: Human Evidence Packet

Reason to run first: the current live state already has a Human action placeholder, and G-003 is the shortest path to learning whether Action Center can carry the required reviewer packet.

Smallest next actions:

1. In the existing `Maestro BPMN` Case plan, inspect the inserted `Human action (placeholder)`.
2. Try the supported configuration path in this order:
   - select the placeholder and look for task-level properties,
   - use `Create new Action app` from the Human action picker if task-level configuration is unavailable,
   - stop before manual JSON/schema edits unless official designer UI exposes the generated structure clearly.
3. Configure the smallest evidence packet with:
   - evidence table,
   - raw agent output,
   - policy decision,
   - closure block reason,
   - recommended options: approve remediation, reject closure, request fresh telemetry,
   - comment field.
4. Publish/debug/run only enough to create one human review task.
5. Open Action Center pending tasks and inspect the packet.
6. Complete the task with one structured outcome, preferably `request_fresh_telemetry`, plus a short comment.
7. Return to the Case instance and inspect whether the outcome is stored as structured case data or event data.

PASS:

- Reviewer sees evidence table, agent output, policy decision, block reason, and recommended options in Action Center or the generated Action app.
- Reviewer can choose approve/reject/request-evidence and enter a comment.
- Case receives structured outcome data, not only free-form text.
- Evidence artifacts show both reviewer UI and returned structured result.

PARTIAL:

- Human task can be created, but packet renders generically or misses fields.
- Reviewer can submit, but result is not clearly structured in the Case instance.
- Action Center works but is not demo-legible; this supports the existing Case App/custom evidence-packet fallback.

FAIL:

- No real human task can be configured or created from the current Case plan.
- Action Center cannot open the created task.
- Human outcome cannot return to the case in any inspectable form.

Stop conditions:

- The UI requires creating a production-like app or unrelated workflow beyond the minimal packet.
- The only apparent path is editing unknown Case JSON by guesswork.
- The platform requests secrets, credentials, or irreversible tenant/deployment changes.

## G-001: Native Case State / Audit Reconstruction

Smallest next actions:

1. Use the same validation case instance from G-003 if it exists; otherwise create the smallest case instance with the fixture fields above.
2. Move the case through at least two observable moments:
   - initial evidence/policy state,
   - policy override or human review task creation/completion.
3. Inspect Case instance view, Case app, history/timeline, incidents, and any available query/export surface.
4. Attempt one-view or one-query reconstruction of:
   - evidence state at each stage,
   - active policy versions,
   - raw agent recommendation,
   - policy decision,
   - closure block reason,
   - human action if present,
   - event timestamps/order.

PASS:

- One Case view or one query reconstructs all required fields and event order without manual log archaeology.

PARTIAL:

- Case view shows stage/state but misses agent/policy/version details.
- Multiple platform views are needed but a custom audit event or Data Fabric/Data Service path is clear.

FAIL:

- Runtime history cannot show enough event order or state to support the audit thesis.
- No live case instance can be created or inspected.

Stop conditions:

- Reconstruction depends on screenshots only.
- Reconstruction requires manually correlating unrelated logs without stable IDs.
- The required state can only be proven by broad custom implementation.

## G-002: Policy Version Pinning

Smallest next actions:

1. Confirm the active case carries both:
   - `interpretation_policy_version`,
   - `decision_policy_version`.
2. Transition the case once and inspect whether both values persist unchanged.
3. Create or simulate a newer approved version label as metadata only, for example `decision-2026-06-25-b`.
4. Confirm the active case does not silently change to the newer value.
5. If the platform supports events, add or inspect an explicit migration event shape without migrating the active validation case.

PASS:

- Active case persists both policy versions across transitions.
- Newer policy version does not silently affect the active case.
- Explicit migration can be represented as an audited event.

PARTIAL:

- Versions can be stored as custom fields or metadata, but native pinning is not available.
- Migration event requires custom audit/Data Fabric/Data Service.

FAIL:

- Active case cannot carry stable policy version fields.
- Platform silently replaces or hides active policy versions.

Stop conditions:

- Proving pinning requires changing production policy or tenant-wide settings.
- The only path is unverified JSON edits.

## G-004: Agent Recommendation Visible Before Override

Smallest next actions:

1. Use the G-001 case instance and missing telemetry fixture.
2. Persist or display the raw agent recommendation before policy action:
   - `recommended_next_stage: closure_candidate`,
   - `recommendation_confidence`,
   - `audit_explanation`,
   - stable `agent_event_id` if available.
3. Persist or display the final policy decision separately:
   - `decision: override_recommendation`,
   - `from_recommended_stage: closure_candidate`,
   - `to_stage: verify_telemetry`,
   - `reason_codes: ["missing_authoritative_signal"]`,
   - link/reference to the raw agent event if available.
4. Capture the before/after UI or event view.

PASS:

- The same live run shows raw recommendation separately from final policy decision.
- The raw recommendation is visible before or alongside the policy override in a controlled demo surface.
- The final policy decision links to or clearly references the raw recommendation.

PARTIAL:

- Both values can be stored, but visibility requires Case App/custom view.
- Event linkage exists only as custom metadata, not native timeline.

FAIL:

- Raw recommendation is overwritten by final policy decision.
- The demo cannot show the agent/policy boundary without fake screenshots.

Stop conditions:

- The next step would make the LLM decide closure or mutate policy.
- The platform only supports a single final status field with no separate advisory event.

## Evaluation Order And Branches

Recommended order:

1. G-003 packet configuration and task creation.
2. G-001 live instance state/history reconstruction.
3. G-002 version persistence on the same instance.
4. G-004 raw recommendation and policy override visibility on the same instance.

If G-003 fails before a live task can be created, continue G-001/G-002/G-004 with the smallest non-human case instance only if the Case designer provides a safe publish/debug path.

If G-001 fails native reconstruction, do not keep searching manually across platform surfaces. Mark G-001 PARTIAL/FAIL and decide whether custom audit events plus Data Fabric/Data Service are required.

If G-004 cannot be shown natively but custom fields/events can preserve the boundary, mark PARTIAL and keep the custom audit/Case App fallback.

## Run Completion Criteria

The run is complete when each hard gate has one of PASS, PARTIAL, or FAIL with:

- exact platform environment,
- exact steps,
- observed behavior,
- artifact paths,
- decision impact,
- follow-up or stop condition.

Do not mark any hard gate PASS from local/provisional eval results alone. Local results can support fixture discipline and expected behavior only.
