# Wave 23: Agent Usefulness Incident

## Goal

Detect when the agent becomes safe but useless.

## Tasks

- Compute low-confidence/unclassified rates relative to baseline.
- Detect invalid schema rate spikes.
- Emit structured usefulness incident.
- Link incident to sample case IDs/eval IDs.

## Exit Criteria

- Persistent low-value agent behavior creates structured incident.
