# Implementation Readiness Slices

This document maps the local service-recovery core to UiPath artifacts and defines the smallest post-gate implementation slices. It is a readiness plan, not permission to start broad implementation.

Current gate status: G-001 through G-004 are PARTIAL. Action Center is enabled and a `Human action (placeholder)` can be inserted, but no live case has proven runtime audit reconstruction, active-case policy pinning, evidence-packet rendering/return, or raw recommendation visibility before policy override.

## Core-to-UiPath Mapping

| Local core object or event | Required UiPath representation | Gate dependency | Notes |
| --- | --- | --- | --- |
| `case` dict | Maestro Case instance fields plus Case App/custom view fields. | G-001, G-002, G-006 | Must carry `case_id`, stage, severity, SLA, derived evidence state, and both policy versions. |
| `evidence` signals | Evidence table in Case App/Action Center packet; optionally Data Fabric/Data Service rows if native case state cannot reconstruct history. | G-001, G-003 | Signals remain structured. Simulated CRM/billing/network/inventory/dispatch sources are honest simulated systems, not real telecom integrations. |
| `agent_event` / Agent Interpretation Event | Raw recommendation event visible before policy action. Candidate surfaces: Case event/custom audit row, Case App panel, or Data Service audit object. | G-001, G-004 | Must preserve `recommended_next_stage`, confidence, rationale codes, extracted claims, and generated-once explanation. |
| `policy_decision` / Policy Decision Event | Separate linked policy event, stage route, closure block reason, and case field update. | G-001, G-002, G-004, G-005 | Must link to `agent_event_id`; must not overwrite the raw recommendation. |
| `apply_policy_decision` transition | Maestro Case stage transition and task routing. | G-001, G-005 | Local policy stages map through `POLICY_STAGE_TO_CASE_STAGE`; UiPath mapper should not invent new routing semantics. |
| Human Review Event | Action Center human action result or Case App/custom evidence-packet result. | G-003 | Required outcomes: approve remediation, reject, request evidence, close after confirmation, and comment. |
| Eval result | Test Manager/Test Cloud artifact if feasible; otherwise a UiPath-compatible eval export attached to policy-improvement evidence. | G-007 | Local evals remain authoritative until native Test Manager mapping is validated. |

## Safe Now

The following are safe before G-001 through G-004 pass because they do not assume unproven UiPath behavior:

| Slice | Files owned | Validation |
| --- | --- | --- |
| Readiness docs and mapping updates. | `docs/architecture/IMPLEMENTATION_SLICES.md`, `docs/architecture/INTEGRATION_MAP.md`, relevant logs. | Readback changed docs; no code tests required. |
| Contract-only fixtures for export examples, if needed later. | `fixtures/` or docs examples only. | `python -m unittest discover -s tests`; `python -m service_recovery_core.evals --output eval_results/local_baseline.json` if fixture JSON changes. |
| Narrow tests that assert existing boundaries before bridge code exists. | `tests/test_policy_state_eval.py`, `tests/test_schemas.py`. | `python -m unittest discover -s tests`; eval command if expected eval behavior changes. |

Do not add UiPath runtime adapters, package/deploy scripts, or Case JSON mutation code until the relevant gate has an observed pass/partial-with-implication result.

## Post-Gate Slices

| Slice | Build only after | Files likely owned | Minimum tests and checks |
| --- | --- | --- | --- |
| Event export schema | G-001 and G-004 establish whether native Case history is sufficient or custom audit storage is required. | `service_recovery_core/exports.py`, `tests/test_exports.py`, `docs/architecture/DATA_MODEL.md`. | `python -m unittest discover -s tests`; `python -m service_recovery_core.evals --output eval_results/local_baseline.json`; targeted fixture asserting raw agent event and policy decision export as separate linked records. |
| Evidence packet renderer data contract | G-003 proves Action Center packet rendering/return or selects Case App/custom packet fallback. | `service_recovery_core/evidence_packet.py`, `tests/test_evidence_packet.py`, `docs/architecture/DATA_MODEL.md`. | Unit tests for required packet sections and allowed human outcomes; eval command if packet uses eval fixtures; manual G-003 rerun against the selected UiPath surface. |
| UiPath case payload mapper | G-001, G-002, G-004 prove where case fields, versions, and events persist. | `service_recovery_core/uipath_mapper.py` or a similarly narrow bridge module, `tests/test_uipath_mapper.py`, `docs/architecture/INTEGRATION_MAP.md`. | Unit tests for stage mapping, version fields, linked event IDs, and closure-block reason; local eval command; live minimal case rerun for G-001/G-002/G-004. |
| Maestro routing slice | G-005 proves structured policy output can drive distinct routes. | UiPath solution assets once export/import path is known; bridge mapper tests. | Scenario checks for E-002 missing evidence to verification/retry and E-004 contradiction to human review; live case run showing both routes. |
| Eval-to-Test-Manager mapping | G-007 proves feasible Test Manager/Test Cloud representation. | `service_recovery_core/evals.py` only if export shape is needed, `tests/test_eval_export.py`, `docs/validation/EVAL_PLAN.md`. | Local eval command; Test Manager/Test Cloud run or documented fallback artifact import/check. |
| CLI packaging/deploy helper | G-008 and a known UiPath solution/package path. | `scripts/` helper, README or runbook updates. | `uip --version`; dry-run/help command for the helper; no deploy claim unless a real package/deploy command succeeds. |

## Blocked By Gate

- G-001 blocks final audit storage choice. If one case view or one query cannot reconstruct the timeline, use explicit custom audit events in Data Fabric/Data Service or equivalent.
- G-002 blocks policy-version persistence implementation. Metadata fields are acceptable, but silent version changes are not.
- G-003 blocks the human evidence packet surface. Action Center is available, but rendering quality and structured return are still unproven.
- G-004 blocks any implementation that claims visible policy override. Raw `agent_event` and final `policy_event` must remain separate linked records.

## Guardrails

- Keep raw agent recommendation and final policy decision separate in every export, mapper, UI packet, and audit event.
- Policy consumes structured fields only; no UiPath mapper should parse `audit_explanation`.
- Closure still requires fresh authoritative telemetry.
- Missing/stale authoritative evidence and contradicting evidence must route differently.
- Simulated telecom systems are acceptable; do not imply live CRM, billing, network, inventory, or dispatch integration.
