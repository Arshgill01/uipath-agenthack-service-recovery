# Wave 30: Demo Scenario Runbook

## Goal

Create repeatable demo steps.

Primary runbook: `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`.

## Tasks

- Write exact scenario setup for 2A. Status: covered by `DEMO_SAFE_PROOF_RUNBOOK.md`.
- Write exact scenario setup for 2B. Status: covered by `DEMO_SAFE_PROOF_RUNBOOK.md`.
- Write exact unstructured-note route-change setup. Status: still pending; do not add until the two core beats are repeatable.
- Write reset steps. Status: covered for local artifact regeneration; live case reset remains pending.
- Include expected screenshots/states. Status: custom evidence packet and bucket readback expectations are documented.

## Exit Criteria

- Another agent can run the demo without inventing steps.

Current result: PARTIAL. Another agent can regenerate local artifacts, verify the core proof fields, and use the validated live IDs. A fully fresh live case run still needs an operator script or updated live-case start procedure.
