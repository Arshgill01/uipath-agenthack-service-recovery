---
name: uipath-service-recovery-builder
description: Use when implementing code, fixtures, schemas, local simulation, Maestro Case mappings, UI surfaces, or runbooks for this repo.
---

# UiPath Service Recovery Builder Skill

Use this skill before implementation work.

## Required Reading

Read:

- `AGENTS.md`
- active `waves/NN_*.md`
- `docs/architecture/DATA_MODEL.md`
- `docs/architecture/AGENT_CONTRACT.md`
- `docs/architecture/POLICY_MODEL.md`
- `docs/product/SCOPE_BOUNDARY.md`

## Build Principles

- Build the smallest concrete slice that proves the wave.
- Keep simulated telecom systems explicit and honest.
- Keep policy deterministic.
- Persist agent interpretation event separately from policy decision event.
- Add tests/evals before broadening behavior.
- Do not add UI that does not support demo-critical proof.

## Implementation Order Preference

1. Fixtures.
2. Schemas.
3. Agent output validator.
4. Evidence reconciliation.
5. Closure policy.
6. Case state machine.
7. Eval harness.
8. UI/demo surfaces.
9. UiPath integration.

## Required End-of-Run Updates

- `docs/logs/BUILD_LOG.md`
- `docs/logs/RISK_REGISTER.md` if risk changed
- `docs/validation/VALIDATION_RESULTS.md` if validation ran
- wave file status notes if useful

## Validation Contract

Never say a wave passed unless the exact command or UiPath run was executed successfully.
