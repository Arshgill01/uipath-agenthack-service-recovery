# Wave 03: Policy Version Pinning Spike

## Goal

Validate hard gate G-002: policy version pinning.

## Tasks

- Add `interpretation_policy_version` and `decision_policy_version` to a case or equivalent state.
- Prove versions persist across stage transitions.
- Create a newer policy version.
- Confirm active case does not silently change.
- Model explicit migration as an event.

## Exit Criteria

- Decide native pinning vs metadata implementation.
- Update [docs/decisions/DECISIONS.md](../docs/decisions/DECISIONS.md).
