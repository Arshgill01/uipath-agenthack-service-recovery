# Product Feedback Evidence Sprint

Date: 2026-06-27.

Objective: gather fresh, scoped UiPath product-feedback evidence that strengthens the Best Product Feedback submission without weakening validated submission claims.

## Guardrails

- Use org `keepingitlowkey`, tenant `DefaultTenant`.
- Prefer read-only CLI/UI inspection before creating any scratch resource.
- If creation is needed, use names prefixed `PFPROBE-20260627-`.
- Do not modify existing submission processes, packages, cases, tasks, Data Fabric entities, or tenant-wide settings.
- Stop after at most two small live probes unless there is a clear blocker and user approval.

## Current Assumption

The strongest existing feedback recommendation is still likely correct: UiPath should add a Maestro Case human-review readiness/preflight path for agent + policy + human workflows.

## Probe Plan

1. Confirm current CLI/org/tenant and inspect only enough resource state to avoid colliding with submission assets.
2. Probe A: test whether the current product/CLI exposes a discoverable readiness path for Maestro Case human-review dependencies before runtime: Actions availability, task required fields, Action app binding, package/process version selection, and reviewer visibility.
3. Probe B: if Probe A yields enough bounded evidence, test a second narrow surface that supports the same recommendation, preferably generated Action app/coded-app diagnostics or Test Manager import/diagnostic discovery without broad validation.

## Evidence To Capture

- Exact commands or UI interactions.
- Expected versus observed behavior.
- Workaround or mitigation.
- Product-feedback classification, severity, confidence.
- Artifact paths under `docs/validation/artifacts/2026-06-27/` or `tmp/product-feedback-probes/`.

## Deliverables

- Add PF entries only for genuinely new observations.
- Update `docs/validation/VALIDATION_RESULTS.md` for actual probes.
- Update `docs/logs/BUILD_LOG.md`.
- Run `git diff --check`.
- Run `scripts/run_submission_check.sh` if tracked files changed.
