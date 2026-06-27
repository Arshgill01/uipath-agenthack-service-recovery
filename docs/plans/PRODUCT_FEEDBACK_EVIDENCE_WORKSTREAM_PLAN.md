# Product Feedback Evidence Workstream Plan

Date: 2026-06-27.

Objective: gather deeper UiPath product-feedback evidence through sustained, scoped workstreams. This plan exists because one-probe threads completed too quickly and left useful but shallow evidence. Future threads should run probe queues, not declare success after the first finding.

## Operating Rule

A product-feedback evidence thread is not complete when it finds one useful issue. It is complete only when one of these is true:

- it finishes its assigned probe queue,
- it reaches the agreed timebox,
- it hits the same external blocker three times and records why further progress would be unsafe or repetitive,
- continuing would mutate existing submission resources, tenant-wide settings, credentials, billing, or destructive state without explicit approval.

## Global Guardrails

- Use org `keepingitlowkey`, tenant `DefaultTenant`.
- Use scratch names prefixed `PFPROBE-20260627-`.
- Do not modify existing submission processes, packages, cases, tasks, Data Fabric entities, Test Manager baseline objects, or tenant-wide settings.
- Prefer read-only inspection first; create scratch resources only when they answer a concrete product-feedback question.
- Keep feedback fair: separate product defect candidates, UX/docs friction, platform limitations, access confusion, and user error.
- Do not claim automated Test Cloud execution, generated Action Center UI final-demo readiness, native Case history alone passing G-001, real telecom integrations, or LLM final closure authority.

## Evidence Bar

Each accepted finding needs:

- product surface and exact workflow,
- expected behavior,
- observed behavior,
- exact commands or UI steps,
- evidence artifact path, screenshot, ID, or saved output,
- workaround or mitigation,
- builder impact and severity,
- confidence level and follow-up needed,
- clear statement of whether it changes submission claims.

## Workstreams

### A. Maestro Case Human-Review Authoring

Minimum queue:

1. Inspect the scratch solution `PFPROBE-20260627-human-review` in Studio Web or CLI and determine whether the missing `Title` / missing-rule problems are visible before runtime.
2. Try the least-mutating repair path on a new scratch copy, not the existing submission Case.
3. Compare `uip maestro case validate`, `uip solution pack --dry-run`, `uip solution upload`, and Studio Web designer validation for the same scratch definition.
4. Capture at least one screenshot or saved CLI output artifact.

Target feedback: shared readiness/preflight contract across Case authoring, solution packaging, upload/import, and runtime.

### B. Action Center / Generated Action App Binding

Minimum queue:

1. Use scratch or existing read-only evidence to inspect how Action schema fields map to generated UI controls.
2. Test whether a generated-field label/binding issue can be diagnosed without starting a submission case.
3. Determine whether app version used by a Case task is discoverable before runtime.
4. Capture screenshot or API/CLI readback proving the field mapping state.

Target feedback: field-binding inspector, app-version propagation visibility, generated UI repair diagnostics.

### C. Test Manager / Test Cloud Eval Import

Minimum queue:

1. Reuse the existing `SREV` mapping read-only unless a scratch test project is necessary.
2. Look for official import/linking paths from eval/JUnit/package outputs without claiming automated Test Cloud execution.
3. If a scratch project is created, prefix it and keep it separate from `SREV`.
4. Capture exact error/readback evidence for automation discovery, folder binding, or import gaps.

Target feedback: eval-suite import, automation-discovery diagnostics, folder/package preflight.

### D. Data Fabric / Audit Storage Readback

Minimum queue:

1. Keep the validated `ServiceRecoveryAuditBundleV2` path untouched.
2. Use scratch entities only if needed to test schema/readback behavior.
3. Compare create/insert/query/get behavior for field naming and projection.
4. Capture readback evidence and distinguish validated audit proof from feedback-only failed paths.

Target feedback: schema-aware insert/import diagnostics and consistent custom-field readback.

## Main-Thread Integration

The main thread should not merge a whole evidence branch blindly. For each branch:

1. Inspect `git diff --stat` and changed files.
2. Promote only evidence-backed PF entries, validation artifacts, and build/validation log entries.
3. Remove or revise prompt artifacts that encode early-stop behavior.
4. Run `git diff --check` and `scripts/run_submission_check.sh`.
5. Commit and push a checkpoint to `master`.

## Prompt Contract For Worker Threads

Worker prompts must include:

- "Do not mark the goal complete after the first useful finding."
- "Run the whole assigned probe queue unless a stop condition is met."
- "Spend the time on evidence gathering, not final prose polish."
- "If blocked, move to the next queued probe before stopping."
- "Leave final survey wording to the main thread unless evidence changes require a short note."

