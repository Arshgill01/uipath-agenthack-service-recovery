# Wave 17: Missing/Stale Override Path

## Goal

Build core demo path 2A.

## Tasks

- Use the canonical "business systems green" fixture from Wave 09.
- Set telemetry missing or stale.
- Agent recommends closure.
- Persist `Agent Interpretation Event` with `recommended_next_stage: closure_candidate`.
- Policy overrides to verification/retry.
- Persist linked `Policy Decision Event` with `agent_event_id`, `decision: override_recommendation`, `from_recommended_stage: closure_candidate`, `to_stage: verify_telemetry`, and block reason.

## Exit Criteria

- Override is visible and auditable.
- Eval E-002 and E-009 pass.
