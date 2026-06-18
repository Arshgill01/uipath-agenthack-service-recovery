---
name: uipath-service-recovery-validator
description: Use when validating UiPath Labs assumptions, eval scenarios, tests, demo readiness, or submission readiness for this repo.
---

# UiPath Service Recovery Validator Skill

Use this skill for validation runs, test design, eval work, demo dry runs, and final submission checks.

## Required Reading

Read:

- `AGENTS.md`
- `docs/validation/VALIDATION_GATES.md`
- `docs/validation/EVAL_PLAN.md`
- `docs/demo/DEMO_STORYBOARD.md`
- `waves/39_final_validation.md`
- relevant active wave.

## Validation Priorities

Hard gates first:

1. Native Case state / audit reconstruction.
2. Policy version pinning.
3. Human evidence packet.
4. Agent recommendation visible before policy override.

Then validate:

- distinct 2A and 2B routes,
- eval scenarios,
- agent usefulness incident,
- policy improvement artifact,
- CLI/coding-agent proof,
- demo runbook repeatability.

## Eval Requirements

Minimum scenarios:

- happy aligned closure,
- missing telemetry,
- stale telemetry,
- contradicting telemetry,
- technician note changes route,
- adversarial pressure,
- invalid agent output,
- usefulness degradation.

## Reporting Format

Record:

- command/run,
- environment,
- expected,
- observed,
- pass/fail/partial,
- screenshots or artifact references if available,
- decision impact.
