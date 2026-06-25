# Wave 07: UiPath-Grounded Build Plan

## Goal

Start the first implementation slice immediately after hard gates are answered, without broad scaffolding. The slice must connect the local service-recovery model to UiPath-visible evidence while preserving the architecture boundary:

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

## Prerequisites

- G-004 is PASS or PARTIAL with a documented explicit-audit fallback.
- G-001, G-002, and G-003 have logged statuses in `docs/validation/VALIDATION_RESULTS.md`.
- Any required material decisions are logged in `docs/decisions/DECISIONS.md`.
- No hard gate requires abandoning Maestro Case as primary track.

## First Slice

Build only the missing/stale telemetry override path from the canonical green business fixture:

- CRM/order active or resolved.
- Billing clear.
- Support note resolved.
- Network telemetry missing or stale.
- Agent recommends `closure_candidate`.
- Policy overrides to verification/retry.
- SLA remains open.
- Raw recommendation and policy decision persist separately.

Persist these fields in the chosen UiPath-visible state or explicit audit event:

- `case_id`
- `fixture_id`
- `derived_evidence_state`
- `interpretation_policy_version`
- `decision_policy_version`
- `recommended_next_stage`
- `policy_decision`
- `closure_block_reason_code`
- `audit_explanation`

## Validation

Run local checks before claiming fixture correctness:

```sh
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
```

Then run one fresh UiPath-visible case and capture:

- fixture ID and case ID,
- raw recommendation event,
- policy decision event,
- policy versions,
- block reason,
- route to verification/retry,
- timestamp/order or event linkage.

## Exit Criteria

- Local evals and UiPath-visible state agree on the canonical fixture semantics.
- The override beat is visible without relying on narration.
- Policy versions are pinned in visible state or explicit audit events.
- No contradiction route, evidence-packet polish, dashboard, Test Cloud mapping, or broad UI work is included in this slice.

## Follow-On Order

1. Contradiction route from the same canonical business fixture.
2. Evidence packet content and structured reviewer outcome.
3. Audit event linkage / one-query reconstruction.
4. Demo runbook.
5. Test Cloud mapping if available.

Stop at the first failed validation and log the implication before continuing.
