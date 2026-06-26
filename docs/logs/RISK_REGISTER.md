# Risk Register

| ID | Risk | Impact | Likelihood | Mitigation | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R-001 | Maestro Case native state/history is insufficient for audit reconstruction. | High | Medium | Use explicit `service-recovery-audit-v1` bundle stored in Orchestrator bucket or persisted in Data Fabric; do not claim native Case history alone. | Platform spike agent | Mitigated via Data Fabric and Bucket |
| R-002 | Policy version pinning is not natively supported. | Medium | Medium | Store policy versions as explicit case metadata/artifact fields and represent migration as audited event. | Platform spike agent | Mitigated explicitly |
| R-003 | Action Center cannot render evidence packet clearly. | Medium | Medium | Use Action Center for lifecycle/return and custom evidence packet/screenshots for judge-readable proof. | UX/build agent | Mitigated with custom surface |
| R-004 | Raw agent recommendation cannot be shown before policy override. | High | Low | Persist agent interpretation event separately from policy decision event in payloads, audit bundles, and evidence packet. | Architecture/build agent | Mitigated |
| R-005 | Test Cloud integration is too heavy for the build timeline. | Medium | Medium | Use local eval harness plus live Test Manager manual mapping; do not claim automated Test Cloud execution. | Eval agent | Partially mitigated |
| R-006 | Agent outputs invalid/low-confidence too often. | High | Medium | Use schema validation, repair loop, eval scenarios, usefulness incident, and deterministic policy fallback. | Agent/eval agent | Mitigated locally |
| R-007 | Demo becomes too complex for five minutes. | High | Medium | Use `scripts/run_submission_check.sh`, `scripts/run_demo.sh`, curated packets/screenshots, and only intentional live reruns. | Demo agent | Reduced |
| R-008 | Platform access/lab readiness blocks build. | High | Low | UiPath Labs access, CLI, Maestro Case, Action Center, Orchestrator, and Test Manager were validated; keep credentials out of repo. | Platform spike agent | Mitigated for current tenant |

## Notes

### 2026-06-18 - Local Core Risk Update

- R-005 mitigation is partially exercised by the local eval harness, but Test Cloud integration remains open.
- R-004 mitigation is partially exercised locally by separate Agent Interpretation Event and Policy Decision Event persistence, but Maestro visibility remains unvalidated.
- R-008 remains open; no UiPath Labs validation was attempted.

### 2026-06-24 - Wave 01 Access Update

- R-008 increased in likelihood for the current run: Safari authentication reached `https://cloud.uipath.com/portal_/missingaccount`, so the logged-in account did not land in an accessible Automation Cloud tenant during validation.
- `uip` CLI availability is no longer a local blocker after installing `@uipath/cli@1.196.0`, but `uip login` still requires an interactive authentication path tied to a valid tenant.
- R-001 through R-004 remain open and unvalidated because Maestro Case access was not confirmed.

### 2026-06-24 20:30 IST - Labs Access Rerun

- R-008 is partially mitigated: Safari login now reaches Automation Cloud org `keepingitlowkey` and tenant `DefaultTenant`.
- Maestro, Studio Web, and Maestro Case project creation are confirmed. R-001 remains open because no live case instance has proven one-view/one-query reconstruction.
- R-002 remains open: platform modeling is available, but live policy-version pinning and migration events are not validated.
- R-003 likelihood increased: Actions / Action Center is not enabled for `DefaultTenant`, so the evidence packet likely needs Case App/custom UI unless tenant service enablement changes.
- R-004 remains open: local override-event persistence is strong, but UiPath live persistence/visibility is not validated.

### 2026-06-24 20:33 IST - Actions Enablement Path

- R-003 root cause is likely tenant service enablement, not missing navigation. Official UiPath docs direct admins to enable Actions through `Admin > Tenants > Edit Services > Actions > Save`.
- CLI auth works, but the CLI does not expose service enablement in the inspected commands.
- Admin/Tenants UI did not render a usable tenants table in Safari automation, so resolution may require manual UI action by the user or a request to UiPath/hackathon administrators.

### 2026-06-24 21:08 IST - Actions Enabled

- R-003 is partially mitigated: Actions was added to `DefaultTenant` after explicit user approval, and Action Center now opens as `Inbox - Action Center`.
- R-003 remains open until a real human review task proves the required evidence packet fields and structured return behavior.

### 2026-06-24 21:40 IST - Maestro Case Designer Checkpoint

- R-001 remains open: Case plan design metadata is visible, but no runtime case instance has proven audit reconstruction.
- R-002 remains open: Case JSON exposes design `version`/`publishVersion`, but active-case policy version pinning is still unvalidated.
- R-003 remains open: Human action is available in the Case task menu, but no evidence packet task has been created or reviewed.
- R-004 remains open: the Case model appears capable of representing agent/policy separation, but live persistence/visibility of linked raw recommendation and override decision is not proven.

### 2026-06-25 01:11 IST - Human Action Placeholder Inserted

- R-003 likelihood decreases but remains open: Studio Web can insert `Human action (placeholder)` into `Stage 1`, proving the Case plan can hold a human-review task scaffold.
- R-003 impact remains medium/high until a configured Action app or equivalent task shows the required evidence packet fields and returns structured reviewer outcomes to the case.
- New product/build risk: selecting the inserted placeholder left the properties panel on stage properties, so task-level configuration may require a separate `Create new Action app` flow or another UI path.
- R-001, R-002, and R-004 remain open because no live case instance has run.

### 2026-06-25 01:22 IST - Action App Schema Inspected

- R-003 likelihood decreases again but remains open: `SimpleApprovalApp` exposes an `ActionSchema` with typed input, input/output, output, and outcome sections.
- R-003 impact remains medium because the stock `Content` and `Comment` fields do not yet prove a structured telecom evidence packet, Action Center rendering, or structured return to a running case.
- New risk: Studio Web announced that RPA/app editing and debugging are moving to local UiPath Assistant and are required for all Community users starting July 22. This may disrupt web-only iteration if the local setup path is required before final submission work.
- Mitigation: keep the current web setup for immediate validation, log PF-005, and avoid relying on web-only app editing after July 22 without validating UiPath Assistant setup.

### 2026-06-25 01:28 IST - Generated Action Page Partial Evidence Packet

- R-003 likelihood decreases because a generated Action page can display custom evidence-packet fields and reviewer approve/reject/comment controls.
- R-003 remains open because `PolicyDecisionJson` failed auto-generation, and a complete reviewer packet plus structured return has not been proven in Action Center or a running case.
- New risk: generated Action pages may silently produce confusing fallback controls (`Unnamed String 1`) when a schema property cannot be rendered, making proof-critical fields easy to miss during a demo build.
- Mitigation: manually bind or regenerate the missing field, capture the repair path, and keep the custom Case App/evidence-packet fallback available until G-003 passes end to end.

### 2026-06-25 01:36 IST - Live Case Runtime Attempt

- R-001 likelihood decreases: a single Maestro case instance view reconstructed ordered execution trail rows, timestamps, stage/task names, global variables, incident details, and job linkage for a live run.
- R-001 remains open because the live run did not yet contain service-recovery evidence state, policy versions, raw agent recommendation, policy decision, closure block reason, or reviewer outcome.
- R-003 remains open with a concrete runtime blocker: the Action app task failed before review with `The Title field is required.`
- New risk: Studio deployment validation can succeed while a required Action task field is missing, surfacing only as a runtime `AppTasks` incident.
- Mitigation: add/map the required Action task title, republish/redeploy, rerun the case, and capture whether the Action Center task renders the evidence packet.

### 2026-06-25 01:46 IST - Title Repair Blocked At Publish

- R-003 is partially mitigated: the required `SimpleApprovalApp` task title was set in the Case designer and the visible task validation warning cleared.
- R-003 remains open because the repaired case definition has not been published into a new package version or validated in a fresh runtime case.
- New risk: Studio Web publish/versioning controls may be difficult to operate through browser automation and are not clearly represented as accessible actionable controls.
- Mitigation: try the publish path again with precise UI interaction, then try UiPath CLI or another browser path if available; keep logs/screenshots so this remains a packaging blocker, not an invented Action Center failure.

### 2026-06-25 18:47 IST - Live 1.0.3 Validation

- R-001 likelihood decreases: `uip maestro case instance get`, `element-executions`, `variables`, and task APIs reconstruct package version, runtime order, stage/task state, timestamps, human action, reviewer metadata, and structured HITL return for case `dde02258-c535-4c52-a8a8-a34d470e0ce6`.
- R-001 remains open because the native case state does not by itself provide a clean domain audit unless raw agent, policy, evidence, block reason, and policy versions are carried as explicit custom payloads.
- R-002 likelihood decreases: package version pinning is observed with direct process `--package-version 1.0.3 --no-auto-update`, and policy versions persisted inside explicit task payloads. Native policy migration is still unproven, so custom migration events remain required.
- R-003 likelihood decreases: Action Center can create, assign, complete, and return structured AppTask output to the case. R-003 remains open for demo legibility because `PolicyDecisionJson` rendered as `Unnamed String 1`.
- R-004 likelihood decreases substantially: task `4295299` persisted raw `AgentInterpretationEvent` with `recommended_next_stage: closure_candidate` and linked `PolicyDecisionEvent` with `decision: override_recommendation`, `to_stage: verify_telemetry`, and `block_reason: missing_authoritative_signal`. Keep R-004 open only for final reviewer UI polish and explicit audit-event implementation.
- R-008 is mitigated for current development: CLI login, Maestro Case, Actions, Orchestrator packages/jobs, and Action Center task APIs are usable in `keepingitlowkey / DefaultTenant`.

### 2026-06-25 19:05 IST - Live 1.0.4 Generated Payload Validation

- R-001 remains open but reduced: live case `3af41e1d-8b04-4eba-aa5e-a95c5c673730` proves explicit E-002 payloads can carry evidence state, raw recommendation, policy decision, block reason, and policy versions through a real Case task. Native one-query domain audit still requires explicit custom audit payloads/events.
- R-002 likelihood decreases again: process `9a7eb300-7b16-4856-b14f-d6f2da3dbe61` read back `ProcessVersion: 1.0.4`, `AutoUpdate: false`, and version history with explicit `1.0.3` then `1.0.4` records. Active-case migration semantics remain a custom-audit concern, but package/process pinning is now observed more strongly.
- R-003 remains open for reviewer UI quality but the task lifecycle is stronger: unassigned task `4300080` required assignment before completion, then returned `Action: reject` and the reviewer comment.
- R-004 is functionally mitigated for API/persistence proof: generated local eval output reached a live task with raw `AIE-E002` `closure_candidate` and linked `PDE-E-002` `override_recommendation` to `verify_telemetry`. Keep open only for final demo UI legibility and custom audit timeline.
- New integration risk: feed-scoped package upload/read succeeded for `1.0.4`, while default package lookup and process creation could not bind the same version. Mitigation: use feed-scoped verification plus `processes update-version` for current validation; log PF-017 and avoid claiming that direct create is reliable for solution-feed Case packages.

### 2026-06-25 19:13 IST - Live 1.0.5 Contradiction Route Validation

- R-004 is further mitigated: live task `4300219` persisted raw `AIE-E004` recommending `closure_candidate` and linked policy `PDE-E-004` requiring `human_review` for `source_contradiction`.
- R-005 likelihood decreases substantially: distinct route behavior is now observed live. Missing authoritative telemetry E-002 routes to `verify_telemetry`; fresh authoritative contradiction E-004 routes to `human_review` with `source_contradiction`.
- R-003 remains open for UI legibility. The task API contains correct `PolicyDecisionJson`, but generated Action Center app binding still likely lacks `ActionProperties.PolicyDecisionJson` and renders `Unnamed String 1`.
- R-001 remains open for native one-query domain audit. Two proof beats are now carried as explicit task payloads, but a durable custom audit event/state model is still needed for final demo-quality reconstruction.

### 2026-06-25 19:25 IST - Custom Audit Bundle Slice

- R-001 is mitigated by an implementation fallback, not by native platform behavior: `service-recovery-audit-v1` reconstructs evidence state, policy versions, raw agent recommendation, policy decision, closure block reason, human review state, and event order in one JSON object.
- R-002 is reduced: the audit bundle pins `interpretation_policy_version` and `decision_policy_version` at top level and inside linked event payloads.
- R-003 is partially reduced for custom UI fallback: `reviewer_packet` gives a structured evidence table, raw agent recommendation, policy decision, block reason, recommended options, and rendering status independent of the generated Action Center label issue.
- New remaining risk: the bundle still needs a live UiPath storage/surface path. Candidate paths are Case custom data, Data Fabric/Data Service, a UiPath-accessible artifact, or a custom Case App/evidence-packet view.

### 2026-06-25 19:35 IST - Static Evidence Packet Renderer

- R-003 is reduced for demo fallback: static HTML artifacts now render the E-002 and E-004 reviewer packets with visible raw agent recommendation, final policy decision, evidence table, block reason, recommended options, and audit order.
- R-003 remains open for live UiPath: the renderer is local/static until embedded in Case App/custom UI or replaced by a repaired Action Center generated page.
- R-007 decreases slightly: the E-004 desktop artifact shows the second proof beat on one screen, reducing demo narration risk.

### 2026-06-25 21:01 IST - Data Fabric Audit Storage Preparation

- R-001 is reduced but still open: Data Fabric is reachable through `uip df`, and the repo now has a proposed `ServiceRecoveryAuditBundle` schema plus an insert-ready E-004 record body. Native Case audit remains PARTIAL, and live Data Fabric create/insert/readback is still unproven.
- R-002 is reduced: the proposed Data Fabric record stores `interpretation_policy_version` and `decision_policy_version` as first-class fields tied to the full audit bundle.
- New risk: Data Fabric entity creation is a tenant schema mutation. Mitigation: keep the schema proposal in repo, request explicit approval before `uip df entities create`, then immediately query/read back any inserted proof-beat record.
- New feedback risk/opportunity: `uip df` works, but Data Fabric did not appear in `uip tools list` during discovery. Mitigation: log PF-018 and use direct `uip df` commands for the next validation step.

### 2026-06-25 21:08 IST - Live Data Fabric Entity Created / Insert Blocked

- R-001 is reduced for schema viability but remains open for durable storage: live entity `ServiceRecoveryAuditBundle` was created and read back by ID, but record insert failed before query-back.
- R-002 is reduced for schema viability: first-class policy-version fields exist in the live entity, but no live audit record has persisted them.
- New blocker: `uip df records insert` rejected valid field-name JSON, minimal JSON, wrapper JSON, field-ID keyed JSON, and array JSON with `case_id` reported missing even though the CLI debug log parsed `case_id`. CSV import also inserted `0` of `1` records. Mitigation: inspect official API/docs or import error file if accessible without secrets; if still blocked, use Case custom payload or file artifact for final audit storage.
- New cleanup consideration: the tenant now contains validation entity `ServiceRecoveryAuditBundle` with zero records. Keep it for continued validation unless the user asks to remove it.

### 2026-06-25 21:17 IST - Orchestrator Bucket Audit Artifact Fallback

- R-001 is materially reduced: native Case history remains partial for domain audit, but a live Orchestrator bucket now stores and returns the E-004 `service-recovery-audit-v1` bundle as one JSON object. This gives the build a validated UiPath-accessible fallback for reconstructing evidence state, policy versions, raw agent recommendation, policy decision, block reason, human review state, and event order.
- R-002 is reduced for explicit version pinning: the bucket-backed artifact persists `interpretation_policy_version` and `decision_policy_version` with the linked events. Native active-case migration still needs a custom audited migration event.
- R-004 is reduced for final audit visibility: the bucket-backed artifact preserves separate `AIE-E004` and `PDE-E-004` objects with `links_to`, `from_recommended_stage`, `to_stage`, and `block_reason`.
- Data Fabric record insert remains open under PF-019, but it is no longer the only viable G-001 fallback. Use Orchestrator bucket artifacts unless Data Fabric insert/query-back is resolved quickly.

### 2026-06-25 23:58 IST - Test Manager Eval Mapping

- R-005 is reduced: the tenant now contains live Test Manager project `SREV` with nine manual test cases and test set `SREV:9` representing E-001 through E-009.
- R-005 is reduced again: manual execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad` contains nine passed manual test case logs.
- R-005 remains open for automated crossover. The local eval harness is not yet linked to a Test Manager automated execution or Orchestrator test automation.
- New nuance: the execution aggregate still reports top-level `Status: Running` after all logs pass, so final claims should cite the passed manual logs and not imply a clean terminal aggregate status until that is resolved.
- Mitigation update: describe the current state as live Test Manager representation plus passed manual logs, not automated Test Cloud execution, until an automated execution record or automation link is validated.

### 2026-06-26 00:36 IST - Demo Live-Ops Readback

- R-007 is reduced for operator repeatability: exact CLI readback commands are now documented for process version, version history, task state, job state, and job history.
- New nuance: completed Action Center AppTasks `4300080` and `4300219` do not prove terminal Case job completion. Both corresponding Case jobs still read back as `State: Running`.
- Mitigation: for the final demo, claim Action Center task lifecycle/reviewer return and audit-bundle reconstruction for the older E-002/E-004 jobs; claim terminal Case Instance completion only for the fresh package `1.0.6` run that reached `LatestRunStatus: Completed`.
- New product feedback captured as PF-022: CaseManagement job/task lifecycle readback needs clearer Case-aware state explanation and more consistent process subcommand folder flag behavior.

### 2026-06-26 00:41 IST - Demo Repeatability and Packet Surface

- R-007 is further reduced: `scripts/run_demo.sh` now gives one safe command to regenerate and verify the E-002/E-004 proof payloads, audit bundles, evidence-packet HTML, and proof manifest.
- R-003 is reduced for final presentation: the custom evidence packet now has a prominent raw AIE -> linked PDE comparison and visually distinguishes controlled verification from escalated exception review.
- Remaining risk: the wrapper intentionally does not start fresh live cases or complete live tasks, because those mutate the tenant. Fresh live reruns still require an explicit operator action and log update.
- Remaining risk: PF-013 still blocks use of generated Action Center UI as the judge-facing proof surface; custom HTML remains the validated workaround.

### 2026-06-26 15:56 IST - Current Risk Posture Refresh

- R-001 is mitigated via the Orchestrator bucket audit bundle fallback. Data Fabric is reduced to a partial row-persistence path until custom payload fields can be read back.
- R-002 is mitigated through explicit package/process/artifact policy-version pinning. Native active-case migration still requires a custom audited event.
- R-003 is mitigated for final presentation by custom evidence packets and committed desktop/mobile screenshot artifacts. Generated Action Center UI remains unsuitable as the primary judge-facing surface.
- R-004 is mitigated by separate persisted AIE/PDE artifacts and evidence-packet comparison panels for E-002, E-004, and the adversarial E-003 packet.
- R-005 remains partial: Test Manager manual mapping and passed logs are validated, but automated Test Cloud execution is not claimed.
- R-006 is mitigated locally by schema validation, the bounded Gemini repair loop, eval coverage, and deterministic policy fallback.
- R-007 is reduced by `scripts/run_submission_check.sh`, `scripts/run_demo.sh`, `scripts/run_llm_demo.sh --evidence-packet-output ...`, and curated proof artifacts.
- R-008 is mitigated for current development because UiPath Labs access and required product surfaces have been validated in `keepingitlowkey / DefaultTenant`.

### 2026-06-26 16:00 IST - Open Risks Resolution (Data Fabric & Case Completion)

- **PF-019 (Data Fabric CSV Import Partial Resolution)**: Data Fabric CSV import created a live E-004 row and readback by record ID succeeds. Direct JSON insert remains unvalidated, and follow-up CLI readback did not expose the imported custom payload fields (`case_id`, policy versions, raw AIE/PDE, audit bundle), so Data Fabric is not yet a proven full audit-reconstruction path.
- **PF-022 (Case Instance Completion Resolution)**: Resolved the Case Instance stuck in `Running` status. The issue was due to a required placeholder human task (`tfTXjrum9`) that had no implementation binding. By updating the Maestro Case package to version `1.0.6`, making the placeholder task optional (`isRequired: false`), uploading it to the Orchestrator solution feed, and updating the process version, new Case Instances now terminally complete (`LatestRunStatus: Completed`) upon completion/submission of the Action Center review tasks.

### 2026-06-26 15:38 UTC - Data Fabric V2 Audit Readback

- R-001 is now mitigated by two UiPath-hosted full-payload paths: Data Fabric V2 and Orchestrator bucket. Native Maestro Case history remains PARTIAL, so do not claim native-only G-001.
- Data Fabric root cause was narrowed: snake_case custom fields in `ServiceRecoveryAuditBundle`/`TestEntity` did not populate through JSON insert/update, and CSV-imported rows read back only system fields. PascalCase custom fields did insert/query/read back correctly.
- Created `ServiceRecoveryAuditBundleV2` (`35e8f6c7-4671-f111-ac9a-002248a16d28`) and inserted E-004 record `F9D838CE-4671-F111-AC9A-0022489A9A06`.
- Query by `CaseId = CASE-BG-CONTRA` returned the domain fields and live refs. Record get returned parseable `RawAgentEventJson`, `PolicyDecisionEventJson`, and `AuditBundleJson`, proving `closure_candidate` raw recommendation linked to the `require_human_review` policy decision.
