# Best Product Feedback Appendix

Status: curated evidence appendix for the UiPath AgentHack feedback survey. This is not final form prose; it is the high-signal source for writing the final answers.

Copy-ready answer bank: [FEEDBACK_SURVEY_COPY_READY.md](FEEDBACK_SURVEY_COPY_READY.md).

## Submission Thesis

UiPath Maestro Case had the right core primitives for a governed telecom service-recovery workflow: case state, stages, human tasks, Action Center lifecycle, Orchestrator process/package/job readback, Test Manager representation, and CLI automation. The strongest product feedback is that first-time builders need a guided readiness and verification path for Maestro Case human-review workflows so they can trust tenant services, generated Action app bindings, required task fields, package/feed bindings, and audit reconstruction before spending hours in live runtime recovery.

The feedback should not read as a complaint list. It should read as:

> We built a real governed Maestro Case workflow, validated the hard gates, found the product primitives strong, and identified exact preflight/diagnostic improvements that would make adoption much faster for agent + policy + human casework.

Forum and winner research are supporting context only. The award claims below are based on our reproduced PF evidence; public participant reports are useful because they show the same classes of friction around Actions enablement, Maestro publishing/package blockers, and Labs access, but they should not be treated as our reproduction evidence.

## Official Context Added On 2026-06-29

This source refresh strengthens the framing without changing the evidence boundary:

| Official source | Why it matters for the feedback form |
| --- | --- |
| Devpost rules: `https://uipath-agenthack.devpost.com/rules` | Best Product Feedback asks for actionable comments UiPath can use. The final form should therefore read as concrete workflow evidence plus product fixes, not as an internal bug list. |
| Devpost track guidance: `https://uipath-agenthack.devpost.com/details/tracks` | Track 1 emphasizes dynamic exception work, human-in-the-loop decisions, visibility, auditability, and collaboration between humans, agents, and automations. That matches our Maestro Case readiness/preflight thesis. |
| Maestro docs: `https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/overview` and `https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/value-proposition` | Official docs frame Maestro as orchestration across automation, AI agents, and humans, including long-running exception-heavy Case Management. This supports praising the primitive while asking for stronger readiness diagnostics. |
| Action Center docs: `https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions` and `https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/create-user-action` | Official docs show Actions is a tenant service and App tasks render Action app inputs in Action Center. This supports the service-readiness and generated-field-binding recommendations. |
| Test Manager docs: `https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/executing-tests` and `https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/selecting-automation` | Official docs distinguish manual and automated executions and describe Orchestrator-published automation selection. This supports claiming manual eval representation while explicitly not claiming automated Test Cloud execution. |
| Data Fabric and Orchestrator docs: `https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/introduction` and `https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-packages` | Official docs support using Data Fabric for persistent process data and Orchestrator for package/version lifecycle. Our reproduced feedback is about diagnostics and consistency around those intended roles. |

Do not paste this table into the Microsoft Form. Use it to keep the final form self-contained and fair: official context explains why the workflows matter; reproduced PF evidence explains what happened in our build; recommendations explain what UiPath could improve.

## Best Final Answer Shape

### Overall Satisfaction

Recommended answer: `Somewhat satisfied`.

Reason:

- Satisfied because the platform supported real Maestro Case, Action Center, Orchestrator bucket, package/process readback, Test Manager mapping, and CLI lifecycle evidence.
- Not `Very satisfied` because setup, generated Action app binding, runtime validation, package/feed diagnostics, and native audit reconstruction required repeated workarounds.

Evidence:

- Positive: PF-013, PF-015, PF-017, PF-020.
- Friction: PF-003, PF-006, PF-007, PF-017, PF-019, PF-022, PF-026, PF-027, PF-028.

### Ease Of Build

Recommended answer: `Somewhat difficult`.

Reason:

- The architecture mapped well to UiPath products.
- The time cost came from discovering platform readiness issues and proving runtime behavior: Actions enablement, generated Action app field rendering, required Action task title, package/feed binding, Data Fabric insert shape, Case job/task readback, and inconsistent readiness signals across Case validation, solution dry-run, and upload/import.

Evidence:

- PF-003, PF-006, PF-007, PF-013, PF-017, PF-019, PF-022, PF-026, PF-027, PF-028.

## Ranked Feedback Thesis

| Rank | Thesis and PF IDs | Severity | Reproduced evidence | Workaround used | UiPath improvement recommendation | What not to claim |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Add a shared Maestro Case human-review readiness/preflight path. PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-026, PF-027, PF-028. | High. This was the slowest build loop because it spans setup, authoring, deployment, runtime, task visibility, package/feed binding, and audit proof. | `docs/validation/artifacts/2026-06-27/product_feedback_readiness_probe.md`; `docs/validation/artifacts/2026-06-27/product_feedback_phase2_scratch_case_probe.md`; `docs/validation/artifacts/2026-06-27/product_feedback_workstream_a_maestro_authoring_repair_probe.md`; `docs/validation/artifacts/2026-06-27/product_feedback_action_binding_probe.md`; PF-003/PF-006/PF-007/PF-013/PF-026/PF-027/PF-028 in `PRODUCT_FEEDBACK_AWARD.md`. | Manually enabled Actions; ran `uip maestro case validate`; repaired scratch Action task by remove/re-add with `--task-title`; used process/task/API readbacks; used custom packet/Data Fabric/bucket proof for legibility. | One preflight contract across Case validate, solution dry-run, Studio Web upload/import, package/process binding, and runtime: check services/roles, reviewer visibility, required Action fields, Action schema bindings, package/feed version, process version, and audit readiness. | Do not claim generated Action Center UI is final-demo ready or that native Case history alone passes G-001. |
| 2 | Add generated Action app field-binding and version inspectors. PF-006, PF-013. | High for G-003/G-004. The platform preserved proof-critical data, but the generated reviewer UI hid or mislabeled it. | `docs/validation/ACTION_CENTER_UI_REPAIR_ASSESSMENT.md`; `docs/validation/artifacts/2026-06-27/product_feedback_action_binding_probe.md`; screenshots `docs/validation/artifacts/2026-06-25/g004-action-center-policy-field-mislabeled-task-4295299.png` and `docs/validation/artifacts/2026-06-25/g003-action-center-e004-completed-generated-ui-empty-fields.png`; task `4333536`. | Kept Action Center for assignment/completion/comment/structured return; used `uip tasks get` and custom evidence packets for readable policy decision proof; did not rely on label-only Studio publish after runtime recheck failed. | Show schema field -> generated control -> label -> binding -> runtime app deployment/version -> Case package/task binding before runtime; fail or repair fields that would render as `Unnamed String 1`. | Do not claim the Studio Web label-only repair fixed runtime Action Center rendering. |
| 3 | Add native Case domain audit/event reconstruction for agent + policy + human workflows. PF-015, with PF-019/PF-023 as storage-related support. | High for regulated Case adoption and G-001. | G-001/G-004 entries in `docs/validation/VALIDATION_RESULTS.md`; `service_recovery_core/audit_bundle.py`; `docs/demo/artifacts/demo_proof_manifest.json`; Data Fabric V2 record `F9D838CE-4671-F111-AC9A-0022489A9A06`; Orchestrator bucket artifact `audit/service_recovery_audit_bundle_E004.json`. | Created explicit `service-recovery-audit-v1` bundles; stored/read full payload through Data Fabric V2 and Orchestrator bucket; kept native Case history as operational trace, not full domain audit. | Let builders declare and query linked Agent Interpretation, Policy Decision, Evidence State, and Human Review events in one Case timeline/query with package/policy versions and block reasons. | Do not claim native Case history alone reconstructs the full domain audit. |
| 4 | Make package/feed/process binding diagnostics consistent and Case-aware. PF-017, PF-010, PF-011, PF-012, PF-026. | High during CLI recovery and version-pinning work. | `docs/validation/VALIDATION_RESULTS.md` Wave 07 entries; `docs/validation/artifacts/2026-06-27/product_feedback_readiness_probe.md`; package `Solution.caseManagement.Maestro.Case:1.0.4`; process `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`. | Verified uploaded package with `--feed-id`; updated an existing process version; read back process/version history before live runs. | Add feed-aware `processes create`, show resolved feed/package/version in every bind path, and make Case diagnostics tie AppTasks errors to required fields, app binding/version, package/feed version, and repair links. | Do not imply every successful CLI response changed runtime state without readback. |
| 5 | Add schema-aware Data Fabric insert/import/update/readback diagnostics. PF-019, PF-023, with PF-018 now improved for CLI discovery. | High for audit storage before mitigation; medium after validated V2 workaround. | `docs/validation/artifacts/2026-06-27/data_fabric_readback_diagnostics_probe.md`; legacy record `DA42769C-33B7-4701-A266-019F032AF376`; V2 entity `ServiceRecoveryAuditBundleV2`; V2 record `F9D838CE-4671-F111-AC9A-0022489A9A06`. | Used PascalCase `ServiceRecoveryAuditBundleV2` for final audit proof; kept legacy snake_case entity as product-feedback evidence only; verified writes through field filters and parseable JSON readback. | Echo recognized/unrecognized fields during insert/import/update, document field-naming constraints if any, reject unsupported names at schema creation, and provide write/readback self-test examples for custom required fields. | Do not use the legacy snake_case entity as proof of full Data Fabric audit persistence. |
| 6 | Support eval-suite import into Test Manager and make automation discovery diagnostics actionable. PF-020, PF-021, PF-024. | Medium/high as cross-product eval feedback; less central than Maestro Case. | `docs/validation/TEST_MANAGER_MAPPING.md`; `docs/validation/artifacts/2026-06-27/pf-workstream-c/README.md`; terminal manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11`; package probe `ServiceRecoveryEvalProcessProbe:0.0.2/0.0.3`. | Created project `SREV`, nine manual cases, test set `SREV:9`; used explicit start-then-finish manual lifecycle; kept local evals as source of truth. | Add JSON/JUnit/agent-eval import with scenario preview, expected/actual policy fields, artifact attachment, and a package automation preflight that explains why an Orchestrator-visible package is not Test Manager-visible. | Do not claim automated Test Cloud execution. |
| 7 | Clarify Case job/task lifecycle readback for operators. PF-022, with PF-016 as UI stale-state support. | Medium. It protects repeatable demo operations and honest status claims. | `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`; `docs/validation/VALIDATION_RESULTS.md` 2026-06-26 demo live-ops readback; tasks `4300080` and `4300219`. | Correlated process, job, task, and audit readbacks manually; refreshed Action Center after external completion; avoided terminal completion claims for older E-002/E-004 jobs. | Add CaseManagement-aware states such as `waiting_for_human_task`, `human_task_completed_continuing`, `case_completed`, or `blocked`, with linked task IDs and current stage in job readback. | Do not claim terminal completion for older E-002/E-004 jobs while they still read `Running`. |

## Claim Boundary Map

| Major feedback claim | Reproduced evidence package | Supporting context only | Caveat / not claimed |
| --- | --- | --- | --- |
| Maestro Case is the right primary product surface and the feedback should focus on human-review readiness. | PF-003/PF-006/PF-007/PF-013/PF-015/PF-026/PF-027/PF-028; `TRACK_SELECTION_DECISION.md`; Workstreams A and B artifacts. | `docs/research/AGENTHACK_FORUM_RESEARCH.md` shows other builders reported Actions, Maestro publishing, and Labs friction. | Forum reports support prioritization only; they are not our PF reproduction evidence. |
| Action Center lifecycle works, but generated reviewer UI is not safe as the final proof surface. | PF-013; `ACTION_CENTER_UI_REPAIR_ASSESSMENT.md`; tasks `4295299`, `4300080`, `4300219`, `4333536`; Workstream B. | None needed. | Action Center is validated for lifecycle/structured return, not generated UI legibility. |
| The full domain audit requires explicit custom audit storage/readback. | PF-015; Data Fabric V2 record; Orchestrator bucket artifact; `service_recovery_core/audit_bundle.py`. | None needed. | Native Case history is PARTIAL, not all-native G-001 PASS. |
| Data Fabric is a viable audit path only on the validated PascalCase V2 schema. | PF-019/PF-023; Workstream D artifact; V2 record `F9D838CE-4671-F111-AC9A-0022489A9A06`. | None needed. | Legacy snake_case record behavior is feedback evidence, not final proof. |
| Test Manager supports manual eval representation but not proven automated Test Cloud execution. | PF-020/PF-021/PF-024; Workstream C artifact; `TEST_MANAGER_MAPPING.md`; JUnit export evidence. | Devpost/Test Cloud category fit is supporting only. | Automated Test Cloud execution and automation linkage remain unclaimed. |

## What Worked Well

Use these as positive counterweights:

- Maestro Case matched the orchestration shape for long-running exception work.
- Action Center worked for real task lifecycle after Actions was enabled: assignment, completion, reviewer comments, and structured return were observable.
- Task APIs preserved raw agent recommendation and final policy decision separately, supporting the governance boundary even when the generated UI was weak.
- Orchestrator buckets worked cleanly for durable JSON audit artifact storage.
- Orchestrator process readback and version history made package pinning visible.
- Test Manager could represent E-001 through E-009 as live manual test cases and a test set; terminal manual execution/report/JUnit worked after using the correct start-then-finish lifecycle.

Evidence:

- PF-013, PF-015, PF-017, PF-020, PF-021.
- `docs/validation/TEST_MANAGER_MAPPING.md`.
- `docs/validation/artifacts/2026-06-25/orchestrator_bucket_audit_artifact_E004_manifest.json`.

## Strongest Critical Feedback

### Primary Recommendation

Add a Maestro Case readiness and human-review preflight path.

It should check:

- tenant services and roles: Actions, Orchestrator, Test Manager, Integration Service, Data Service/Data Fabric,
- Action task required fields such as Title,
- schema-to-generated-page binding for each input/output property,
- case variable to Action input mapping,
- Action output to Case variable mapping,
- package/feed binding and package version to be used by the next run,
- process `AutoUpdate` and package version readback,
- native audit coverage versus required custom audit events.

Why:

- It would have prevented or shortened PF-003, PF-006, PF-007, PF-008, PF-013, PF-017, PF-026, PF-027, and PF-028.
- It should surface when native Case history is not enough for the required domain audit, then guide builders toward validated custom audit storage/readback patterns; PF-015, PF-019, and PF-023 show why this matters for governed human-review workflows.
- It aligns with Maestro Case's target use: end-to-end orchestration across agents, APIs, RPA, and people.

### Secondary Recommendations

- Add a native Case audit/event inspector for linked domain events.
- Add an Action app field-binding inspector and repair flow.
- Add feed-aware process creation and package lookup diagnostics.
- Add schema-aware Data Fabric insert/import diagnostics.
- Add Test Manager eval import from JSON/JUnit/agent-eval outputs, plus a package preflight that explains whether an uploaded Orchestrator package contains Test Manager-visible automations.
- Add CaseManagement-aware job state explanations for human-task workflows.
- Make Case validation, solution dry-run, and Studio Web upload/import share the same readiness contract for human-review cases.

## Final Survey Building Blocks

### Use Case

We built a telecom/broadband service activation and restoration exception workflow in Maestro Case. Business systems can look green while authoritative network evidence is missing, stale, or contradictory. An agent interprets ambiguous notes into structured signals, but deterministic policy makes the closure/routing decision. The demo proves that a raw `closure_candidate` recommendation is preserved, policy can override it to `verify_telemetry` when authoritative telemetry is missing, and policy can escalate to `human_review` when fresh authoritative telemetry contradicts the business state.

The optional live Gemini/Vertex path deepens the same thesis without weakening the control boundary: an advocate interpretation can recommend closure, a skeptic interpretation can find unresolved risk in the same evidence, and policy can route on the structured disagreement signal. The LLMs add useful interpretation pressure; deterministic policy still owns closure and escalation.

### Challenges

The hardest part was not the local policy model. It was turning a first-time Maestro Case build into a repeatable, observable runtime proof. Official docs and Devpost guidance make this the right target for long-running exception work with humans in the loop, but in practice we had to validate tenant service readiness, generated Action app bindings, required Action task fields, package/feed resolution, process version pinning, Action Center task return, Test Manager mapping, audit storage, and whether Case validation agreed with solution dry-run/upload. The strongest pattern is that UiPath exposed the needed primitives, but the product needs more shared preflight and diagnostic guidance for a new builder doing agent + policy + human orchestration.

### One Thing To Change

Add a Maestro Case human-review readiness/preflight wizard. It should verify services, roles, task required fields, Action app schema binding, input/output mappings, package/feed binding, package version pinning, audit-readiness, and agreement between Case validation, solution dry-run, and Studio Web upload/import before the builder starts a live case. This would turn hours of runtime recovery into a short checklist and would align with Maestro Case's official role as the coordination layer for agents, automations, and people.

### What Surprised Us

The positive surprise was that the platform persisted the governance boundary better than the generated UI showed. The raw agent recommendation and policy decision were available through task/API/audit data even when the generated reviewer page mislabeled or hid a proof-critical field. The adoption advice is to validate hard gates early with API readback, not only with the designer or generated UI.

### What Maestro Simplified

Without Maestro, we would have had to stitch together case state, task lifecycle, reviewer comments, policy outputs, package/process versioning, job history, and audit artifacts across unrelated tools. Maestro Case and Action Center gave the core orchestration shell; our feedback is that Maestro should make the domain audit timeline native so agent interpretation, policy decision, evidence state, human action, and versions appear in one place.

## Claims To Avoid

- Do not claim automated Test Cloud execution; current Test Manager validation is manual mapping plus terminal manual execution/report/JUnit export. The `ServiceRecoveryEvalProcessProbe:0.0.2/0.0.3` package probe was Orchestrator-visible but not Test Manager-discoverable/linkable.
- Claim Data Fabric V2 full-payload persistence only for the PascalCase `ServiceRecoveryAuditBundleV2` path; keep the legacy snake_case entity as product-feedback evidence, not final proof.
- Do not claim generated Action Center UI is final-demo ready.
- Do not claim native Case history alone passes the domain audit gate.
- Do not pitch the project as a generic governance platform.
- Do not imply terminal Case job completion while E-002/E-004 jobs still read back as `Running`.

## Evidence Index

| Evidence | Use |
| --- | --- |
| `docs/product/PRODUCT_FEEDBACK_AWARD.md` | Source PF log and evidence matrix. |
| `docs/product/FEEDBACK_SURVEY_DRAFT.md` | Survey question scaffold and draft answer material. |
| `docs/validation/VALIDATION_RESULTS.md` | Chronological validation results and command evidence. |
| `docs/validation/VALIDATION_GATES.md` | Hard gate PASS/PARTIAL implications. |
| `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md` | Repeatable proof path and live readback commands. |
| `scripts/run_demo.sh` | Safe local command to regenerate and verify E-002/E-004 proof artifacts before submission work. |
| `scripts/run_submission_check.sh` | Non-mutating local sanity check for tests, evals, proof artifacts, and key proof strings. |
| `docs/demo/artifacts/demo_proof_manifest.json` | Local 2A/2B proof artifact manifest. |
| `docs/demo/artifacts/evidence_packet_E002_desktop.png` | Judge-facing 2A packet screenshot with controlled verification route. |
| `docs/demo/artifacts/evidence_packet_E004_desktop.png` | Judge-facing 2B packet screenshot with escalated human-review route. |
| `docs/demo/artifacts/evidence_packet_E003_adversarial_desktop.png` | Judge-facing adversarial LLM packet screenshot showing advocate, skeptic, disagreement, and policy escalation. |
| `docs/demo/artifacts/evidence_packet_E003_adversarial_mobile.png` | Mobile viewport check for the adversarial LLM packet. |
| `docs/validation/artifacts/2026-06-26/evidence_packet_E003_adversarial_desktop_1440x1100.png` | Refreshed 1440x1100 adversarial packet screenshot used for final visual review. |
| `docs/validation/artifacts/2026-06-26/evidence_packet_E003_adversarial_mobile_390x900.png` | Refreshed mobile adversarial packet screenshot proving long fields remain legible. |
| `docs/validation/TEST_MANAGER_MAPPING.md` | Test Manager eval mapping and manual execution evidence. |
