# Hard Gate 2-Hour Live Run Checklist

Date: 2026-06-25

Purpose: guide the next focused live run after the current Studio Web repair. This is an execution plan, not a results log. It exists so a future agent can resume after context compaction without re-deciding the gate order.

Scope:

- Finish the G-004 live proof if the repaired case can run.
- Decide G-001, G-002, and G-003 statuses from the same fresh case where possible.
- If gates permit, implement only the smallest UiPath-grounded build slice needed to connect the local service-recovery model to visible UiPath evidence.

Do not start broad implementation during this block. Do not edit application code until the hard-gate disposition is recorded. Do not claim platform behavior from intent, screenshots alone, or local evals.

## Operating Loop

Use this loop for each chunk:

1. Observe: record the current UI/CLI state, IDs, version, and exact evidence path.
2. Plan: name the gate, assumption, files/artifacts affected, and pass condition.
3. Act: make the smallest live platform action or doc update.
4. Evaluate: mark PASS, PARTIAL, FAIL, or BLOCKED against `docs/validation/VALIDATION_GATES.md`.
5. Reflect: note architecture impact and the next allowed slice.
6. Log: update only the required result docs after the run, then commit if meaningful.

For this checklist edit, the only planned write is this file and optionally `waves/07_uipath_grounded_build_plan.md`. During the live run, update the normal logs only after observations are real.

## Starting State To Reuse

- UiPath org: `keepingitlowkey`.
- Tenant: `DefaultTenant`.
- User observed in UI: `Arshdeep Singh`.
- Studio Web solution ID: `b6446ea0-7ebd-4712-ccbf-08ded1e3ee41`.
- Maestro Case project ID: `35207db4-6227-4833-aee1-5cb461f3eb69`.
- Maestro Case file ID: `31c38730-c81e-40e2-be4d-c71a7e6031e5`.
- Action app project ID: `986ee0c8-915c-4569-8df9-a74b454589a9`.
- Action key: `5e4cfd91-d8f9-46f7-83da-fdb3572e6ece`.
- Orchestrator folder from prior deployment: `Solution`, folder key `9d7ae568-d60e-4395-94d7-db115bfb25de`.
- Existing published solution version: `1.0.0`.
- Prior live case identifier: `CASE-693515549`.
- Prior live Maestro case ID: `320c067a-27b9-4c2f-8b26-f6ee38ad97cc`.
- Prior live case instance / job key: `e1dbad8e-e37c-409d-8cfb-5f4e6125102b`.
- Prior runtime incident ID: `D689487C-F874-4E2C-B5ED-B0F6814630AF`.
- Prior runtime incident error: `The Title field is required.`
- Design-time repair is documented: `SimpleApprovalApp` remains in `Stage 1`, the title was set to `Review service recovery evidence`, and the visible task validation warning cleared.
- `Manage > Versions` still showed only `1.0.0`; no repaired package version was published at the last checkpoint.

## Not Yet Proven

- The repaired case definition has not been published as `1.0.1` or later.
- The repaired version has not been deployed or activated.
- A fresh case instance has not reached Action Center after the title repair.
- G-001 is not pass-certified: prior case view showed runtime order/timestamps/incidents, but not service-recovery evidence state, policy versions, raw agent recommendation, policy decision, closure block reason, or reviewer outcome.
- G-002 is not pass-certified: active-case `interpretation_policy_version`, `decision_policy_version`, and explicit migration event behavior are not proven.
- G-003 is not pass-certified: Action Center evidence-packet rendering and structured return are not proven.
- G-004 is not pass-certified: raw `closure_candidate` agent recommendation has not been shown separately from final policy override in a live case.

## Evidence Setup

Create or reuse the dated evidence folder:

```sh
mkdir -p docs/validation/artifacts/2026-06-25
git status --short
uip --version
```

Record browser evidence with screenshots only when the screen proves a gate condition or a blocker. Record exact URLs only if they contain no secrets. Never store cookies, tokens, MFA codes, or credentials.

Keep screenshots that prove:

- published version exists after repair,
- deployed/activated package version,
- fresh case/job started after the repair,
- Action Center task rendering after repair,
- structured submit/outcome returned to case,
- one case view or one query reconstructing gate fields,
- policy version fields on the active case,
- raw agent recommendation visible before policy override.

Drop screenshots that only show:

- generic loading states,
- duplicate navigation pages,
- broad portal home pages without IDs,
- screenshots containing secrets or irrelevant user data,
- failed click attempts already superseded by a clearer success/failure screenshot.

Recommended new evidence names:

- `g003-repaired-version-published.png`
- `g003-repaired-version-deployed.png`
- `g003-fresh-case-started-after-title-repair.png`
- `g003-action-center-task-after-title-repair.png`
- `g003-action-center-structured-submit.png`
- `g001-fresh-case-execution-trail-after-repair.png`
- `g002-policy-version-fields-live-case.png`
- `g004-raw-agent-before-policy-override-live-case.png`

## Chunk 1: Publish And Activate Repair, 0-30 Minutes

Gate focus: unblock G-003 and fresh-case G-001/G-004 evidence.

Assumption being tested: the title repair can be published and deployed without changing the architecture.

Browser steps:

1. Open the existing Studio Web solution and `Maestro Case` case plan.
2. Confirm `SimpleApprovalApp` is under `Stage 1`.
3. Confirm the task title is `Review service recovery evidence`.
4. Publish a repaired version, preferably `1.0.1`, with release notes `G-003 title repair validation`.
5. Open `Manage > Versions` and capture the version list.
6. Deploy/activate the repaired package version.
7. Open the deployed Orchestrator `Solution` folder.
8. Confirm the runnable process/package version reflects the repaired version, not only `Solution.caseManagement.Maestro.Case@1.0.0`.

CLI evidence to capture if available:

```sh
uip --version
```

Browser evidence to capture:

- version list after publish,
- deployment success/failure screen,
- Orchestrator package/process version,
- any deployment warning or validation error.

Exit criteria:

- PASS: a repaired version is published, deployed, activated, and visibly runnable.
- BLOCKED: publish/deploy cannot be completed through Studio Web, alternate browser, or known UiPath CLI actions without unknown/destructive steps.
- If BLOCKED, stop the live rerun. Log the publish/versioning blocker. Do not infer Action Center behavior from the unpublished repair.

Commit checkpoint after logging, if meaningful:

```sh
git status --short
git add docs/validation/VALIDATION_RESULTS.md docs/logs/BUILD_LOG.md docs/logs/RISK_REGISTER.md docs/product/PRODUCT_FEEDBACK_AWARD.md docs/decisions/DECISIONS.md
git commit -m "Log repaired Maestro Case publish gate result"
```

Only include files that actually changed. Do not commit in this checklist-prep task.

## Chunk 2: Start Fresh Case And Finish G-004, 30-75 Minutes

Gate focus: G-004, with G-001 evidence captured from the same run.

Assumption being tested: the demo can show raw agent recommendation separately from final policy decision in a live Maestro Case.

Browser steps:

1. Start a fresh `Maestro Case` job from Orchestrator.
2. Use entry point `Trigger 1` and `{}` input only if the same minimal start path is still exposed.
3. Record the new case identifier, Maestro case ID, job key, package version, start time, and folder.
4. Open the case from Orchestrator using `Open in Maestro`.
5. Look for event, variable, form, or case data that can show:
   - `recommended_next_stage: closure_candidate`,
   - `decision: override_recommendation`,
   - `from_recommended_stage: closure_candidate`,
   - `to_stage: verify_telemetry` or equivalent,
   - `closure_block_reason_code: missing_authoritative_signal` or `stale_authoritative_signal`.
6. Capture the before/after boundary in one controlled screen if possible. If not, capture the smallest set of screens that proves the link between raw recommendation and policy decision.

Browser evidence to capture:

- fresh job/case header with IDs,
- visible raw recommendation,
- visible final policy decision,
- event/order/timestamp linkage between them.

Exit criteria for G-004:

- PASS: the same live case visibly persists raw recommendation and final policy decision as separate linked evidence before/after override.
- PARTIAL: both values exist but require awkward navigation or are not linked clearly enough for the demo.
- FAIL: the platform path hides or overwrites the raw recommendation unless custom audit events/UI are added.
- BLOCKED: fresh case cannot run far enough to inspect the fields.

Decision after G-004:

- If PASS/PARTIAL, keep Maestro Case as primary and plan explicit audit/event display if demo legibility is weak.
- If FAIL, do not fake the override. Use explicit custom audit events and/or a Case App/custom evidence view as the implementation requirement.

Commit checkpoint after logging, if meaningful:

```sh
git status --short
git add docs/validation/VALIDATION_RESULTS.md docs/logs/BUILD_LOG.md docs/logs/RISK_REGISTER.md docs/product/PRODUCT_FEEDBACK_AWARD.md docs/decisions/DECISIONS.md
git commit -m "Log live agent override visibility gate"
```

## Chunk 3: Decide G-001, G-002, G-003, 75-115 Minutes

Gate focus: record the remaining hard-gate statuses from the fresh case before building.

### G-001 Native Case State / Audit Reconstruction

Check in the fresh case:

- evidence state at each stage,
- policy version active,
- raw agent recommendation,
- policy decision,
- closure block reason,
- human action if present,
- timestamp/order of events,
- job/case linkage,
- incident linkage if any.

Evidence:

- one case view screenshot or one query output that reconstructs all fields,
- if not possible, screenshots showing the missing fields and where manual log archaeology would be required.

Exit criteria:

- PASS: one view or one query reconstructs all required fields.
- PARTIAL: native history reconstructs runtime order but misses service-recovery domain fields.
- FAIL: reconstruction requires manual log archaeology across many unrelated views.

Implementation implication:

- PASS: use native case history as the main audit surface.
- PARTIAL/FAIL: implement explicit custom audit events and a one-query/event view in the smallest UiPath-grounded slice.

### G-002 Policy Version Pinning

Check in the fresh case:

- `interpretation_policy_version`,
- `decision_policy_version`,
- persistence across at least one transition,
- whether a migration can be represented as an explicit audited event.

Evidence:

- active case data screen with both versions,
- post-transition screen showing unchanged versions,
- any migration-event shape if available.

Exit criteria:

- PASS: version fields persist and migration can be explicitly audited.
- PARTIAL: metadata fields can be represented but native pinning/migration is not automatic.
- FAIL: versions cannot be attached to or recovered from active case state without custom storage.

Implementation implication:

- PASS/PARTIAL: store policy versions explicitly as case metadata and audit event fields.
- FAIL: use Data Fabric/Data Service or local simulated audit storage for demo truth, with Maestro linking to it.

### G-003 Human Evidence Packet

Check in Action Center or the chosen review surface:

- evidence table,
- agent output,
- policy decision,
- block reason,
- recommended options,
- approve/reject/request-evidence/comment result returned as structured data.

Evidence:

- rendered packet before submit,
- submitted reviewer outcome,
- case/action data after submit.

Exit criteria:

- PASS: reviewer sees the packet clearly and result returns as structured data.
- PARTIAL: Action Center works but packet is generic or only partly structured.
- FAIL: Action Center/custom task path cannot support the required packet.
- BLOCKED: Actions remains unavailable or the task never renders.

Implementation implication:

- PASS: use Action Center for the evidence packet.
- PARTIAL: prefer Case App/custom evidence-packet UI for demo legibility.
- FAIL/BLOCKED: implement a custom review surface and keep Action Center only as a platform note if useful.

Commit checkpoint after logging, if meaningful:

```sh
git status --short
git add docs/validation/VALIDATION_RESULTS.md docs/logs/BUILD_LOG.md docs/logs/RISK_REGISTER.md docs/product/PRODUCT_FEEDBACK_AWARD.md docs/decisions/DECISIONS.md
git commit -m "Decide hard Maestro Case validation gates"
```

## Chunk 4: Smallest UiPath-Grounded Build Slice, 115-120 Minutes Or Next Session

Start this only if:

- G-004 is PASS or PARTIAL with a clear explicit-audit fallback,
- G-001/G-002/G-003 statuses are logged,
- no hard gate requires abandoning Maestro Case as the primary track,
- the build slice can be completed without broad scaffolding.

Do not start this slice in the same session if gate logging is not done.

Smallest allowed slice:

1. Create one canonical green business fixture variant for the demo:
   - CRM/order active or resolved,
   - billing clear,
   - support note resolved,
   - network telemetry missing/stale,
   - agent recommendation `closure_candidate`,
   - policy override to verification/retry.
2. Persist the following fields into the chosen UiPath-visible state:
   - `case_id`,
   - `fixture_id`,
   - `derived_evidence_state`,
   - `interpretation_policy_version`,
   - `decision_policy_version`,
   - `recommended_next_stage`,
   - `policy_decision`,
   - `closure_block_reason_code`,
   - `audit_explanation`.
3. Link raw recommendation and final policy decision as separate events.
4. Make only one route visible: missing/stale telemetry to verification/retry with SLA still open.
5. Run the narrowest local validation to keep fixture semantics honest:

```sh
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
```

Exit criteria:

- a fresh UiPath-visible run shows the same canonical fixture values that local tests/evals expect,
- raw recommendation and policy decision are separate,
- policy versions are pinned in visible state or explicit audit events,
- no contradiction route, human packet polish, dashboard, or Test Cloud work is started yet.

Commit checkpoint after implementation, if meaningful:

```sh
git status --short
git add <only files changed for the slice>
git commit -m "Add UiPath-grounded missing telemetry slice"
```

## Next Build Slices After Gates

Execute these in order. Stop after the first slice that fails validation.

1. Canonical green business fixture:
   - Build the shared CRM/order/billing/support baseline used by both 2A and 2B.
   - Exit when local evals and one UiPath-visible case agree on fixture IDs and field names.
2. Missing telemetry route:
   - Route `missing_pending` or stale authoritative telemetry to verification/retry with SLA clock open.
   - Exit when G-004-style override remains visible.
3. Contradiction route:
   - Change only authoritative telemetry/inventory from the canonical fixture.
   - Route `contradicting` to elevated severity and human exception review.
   - Exit when 2A and 2B are visually distinct from the same business baseline.
4. Evidence packet content:
   - Add evidence table, agent output, policy decision, block reason, recommended options, and structured reviewer outcome.
   - Use Action Center only if G-003 PASS; otherwise use Case App/custom UI.
5. Audit event linkage:
   - Add one-query/event reconstruction for raw recommendation, policy decision, block reason, policy versions, human action, timestamps, and case/job linkage.
   - Required if G-001 is PARTIAL/FAIL.
6. Demo runbook:
   - Create the repeatable operator steps for missing telemetry, contradiction, unstructured note route change, and eval/policy-improvement beat.
7. Test Cloud mapping if available:
   - Map local eval scenarios to Test Cloud or document a UiPath-compatible harness if full Test Cloud execution is too heavy.
   - Do not block the core demo on full Test Cloud if the mapping is clear and honest.

## Required Logging After The Live Run

Update only after real observations:

- `docs/validation/VALIDATION_RESULTS.md`: exact environment, steps, observed behavior, result, evidence paths.
- `docs/logs/BUILD_LOG.md`: actions, commands, validation status, next step.
- `docs/logs/RISK_REGISTER.md`: only if likelihood/status changed.
- `docs/decisions/DECISIONS.md`: only for material architecture decisions.
- `docs/product/PRODUCT_FEEDBACK_AWARD.md`: only for concrete product feedback.

Result vocabulary:

- PASS: documented pass condition was observed.
- PARTIAL: path works but misses a required proof element.
- FAIL: platform behavior blocks the required architecture without fallback.
- BLOCKED: the run could not reach the validation point.

Do not update `AGENTS.md`, architecture docs, data model, product feedback, decisions, or main validation results during plan preparation. During execution, update them only when the live observations require it.
