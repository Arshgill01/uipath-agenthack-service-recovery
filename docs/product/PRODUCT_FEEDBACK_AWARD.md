# Product Feedback Award Log

The team wants to seriously compete for the Best Product Feedback award. This file is the working evidence log.

## Feedback Principles

Good feedback is:

- specific,
- reproducible,
- tied to a real workflow,
- fair about uncertainty,
- clear about builder impact,
- paired with a concrete improvement suggestion.

Bad feedback is:

- vague frustration,
- unsupported claims,
- duplicate notes with no reproduction detail,
- complaints about user/account setup mixed with product bugs,
- feedback written only at the end from memory.

## How To Use This Log

- Add one feedback entry during every UiPath-facing validation run.
- Prefer one entry per product surface/workflow, not one giant daily entry.
- Link each entry to the relevant wave/gate and validation result.
- Capture evidence while the browser/session is still open.
- Mark duplicate sightings as repeats under the original entry instead of creating vague duplicates.
- Keep the `Feedback Evidence Matrix` current. It is the compaction-resistant source for survey answers 10-13.
- Do not promote a draft survey claim unless it has a feedback ID, expected/observed detail, workaround or mitigation, and evidence path.
- Every entry should carry classification, confidence, and follow-up validation needed so product defects, platform limitations, UX/docs friction, and access confusion stay separate.
- The exact survey-prep capture fields are preserved in `docs/product/FEEDBACK_SURVEY_DRAFT.md`.

## Feedback Evidence Matrix

This matrix groups the current evidence into issue classes. Add new observations as rows, or append repeat sightings to the existing PF entry when the issue class is the same.

| Issue class | Feedback IDs | Classification | Severity | Expected | Observed | Workaround / mitigation | Product improvement | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Labs account and tenant routing clarity | PF-001 | access / UX / docs | high during setup | After Labs login, the builder lands in a usable Automation Cloud org/tenant or gets a clear next action. | Safari login reached `portal_/missingaccount`; no clear account-linking or invite/provisioning status was visible in that session. | User later accessed org `keepingitlowkey` / tenant `DefaultTenant` through a working browser session; Wave 01 was rerun. | Show invite/account/provisioning state on `missingaccount`, including wrong-account, pending-invite, missing-tenant, and switch-org guidance. | `docs/validation/VALIDATION_RESULTS.md` 2026-06-24 Wave 01; PF-001. |
| Maestro recent-projects diagnostic quality | PF-002 | product defect / UX | medium | Maestro home loads recent projects, shows a clear empty state, or identifies the permission/service/backend condition. | Maestro home showed `There was an error fetching your recent projects` while Studio Web and Maestro Case creation still worked. | Use `Start modeling` and capture the created solution URL directly. | Replace the generic error with diagnostic cause, retry action, and correlation/session ID. | `docs/validation/artifacts/2026-06-24/wave01-maestro-home.png`; `docs/validation/VALIDATION_RESULTS.md` 2026-06-24 20:30 IST; PF-002. |
| Action Center dependency readiness | PF-003 | access / missing feature / UX | high | Maestro Case human-review dependencies are enabled or the disabled-service page gives the exact self-service/admin path. | Actions route opened an unregistered-service page for `DefaultTenant`; later Admin `DefaultTenant > Services > Add services > Actions > Add` resolved service availability. | Enabled only `Actions` after explicit user approval; G-003 stayed partial until evidence-packet rendering and structured return are validated. | Add a Labs/Maestro readiness checklist and direct enable/request path for Actions, Test Manager, Orchestrator, Integration Service, Data Service, and required roles. | `docs/validation/artifacts/2026-06-24/wave01-actions-not-enabled.png`; `docs/validation/artifacts/2026-06-24/actions-admin-services-list.png`; `docs/validation/artifacts/2026-06-24/actions-enabled-inbox.png`; PF-003. |
| Maestro Case human-task creation and configuration clarity | PF-004 | UX / accessibility | medium | Filtered task-picker rows are keyboard/click activatable, inserted tasks become clearly configurable, and human-review evidence inputs/outputs are discoverable. | Filtered `Human action` row did not activate in the Zen/computer-use session; unfiltered path inserted `Human action (placeholder)`; `Create new Action app` produced an Action schema path, but mapping back to the case is still not obvious from the Case task. | Use `Add first task > Human action > Human action placeholder` or `Create new Action app`; continue validation through publish/debug and case return mapping. | Make task rows first-class accessible controls; after insertion, select the task and expose `Configure Action app`, `Map inputs`, `Map outputs`, and an evidence-packet starter template. | `docs/validation/artifacts/2026-06-24/g001-maestro-case-json-code-view.png`; `docs/validation/artifacts/2026-06-25/g003-human-action-placeholder-canvas.png`; `docs/validation/artifacts/2026-06-25/g003-action-schema-input-output-properties.png`; PF-004. |
| Studio Web local Assistant migration prompt during hackathon build | PF-005 | UX / integration / docs | medium | A time-boxed hackathon builder can continue or switch environments with clear impact on current project, debugging, and publication. | Studio Web interrupted Action app validation with a prompt saying RPA/app editing and debugging are moving to local UiPath Assistant and are required for all Community users starting July 22. | Selected `Do this later`, then `I'll switch later, just not today` and `Stay on current setup` to keep the current web validation moving. | Add a hackathon-safe readiness banner with exact local Assistant requirements, what still works in web Studio today, deadline impact, and a one-click environment check. | `docs/validation/artifacts/2026-06-25/g003-safari-simple-approval-upgrade-prompt.png`; PF-005. |
| Action app schema-to-page generation for custom evidence fields | PF-006 | UX / product defect candidate / integration | high for G-003 | All valid string input properties generate readable, bound reviewer controls, or the generator gives precise repair actions before/after generation. | `EvidencePacketJson` and `RawAgentRecommendation` generated visible controls, but `PolicyDecisionJson` triggered an auto-generation warning and the page showed an ambiguous `Unnamed String 1` control. | Manual binding/regeneration still needs validation; keep a custom Case App/evidence-packet fallback if the missing policy decision cannot be repaired reliably. | Add schema preflight, per-property generation status, jump-to-failed-control, and an automatic repair/regenerate option that preserves existing controls. | `docs/validation/artifacts/2026-06-25/g003-generated-action-page-partial-evidence-packet.png`; PF-006. |
| Action task deployment/runtime validation for required fields | PF-007 | UX / integration / product defect candidate | high for G-003 | Publish/deploy or task configuration validation catches missing required Action task fields before runtime, with a direct link to the field to repair. | Deployment succeeded and Orchestrator/Apps activated, but the live Maestro case faulted at `SimpleApprovalApp` with `Failure in the AppTasks request - (170000)` and `The Title field is required.` | Add/map the required Action task title, republish/redeploy, and retry/start a fresh case instance. | Add a preflight validator for Action task required fields such as Title, show missing mappings in Studio before deployment, and include field-specific repair links in Maestro incidents. | `docs/validation/artifacts/2026-06-25/g003-action-app-deployment-success.png`; `docs/validation/artifacts/2026-06-25/g003-maestro-action-task-title-required-incident.png`; PF-007. |
| Studio Web publish/versioning after case repair | PF-008 | UX / accessibility / integration | high for G-003 iteration | After a designer repair, the builder can clearly publish a new package version and see whether deployment will use the repaired definition. | The required Action task title was repaired in the Case designer, but `Manage > Versions` still showed only `1.0.0`; the visual `Publish` control was exposed through accessibility only as text inside a broad toolbar/tab group and did not open reliably through available automation. | Keep the repair in the designer, retry publish with precise UI interaction or alternate publish path, and do not rerun the old `1.0.0` package as if it contains the fix. | Make Publish a first-class accessible button; show unsaved/unpublished changes and a direct `Publish new version` callout from Manage when the designer has changed since latest version. | `docs/validation/artifacts/2026-06-25/g003-title-repaired-publish-control-not-opened.png`; PF-008. |
| Studio Web download to CLI pack round trip | PF-009 | product defect candidate / packaging / integration | high for CLI bonus and recovery path | A downloaded Studio Web solution that Studio can publish should either pack locally or give a precise unsupported-feature/preflight reason. | Local CLI pack of the downloaded solution failed generated `SimpleApprovalApp` validation with `Activity is valid only inside Trigger Scope`. | Keep Studio Web publish/deploy as the primary path; treat CLI pack as a diagnostic path until the generated Action app project can be packed cleanly. | Make generated Action app projects CLI-packable or add a compatibility preflight that identifies unsupported generated activities and the repair path. | `tmp/uipath-downloads/maestro-case-current/`; `tmp/uipath-downloads/maestro-case-pack-experiment/`; PF-009. |
| Package upload diagnostic quality | PF-010 | UX / diagnostics / integration | high during package recovery | Package upload errors should identify the invalid package field, manifest/nuspec issue, or missing metadata. | Upload failed with `Invalid package details!` and did not become actionable until the original `.nuspec` was preserved. | Preserve the original `.nuspec` when repacking manually and keep before/after package artifacts for comparison. | Return structured upload validation errors with the failing field, expected value, package part, and a repair hint. | `tmp/uipath-case-packages/manual-1.0.1/Solution.caseManagement.Maestro.Case.nuspec`; PF-010. |
| Case package app binding portability | PF-011 | product defect candidate / packaging / integration | high for live reruns | A republished Case process package should preserve the Action app binding or fail validation before runtime. | Direct Case process package `1.0.1` lost the `.app` binding and faulted `No app: SimpleApprovalApp found in folder: .app`; package `1.0.2` worked after binding the explicit folder path. | Use an explicit folder path for the app binding and verify a fresh case reaches Action Center before claiming G-003. | Validate app bindings at package upload/deploy time and show the resolved folder/app target before activation. | `tmp/uipath-case-packages/Solution.caseManagement.Maestro.Case.1.0.1.nupkg`; `tmp/uipath-case-packages/Solution.caseManagement.Maestro.Case.1.0.2.nupkg`; PF-011. |
| Orchestrator process auto-update readback | PF-012 | product limitation candidate / UX / integration | medium/high for rerun safety | A successful process auto-update command should update the process or report that update is unsupported/no-op with the current package. | Command returned success, but readback stayed `false` / `1.0.0`. | Treat success responses as provisional; always read back process version and auto-update state before rerunning a case. | Make no-op success impossible, or return an operation result that includes before/after auto-update state and package version. | Needs exact command output/readback artifact; PF-012. |
| Action Center generated app task rendering and return | PF-013 | UX / product defect candidate / integration | high for G-003 legibility | Action Center should render generated app fields with the schema display names and return reviewer action/comment as structured case data. | Action Center mechanics proved claim/approve/reject/structured return, but `PolicyDecisionJson` rendered as `Unnamed String 1` while the task API showed the correct persisted value. | Use Action Center mechanics for proof of task lifecycle; repair the generated page label/binding or use a custom packet view for demo legibility. | Preserve schema display names in generated runtime tasks and expose a field-binding inspector for Action Center tasks. | `docs/validation/artifacts/2026-06-25/g003-action-center-task-renders-unassigned-fields-null.png`; `docs/validation/artifacts/2026-06-25/g004-action-center-policy-field-mislabeled-task-4295299.png`; PF-013. |
| Generated app image component placeholder | PF-014 | UX / generated app quality | low/medium | Generated apps should avoid unconfigured media placeholders or show a clear design-time configuration message. | Generated app image component showed `Unable to render image` when no/invalid image was configured. | Remove or configure the image component before demo; do not treat it as a blocking G-003 issue unless it obscures evidence fields. | Omit image controls from generated forms unless an image source exists, or render a design-time-only placeholder with a direct configure/remove action. | `docs/validation/artifacts/2026-06-25/g004-action-center-raw-recommendation-visible-task-4295299.png`; PF-014. |
| Live Case audit and override visibility | PF-015 | integration / UX / missing feature | high for G-001/G-004 audit | One case view or one query reconstructs evidence state, policy versions, raw recommendation, policy decision, closure block, human action, and timestamps. | CLI/task APIs can reconstruct most of the evidence chain, but native Case history still needs explicit custom payloads for a clean one-query domain audit; Action Center UI hid the policy value behind a generated label issue. | Use the `service-recovery-audit-v1` bundle, explicit package/policy version fields, and generated reviewer packets; keep generated Action Center UI as task mechanics, not the sole audit surface. | Add a native Case audit/event inspector for custom domain events with linked agent interpretation, policy decision, human action, and package/policy versions in one timeline/query. | `docs/validation/VALIDATION_RESULTS.md` 2026-06-25 18:47/19:25 IST; `service_recovery_core/audit_bundle.py`; PF-015. |
| Action Center refresh after external task completion | PF-016 | UX / integration | medium | If a task is completed through API/CLI, an open Action Center task tab should either update automatically or clearly require refresh. | After `uip tasks complete` returned success and task API showed `Completed`, the open Safari tab still displayed the task under `Pending` until browser refresh. | Refresh the task tab; after refresh, Action Center correctly moved task `4295299` to `Completed` and showed `(reject)`. | Add real-time status sync or a stale-state banner when an open task has been completed outside the current browser session. | `docs/validation/artifacts/2026-06-25/g004-action-center-stale-pending-after-cli-complete-task-4295299.png`; `docs/validation/artifacts/2026-06-25/g004-action-center-completed-reject-task-4295299.png`; PF-016. |
| Solution-feed package visibility and process binding | PF-017 | integration / UX / diagnostics | high for CLI/package recovery | A package uploaded successfully to a solution feed should be visible to the process-binding path, or the CLI should require/propagate the feed selector consistently. | Upload and feed-scoped `packages get` succeeded for `Solution.caseManagement.Maestro.Case:1.0.4`; default package lookup and `processes create --package-version 1.0.4` could not bind it. | Use `packages get --feed-id` to verify the package and `processes update-version` on an existing process to move to `1.0.4`. | Add feed-aware process creation or a clear diagnostic that says the package exists in feed X but the requested folder/process binding is resolving feed Y. | `docs/validation/VALIDATION_RESULTS.md` 2026-06-25 19:05 IST; PF-017. |
| Data Fabric CLI discovery mismatch | PF-018 | UX / integration / diagnostics | medium | CLI tool discovery should show the Data Fabric capability when `uip df` is installed and usable, or explain why it is a built-in command rather than a listed tool. | `uip df --help` and `uip df entities list --native-only --output json` worked, but `uip tools list --output json` did not expose a corresponding Data Fabric tool entry during discovery. | Use direct `uip df` commands and document the exact entity schema/record commands before mutating the tenant. | Make `uip tools list` include built-in product command surfaces or add a `uip tools explain df` style diagnostic so builders can discover available CLI capabilities consistently. | `docs/validation/VALIDATION_RESULTS.md` 2026-06-25 21:01 IST; `docs/architecture/data_fabric/service_recovery_audit_bundle_entity.json`; PF-018. |
| Data Fabric record insertion payload mapping | PF-019 | product defect candidate / integration / diagnostics | high for G-001 custom audit storage | After creating and reading a Data Fabric entity, `records insert` should accept JSON keyed by documented field names or return the exact expected payload shape. | Entity create/readback succeeded, but `records insert` rejected file, inline object, minimal object, wrapper object, field-ID keyed object, and array payloads with `case_id` reported missing even when debug parsing showed `case_id` in the body. CSV import returned success envelope but inserted `0` of `1` records. | Keep the entity for continued validation; inspect import error file/API docs if accessible; use Case custom payload/file artifact if insert remains blocked. | Add schema-aware insert/import validation that echoes recognized/unrecognized fields, fixes docs/help examples if the expected shape differs, and includes a correlation/session ID for support. | `docs/validation/VALIDATION_RESULTS.md` 2026-06-25 21:08 IST; PF-019. |

## Best Insights So Far

- The highest-impact feedback is not a single bug; it is dependency readiness for a first-time Maestro Case builder. PF-003 shows that Action Center was required for the intended human-review path but was not enabled by default, and the disabled-service page did not point to the observed admin resolution path.
- The strongest product-design insight is that Maestro Case successfully exposes the right primitives for this architecture: Case app, case plan, stages, rules, task types, Human action, Agent, Agentic process, and Case JSON/code view. The remaining friction is discovery and configuration clarity, not lack of conceptual fit.
- The fairest framing for PF-001 is access/account-state ambiguity, not a confirmed product defect. Later tenant access worked, so this should be submitted as onboarding diagnostics feedback.
- PF-004 should be framed as three related observations: filtered picker activation/accessibility friction, post-insertion configuration ambiguity, and the separate Action app path that exposes schema/page primitives but not obvious case return mapping.
- PF-006, PF-007, and PF-008 are currently the strongest high-specificity feedback items for G-003: PF-006 covers design-time generation reliability; PF-007 covers deploy/runtime validation gap for a required Action task field; PF-008 covers repair-to-publish iteration friction.
- Action Center moved from tenant-service blocker to usable task lifecycle: claim, approve, and structured return have now been observed through the live validation artifacts. The remaining product-feedback issue is legibility and binding quality, especially `PolicyDecisionJson` rendering as `Unnamed String 1`.
- PF-013 is a headline feedback candidate: the platform persisted the proof-critical policy payload correctly through task APIs, but the generated reviewer UI lost the field binding/label. This is fair feedback because it separates a strong backend/runtime result from a UX/generation issue.
- PF-015 is a headline product-design insight: Maestro Case can orchestrate the right participants, but regulated/domain workflows need a native audit/event inspector for linked agent interpretation, policy decision, human action, package version, and policy versions.
- PF-017 is the strongest CLI/platform integration feedback: the package existed in the solution feed and could be read with `--feed-id`, but the process-create path could not bind it and did not expose the same feed selector.
- PF-018 is a smaller but useful CLI-discovery feedback item: Data Fabric was available through `uip df`, but the general tool listing did not reveal it. This matters because first-time builders use discovery commands to decide which platform surfaces are actually accessible.
- PF-019 is now a high-impact Data Fabric integration finding: entity create/readback worked, but record insert could not map documented JSON payloads to required fields. This directly affects regulated audit storage and is a strong product-feedback candidate if the CSV/API workaround also fails.
- The Orchestrator bucket lifecycle is a useful positive counterpoint: create/upload/list/download worked cleanly for a JSON audit artifact and gave the build a real UiPath-hosted fallback when Data Fabric records were blocked. This should be cited under "what worked well" rather than turned into a complaint.
- The CLI/package recovery path is valuable feedback because it shows a second integration surface: downloaded Studio Web assets, local pack/upload, package metadata, app bindings, and Orchestrator process versioning. Keep those entries separate from Action Center rendering claims.

## Draft Survey Answer Scaffold

Draft only. Evidence-backed but not final submission prose.

| Survey question | Draft evidence-backed answer components | Evidence to cite before finalizing |
| --- | --- | --- |
| Q10 - What UiPath products did you use? | Automation Cloud, Maestro, Maestro Case / Case app, Studio Web, Actions / Action Center, Orchestrator service listing, Integration Service listing, Data Fabric listing, Test Manager listing, UiPath CLI. Note that deep validation has so far centered on Automation Cloud, Maestro, Studio Web, Maestro Case, and Actions. | Wave 01 validation results; product launcher screenshot; CLI help output in `docs/validation/VALIDATION_RESULTS.md`. |
| Q11 - What worked well? | Automation Cloud eventually landed in org `keepingitlowkey` / tenant `DefaultTenant`; Maestro opened and exposed case/process surfaces; Studio Web created a real `Maestro Case` project; Case designer exposed stages, rules, Case app metadata, task types, and JSON/code view; Action Center opened after Actions was enabled; JSON editor guarded against saving malformed accidental input; Action app schema exposed typed inputs, outcomes, and generated a mostly usable evidence review page; Orchestrator bucket operations worked cleanly for a JSON audit artifact through CLI create/upload/list/download/readback verification. | PF-002, PF-003, PF-004, PF-006; `wave01-studio-maestro-bpmn-created.png`; `g001-maestro-case-project-created.png`; `g001-maestro-case-json-code-view.png`; `actions-enabled-inbox.png`; 2026-06-25 G-003 validation results; `docs/validation/artifacts/2026-06-25/orchestrator_bucket_audit_artifact_E004_manifest.json`. |
| Q12 - What challenges did you encounter? | Group by issue class: account/tenant routing ambiguity, Maestro recent-projects generic fetch error, Action Center dependency not enabled with insufficient disabled-service guidance, Human action picker/configuration ambiguity, Studio Web local Assistant migration uncertainty, schema-to-page generation failure for a proof-critical evidence field, deployment validation passing even though the live Action task was missing a required Title, CLI/package round-trip failure, generic upload diagnostics, app binding drift, process auto-update/readback ambiguity, runtime task label legibility, solution-feed package/process binding mismatch, Data Fabric CLI discovery mismatch, Data Fabric record insert payload mapping failure, and generated image placeholder quality. Keep access confusion, product limitations, UX/docs friction, and product defect candidates separate. | Feedback Evidence Matrix rows PF-001 through PF-019. |
| Q13 - What should UiPath improve? | Recommended top answer: add a Maestro Case readiness and human-review setup path that checks tenant services/roles, links directly to enable Actions when permitted, scaffolds a human evidence-packet task, shows exact input/output mapping steps, validates generated Action page controls per schema property, and runs a preflight for required Action task fields before deployment. Secondary improvements: native case audit/event inspector, schema-aware Data Fabric insert diagnostics, feed-aware CLI process creation, consistent CLI discovery for built-in product command surfaces such as Data Fabric, better package/upload diagnostics, app binding validation, process version readback, `missingaccount` diagnostics, recent-projects error diagnostics, accessible task-picker rows, and Studio Web/local Assistant transition guidance. | PF-003 as highest-impact setup blocker; PF-006/PF-007/PF-013 as proof-critical G-003 build blockers; PF-015 as native audit insight; PF-019 as Data Fabric storage blocker; PF-017 as feed/process CLI integration issue; PF-018 as CLI discovery issue; PF-009 through PF-012 as CLI/package recovery blockers; PF-004 as core human-task workflow friction. |

## Scoring Rubric For Future Feedback

Use this rubric before promoting an observation into a survey claim.

| Score | Standard |
| --- | --- |
| 5 | Reproduced or directly observed, exact workflow captured, expected vs observed written, severity tied to a gate/build impact, workaround documented, concrete product improvement proposed, evidence artifact linked. |
| 4 | Directly observed with evidence and impact, but reproduction count or workaround quality is incomplete. |
| 3 | Directly observed but missing expected/observed detail, severity rationale, or evidence artifact. Keep in log, do not make it a headline survey claim yet. |
| 2 | Plausible but based on inference from adjacent behavior. Convert to a future validation placeholder instead of feedback. |
| 1 | Frustration, preference, or memory-only note. Do not use for award submission. |

## Survey Answer Map

Use accumulated entries to answer the final feedback survey.

| Survey question | Evidence source in this file | How to answer |
| --- | --- | --- |
| Which UiPath products did you use? | `Product surface`, `Wave/gate` | Summarize surfaces touched: Automation Cloud, Maestro Case, Studio Web, Action Center/Actions, Test Manager, Integration Service, Orchestrator, CLI. |
| What worked well? | `What worked` | Pull concrete successful workflows, not general praise. |
| What challenges did you encounter? | `What failed or confused us`, `Expected`, `Observed` | Group by access, docs, UX, missing feature, product defect, integration, performance. |
| How did it affect your build? | `Impact` | Tie to blocked gates, delayed implementation, workaround cost, demo risk, architecture change. |
| What workaround did you use? | `Workaround` | List exact workaround and whether it is acceptable for demo only or durable. |
| What one thing should UiPath improve? | `Suggested improvement` | Convert the highest-impact issue into a concrete product/doc improvement. |
| What surprised you? | `What worked`, `What failed or confused us` | Pair positive surprises with adoption advice for first-time builders. |
| What did Maestro simplify? | Gate entries for Maestro/Studio | Cite specific orchestration surfaces that avoided custom glue. |
| What evidence supports this? | `Evidence` | Include screenshots, URLs, commands, validation result links, artifact paths. |

## Feedback Index

| ID | Date | Surface | Workflow | Wave/gate | Classification | Severity | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PF-001 | 2026-06-24 | Automation Cloud | Labs tenant access | Wave 01 | access / UX / docs | high | superseded | `docs/validation/VALIDATION_RESULTS.md` |
| PF-002 | 2026-06-24 | Maestro | Home/recent projects | Wave 01 | product defect / UX | medium | open | `docs/validation/artifacts/2026-06-24/wave01-maestro-home.png` |
| PF-003 | 2026-06-24 | Actions / Action Center | Pending task access | Wave 01 / G-003 | access / missing feature | high | resolved | `docs/validation/artifacts/2026-06-24/wave01-actions-not-enabled.png` |
| PF-004 | 2026-06-24 | Studio Web / Maestro Case | Add Human action task | G-003 | UX / accessibility | medium | repeated / partial | `docs/validation/artifacts/2026-06-25/g003-human-action-placeholder-canvas.png` |
| PF-005 | 2026-06-25 | Studio Web | Local Assistant migration prompt | G-003 | UX / integration / docs | medium | open | `docs/validation/artifacts/2026-06-25/g003-safari-simple-approval-upgrade-prompt.png` |
| PF-006 | 2026-06-25 | Studio Web / Action app | Generate page from Action schema | G-003 | UX / product defect candidate / integration | high | open | `docs/validation/artifacts/2026-06-25/g003-generated-action-page-partial-evidence-packet.png` |
| PF-007 | 2026-06-25 | Maestro Case / Action tasks | Live Action task runtime validation | G-003 | UX / integration / product defect candidate | high | open | `docs/validation/artifacts/2026-06-25/g003-maestro-action-task-title-required-incident.png` |
| PF-008 | 2026-06-25 | Studio Web / Publish | Publish repaired Case plan | G-003 | UX / accessibility / integration | high | open | `docs/validation/artifacts/2026-06-25/g003-title-repaired-publish-control-not-opened.png` |
| PF-009 | 2026-06-25 | Studio Web / UiPath CLI | Downloaded solution local pack | G-003 / G-008 | product defect candidate / packaging / integration | high | provisional | `tmp/uipath-downloads/maestro-case-current/` |
| PF-010 | 2026-06-25 | Orchestrator / package upload | Manual repack upload diagnostics | G-003 / G-008 | UX / diagnostics / integration | high | provisional | `tmp/uipath-case-packages/manual-1.0.1/Solution.caseManagement.Maestro.Case.nuspec` |
| PF-011 | 2026-06-25 | Maestro Case package / app binding | Direct Case process package rerun | G-003 | product defect candidate / packaging / integration | high | workaround found | `tmp/uipath-case-packages/Solution.caseManagement.Maestro.Case.1.0.2.nupkg` |
| PF-012 | 2026-06-25 | Orchestrator process versioning | Process auto-update command/readback | G-003 / G-008 | product limitation candidate / UX / integration | medium/high | provisional | needs command/readback artifact |
| PF-013 | 2026-06-25 | Action Center / generated app task | Claim, approve/reject, structured return, field rendering | G-003 | UX / product defect candidate / integration | high | observed with caveat | `docs/validation/artifacts/2026-06-25/g004-action-center-policy-field-mislabeled-task-4295299.png` |
| PF-014 | 2026-06-25 | Studio Web / generated app | Image component rendering | G-003 | UX / generated app quality | low/medium | observed | `docs/validation/artifacts/2026-06-25/g004-action-center-raw-recommendation-visible-task-4295299.png` |
| PF-015 | 2026-06-25 | Maestro Case / Action Center / CLI | Live case audit and override proof | G-001 / G-002 / G-004 | integration / UX / missing feature | high | observed / implementation decision made | `docs/validation/VALIDATION_RESULTS.md` |
| PF-016 | 2026-06-25 | Action Center / Tasks API | Open task tab after CLI completion | G-003 / G-008 | UX / integration | medium | observed | `docs/validation/artifacts/2026-06-25/g004-action-center-completed-reject-task-4295299.png` |
| PF-017 | 2026-06-25 | Orchestrator / UiPath CLI / solution feed | Upload package, read package, create/update process | Wave 07 / G-002 / G-008 | integration / UX / diagnostics | high | observed workaround | `docs/validation/VALIDATION_RESULTS.md` |
| PF-018 | 2026-06-25 | Data Fabric / UiPath CLI | CLI command discovery for Data Fabric | G-001 / G-002 / G-008 | UX / integration / diagnostics | medium | observed | `docs/validation/VALIDATION_RESULTS.md` |
| PF-019 | 2026-06-25 | Data Fabric / UiPath CLI | Record insert payload mapping | G-001 / G-002 / G-008 | product defect candidate / integration / diagnostics | high | open blocker | `docs/validation/VALIDATION_RESULTS.md` |

## Entry Template

```md
### PF-XXX - YYYY-MM-DD - Product Surface / Workflow

Context:
- ID:
- Status: open / repeated / resolved / superseded
- Goal:
- Product surface:
- Account/tenant:
- Wave/gate:

What worked:
- ...

What failed or confused us:
- ...

Expected:
- ...

Observed:
- ...

Impact:
- Build impact:
- Demo/submission impact:
- Severity: low / medium / high

Workaround:
- ...

Suggested improvement:
- ...

Evidence:
- Screenshot/path/link:
- Commands/logs:

Classification:
- access / docs / UX / missing feature / product defect / performance / integration / other

Confidence:
- high / medium / low, with reason

Follow-up validation needed:
- exact screenshot, command output, run ID, package artifact, or none

Survey tags:
- product-used
- worked-well
- pain-point
- workaround
- improvement
- evidence
```

## Feedback Entries

### PF-001 - 2026-06-24 - Automation Cloud Login / Labs Tenant Access

Context:

- ID: PF-001.
- Status: superseded by the later successful Safari login on 2026-06-24 20:30 IST.
- Goal: complete Wave 01 platform access inventory.
- Product surface: Automation Cloud login / portal routing.
- Account/tenant: Google login attempted for the hackathon account.
- Wave/gate: Wave 01.

What worked:

- UiPath CLI package could be installed locally.
- Browser reached UiPath login.

What failed or confused us:

- After login attempt, browser landed at `portal_/missingaccount` rather than an accessible Automation Cloud tenant.
- It was not clear from that page/session what action was required to attach the account to the AgentHack Labs tenant.

Expected:

- After accepting a Labs invite and logging in, the account should land in a usable Automation Cloud organization/tenant or provide a clear next action.

Observed:

- Prior agent recorded `https://cloud.uipath.com/portal_/missingaccount`.
- Product surfaces such as Maestro, Maestro Case, Action Center, Test Cloud, Integration Service, and Orchestrator could not be inventoried in that session.

Impact:

- Build impact: blocked hard validation gates G-001 through G-004.
- Demo/submission impact: delayed confirmation of the primary Maestro Case track.
- Severity: high during access setup.

Workaround:

- User later reported receiving Labs access and logging in through Zen browser. Wave 01 must be rerun against the working session before closing this feedback item.

Suggested improvement:

- Provide clearer Labs invite/account-linking status on `missingaccount`, including whether invite acceptance is pending, wrong account is logged in, tenant provisioning is incomplete, or the user needs to switch organizations.

Evidence:

- See `docs/validation/VALIDATION_RESULTS.md`, Wave 01 entry.

Classification:

- access / UX / docs

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence

### PF-015 - 2026-06-25 - Maestro Case / Domain Audit And Override Timeline

Context:

- ID: PF-015.
- Status: observed / implementation fallback created.
- Goal: validate whether one case view or one query can reconstruct the governed service-recovery proof beat.
- Product surface: Maestro Case, Case instance APIs, Action Center task APIs, UiPath CLI.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-001, G-002, G-004, G-005.

What worked:

- Live Case and task APIs exposed package version, runtime order, stage/task state, task source linkage, timestamps, reviewer action, and structured HITL return.
- Action Center task payloads preserved raw `AgentInterpretationEvent` and linked `PolicyDecisionEvent` separately.
- Process readback and version history made package pinning visible across `1.0.3`, `1.0.4`, and `1.0.5`.
- The local implementation now generates a `service-recovery-audit-v1` bundle containing evidence state, policy versions, raw agent recommendation, policy decision, closure block reason, human review state, and event order in one JSON object.

What failed or confused us:

- Native Case history alone did not provide a clean domain audit timeline for the proof beat.
- To reconstruct the governed decision, we still had to carry explicit payloads and combine Case instance, task, process, and package/version reads.
- The generated Action Center UI rendered a proof-critical policy field as `Unnamed String 1`, so the reviewer-facing surface was weaker than the persisted audit data.

Expected:

- A governed agentic Case should expose one audit view or one query that shows the linked sequence: evidence state, active policy versions, raw agent recommendation, policy decision, closure block reason, human action, and event timestamps.

Observed:

- The platform can orchestrate and persist the pieces, but the domain audit must currently be modeled explicitly.
- The project now uses `service-recovery-audit-v1` as the custom audit contract and can generate it with `python -m service_recovery_core.evals --audit-bundle-scenario E-002` or `E-004`.

Impact:

- Build impact: high. This determines whether G-001 is native PASS or custom-audit PARTIAL/PASS.
- Demo/submission impact: high. The main demo needs to show that policy overrode a raw agent recommendation, not merely that the final route changed.
- Severity: high for regulated or audit-heavy Maestro Case adoption.

Workaround:

- Use explicit domain audit bundles/events and store them in the chosen UiPath-accessible path: Case custom data, Data Fabric/Data Service, file artifact, or custom evidence-packet view.
- Keep native Case runtime/history for operational traceability, but do not rely on it as the sole governed-domain audit record.

Suggested improvement:

- Add a native Maestro Case audit/event inspector for custom domain events.
- Let builders declare linked event types, such as Agent Interpretation Event, Policy Decision Event, Evidence State Event, and Human Review Event.
- Show event links, policy/package versions, source payload refs, stage transitions, and human actions in one timeline/query.
- Provide a standard evidence-packet audit template for agent + policy + human workflows.

Evidence:

- Commands/logs: `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 18:47, 19:05, 19:13, and 19:25 IST entries.
- Code artifact: `service_recovery_core/audit_bundle.py`.
- Tests: `tests/test_audit_bundle.py`.
- Live E-002 task/case: task `4300080`, case `3af41e1d-8b04-4eba-aa5e-a95c5c673730`.
- Live E-004 task/case: task `4300219`, case `60e52ca5-6891-45b4-9e98-e1b08a984f06`.

Classification:

- integration / UX / missing feature

Confidence:

- high. The observation is based on live Case/task/process reads plus a tested implementation fallback.

Follow-up validation needed:

- Store or surface the `service-recovery-audit-v1` bundle in a live UiPath path.
- Repair or replace the generated Action Center reviewer view so the same audit fields are legible in the demo.

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence

### PF-013 - 2026-06-25 - Action Center / Generated App Task Field Rendering

Context:

- ID: PF-013.
- Status: observed with caveat.
- Goal: validate whether a human reviewer can clearly see the structured evidence packet, raw agent recommendation, policy decision, block reason, recommended options, and return an approve/reject/comment result.
- Product surface: Action Center, generated Action app runtime, Maestro Case human task.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-003, G-004, Wave 07.

What worked:

- Action Center created real AppTasks from live Maestro Case runs.
- Task APIs persisted structured `Content`, `EvidencePacketJson`, `RawAgentRecommendation`, `PolicyDecisionJson`, and `Comment` fields.
- The raw agent event and final policy decision remained separate in task data.
- Reviewer actions returned structurally to the case: assigned user, completed user, action, comment, timestamps, and task source metadata.
- Unassigned tasks could be assigned to the logged-in user and then completed through the CLI.

What failed or confused us:

- The generated reviewer page did not render the proof-critical policy decision under its schema name.
- Action Center showed `Unnamed String 1` / `Unnamed string 1` instead of a readable `PolicyDecisionJson` field.
- The task API showed the correct `PolicyDecisionJson` value, so the failure appears to be generated page binding/label legibility rather than task-data loss.
- A read-only inspection of downloaded generated app assets found bindings for `ActionProperties.Content`, `ActionProperties.EvidencePacketJson`, `ActionProperties.RawAgentRecommendation`, and `ActionProperties.Comment`, but not for `ActionProperties.PolicyDecisionJson`; the page had two `Unnamed String 1` label controls instead.

Expected:

- Every valid schema property should either generate a visible, correctly labeled reviewer field or fail generation with a precise repair action.
- For a governance/audit workflow, policy decision fields should be as visible as raw agent recommendations; otherwise the demo can accidentally show only the agent output and hide the governing override.

Observed:

- Task `4295299` persisted `PolicyDecisionJson` with `decision: override_recommendation`, `to_stage: verify_telemetry`, and `block_reason: missing_authoritative_signal`, but the Action Center page mislabeled/hid the value.
- Task `4300080` persisted generated E-002 `PolicyDecisionJson` from the local eval exporter.
- Task `4300219` persisted generated E-004 `PolicyDecisionJson` with `decision: require_human_review`, `to_stage: human_review`, and `block_reason: source_contradiction`.
- Reviewer lifecycle worked after assignment, but final demo legibility remains partial until the generated field binding is repaired.

Impact:

- Build impact: high for G-003/G-004 demo quality. The platform preserved the core evidence, but the reviewer UI did not make a proof-critical field legible.
- Demo/submission impact: high. The central story depends on showing raw agent recommendation separately from final policy decision.
- Severity: high for generated human-review app adoption in governed workflows.

Workaround:

- Use task API/Case variables as the authoritative evidence during validation.
- For demo polish, repair the generated page by changing the `Unnamed String 1` label to `Policy Decision` and binding the value to `ActionProperties.PolicyDecisionJson.toString`, or replace the generated view with a custom evidence-packet view.
- Keep Action Center for task lifecycle and structured return, but do not rely on the current generated page as the sole audit surface.

Suggested improvement:

- Add a generated-app field binding inspector showing each schema property, generated control, label, binding expression, and validation status.
- If a schema property cannot be rendered, fail generation or show a repair card instead of silently producing `Unnamed String 1`.
- Add a human-review evidence-packet template for Maestro Case that treats policy decisions, raw agent output, evidence state, and block reason as first-class fields.
- In Action Center runtime, expose a debug/read-only task data panel so reviewers/builders can compare rendered fields with persisted task data during development.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g004-action-center-policy-field-mislabeled-task-4295299.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g004-action-center-raw-recommendation-visible-task-4295299.png`.
- Comparison artifact: `docs/demo/artifacts/evidence_packet_E004_desktop.png` shows the same proof beat rendered with the policy decision field legible.
- Commands/logs: `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 18:47, 19:05, and 19:13 IST entries.
- Live task IDs: `4295299`, `4300080`, `4300219`.

Classification:

- UX / product defect candidate / integration

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence

### PF-017 - 2026-06-25 - Orchestrator / CLI Solution-Feed Package Binding

Context:

- ID: PF-017.
- Status: observed workaround.
- Goal: validate Wave 07 with a generated E-002 payload in a fresh live Case package version.
- Product surface: UiPath CLI, Orchestrator package feed, solution feed, process versioning.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: Wave 07, G-002, G-008.

What worked:

- `uip or packages upload ... --feed-id 831bf59a-a3f1-4aa8-8890-f01b857c18f3` successfully uploaded `Solution.caseManagement.Maestro.Case:1.0.4`.
- `uip or packages get Solution.caseManagement.Maestro.Case:1.0.4 --feed-id 831bf59a-a3f1-4aa8-8890-f01b857c18f3 --all-fields` confirmed the package as active Case Management package version `1.0.4`.
- `uip or processes update-version ... --package-version 1.0.4` successfully moved the existing validation process to `1.0.4`.
- Process readback and version history showed explicit `1.0.3` then `1.0.4` records while `AutoUpdate` remained `false`.

What failed or confused us:

- Default `uip or packages get Solution.caseManagement.Maestro.Case:1.0.4` returned `HTTP 404: Package not found` unless the solution feed ID was supplied.
- `uip or processes create ... --package-version 1.0.4` failed with `Error validating process runtime prerequisites` and instructed the builder to run the default package lookup command, which also could not see the feed-scoped package.
- `processes create` did not expose a `--feed-id` option, so the successful upload/read path could not be passed into new process creation.
- A second upload using `--folder-key` reported `HTTP 409: Package already exists`, confirming the package existed while the default process-create path still could not bind it.

Expected:

- If package upload succeeds to a solution feed, process creation in the same folder should resolve that feed or expose the required feed selector.
- If the package exists in one feed but the process binder is checking another feed, the CLI should say that explicitly and name both feed/folder contexts.

Observed:

- Feed-scoped package read succeeded for feed `831bf59a-a3f1-4aa8-8890-f01b857c18f3`.
- Default package read returned 404.
- Direct process creation failed prerequisite validation.
- Existing-process `update-version` succeeded and let the live validation continue.

Impact:

- Build impact: high during hackathon iteration because it looked like the package version was uploaded but unusable for a new process.
- Demo/submission impact: medium/high; package/version repeatability is central to policy-version pinning evidence and CLI/coding-agent bonus proof.
- Severity: high for CLI recovery path and repeatable build operations.

Workaround:

- Verify solution-feed packages with `--feed-id`.
- Use `uip or processes update-version <existing-process> --package-version <version> --folder-key <folder>` when new process creation cannot bind the feed-scoped package.
- Always read back `uip or processes get` and `uip or processes version-history` before starting a case.

Suggested improvement:

- Add `--feed-id` to `uip or processes create`, or make it infer the folder's solution feed when `--folder-key` targets a solution folder.
- When package validation fails, return a diagnostic such as: `Package exists in feed 831... but process creation searched tenant feed/default feed`.
- Make upload/get/list/create process commands use consistent feed-resolution rules, or show the resolved feed in every command response.
- In process-create error instructions, include the exact `packages get ... --feed-id ...` command if the package was uploaded to a non-default feed.

Evidence:

- Commands/logs: `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 19:05 IST Wave 07 Live Generated Payload Run.
- Package under test: `Solution.caseManagement.Maestro.Case:1.0.4`.
- Process updated: `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`.
- Live case proving workaround: `3af41e1d-8b04-4eba-aa5e-a95c5c673730`.

Classification:

- integration / UX / diagnostics

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence

### PF-018 - 2026-06-25 - Data Fabric / CLI Command Discovery

Context:

- ID: PF-018.
- Status: observed.
- Goal: prepare a durable UiPath-accessible storage path for `service-recovery-audit-v1` bundles if native Maestro Case history remains insufficient for G-001.
- Product surface: UiPath CLI, Data Fabric.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-001, G-002, G-008.

What worked:

- `uip df --help` exposed Data Fabric entity and record commands.
- `uip df entities list --native-only --output json` returned success with an empty native entity list, proving the command surface is reachable in the tenant.
- The CLI help for entity creation and record insertion provided enough structure to design a tenant-safe schema proposal before mutating Data Fabric.

What failed or confused us:

- `uip tools list --output json` did not expose a corresponding Data Fabric tool entry in the inspected output, even though `uip df` was usable.
- For a first-time builder trying to discover available UiPath platform capabilities from the CLI, this makes Data Fabric look absent unless they already know the direct `uip df` command.

Expected:

- General CLI discovery should list available product command surfaces, including Data Fabric, or clearly distinguish built-in commands from installable tools.

Observed:

- Direct Data Fabric commands worked.
- Tool discovery did not reveal the same capability in the inspected output.

Impact:

- Build impact: medium. It did not block the build after the direct command was found, but it slowed platform inventory and could cause builders to miss a viable audit-storage path.
- Demo/submission impact: low/medium. The CLI/coding-agent bonus story is stronger when discovery commands accurately reflect available lifecycle tools.
- Severity: medium.

Workaround:

- Use direct `uip df` commands.
- Keep schema proposals in repo and ask for explicit approval before live `uip df entities create`.

Suggested improvement:

- Include built-in product command surfaces such as Data Fabric in `uip tools list`, or add a command that explains whether a surface is built-in, installed, unavailable, or permission-blocked.
- If `uip tools list` is intentionally scoped only to installable tools, name that scope in the output/help text and point to the product command groups.

Evidence:

- Commands/logs: `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 21:01 IST Data Fabric Audit Storage Preparation.
- Schema proposal: `docs/architecture/data_fabric/service_recovery_audit_bundle_entity.json`.

Classification:

- UX / integration / diagnostics

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence

### PF-019 - 2026-06-25 - Data Fabric / Record Insert Payload Mapping

Context:

- ID: PF-019.
- Status: open blocker.
- Goal: persist the E-004 `service-recovery-audit-v1` contradiction audit bundle in Data Fabric for G-001/G-002 reconstruction.
- Product surface: UiPath CLI, Data Fabric entity and record APIs.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-001, G-002, G-008.

What worked:

- `uip df entities create ServiceRecoveryAuditBundle --file docs/architecture/data_fabric/service_recovery_audit_bundle_entity.json --output json` succeeded.
- Created entity ID: `328ef8b6-ab70-f111-ac9a-002248a16d28`.
- `uip df entities get 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json` read back the expected schema, including required `case_id`, policy-version fields, JSON payload fields, and system fields.
- `uip df records list 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json` succeeded and confirmed no partial records were inserted after failures.
- `uip df records import` returned a structured result with an error file link instead of silently failing.

What failed or confused us:

- `uip df entities get ServiceRecoveryAuditBundle --output json` failed with `The value 'ServiceRecoveryAuditBundle' is not valid`, even though list/readback show that name.
- Record insert failed when using the generated file object, inline full object, minimal required field object, `{"Data": {...}}` wrapper, field UUID keys, and array object.
- Every insert attempt failed with `Required field "case_id" (...) is not provided and there is no default.`
- A debug run showed the CLI parsed a `--body` containing `case_id`, so the failure appears to be in payload mapping or expected request shape rather than shell quoting.
- CSV import inserted `0` of `1` records and returned an error file link, so the documented import fallback did not prove persistence either.

Expected:

- The insert command help says `--file` or `--body` accepts a JSON object or array of objects. A payload keyed by field names returned by schema readback should map to entity fields.
- If the expected insert payload shape differs, CLI validation should reject the payload before calling the service and show the exact expected shape.

Observed:

- Schema creation/readback worked.
- Insert payload parsing happened.
- Required field validation still behaved as if no supplied fields were mapped.
- CSV import returned an error file link with zero inserted records.
- Record list remained empty after failures.

Impact:

- Build impact: high for G-001 custom audit storage. Data Fabric is the cleanest durable one-query audit store candidate, but record insert/query-back is the proof step.
- Demo/submission impact: medium/high. The team can still use Case custom payload or file artifact, but Data Fabric would be stronger cross-platform integration if insert works.
- Severity: high for CLI/API storage path, product defect candidate until a documented alternate payload shape is found.

Workaround:

- Keep the entity for continued validation.
- Inspect the CSV import error file or official API/docs if accessible without exposing secrets.
- If insert remains blocked, use a UiPath-accessible file artifact or Case custom payload for final demo audit reconstruction and submit PF-019 as Data Fabric feedback.

Suggested improvement:

- Add schema-aware insert diagnostics that echo recognized fields, unrecognized fields, missing required fields, and the expected payload shape.
- Make `records insert` examples include a freshly-created custom entity with required fields.
- If entity ID is required for `entities get`, update help/error text to say so or make name lookup work consistently.
- Include a correlation/session ID for insert failures to make hackathon support escalation practical.

Evidence:

- Commands/logs: `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 21:08 IST Live Data Fabric Entity Created / Insert Blocked.
- Entity ID: `328ef8b6-ab70-f111-ac9a-002248a16d28`.
- Debug log was written locally to `tmp/data-fabric-insert-debug.log` but is intentionally not committed because CLI debug logs can contain request metadata.

Classification:

- product defect candidate / integration / diagnostics

Survey tags:

- product-used
- pain-point
- blocker
- workaround
- improvement
- evidence

### PF-004 - 2026-06-24 - Studio Web / Maestro Case Task Picker

Context:

- ID: PF-004.
- Status: repeated / partial. The original filtered-row activation issue was bypassed on 2026-06-25 by selecting `Human action` from the unfiltered task picker and then selecting `Human action placeholder`, but task configuration remains unclear.
- Goal: create the smallest real human review task for G-003 evidence-packet validation.
- Product surface: Studio Web, Maestro Case designer.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-003, with G-001/G-004 dependency.

What worked:

- `Add to solution` exposes `Maestro Case`.
- The Case designer creates a real `Case plan` with stages, rules, Case app metadata, and code view.
- The `Add task` menu lists architecture-relevant task types, including `Agent`, `Agentic process`, workflows, connector waits, and `Human action`.
- Searching the task picker for `Human action` filters to the expected single option.
- Selecting `Human action` from the unfiltered task picker opened a second-level picker with `Human action placeholder` and `Create new Action app`.
- Selecting `Human action placeholder` inserted a visible `Human action (placeholder)` task under `Stage 1` sequential tasks.
- The JSON editor guarded against a malformed accidental edit by disabling `Save` and prompting to discard unsaved changes.

What failed or confused us:

- The filtered `Human action` option was exposed as selectable text, not a button/action, in the accessibility tree.
- Clicks and Return did not activate the filtered row in the Zen/computer-use session.
- The task picker gave no visible error or hint about whether the row was selected, disabled, required drag/drop, or waiting for a different interaction.
- After placeholder insertion, selecting the placeholder did not obviously switch the properties panel to task-level configuration; the visible properties panel still showed stage properties.
- It was not yet clear from the designer where to configure reviewer-facing evidence fields, decision outcomes, comments, and structured return mapping.

Expected:

- A filtered task-picker result should be activatable through click and keyboard, with clear focus/selection feedback.
- If a task type requires drag/drop, permissions, configuration, or a different gesture, the UI should say so.

Observed:

- The menu remained open after selecting/filtering; no human action task was added to `Stage 1`.
- Accessibility secondary action was unavailable for the row.
- In the follow-up run, the unfiltered-selection path inserted `Human action (placeholder)`.
- The inserted placeholder is a useful scaffold but not a G-003 pass because it does not yet show the structured evidence packet or reviewer return contract.

Impact:

- Build impact: medium; it delays G-003 because evidence-packet validation needs a real human action task.
- Demo/submission impact: medium; task creation is part of the first-time Maestro Case builder path and should be smooth under hackathon time pressure.
- Severity: medium.

Workaround:

- Continue by trying the same action manually in the browser, using a different selection gesture, or finding a supported Case JSON/schema route after inspecting docs/platform behavior.
- Keep Case App/custom evidence-packet fallback open until Action Center task rendering is validated end to end.
- Prefer the unfiltered path: `Add first task > Human action > Human action placeholder`.
- Next try `Create new Action app` because the placeholder alone does not expose the evidence-packet configuration needed for the demo.

Suggested improvement:

- Make task-picker rows first-class buttons/options with keyboard activation, visible focus state, and accessible action metadata.
- Add microcopy or inline hints for any task types that require drag/drop, prior resource setup, catalog selection, or permissions before insertion.
- For Maestro Case, add a guided `Add human review` template that scaffolds reviewer instructions, decision outputs, comments, and return mapping to the case.
- After inserting a task, automatically select it and show task-level configuration, or display a clear next-step affordance such as `Configure Action app`, `Map inputs`, and `Map outputs`.
- Add an evidence-packet starter template for case review tasks with a table section, raw agent output, policy decision, block reason, recommended actions, decision buttons, comment, and typed return schema.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-24/g001-maestro-case-json-code-view.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g003-human-action-placeholder-canvas.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g003-action-schema-input-output-properties.png`.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-24 21:40 IST Zen Session Maestro Case Designer Checkpoint.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 01:11 IST G-003 Human Action Placeholder Inserted.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 01:22 IST G-003 Action App Schema Inspection.

### PF-005 - 2026-06-25 - Studio Web / Local Assistant Migration Prompt

Context:

- ID: PF-005.
- Status: open.
- Goal: continue G-003 Action app validation in the logged-in Safari browser without losing the current edit session.
- Product surface: Studio Web, Action app designer.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-003.

What worked:

- Safari opened the existing `SimpleApprovalApp` Studio project and authenticated without credentials in chat.
- The duplicate-editing banner allowed moving the active editing session into Safari with `Edit here`.
- Selecting `Do this later`, then `I'll switch later, just not today`, then `Stay on current setup` allowed validation to continue.

What failed or confused us:

- During a time-boxed hackathon validation, Studio Web interrupted the Action app workflow with a broad environment migration prompt.
- The prompt said RPA/app editing and debugging are moving to local UiPath Assistant and that the change is required for Community users starting July 22.
- The prompt did not make the immediate impact concrete enough for the current project: whether publishing, debugging, Action app editing, and Maestro Case validation would continue working fully in the web session today.

Expected:

- A migration prompt should distinguish current-session impact from future deadline impact.
- For hackathon/community builders, it should provide a fast readiness check: installed Assistant version, required extensions/services, unsupported web-only actions, and whether the current project can safely continue.

Observed:

- The prompt was dismissible, but it consumed validation time and introduced uncertainty about whether the web-only path is durable for final build/demo work.

Impact:

- Build impact: medium. It did not block this session, but it adds environment risk while validating Action app and case workflows.
- Demo/submission impact: medium if later publish/debug requires local Assistant setup without clear preflight.

Workaround:

- Continued in the current web setup for immediate validation.
- Logged the prompt and kept UiPath Assistant setup as an environment risk rather than changing architecture.

Suggested improvement:

- Add a hackathon-safe migration/readiness banner with explicit answers for: what works in Studio Web today, what requires Assistant now, what changes after the deadline, and how to validate local Assistant readiness before a demo.
- Add a `Continue web validation for this project` option that records the choice and suppresses repeated prompts for the session.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g003-safari-simple-approval-upgrade-prompt.png`.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 01:22 IST G-003 Action App Schema Inspection.

### PF-006 - 2026-06-25 - Studio Web / Action Schema Page Generation

Context:

- ID: PF-006.
- Status: open.
- Goal: generate a reviewer-facing evidence packet page from typed Action schema fields for G-003.
- Product surface: Studio Web, Action app designer, Action schema, generated page layout.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-003.

What worked:

- `ActionSchema` exposed typed input, input/output, output, and outcome sections.
- Custom `System.String` inputs could be added for `EvidencePacketJson`, `RawAgentRecommendation`, and `PolicyDecisionJson`.
- `Generate page` produced a reviewer page with approve/reject click workflow files.
- The generated page rendered visible controls for `Evidence Packet Json`, `Raw Agent Recommendation`, `Comment`, `Approve`, and `Reject`.

What failed or confused us:

- Page generation displayed `Auto-generation of controls failed for few properties` and specifically named `PolicyDecisionJson`.
- The generated page also showed an ambiguous `Unnamed String 1` label/value, which made it unclear whether the failed policy field was partially generated, blank, or unrelated.
- Selecting the ambiguous label exposed label properties, but the visible `. Edit` action edited the control name rather than clearly editing the display label or property binding.
- The builder did not get a direct repair path such as `add missing control`, `jump to failed property`, or `regenerate only failed fields`.

Expected:

- Every valid string input property should generate a readable, bound reviewer control.
- If generation fails, the designer should show a per-property status table and a safe repair action.
- Ambiguous fallback labels should not appear without binding/status context.

Observed:

- Two custom string properties generated readable fields, while one proof-critical custom string property did not.
- The generated page was useful but not pass-worthy for G-003 because the final policy decision field is central to the human evidence packet.

Impact:

- Build impact: high for G-003. The missing policy decision field is proof-critical for showing why the raw `closure_candidate` recommendation was overridden.
- Demo/submission impact: high if a manual repair cannot be validated quickly, because the human reviewer must see both agent output and policy decision.

Workaround:

- Continue with manual binding/regeneration attempts.
- Keep a custom Case App/evidence-packet fallback open until the generated Action page can render all proof-critical fields reliably.

Suggested improvement:

- Add schema-generation preflight that validates each field name/type before page generation.
- After generation, show a table of `property -> generated control -> binding status`.
- For failed properties, provide `Create missing control`, `Jump to schema property`, and `Regenerate failed controls only`.
- Preserve existing generated controls during repair so builders can fix one field without losing layout work.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g003-generated-action-page-partial-evidence-packet.png`.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 01:28 IST G-003 Generated Evidence Packet Page.

### PF-007 - 2026-06-25 - Maestro Case / Action Task Runtime Validation

Context:

- ID: PF-007.
- Status: open.
- Goal: run a live Maestro Case instance with a deployed Action app task for G-001/G-003.
- Product surface: Studio Web deployment workflow, Orchestrator, Maestro Case instance view, Action task runtime.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-001 and G-003.

What worked:

- Studio Web published and deployed `Solution v1.0.0`.
- Deployment logs reported Orchestrator and Apps activated, with all services activated successfully.
- Orchestrator created a `Solution` folder and listed runnable processes including `Maestro Case`.
- Starting `Maestro Case` from Orchestrator created a live job and exposed an `Open in Maestro` link.
- Maestro opened a single case instance view with ordered execution trail, stage/task progression, timestamps, global variables, incidents, and job linkage.

What failed or confused us:

- The deployment workflow succeeded even though the configured Action task was missing a required Title.
- The missing required field appeared only after starting a live case, as a runtime incident: `Failure in the AppTasks request - (170000)` and `The Title field is required.`
- The incident named the missing field but did not link back to the Studio task/property/mapping that needs repair.

Expected:

- Studio/Deployment validation should catch missing required Action task fields before deployment or before runtime.
- The required Title field should be visible in the Action task configuration and clearly marked as required.
- Runtime incident detail should include a direct repair path back to the failing task configuration.

Observed:

- Deployment succeeded and activated Orchestrator/Apps.
- The live case faulted at the `SimpleApprovalApp` user task in `Stage 1`.
- Maestro showed the fault in the case canvas, execution trail, and incidents panel.

Impact:

- Build impact: high. It blocks G-003 reviewer rendering even though deploy succeeded.
- Demo/submission impact: high if not fixed, because the live case cannot reach the human evidence packet.
- Product-feedback impact: high. This is a precise design-time/runtime validation gap with strong evidence and a concrete fix suggestion.

Workaround:

- Return to Studio task configuration.
- Add/map the required Action task title.
- Republish/redeploy and retry or start a fresh case instance.

Suggested improvement:

- Add a deployment preflight that validates all required Action task request fields, including Title.
- In the Case designer, mark required Action task fields and mappings inline.
- In Maestro incidents, add `Open failing task configuration` or `Open required field mapping` links.
- Include the failed task name, required field, expected type, and current mapping state in the incident details.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g003-action-app-deployment-success.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g001-maestro-case-orchestrator-running-job.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g001-maestro-live-case-execution-trail-faulted.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g003-maestro-action-task-title-required-incident.png`.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 01:36 IST G-001/G-003 Live Case Runtime Attempt.

Classification:

- UX / accessibility

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence

### PF-002 - 2026-06-24 - Maestro Home / Recent Projects Fetch

Context:

- ID: PF-002.
- Status: resolved after manual tenant service enablement.
- Goal: complete Wave 01 platform access inventory and start Maestro hard-gate validation.
- Product surface: UiPath Maestro home.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: Wave 01, pre-G-001.

What worked:

- Maestro opened successfully from Automation Cloud.
- The left navigation exposed Home, Process instances, Process incidents, Case app, Case instances, and Case incidents.
- Studio Web could create a validation-scoped `Maestro BPMN` solution and add a `Maestro Case` project.

What failed or confused us:

- The Maestro home page displayed `There was an error fetching your recent projects` even though the account could create a new Maestro/Studio solution.
- The message did not say whether this was a transient fetch failure, missing permission, no projects, or backend issue.

Expected:

- Recent projects should either load, show a clear empty state, or explain the permission/service issue.

Observed:

- Recent projects area showed an error while the rest of Maestro remained usable.

Impact:

- Build impact: medium; it did not block creation, but it created uncertainty during the first Maestro validation pass.
- Demo/submission impact: low to medium; project discovery reliability matters for repeatable demo setup.
- Severity: medium.

Workaround:

- Use `Start modeling` to create/open the validation solution directly and capture the solution URL.

Suggested improvement:

- Replace the generic recent-projects fetch error with a diagnostic empty/error state that identifies whether the cause is no projects, permission, tenant service registration, timeout, or backend failure, and include a retry action plus correlation/session ID.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-24/wave01-maestro-home.png`.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-24 Wave 01 rerun.

Classification:

- product defect / UX

Survey tags:

- product-used
- worked-well
- pain-point
- workaround
- improvement
- evidence

### PF-003 - 2026-06-24 - Actions / Action Center Not Enabled

Context:

- ID: PF-003.
- Status: open.
- Goal: validate human evidence packet feasibility for G-003.
- Product surface: Actions / Action Center.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: Wave 01 / G-003.

What worked:

- Automation Cloud linked to the Actions route from the home page's pending actions surface.
- The error page included a session ID.

What failed or confused us:

- Actions opened to an unregistered-service page: `Actions is not enabled for this tenant`.
- The page said to contact an administrator, but the hackathon builder flow did not indicate where to enable it, whether the user had permission, or whether Labs tenants are expected to include Actions by default.

Expected:

- Since Maestro Case human review depends on people/tasks, the Labs tenant should either have Actions enabled or provide a clear self-service enablement path and track guidance.

Observed:

- URL redirected to `portal_/unregistered?serviceType=actions&organizationName=keepingitlowkey&tenantName=defaulttenant`.
- Session ID: `32e450e2-89ca-4a80-a0c9-16df19a3d6b4`.
- Later same-run resolution: Admin `DefaultTenant > Services > Add services` exposed `Actions` as an addable service. After user-approved enablement, the direct Actions URL opened as `Inbox - Action Center`.

Impact:

- Build impact: high; G-003 cannot pass through Action Center in the current tenant state.
- Demo/submission impact: high; human evidence packet may need a Case App/custom evidence-packet view unless Actions is enabled.
- Severity: high.

Workaround:

- Enabled `Actions` from Admin `DefaultTenant > Services > Add services` after explicit user approval.
- Keep G-003 partial until structured human action return is validated.
- Official docs indicate the intended enablement path is `Admin > Tenants > Edit Services > Actions > Save`; in the current Automation Cloud UI, the observed path was `DefaultTenant > Services > Add services > Actions > Add`.

Suggested improvement:

- For hackathon/Labs tenants, surface a product-readiness checklist for Maestro Case dependencies: Actions enabled, Test Manager enabled, Orchestrator tenant, Integration Service, Data Service, required roles, and direct admin enablement links. The unregistered-service page should include the exact permission or tenant setting needed.
- Add a direct `Request/enable Actions` path from the `Actions is not enabled for this tenant` page when the current user has admin rights, or show the exact admin role/contact needed when they do not.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-24/wave01-actions-not-enabled.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-24/actions-admin-services-list.png`.
- Screenshot/path/link: `docs/validation/artifacts/2026-06-24/actions-enabled-inbox.png`.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-24 Wave 01 rerun and 20:33 IST Actions blocker investigation.
- Official docs: `https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions`.

Classification:

- access / missing feature / UX

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence

### PF-008 - 2026-06-25 - Studio Web / Publish Repaired Case Plan

Context:

- ID: PF-008.
- Status: open.
- Goal: publish the repaired Maestro Case definition after fixing the required Action task title for G-003.
- Product surface: Studio Web publish/versioning workflow for Maestro Case solutions.
- Account/tenant: `keepingitlowkey` / `DefaultTenant`, user `Arshdeep Singh`.
- Wave/gate: G-003, with G-001/G-002/G-004 dependent on a fresh live case rerun.

What worked:

- The Case designer exposed the required `Task title` field for `SimpleApprovalApp`.
- After setting `Review service recovery evidence`, the visible task validation warning cleared in the Case plan.
- `Manage > Versions` clearly showed the currently published package version and release notes.

What failed or confused us:

- After the design-time repair, `Manage > Versions` still showed only `1.0.0`, so the fixed case definition was not available for deployment.
- The visual `Publish` control was not represented as a normal actionable button in the accessibility tree; it appeared as text inside a broader toolbar/tab group.
- Repeated accessibility and coordinate-based attempts did not reliably open the publish flow in this session, making it difficult to move from a confirmed designer repair to a live rerun.

Expected:

- A builder who fixes a runtime-blocking Case task field should have a clear `Publish new version` path and a visible indication that the deployed version is stale.
- Publish should be a first-class accessible button/menu with deterministic behavior in browser automation.

Observed:

- Current published version remained `1.0.0` with release notes `G-003 evidence packet validation`.
- No `1.0.1` or later repaired package appeared in `Manage > Versions`.
- The Case plan showed `SimpleApprovalApp` in `Stage 1` without the earlier visible validation warning, but runtime validation could not continue because the repaired definition was not published.

Impact:

- Build impact: high for G-003. The team had a concrete fix for the previous `The Title field is required` runtime failure, but could not yet prove it in a fresh live case.
- Demo/submission impact: medium/high. It slows iteration on the central human evidence packet proof and increases the risk of accidentally rerunning stale package versions.
- Severity: high during hackathon iteration.

Workaround:

- Do not rerun the old `1.0.0` deployment as if it contains the fix.
- Retry the publish path with precise UI interaction or another browser/session.
- If available, test whether UiPath CLI can publish/package the current project state.
- Keep this as a packaging/publish blocker, not an Action Center rendering failure.

Suggested improvement:

- Make `Publish` a first-class accessible button with explicit menu items exposed to automation and keyboard users.
- Show a persistent `Unpublished changes` indicator when the designer state differs from the latest package version.
- On `Manage > Versions` and `New deployment`, add a callout such as `Latest package does not include current designer changes` with a direct `Publish new version` action.
- After a runtime incident points to a required field, provide a repair-and-republish guided flow from the incident or task properties.

Evidence:

- Screenshot/path/link: `docs/validation/artifacts/2026-06-25/g003-title-repaired-publish-control-not-opened.png`.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 01:46 IST G-003 Action Task Title Repair / Publish Blocker.

Classification:

- UX / accessibility / integration

Survey tags:

- product-used
- pain-point
- workaround
- improvement
- evidence
