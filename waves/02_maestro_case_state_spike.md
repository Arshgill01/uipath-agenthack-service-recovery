# Wave 02: Maestro Case State Spike

## Goal

Validate hard gate G-001: native Case state and audit reconstruction.

## Tasks

- Create the smallest possible Maestro Case.
- Add fields for evidence state, policy versions, agent recommendation, policy decision, block reason.
- Run one case through at least two stages.
- Attempt reconstruction through one case view or one query.
- Record whether native case history is enough.

## Pass Condition

One-view or one-query reconstruction of:

- evidence state at each stage,
- policy version active,
- raw agent recommendation,
- policy decision,
- closure block reason,
- human action if present,
- timestamp/order of events.

## Fallback

If native reconstruction is not enough, choose custom audit events and/or Data Fabric/Data Service.
