# UiPath Integration Map

This map is now grounded in live UiPath validation. The hard gates are answered with explicit implementation implications: native Case state is not sufficient alone for the domain audit, Action Center is not the final evidence UI, and the validated demo-safe path combines Action Center lifecycle, custom evidence packet, and Orchestrator bucket audit bundle.

Implementation readiness slices are tracked in [IMPLEMENTATION_SLICES.md](IMPLEMENTATION_SLICES.md). Future implementation should follow the validated demo-safe path unless new platform evidence supersedes it.

| Capability | Planned use | Validation dependency |
| --- | --- | --- |
| Maestro Case | Primary case lifecycle, stages, routing, incident/recovery, human accountability. | G-001, G-002, G-005, G-006 |
| Agent Builder / Coded Agent | Interpret unstructured notes/messages into structured schema. | Stack choice and UiPath access |
| API Workflows | Query simulated CRM/billing/telemetry/inventory/dispatch APIs. | G-005 and Wave 28 |
| Action Center | Human review lifecycle: create, assign, complete, reviewer action/comment, structured task output into case variables. Not the final judge-readable evidence UI. | G-003 PASS/PARTIAL |
| Case App / custom UI | Primary final evidence packet/demo surface because generated Action Center UI is not demo-legible. | G-003, G-004, G-006 |
| Data Fabric/Data Service | Validated full-payload audit storage with `ServiceRecoveryAuditBundleV2` PascalCase fields and E-004 record readback by `CaseId`. Legacy snake_case entity remains product-feedback evidence. | G-001, G-002; PF-019, PF-023 |
| Orchestrator storage buckets | Validated alternate fallback for storing one-object `service-recovery-audit-v1` audit artifacts when native Case audit is insufficient. | G-001, G-002, G-004, G-008 |
| Test Cloud / Test Manager | Eval/regression representation. Live project `SREV`, test set `SREV:9`, and terminal manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` represent E-001 through E-009; automated execution is not claimed because no ready automation target was found. | G-007 PASS/PARTIAL; PF-024 |
| UiPath CLI + skills | Coding-agent bonus proof and lifecycle automation, including explicit process creation with pinned package versions. | G-008; current CLI readback `1.195.1`, logged into org `keepingitlowkey`, tenant `DefaultTenant` |
| Orchestrator | Assets, packages, jobs, logs, deployment, secrets if needed. | Wave 01 and stack selection |

## Rule

Do not use a UiPath component for checkbox breadth. Use it when it has visible responsibility in the demo or build lifecycle.

## Wave 01 Observed Access Status

Observed on 2026-06-24:

- Local `uip` CLI is installed and currently reports version `1.195.1`.
- Automation Cloud browser access did not reach a tenant; Safari landed at `portal_/missingaccount`.
- Product access for Maestro, Maestro Case, Studio Web, Action Center, Test Cloud/Test Manager, Integration Service, and Orchestrator is unconfirmed.
- Initial access blocker is historical. Current Automation Cloud tenant access and Maestro Case availability are confirmed.

Observed on 2026-06-24 20:30 IST rerun:

- Automation Cloud access is confirmed for org `keepingitlowkey`, tenant `DefaultTenant`, user `Arshdeep Singh`.
- Product launcher exposes Studio, Orchestrator, Maestro, Admin, Agents, Apps, Automation Ops, Assistant, Data Fabric, Integration Service, Marketplace, and Test Manager.
- Maestro access is confirmed. Maestro exposes Case app, Case instances, and Case incidents.
- Studio Web can create a validation-scoped Maestro BPMN solution.
- `Add to solution` includes `Maestro Case`, and a `Maestro Case` project can be added to the Studio solution.
- Case App opens and shows active-case columns for Case ID, Case type, Last modified, Stage, Case SLA, SLA status, and Case state.
- Actions / Action Center was initially disabled for `DefaultTenant`, then enabled from Admin `DefaultTenant > Services > Add services` after user approval. Action Center now opens as `Inbox - Action Center`.
- Test Manager is validated through project `SREV`, test set `SREV:9`, and terminal manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11`; the earlier execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad` remains a negative lifecycle/control run.
- Hard gates are answered with documented partials and implementation choices. Proceed with the demo-safe proof path instead of reopening broad validation.

Observed live validation facts to carry into implementation:

- A live case instance exposes the Case process package through `PackageKey`.
- Direct process creation can pin a Case package version with `--package-version` and `--no-auto-update`.
- Active cases/processes should be treated as package-version pinned unless an explicit migration event is recorded.
- The original solution-created process remained on package `1.0.0` with `AutoUpdate` false even after an update command reported success. Treat auto-update or implicit migration as an open risk.
- Direct Case package `1.0.1` failed to resolve the generated app folder `.app`.
- Direct Case package `1.0.2` resolved the app by replacing the binding with the explicit folder path `arshgill6120@gmail.com's workspace/Solution`.
- Action Center AppTask creation, assignment, completion, and structured output return into case variables are validated.
- Raw agent recommendation and final policy decision can be represented as separate structured HITL payload fields.
- Package `1.0.3` live validation reached Action Center task `4295299`. The task API persisted both `RawAgentRecommendation` and `PolicyDecisionJson`; Action Center rendered the raw recommendation and evidence packet, but rendered the policy field as `Unnamed String 1`.
- Treat G-004 persistence as validated for the proof beat, with a reviewer-legibility caveat that needs a label/binding repair before the final demo.
- Later E-004 completed-task recheck showed the generated Action Center UI still leaves proof-critical values blank/generic. D-009 is activated: use Action Center for lifecycle and custom packet/audit UI for legibility.

## Custom Audit Bundle Mapping

Live validation moved the architecture from "maybe Data Fabric/Data Service" to a concrete custom-audit contract:

- `service_recovery_core.audit_bundle.build_case_audit_bundle(...)` emits a one-object domain audit bundle.
- `python -m service_recovery_core.evals --audit-bundle-scenario E-002` emits the missing-telemetry proof beat.
- `python -m service_recovery_core.evals --audit-bundle-scenario E-004` emits the contradiction/human-review proof beat.
- The bundle can be stored as Case custom data, Data Fabric/Data Service record, or a UiPath-accessible file/artifact depending on the final implementation path.
- Data Fabric is reachable through `uip df`; live validation now uses `ServiceRecoveryAuditBundleV2` for queryable audit storage.
- `docs/architecture/data_fabric/service_recovery_audit_bundle_v2_entity.json` is the live-validated Data Fabric schema for storing the bundle with PascalCase fields.
- `python -m service_recovery_core.evals --data-fabric-record-scenario E-004 --data-fabric-field-style pascal` emits an insert-ready record body for the contradiction proof beat, including live Case/task/package references from package `1.0.6`.
- Live Data Fabric entity `ServiceRecoveryAuditBundleV2` was created with ID `35e8f6c7-4671-f111-ac9a-002248a16d28`.
- Live Data Fabric record `F9D838CE-4671-F111-AC9A-0022489A9A06` was inserted and queried by `CaseId = CASE-BG-CONTRA`; readback includes `InterpretationPolicyVersion = ip-v1`, `DecisionPolicyVersion = dp-v1`, `ClosureBlockReason = source_contradiction`, `SourceCaseInstanceKey = 9fc6fece-55ed-4fb2-b11a-6c96f7a3314e`, `SourceTaskId = 4328396`, and `PackageVersion = 1.0.6`.
- Parsed readback from `RawAgentEventJson`, `PolicyDecisionEventJson`, and `AuditBundleJson` proves raw recommendation `closure_candidate`, policy decision `require_human_review`, policy link `PDE-E-004 -> AIE-E004`, and event count `4`.
- After explicit user approval, live Data Fabric entity `ServiceRecoveryAuditBundle` was created with ID `328ef8b6-ab70-f111-ac9a-002248a16d28` and schema readback by ID succeeded.
- The original snake_case entity is retained only as a legacy finding: JSON insert rejected field-name, wrapper, field-ID keyed, and array payloads with required `case_id` reported missing. CSV import created record `DA42769C-33B7-4701-A266-019F032AF376` in entity `328ef8b6-ab70-f111-ac9a-002248a16d28`, but follow-up CLI readback returned only system fields and did not prove the domain payload values.
- Orchestrator bucket fallback is live-validated. Bucket `service-recovery-audit-validation` with key `dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb` stores `audit/service_recovery_audit_bundle_E004.json`.
- The bucket artifact was uploaded, listed, downloaded to `eval_results/downloaded_audit_bundle_E004.json`, and byte-compared against `docs/validation/artifacts/2026-06-25/service_recovery_audit_bundle_E004.json`.
- The artifact manifest is `docs/validation/artifacts/2026-06-25/orchestrator_bucket_audit_artifact_E004_manifest.json`.

Mapping to hard gates:

- G-001: one bundle reconstructs evidence state, policy versions, raw agent recommendation, policy decision, closure block reason, human action placeholder/result, and event order.
- G-002: policy versions are explicit top-level fields and remain tied to the generated policy event.
- G-003: `reviewer_packet` contains the evidence table, raw agent recommendation, policy decision, block reason, recommended options, and rendering status for a custom evidence packet view.
- G-004: `agent_interpretation_event` and `policy_decision_event` are separate linked objects; the policy event points back through `links_to`.
