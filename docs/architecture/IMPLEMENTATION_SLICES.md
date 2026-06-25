# Implementation Readiness Slices

This document maps the local service-recovery core to UiPath artifacts and defines the smallest post-gate implementation slices. It is a readiness plan, not permission to start broad implementation.

Current gate status: G-001 through G-004 are answered with implementation implications, not all-native PASS:

- G-001 is PARTIAL natively and PASS with the custom UiPath-hosted `service-recovery-audit-v1` audit bundle stored in an Orchestrator bucket.
- G-002 is PASS for explicit package/process/artifact policy-version pinning; active-case migration remains a custom audited event.
- G-003 is PASS for Action Center lifecycle and structured reviewer return, PARTIAL for generated Action Center evidence-packet legibility.
- G-004 is PASS for persisted raw Agent Interpretation Event and linked Policy Decision Event in payload/API/audit data, PARTIAL for generated Action Center display.

Implementation should follow the validated demo-safe path: Action Center for human-task mechanics, custom evidence packet for judge-readable proof, and Orchestrator bucket audit bundle for durable UiPath-hosted reconstruction.

## Core-to-UiPath Mapping

| Local core object or event | Required UiPath representation | Gate dependency | Notes |
| --- | --- | --- | --- |
| `case` dict | Maestro Case instance fields plus Case App/custom view fields. | G-001, G-002, G-006 | Must carry `case_id`, stage, severity, SLA, derived evidence state, and both policy versions. |
| `evidence` signals | Evidence table in Case App/Action Center packet; optionally Data Fabric/Data Service rows if native case state cannot reconstruct history. | G-001, G-003 | Signals remain structured. Simulated CRM/billing/network/inventory/dispatch sources are honest simulated systems, not real telecom integrations. |
| `agent_event` / Agent Interpretation Event | Raw recommendation event visible before policy action. Candidate surfaces: Case event/custom audit row, Case App panel, or Data Service audit object. | G-001, G-004 | Must preserve `recommended_next_stage`, confidence, rationale codes, extracted claims, and generated-once explanation. |
| `policy_decision` / Policy Decision Event | Separate linked policy event, stage route, closure block reason, and case field update. | G-001, G-002, G-004, G-005 | Must link to `agent_event_id`; must not overwrite the raw recommendation. |
| `apply_policy_decision` transition | Maestro Case stage transition and task routing. | G-001, G-005 | Local policy stages map through `POLICY_STAGE_TO_CASE_STAGE`; UiPath mapper should not invent new routing semantics. |
| Human Review Event | Action Center human action result or Case App/custom evidence-packet result. | G-003 | Required outcomes: approve remediation, reject, request evidence, close after confirmation, and comment. |
| Eval result | Test Manager/Test Cloud artifact if feasible; otherwise a UiPath-compatible eval export attached to policy-improvement evidence. | G-007 | Live Test Manager project `SREV`, test set `SREV:9`, and manual execution logs represent E-001 through E-009. Do not claim automated Test Cloud execution. |

## Safe Now

The following are safe because they preserve the validated gate implications and do not depend on unproven native Case audit or generated Action Center UI behavior:

| Slice | Files owned | Validation |
| --- | --- | --- |
| Readiness docs and mapping updates. | `docs/architecture/IMPLEMENTATION_SLICES.md`, `docs/architecture/INTEGRATION_MAP.md`, relevant logs. | Readback changed docs; no code tests required. |
| Contract-only fixtures for export examples, if needed later. | `fixtures/` or docs examples only. | `python -m unittest discover -s tests`; `python -m service_recovery_core.evals --output eval_results/local_baseline.json` if fixture JSON changes. |
| Narrow tests that assert existing boundaries before bridge code exists. | `tests/test_policy_state_eval.py`, `tests/test_schemas.py`. | `python -m unittest discover -s tests`; eval command if expected eval behavior changes. |

Do not add broad UiPath runtime adapters, package/deploy scripts, or Case JSON mutation code unless the slice directly supports the demo-safe proof path and keeps the validated partials explicit.

## Post-Gate Slices

| Slice | Build only after | Files likely owned | Minimum tests and checks |
| --- | --- | --- | --- |
| Event export schema | Now safe if it emits the validated audit bundle/payload shape. | `service_recovery_core/exports.py`, `tests/test_exports.py`, `docs/architecture/DATA_MODEL.md`. | `python -m unittest discover -s tests`; `python -m service_recovery_core.evals --output eval_results/local_baseline.json`; targeted fixture asserting raw agent event and policy decision export as separate linked records. |
| Evidence packet renderer data contract | Already selected: custom evidence packet is the demo-readable surface; Action Center remains lifecycle/return. | `service_recovery_core/evidence_packet_view.py`, `tests/test_evidence_packet_view.py`, `docs/architecture/DATA_MODEL.md`. | Unit tests for required packet sections and allowed human outcomes; proof verifier for E-002/E-004. |
| UiPath case payload mapper | Now safe for the validated payload/API/audit path, not for claiming native Case audit alone. | `service_recovery_core/uipath_payload.py`, mapper tests if expanded, `docs/architecture/INTEGRATION_MAP.md`. | Unit tests for stage mapping, version fields, linked event IDs, and closure-block reason; local eval command; live rerun only if package/process/task IDs change. |
| Maestro routing slice | G-005 is live-validated for E-002 and E-004. | UiPath solution assets once export/import path is known; bridge mapper tests. | Scenario checks for E-002 missing/stale evidence to verification/retry and E-004 contradiction to human review; live rerun only if route implementation changes. |
| Eval-to-Test-Manager mapping | G-007 is validated as manual Test Manager representation. | `docs/validation/TEST_MANAGER_MAPPING.md`, `service_recovery_core/evals.py` only if export shape is needed. | Local eval command; do not claim automated Test Cloud execution unless a real automated run is added later. |
| CLI packaging/deploy helper | G-008 has CLI lifecycle evidence; helper scripts should focus on repeatable proof/readback rather than broad deployment. | `scripts/`, README or runbook updates. | `uip --version`; dry-run/help command for helper; no deploy claim unless a real package/deploy command succeeds and is logged. |

## Remaining Partials / Do Not Overclaim

- Do not claim native Case history alone satisfies G-001; use the explicit audit bundle.
- Do not claim Data Fabric record persistence; entity creation/readback worked, but record insert/query-back is still blocked.
- Do not claim generated Action Center UI is final-demo ready; use the custom evidence packet for legibility.
- Do not claim automated Test Cloud execution; Test Manager mapping is manual.
- Do not claim terminal Case job completion for E-002/E-004 while job readback remains `Running`.
- Do not claim broad real telecom integrations.

## Guardrails

- Keep raw agent recommendation and final policy decision separate in every export, mapper, UI packet, and audit event.
- Policy consumes structured fields only; no UiPath mapper should parse `audit_explanation`.
- Closure still requires fresh authoritative telemetry.
- Missing/stale authoritative evidence and contradicting evidence must route differently.
- Simulated telecom systems are acceptable; do not imply live CRM, billing, network, inventory, or dispatch integration.
