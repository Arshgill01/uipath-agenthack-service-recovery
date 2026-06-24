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
| Future: live case audit and override visibility | placeholder | unknown until observed | TBD | One case view or one query reconstructs evidence state, policy versions, raw recommendation, policy decision, closure block, human action, and timestamps. | Not observed yet. Do not claim. | Run minimal live Maestro Case instance for G-001/G-002/G-004. | TBD after observation. | `docs/validation/VALIDATION_GATES.md` G-001, G-002, G-004; `docs/logs/RISK_REGISTER.md` R-001/R-002/R-004. |

## Best Insights So Far

- The highest-impact feedback is not a single bug; it is dependency readiness for a first-time Maestro Case builder. PF-003 shows that Action Center was required for the intended human-review path but was not enabled by default, and the disabled-service page did not point to the observed admin resolution path.
- The strongest product-design insight is that Maestro Case successfully exposes the right primitives for this architecture: Case app, case plan, stages, rules, task types, Human action, Agent, Agentic process, and Case JSON/code view. The remaining friction is discovery and configuration clarity, not lack of conceptual fit.
- The fairest framing for PF-001 is access/account-state ambiguity, not a confirmed product defect. Later tenant access worked, so this should be submitted as onboarding diagnostics feedback.
- PF-004 should be framed as three related observations: filtered picker activation/accessibility friction, post-insertion configuration ambiguity, and the separate Action app path that exposes schema/page primitives but not obvious case return mapping.
- PF-006 and PF-007 are currently the strongest high-specificity feedback items for G-003: PF-006 covers design-time generation reliability; PF-007 covers deploy/runtime validation gap for a required Action task field.
- Do not claim Action Center evidence-packet rendering is poor or sufficient yet. The observed facts are that Action Center opens, the Case plan can hold a Human action placeholder, and a generated Action page can show some but not all custom evidence packet fields.

## Draft Survey Answer Scaffold

Draft only. Evidence-backed but not final submission prose.

| Survey question | Draft evidence-backed answer components | Evidence to cite before finalizing |
| --- | --- | --- |
| Q10 - What UiPath products did you use? | Automation Cloud, Maestro, Maestro Case / Case app, Studio Web, Actions / Action Center, Orchestrator service listing, Integration Service listing, Data Fabric listing, Test Manager listing, UiPath CLI. Note that deep validation has so far centered on Automation Cloud, Maestro, Studio Web, Maestro Case, and Actions. | Wave 01 validation results; product launcher screenshot; CLI help output in `docs/validation/VALIDATION_RESULTS.md`. |
| Q11 - What worked well? | Automation Cloud eventually landed in org `keepingitlowkey` / tenant `DefaultTenant`; Maestro opened and exposed case/process surfaces; Studio Web created a real `Maestro Case` project; Case designer exposed stages, rules, Case app metadata, task types, and JSON/code view; Action Center opened after Actions was enabled; JSON editor guarded against saving malformed accidental input; Action app schema exposed typed inputs, outcomes, and generated a mostly usable evidence review page. | PF-002, PF-003, PF-004, PF-006; `wave01-studio-maestro-bpmn-created.png`; `g001-maestro-case-project-created.png`; `g001-maestro-case-json-code-view.png`; `actions-enabled-inbox.png`; 2026-06-25 G-003 validation results. |
| Q12 - What challenges did you encounter? | Group by issue class: account/tenant routing ambiguity, Maestro recent-projects generic fetch error, Action Center dependency not enabled with insufficient disabled-service guidance, Human action picker/configuration ambiguity, Studio Web local Assistant migration uncertainty, schema-to-page generation failure for a proof-critical evidence field, and deployment validation passing even though the live Action task was missing a required Title. Keep user/access uncertainty separate from product defect claims. | Feedback Evidence Matrix rows PF-001 through PF-007. |
| Q13 - What should UiPath improve? | Recommended top answer: add a Maestro Case readiness and human-review setup path that checks tenant services/roles, links directly to enable Actions when permitted, scaffolds a human evidence-packet task, shows exact input/output mapping steps, validates generated Action page controls per schema property, and runs a preflight for required Action task fields before deployment. Secondary improvements: better `missingaccount` diagnostics, recent-projects error diagnostics, accessible task-picker rows, and Studio Web/local Assistant transition guidance. | PF-003 as highest-impact setup blocker; PF-006/PF-007 as proof-critical G-003 build blockers; PF-004 as core human-task workflow friction; PF-001/PF-002/PF-005 as supporting onboarding diagnostics. |

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
