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

## 2026-06-25 Implementation Checkpoint

Completed:

- Added a local UiPath Action Center payload exporter for the canonical missing-telemetry scenario.
- Export command:

```sh
python -m service_recovery_core.evals --uipath-payload-scenario E-002 --output eval_results/uipath_action_payload_E002.json
```

Validated:

- `RawAgentRecommendation` preserves `recommended_next_stage: closure_candidate`.
- `PolicyDecisionJson` preserves `decision: override_recommendation`, `to_stage: verify_telemetry`, and `block_reason: missing_authoritative_signal`.
- Full unit suite and eval baseline pass.

Still next:

- Repair Action Center `PolicyDecisionJson` rendering before demo polish.

## 2026-06-25 Live UiPath Checkpoint

Completed:

- Repacked the known-good Case package as `Solution.caseManagement.Maestro.Case:1.0.4` using the generated E-002 payload.
- Updated validation process `9a7eb300-7b16-4856-b14f-d6f2da3dbe61` to `1.0.4` with `AutoUpdate: false`.
- Started live case `3af41e1d-8b04-4eba-aa5e-a95c5c673730`.
- Verified task `4300080` before human action contained:
  - raw `AIE-E002` recommendation to `closure_candidate`,
  - linked `PDE-E-002` override to `verify_telemetry`,
  - `missing_authoritative_signal`,
  - `interpretation_policy_version: ip-v1`,
  - `decision_policy_version: dp-v1`.
- Assigned and rejected the task; the case completed.

Validated:

- Local eval output can drive a real UiPath-visible Case task without hand-writing the proof payload.
- The first slice exit criteria are met at API/persistence level.
- Reviewer UI polish remains incomplete because generated Action Center labels still need repair.

Still next:

- Repair Action Center `PolicyDecisionJson` rendering before demo polish.
- Add explicit custom audit event/state storage for one-query domain reconstruction.

## 2026-06-25 Live Contradiction Checkpoint

Completed:

- Repacked the Case package as `Solution.caseManagement.Maestro.Case:1.0.5` using generated E-004 contradiction payload.
- Updated validation process `9a7eb300-7b16-4856-b14f-d6f2da3dbe61` to `1.0.5` with `AutoUpdate: false`.
- Started live case `60e52ca5-6891-45b4-9e98-e1b08a984f06`.
- Verified task `4300219` before human action contained:
  - raw `AIE-E004` recommendation to `closure_candidate`,
  - linked `PDE-E-004` requiring `human_review`,
  - `source_contradiction`,
  - `derived_evidence_state: contradicting`,
  - fresh authoritative `network_telemetry.service_live_status = not_live`,
  - `interpretation_policy_version: ip-v1`,
  - `decision_policy_version: dp-v1`.
- Assigned and rejected the task; the case completed.

Validated:

- The same canonical green business fixture now has both UiPath-visible proof beats:
  - E-002 missing authoritative telemetry -> `verify_telemetry`.
  - E-004 fresh authoritative contradiction -> `human_review`.
- Distinct route behavior is proven at API/persistence level.

Still next:

- Repair Action Center `PolicyDecisionJson` rendering before demo polish.
- Add explicit custom audit event/state storage for one-query domain reconstruction.

## Follow-On Order

1. Evidence packet UI legibility and structured reviewer outcome polish.
2. Audit event linkage / one-query reconstruction.
3. Demo runbook.
4. Test Cloud mapping if available.

Stop at the first failed validation and log the implication before continuing.
