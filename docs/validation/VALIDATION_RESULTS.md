# Validation Results

UiPath Labs hard gate validation has answered G-001 through G-004 with implementation implications. The current architecture uses native Maestro Case and Action Center for lifecycle and human return, a custom evidence-packet/audit surface for demo legibility, and an Orchestrator bucket-backed `service-recovery-audit-v1` bundle for durable one-object audit reconstruction.

Use [VALIDATION_GATES.md](VALIDATION_GATES.md) for pass/fail criteria.

The data model and integration map are now grounded in observed platform facts. Remaining partials are explicit: native Case does not provide the full domain audit alone, generated Action Center UI is not demo-legible, Data Fabric record insert is blocked, and Test Manager automation is not claimed.

## 2026-06-18 - Local Provisional Core Baseline

Environment:

- Local Python 3.9.12.
- No UiPath Labs tenant or Maestro Case surface used.

Steps:

1. Installed local package with `python -m pip install .`.
2. Ran unit tests with `python -m unittest discover -s tests`.
3. Ran eval baseline with `python -m service_recovery_core.evals --output eval_results/local_baseline.json`.

Observed:

- Package build/install completed.
- Unit suite ran 16 tests.
- Eval suite ran E-001 through E-009 with 9/9 passing.
- E-009 persisted the raw agent recommendation and policy decision as separate linked events.

Result:

- PASS for local/provisional validation only.
- Not a UiPath Labs validation result.

Decision impact:

- Waves 07-14 are stable enough for local development.
- Wave 22 baseline is stable enough as a portable harness pending Test Cloud mapping.

Follow-up:

- Run G-001 through G-004 when Labs access is available.
- Map local eval scenarios to UiPath/Test Cloud only after platform assumptions are verified.

## 2026-06-24 - Wave 01 Platform Access And Inventory

Environment:

- Local macOS development machine.
- Safari opened to UiPath Automation Cloud for interactive Google login by the user.
- Controlled `agent-browser` Chromium session was available but did not inherit the user's Zen browser login.
- Node `v22.21.0`, npm `10.9.4`.
- UiPath CLI package `@uipath/cli` installed globally during this run.

Steps:

1. Confirmed repo status with `git status --short --branch`.
2. Confirmed recent commits with `git log --oneline -5`.
3. Re-ran local validation with `python -m unittest discover -s tests`.
4. Re-ran local eval baseline with `python -m service_recovery_core.evals --output eval_results/local_baseline.json`.
5. Checked for `uip` before install with `command -v uip && uip --version`.
6. Checked npm metadata with `npm view @uipath/cli version bin --json`.
7. Installed CLI with `npm install -g @uipath/cli@1.196.0`.
8. Verified CLI with `uip --version`.
9. Opened `https://cloud.uipath.com` in a controlled browser session and in Safari.
10. Started `uip login`; stopped it after it waited without producing a usable prompt in the terminal.

Observed:

- Repo was clean on `master...origin/master`.
- Latest commit remained `17a7017 Build local provisional service recovery core`.
- Unit suite ran 16 tests and passed.
- Eval suite ran E-001 through E-009 with 9/9 passing.
- `uip` was initially unavailable on PATH.
- `@uipath/cli` published version observed from npm was `1.196.0`; after install, `uip --version` returned `1.196.0`.
- Controlled browser reached the UiPath login page but was not authenticated.
- Safari reached `https://cloud.uipath.com/portal_/missingaccount` after the user attempted login, indicating authentication did not land in an accessible Automation Cloud account/tenant in that browser session.
- Access could not be confirmed for Maestro, Maestro Case, Studio Web, Action Center, Test Cloud/Test Manager, Integration Service, or Orchestrator.

Result:

- PARTIAL for Wave 01.
- PASS for local repo and local validation readiness.
- PASS for CLI installation/version verification.
- BLOCKED for UiPath tenant and product-surface inventory.
- NOT RUN for hard gates G-001 through G-004 because authenticated Labs tenant access was not available.

Decision impact:

- Do not start broad UiPath implementation.
- Keep Maestro Case, Action Center, Test Cloud, Integration Service, and Orchestrator mappings provisional.
- Hard validation gates remain blocked until the user account is associated with the correct UiPath Labs Automation Cloud organization/tenant or an inspectable authenticated browser session is available.

Follow-up:

- Resolve UiPath account/tenant access for `arshgill6120@gmail.com`.
- Re-run Wave 01 surface inventory after Automation Cloud lands in a tenant instead of `portal_/missingaccount`.
- Run `uip login` again only when the browser/device-code flow can be completed interactively.
- Run G-001 through G-004 only after Maestro Case access is confirmed.

## 2026-06-24 20:30 IST - Wave 01 Rerun And Hard-Gate Stop

Environment:

- Local macOS development machine.
- Safari with Google login for `arshgill6120@gmail.com`.
- UiPath Automation Cloud organization slug: `keepingitlowkey`.
- Tenant observed in URLs: `DefaultTenant`.
- User observed in UI: `Arshdeep Singh`.
- UiPath CLI `uip` version `1.196.0`.

Steps:

1. Reconfirmed repo status with `git status --short --branch`.
2. Reconfirmed recent commits with `git log --oneline -5`.
3. Re-ran unit tests with `python -m unittest discover -s tests`.
4. Re-ran eval baseline with `python -m service_recovery_core.evals --output eval_results/local_baseline.json`.
5. Verified CLI and remote with `command -v uip && uip --version && git remote -v`.
6. Opened `https://cloud.uipath.com` in Safari.
7. Continued with Google account `arshgill6120@gmail.com`.
8. Opened the Automation Cloud product launcher and inventoried visible services.
9. Opened Maestro, Case app, and Studio Web from Maestro `Start modeling`.
10. Created a validation-scoped Studio solution named by the platform as `Maestro BPMN`.
11. Added a `Maestro Case` project to that solution from `Add to solution`.
12. Opened the Actions / Action Center pending tasks route.
13. Ran CLI help checks: `uip --help` and `uip skills --help`.

Observed:

- Automation Cloud login now succeeds and lands at `https://cloud.uipath.com/keepingitlowkey/portal_/home`.
- Product launcher exposes Studio, Orchestrator, Maestro, Admin, Agents, Apps, Automation Ops, Assistant, Data Fabric, Integration Service, Marketplace, and Test Manager.
- Home shows Orchestrator service `DefaultTenant`.
- Home shows Test Manager projects, but `No projects are accessible at this time`.
- Maestro opens at `https://cloud.uipath.com/keepingitlowkey/DefaultTenant/maestro_/home`.
- Maestro home exposes Process instances, Process incidents, Case app, Case instances, and Case incidents.
- Maestro home shows `There was an error fetching your recent projects`.
- Maestro Case app opens at `/maestro_/case-management` and shows active case columns: Case ID, Case type, Last modified, Stage, Case SLA, SLA status, Case state. No active cases exist.
- Studio Web opens from Maestro `Start modeling` and creates a real solution with `Process.bpmn`.
- `Add to solution` includes `Maestro Case`; selecting it adds a `Maestro Case` project with a case start event and zero validation issues.
- Actions / Action Center is not enabled for this tenant. The route redirects to `portal_/unregistered?serviceType=actions&organizationName=keepingitlowkey&tenantName=defaulttenant` and displays session ID `32e450e2-89ca-4a80-a0c9-16df19a3d6b4`.
- `uip --help` confirms installed CLI tools include `maestro`, `or`, `tasks`, `tm`, `is`, `platform`, `user`, and `skills`.
- `uip skills --help` confirms Codex skill install target `.agents/skills/<skill>/`.

Result:

- Wave 01: PARTIAL/PASS for access inventory. Automation Cloud, Maestro, Maestro Case creation, Studio Web, Orchestrator presence, Integration Service listing, Data Fabric listing, Test Manager listing, Agents listing, and CLI availability are confirmed.
- G-001: PARTIAL. Maestro Case project creation and Case app columns are confirmed, but no case instance was run; one-view/one-query audit reconstruction is not proven.
- G-002: PARTIAL. Platform can add a Maestro Case project where metadata can likely be modeled, but policy version pinning across live case transitions and explicit migration event are not proven.
- G-003: BLOCKED/PARTIAL. Case App exists, but Actions / Action Center is not enabled for `DefaultTenant`; structured human evidence packet return is not proven.
- G-004: PARTIAL. Separate raw recommendation and policy decision can likely be modeled as Case fields/events, and the local core already proves the event shape, but UiPath persistence/visibility before override is not proven in a live case.

Decision impact:

- Do not start broad implementation yet.
- Continue with a focused Maestro Case spike only after deciding whether to use Case App/custom evidence packet instead of Action Center for G-003.
- Treat Action Center as unavailable unless tenant service enablement changes.
- Keep custom audit events/Data Service as likely fallback for G-001/G-004 until a real case instance proves native reconstruction.

Product feedback:

- PF-002 in `docs/product/PRODUCT_FEEDBACK_AWARD.md`.
- PF-003 in `docs/product/PRODUCT_FEEDBACK_AWARD.md`.

Evidence:

- `docs/validation/artifacts/2026-06-24/wave01-automation-cloud-home.png`
- `docs/validation/artifacts/2026-06-24/wave01-product-launcher.png`
- `docs/validation/artifacts/2026-06-24/wave01-maestro-home.png`
- `docs/validation/artifacts/2026-06-24/g001-case-app-empty.png`
- `docs/validation/artifacts/2026-06-24/wave01-studio-maestro-bpmn-created.png`
- `docs/validation/artifacts/2026-06-24/g001-maestro-case-project-created.png`
- `docs/validation/artifacts/2026-06-24/wave01-actions-not-enabled.png`

Follow-up:

- Decide whether to request Actions enablement or proceed with Case App/custom evidence packet for the demo.
- Run a minimal Maestro Case instance through at least two stages before marking G-001/G-002/G-004 pass.
- Check Test Manager directly if G-003 unblocks or after the hard-gate decision is logged.

## 2026-06-24 20:33 IST - Actions Blocker Investigation

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Safari session authenticated as `arshgill6120@gmail.com`.
- UiPath CLI authenticated as `arshgill6120@gmail.com`.

Steps:

1. Searched official UiPath documentation for Action Center tenant enablement.
2. Confirmed CLI auth with `uip user --output json`.
3. Inspected CLI platform commands with `uip platform --help`, `uip platform tenants --help`, and `uip platform tenants licenses get --help`.
4. Attempted to open Admin tenants page at `https://cloud.uipath.com/keepingitlowkey/portal_/admin/tenants`.

Observed:

- Official UiPath Action Center documentation states Actions is enabled at tenant level from Automation Cloud by navigating to `Admin > Tenants`, opening the tenant row menu, selecting `Edit Services`, selecting `Actions`, and clicking `Save`.
- `uip user --output json` returned the authenticated user `arshgill6120@gmail.com`.
- CLI exposes tenant license commands but did not expose a tenant service enablement command.
- Admin/Tenants UI did not render a usable tenants table in the Safari automation session; it showed a mostly blank page and language/tenant selector overlays.

Result:

- Actions blocker root cause is narrowed to tenant service enablement.
- Not fixed in this run because enabling a cloud tenant service is a configuration change requiring explicit approval at action time, and the Admin UI was not usable through automation.

Decision impact:

- If the user is an org/tenant admin, try enabling Actions from `Admin > Tenants > DefaultTenant > Edit Services > Actions > Save`.
- If the user is not an admin or the UI remains blank, send a support/hackathon request with the org, tenant, service, and session ID.

Product feedback:

- PF-003 in `docs/product/PRODUCT_FEEDBACK_AWARD.md`.

Follow-up:

- Ask for approval before enabling Actions if the UI exposes the Save action.
- Ask for approval before sending any support/hackathon email or form submission.

## 2026-06-24 21:08 IST - Actions Enabled For G-003

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Tenant GUID observed in Admin URL: `ce9f6b89-4e70-47ee-a0b3-8bc4986b8772`.
- Support ID observed in Admin UI: `7963-2959-3848-9528`.
- Safari session authenticated as `arshgill6120@gmail.com`.

Steps:

1. Reopened Admin for `DefaultTenant`.
2. Opened `Services`.
3. Confirmed the enabled service list contained Orchestrator, Maestro, Integration Service, Data Fabric, and Test Manager, but not Actions.
4. Opened `Add services`.
5. Confirmed `Actions` was available as an additional service.
6. With user approval, selected only `Actions` and clicked `Add`.
7. Opened `https://cloud.uipath.com/keepingitlowkey/DefaultTenant/actions_/tasks?status=Pending`.

Observed:

- `Actions` was addable from the tenant services drawer.
- After selecting only `Actions` and clicking `Add`, the previous unregistered-service blocker no longer appeared.
- Direct Actions URL opened with browser title `UiPath Actions`, then `Inbox - Action Center`.

Result:

- Wave 01: PASS for Action Center service availability after tenant service enablement.
- G-003: PARTIAL, no longer blocked by tenant service availability. Action Center opens, but structured evidence-packet rendering and structured return actions still need a real human review task.

Decision impact:

- Continue G-003 validation against Action Center before choosing Case App/custom evidence packet fallback.
- Keep PF-003 as a resolved product-feedback entry because the original disabled-service page did not expose the admin enablement path directly.

Product feedback:

- PF-003 in `docs/product/PRODUCT_FEEDBACK_AWARD.md`.

Evidence:

- `docs/validation/artifacts/2026-06-24/actions-admin-services-list.png`
- `docs/validation/artifacts/2026-06-24/actions-enabled-inbox.png`

Follow-up:

- Create or trigger a minimal human review task from Maestro/Studio and validate evidence table, agent output, policy decision, block reason, recommended options, approve/reject/request-evidence/comment, and structured return to case.

## 2026-06-24 21:40 IST - Zen Session Maestro Case Designer Checkpoint

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Zen browser session authenticated as `Arshdeep Singh`.
- Studio Web solution `Maestro BPMN`, solution ID `b6446ea0-7ebd-4712-ccbf-08ded1e3ee41`.
- Maestro Case designer project URL observed with project ID `35207db4-6227-4833-aee1-5cb461f3eb69` and file ID `31c38730-c81e-40e2-be4d-c71a7e6031e5`.

Steps:

1. Opened Action Center pending tasks in Zen at `https://cloud.uipath.com/keepingitlowkey/DefaultTenant/actions_/tasks?status=Pending`.
2. Confirmed Action Center loads as `Inbox - Action Center` with user `Arshdeep Singh`.
3. Opened the existing Studio Web solution in Zen.
4. Confirmed `Add to solution` exposes `Maestro Case`.
5. Added a `Maestro Case` project to the solution and opened `Case plan`.
6. Opened Case JSON/code view for the case plan.
7. Opened the stage `Add task` menu and filtered for `Human action`.

Observed:

- Action Center now works in the logged-in Zen/cmux browser session and shows `No Pending tasks`.
- Studio Web Case designer creates a real `Maestro Case` project with `Case plan`.
- The default Case plan exposes `Stage 1`, stage entry/completion rules, `Add task`, `Add trigger`, `Add stage`, `Rules`, `Case manager AI Orchestrator`, and a Case app section.
- Case properties expose `caseIdentifier` prefix `CASE`; generated IDs will use `CASE-12345`.
- Case JSON/code view exposes design metadata including `id`, `version: 23.0.0`, `caseIdentifier`, `caseIdentifierType`, `caseAppEnabled: true`, `publishVersion`, and `caseUnifiedSchemaEnabled: true`.
- The `Add task` menu lists task types relevant to the architecture: `Agent`, `External agent`, `External workflow`, `Agentic process`, `RPA workflow`, `Human action`, `Connector activity`, `Wait for connector`, `API workflow`, and `Wait for timer`.
- Filtering the task picker to `Human action` works, but the filtered row did not activate through click, Return, or accessibility secondary action in this computer-use session.

Result:

- G-001: PARTIAL. Case plan design surfaces and Case app metadata are confirmed, but runtime case audit reconstruction is still not proven.
- G-002: PARTIAL. Case design metadata/versioning exists, but active-case policy pinning and explicit migration events are not proven.
- G-003: PARTIAL. Action Center is enabled and Human action is available as a case task type, but a real evidence packet task was not created or reviewed yet.
- G-004: PARTIAL. Case stage/task model can represent the separation, but raw agent recommendation and linked policy decision visibility are still not proven in a live case.

Decision impact:

- Do not start broad implementation yet.
- Continue with a focused task-creation path: try keyboard/mouse/manual UI selection, Case JSON edit if safe, or a UiPath CLI/API deployment route only after understanding the intended Studio task schema.
- Keep Case App/custom evidence-packet fallback open until Action Center task rendering is actually validated.

Product feedback:

- PF-004 in `docs/product/PRODUCT_FEEDBACK_AWARD.md`.

Evidence:

- `docs/validation/artifacts/2026-06-24/actions-enabled-inbox-zen.png`
- `docs/validation/artifacts/2026-06-24/g001-maestro-case-json-code-view.png`

Follow-up:

- Add a minimal human action task to `Stage 1`.
- Publish/debug the smallest case instance.
- Inspect whether one Case view or query reconstructs evidence state, policy versions, raw recommendation, policy decision, closure block, human action, and event timestamps.

## 2026-06-25 01:11 IST - G-003 Human Action Placeholder Inserted

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Zen browser session authenticated as `Arshdeep Singh`.
- Studio Web solution `Maestro BPMN`, solution ID `b6446ea0-7ebd-4712-ccbf-08ded1e3ee41`.
- Maestro Case project URL observed with project ID `35207db4-6227-4833-aee1-5cb461f3eb69` and file ID `31c38730-c81e-40e2-be4d-c71a7e6031e5`.

Gate:

- G-003: Human Evidence Packet.
- Assumption tested: Studio Web can insert a real `Human action` task into the Maestro Case plan, which is the first platform prerequisite for an Action Center evidence-packet review.

Steps:

1. Reopened the existing `Maestro Case` project in the logged-in Zen/cmux browser session.
2. Closed the introductory Case Management modal.
3. Opened `Stage 1 > Add first task`.
4. Selected `Human action` from the task picker.
5. Selected `Human action placeholder` from the second-level Human action picker.
6. Opened Case JSON/code view to inspect the generated case-plan metadata, then canceled without saving after the editor showed an unsaved malformed test edit.
7. Captured a clean canvas screenshot after returning to the Case designer.

Observed:

- `Human action` is not just listed in the first-level task picker; selecting it opens a second-level picker with `Human action placeholder` and `Create new Action app`.
- Selecting `Human action placeholder` inserts a visible `Human action (placeholder)` task under `Stage 1` sequential tasks.
- The right properties panel still showed stage properties after selecting the inserted task; task-level evidence packet fields, reviewer outcomes, and return mappings were not visible in this observation.
- The Case JSON editor is available and showed case metadata including `id: case-rNCvlV3LxR`, `version: 23.0.0`, `caseIdentifier: CASE`, `caseIdentifierType: constant`, `caseAppEnabled: true`, `publishVersion: 2`, and `caseUnifiedSchemaEnabled: true`.
- The JSON editor accepted accidental typed text into the modal but kept `Save` disabled and prompted to discard changes; the malformed editor-only change was discarded.

Result:

- G-003: PARTIAL. Studio Web can insert a real Human action placeholder task into a Maestro Case plan, but the pass condition is not met because reviewer-visible evidence table, agent output, policy decision, block reason, recommended options, approve/reject/request-evidence/comment outcome, and structured return to the case are still unproven.
- G-001/G-002/G-004 remain PARTIAL. This observation improves the build path for human review but does not prove runtime audit reconstruction, active-case policy version pinning, or raw-recommendation-before-override visibility.

Decision impact:

- Continue G-003 through `Create new Action app` or task configuration before choosing a Case App/custom evidence-packet fallback.
- Do not start broad implementation yet; the next validation action must create/configure a real evidence packet and run or publish the smallest case instance.
- Treat `Human action placeholder` as a scaffold only, not a pass-worthy evidence packet.

Product feedback:

- PF-004 updated from open friction to partially resolved insertion path with remaining task-configuration ambiguity.

Evidence:

- `docs/validation/artifacts/2026-06-25/g003-human-action-placeholder-canvas.png`

## 2026-06-25 01:22 IST - G-003 Action App Schema Inspection

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Safari browser session authenticated as `Arshdeep Singh`.
- Studio Web solution ID `b6446ea0-7ebd-4712-ccbf-08ded1e3ee41`.
- Action app project URL observed with project ID `986ee0c8-915c-4569-8df9-a74b454589a9`.

Gate:

- G-003: Human Evidence Packet.
- Assumption tested: `Create new Action app` can expose structured inputs, outcomes, comments, and return fields for a reviewer evidence packet.

Steps:

1. Switched from the logged-in Zen session to Safari at user request.
2. Opened the existing `SimpleApprovalApp` Studio URL in Safari and confirmed Safari could authenticate into UiPath.
3. Clicked `Edit here` to move the active editing session from the duplicate Zen browser tab into Safari.
4. Dismissed the Studio Web local-Assistant migration prompt by selecting `Do this later`, then selected `I'll switch later, just not today` and `Stay on current setup`.
5. Expanded `SimpleApprovalApp` and opened `ActionSchema`.
6. Inspected the generated Simple Approval action schema.
7. Clicked `Add property` once under input properties to test the next schema-edit affordance; it opened a data-type chooser but did not immediately create a visible field row in this observation.

Observed:

- Safari can access the same UiPath Studio project without requesting secrets or credentials in chat.
- Studio Web showed a duplicate-editing banner: `This project is being edited by you in another tab or browser. You may view it in read-only mode or continue editing here.`
- `Edit here` moved the editing session to Safari.
- Studio Web showed an upgrade prompt stating that editing and debugging RPA and app projects are moving to local UiPath Assistant and are required for all Community users starting July 22.
- Selecting `Stay on current setup` allowed the web-based validation to continue.
- `SimpleApprovalApp` contains page `SimpleApproval`, workflow files `SimpleApproval_ApproveButton_click.xaml` and `SimpleApproval_RejectButton_click.xaml`, and action `ActionSchema`.
- The generated review page exposes visible reviewer controls: `Content for Review`, `Comment`, `Approve`, and `Reject`.
- `ActionSchema` explicitly models outcomes `approve` and `reject`, input property `Content` typed `System.String`, input/output property `Comment` typed `System.String`, an output properties section with `Add property`, and action key `5e4cfd91-d8f9-46f7-83da-fdb3572e6ece`.
- The action schema text says it defines data exchanged between the app and external workflows or agents and configures inputs, outputs, and outcomes.

Result:

- G-003: PARTIAL. UiPath Action app schema is a credible path for structured human review because it exposes explicit outcomes, typed inputs, input/output comments, and output properties. The gate is not a pass yet because the full service-recovery evidence packet was not configured, rendered to a reviewer, submitted through Action Center, or returned structurally to a running case.
- G-001/G-002/G-004 remain PARTIAL. This observation does not prove runtime case audit reconstruction, policy version pinning, or raw agent recommendation visibility before policy override.

Decision impact:

- Continue with Action app schema as the primary G-003 path for the next live validation.
- Keep the Case App/custom evidence-packet fallback open until a real task shows the evidence packet clearly in reviewer context and returns structured outcome data to the case.
- Do not start broad implementation until a minimal live case instance is published/debugged and G-001, G-002, and G-004 are answered.

Product feedback:

- PF-004 updated with `Create new Action app` / `ActionSchema` findings.
- PF-005 added for the Studio Web local-Assistant migration prompt and duplicate-browser edit handoff during hackathon validation.

Evidence:

- `docs/validation/artifacts/2026-06-25/g003-safari-simple-approval-upgrade-prompt.png`
- `docs/validation/artifacts/2026-06-25/g003-action-schema-input-output-properties.png`

## 2026-06-25 01:28 IST - G-003 Generated Evidence Packet Page

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Safari browser session authenticated as `Arshdeep Singh`.
- Studio Web solution ID `b6446ea0-7ebd-4712-ccbf-08ded1e3ee41`.
- Action app project ID `986ee0c8-915c-4569-8df9-a74b454589a9`.

Gate:

- G-003: Human Evidence Packet.
- Assumption tested: a generated Action app page can render the service-recovery evidence packet fields needed for human review.

Steps:

1. Added custom `System.String` input properties to `ActionSchema`: `EvidencePacketJson`, `RawAgentRecommendation`, and `PolicyDecisionJson`.
2. Ran `Generate page` from the Action schema.
3. Waited for page generation to complete after the initial `Generating page layout...` state.
4. Inspected the generated review page and attempted to identify a safe manual repair path for the missing policy decision field.
5. Captured the generated page state.

Observed:

- Studio Web generated `FeedbackSubmissionPagePage` and click workflow files for approve/reject outcomes.
- The generated page rendered visible reviewer fields for `Content`, `Evidence Packet Json`, `Raw Agent Recommendation`, `Comment`, `Approve`, and `Reject`.
- Studio Web warned: `Auto-generation of controls failed for few properties` and specifically named `PolicyDecisionJson`.
- The page showed an `Unnamed String 1` label/value pair, which appears related to the failed or ambiguous field generation, but this was not confirmed.
- Selecting the `Unnamed String 1` label opened label properties, but the visible `. Edit` affordance edited the control name (`Label4`) rather than clearly editing the displayed field text or binding.
- Publishing/running the Action app was not yet attempted successfully in this observation.

Result:

- G-003: PARTIAL with a narrower blocker. UiPath can generate most of the evidence packet page from typed Action schema fields, but the proof-critical `PolicyDecisionJson` field did not auto-generate and no Action Center task has yet shown the packet or returned a structured decision to a running case.
- G-001/G-002/G-004 remain PARTIAL because no live case instance has run and no runtime case history/metadata/linked override events have been inspected.

Decision impact:

- Continue trying the Action app path because evidence packet rendering is now mostly concrete.
- Before broad implementation, validate whether `PolicyDecisionJson` can be manually bound, the app can be published, and a case/human task can return approve/reject/comment data.
- Keep Case App/custom evidence-packet fallback open if the generated Action page cannot reliably render all proof-critical fields.

Product feedback:

- PF-004 remains relevant for human-task setup and mapping ambiguity.
- PF-006 added for generated Action page reliability/repairability when custom schema properties are used.

Evidence:

- `docs/validation/artifacts/2026-06-25/g003-generated-action-page-partial-evidence-packet.png`

## 2026-06-25 01:36 IST - G-001/G-003 Live Case Runtime Attempt

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Safari browser session authenticated as `Arshdeep Singh`.
- Deployed solution version: `Solution v1.0.0`.
- Orchestrator folder: `Solution`, folder key `9d7ae568-d60e-4395-94d7-db115bfb25de`.
- Live Maestro case ID: `320c067a-27b9-4c2f-8b26-f6ee38ad97cc`.
- Live case instance / job key: `e1dbad8e-e37c-409d-8cfb-5f4e6125102b`.
- Case identifier: `CASE-693515549`.

Gates:

- G-001: Native Case State / Audit Reconstruction.
- G-003: Human Evidence Packet.
- G-004 dependency check: whether raw/final event separation can be represented once the case runs.

Steps:

1. Opened `Manage` for `SimpleApprovalApp`.
2. Started the publish/deploy workflow for version `1.0.0` with release notes `G-003 evidence packet validation`.
3. Observed deployment pipeline stages: setup, publish package, configure, deploy, activate.
4. Observed `Deployment successful`; logs showed Orchestrator and Apps activated and `All 2 service(s) activated successfully`.
5. Opened the deployed Orchestrator `Solution` folder.
6. Started a `Maestro Case` job from Orchestrator with entry point `Trigger 1` and `{}` input.
7. Opened the live case instance from Orchestrator using `Open in Maestro`.
8. Inspected Maestro case execution trail, global variables, action history, and incident details.

Observed:

- Orchestrator process picker listed `Maestro BPMN`, `Maestro Case`, and `SimpleApprovalApp`.
- Starting `Maestro Case` created a running job with package `Solution.caseManagement.Maestro.Case@1.0.0`.
- Orchestrator exposed an `Open in Maestro` link for the live case instance.
- Maestro opened a single case instance view for `CASE-693515549`.
- The case instance status became `Faulted`.
- The visible execution trail reconstructed ordered runtime steps with timestamps:
  - `Trigger 1` completed at `2026-06-24 20:06:14 UTC`.
  - `Case manager` completed at `2026-06-24 20:06:21 UTC`.
  - `Human action (placeholder)` completed in `Stage 1` at `2026-06-24 20:06:29 UTC`.
  - `Case manager` completed at `2026-06-24 20:06:35 UTC`.
  - `SimpleApprovalApp` failed in `Stage 1` at `2026-06-24 20:06:42 UTC`.
- Global variables visible in the case view included `caseEndMessageResponse = null`, `CaseId = CASE-693515549`, and `stageHasRun_Stage_1 = false`.
- Action history showed `No actions yet`.
- Incidents showed `Failure in the AppTasks request - (170000)` with error `The Title field is required.` and incident ID `D689487C-F874-4E2C-B5ED-B0F6814630AF`.

Result:

- G-001: PARTIAL. A single Maestro case instance view reconstructs runtime order, timestamps, stage/task progression, global variables, incident detail, and job linkage. It does not yet reconstruct the required service-recovery evidence state, policy versions, raw agent recommendation, policy decision, closure block reason, or human reviewer action because the current case is still a scaffold and the Action task faulted before review.
- G-003: PARTIAL with concrete runtime blocker. Deployment and live case execution work, but the Action app task fails before reviewer rendering because a required Title field is missing from the AppTasks request.
- G-002: PARTIAL. Live case view exposes runtime instance state but no explicit `interpretation_policy_version`, `decision_policy_version`, or migration event yet.
- G-004: PARTIAL. The live case has not yet persisted/showed raw `closure_candidate` Agent Interpretation Event linked to Policy Decision Event override.

Decision impact:

- The next fix is not broad implementation. It is a minimal Action task configuration repair: provide/map a required Title for `SimpleApprovalApp`, republish/redeploy, then retry or start a fresh case instance.
- Maestro's native case instance view is promising for G-001 but must be extended with explicit custom audit/state variables or events for evidence state, policy versions, raw agent event, policy decision, block reason, and reviewer result.
- The product feedback award ledger should treat `Title field is required` as a high-impact configuration validation issue: deployment succeeded, but the required task field was only surfaced as a runtime incident.

Evidence:

- `docs/validation/artifacts/2026-06-25/g003-action-app-deployment-success.png`
- `docs/validation/artifacts/2026-06-25/g001-maestro-case-orchestrator-running-job.png`
- `docs/validation/artifacts/2026-06-25/g001-maestro-live-case-execution-trail-faulted.png`
- `docs/validation/artifacts/2026-06-25/g003-maestro-action-task-title-required-incident.png`

## 2026-06-25 01:46 IST - G-003 Action Task Title Repair / Publish Blocker

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Safari browser session authenticated as `Arshdeep Singh`.
- Existing published solution version remained `1.0.0`.

Gate:

- G-003: Human Evidence Packet.

Steps:

1. Reopened the `Maestro Case` case plan after the live runtime fault.
2. Selected the `SimpleApprovalApp` human action task.
3. Set the required task title to `Review service recovery evidence`.
4. Confirmed the task no longer showed the visible validation warning in the Case plan canvas.
5. Opened `Manage > Deployments` and `Manage > Versions`.
6. Confirmed the published package list still contained only version `1.0.0` with release notes `G-003 evidence packet validation`.
7. Attempted to open the Studio Web `Publish` control through accessibility clicks and direct screen coordinates.

Observed:

- The design-time title repair is real: `SimpleApprovalApp` remains in `Stage 1`, and the visible task validation warning is gone.
- The repair has not been validated at runtime because no new package version was published after the title change.
- `Manage > Versions` showed only published version `1.0.0`; no `1.0.1` or later repaired package was available.
- The publish control is visually present in Studio Web, but it was exposed in the accessibility tree only as text inside a broad toolbar/tab group and did not open reliably through the available automation path in this session.

Result:

- G-003: PARTIAL. The concrete runtime blocker from the previous run has a design-time repair, but the repair is not proven until a new package version is published, deployed, and a fresh case instance reaches Action Center.
- G-001/G-002/G-004: unchanged PARTIAL. No new live case instance was started after the repair.

Decision impact:

- Continue with the same minimal validation path, but the next live step is packaging/publishing the repaired case definition, not broad implementation.
- If Studio Web publish remains unreliable, use an alternate publish path if available through UiPath CLI or another browser/session; otherwise document it as a product/build blocker and ask for interactive user help only for the click, not credentials.

Product feedback:

- PF-008 added for Studio Web publish/versioning control accessibility and packaging clarity.

Evidence:

- `docs/validation/artifacts/2026-06-25/g003-title-repaired-publish-control-not-opened.png`

## 2026-06-25 18:47 IST - G-003/G-004 Live Package 1.0.3 Validation

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- UiPath CLI `uip` authenticated for `arshgill6120@gmail.com`.
- Orchestrator folder key `9d7ae568-d60e-4395-94d7-db115bfb25de`, folder ID `7978263`.
- Case package feed ID `831bf59a-a3f1-4aa8-8890-f01b857c18f3`.
- Case package under test: `Solution.caseManagement.Maestro.Case:1.0.3`.
- Direct process created for validation: `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`.
- Live case instance/job key: `dde02258-c535-4c52-a8a8-a34d470e0ce6`.
- Live case external ID: `CASE-693765876`.
- Action Center task ID: `4295299`, task key `d88c4d59-0aa1-464c-8abf-e15dc1304633`.

Gates:

- G-001: Native Case State / Audit Reconstruction.
- G-002: Policy Version Pinning.
- G-003: Human Evidence Packet.
- G-004: Agent Recommendation Visible Before Override.

Steps:

1. Downloaded/exported the Studio Web solution with `uip solution download` and inspected the generated case package source.
2. Built validation package `1.0.1`; uploaded successfully, then observed runtime failure `No app: SimpleApprovalApp found in folder: .app`.
3. Built validation package `1.0.2` with explicit app folder binding to `arshgill6120@gmail.com's workspace/Solution`.
4. Created a direct process for `1.0.2`, started a case, observed Action Center task creation, assigned it, approved it, and verified structured task return to the case.
5. Built validation package `1.0.3` with explicit app folder binding and populated evidence packet fields:
   - `EvidencePacketJson` with green business state and missing authoritative network telemetry.
   - `RawAgentRecommendation` with `event_type: AgentInterpretationEvent`, `interpretation_policy_version: interp-2026-06-25.1`, and `recommended_next_stage: closure_candidate`.
   - `PolicyDecisionJson` with `event_type: PolicyDecisionEvent`, link to `aie-g004-missing-telemetry`, `decision_policy_version: decision-2026-06-25.1`, `decision: override_recommendation`, `from_recommended_stage: closure_candidate`, `to_stage: verify_telemetry`, and `block_reason: missing_authoritative_signal`.
6. Uploaded `Solution.caseManagement.Maestro.Case:1.0.3`.
7. Created direct process `Maestro Case G004 1.0.3 Evidence Validation` pinned to package `1.0.3` with `--no-auto-update`.
8. Started one case instance and polled `uip maestro case instance get`, `uip maestro case instance element-executions`, and `uip tasks list`.
9. Opened Action Center task `4295299` in Safari and captured reviewer-visible evidence.
10. Assigned the task to self, completed it with `uip tasks complete ... --action reject`, and verified task/case completion through CLI.

Observed:

- `uip or processes create` returned `ProcessVersion: 1.0.3` for process `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`.
- `uip maestro case instance get dde02258...` returned `PackageKey: Solution.caseManagement.Maestro.Case:1.0.3`, `PackageVersion: 1.0.3`, `LatestRunStatus: Completed`, and no incidents.
- `uip tasks get 4295299` before completion returned task `Data` containing:
  - `EvidencePacketJson` with `closure_block_reason: missing_authoritative_signal`.
  - `RawAgentRecommendation` with `recommended_next_stage: closure_candidate`.
  - `PolicyDecisionJson` with `decision: override_recommendation`, `from_recommended_stage: closure_candidate`, `to_stage: verify_telemetry`, `block_reason: missing_authoritative_signal`, and `decision_policy_version: decision-2026-06-25.1`.
- Action Center rendered the evidence packet and raw recommendation in the reviewer task.
- Action Center did not render the policy decision with its schema label; it showed `Unnamed String 1` / `Unnamed string 1` instead of the `PolicyDecisionJson` value.
- Completing task `4295299` with `--action reject` returned `TaskCompleted`.
- `uip tasks get 4295299` after completion returned `Status: Completed`, `Action: reject`, `ActionLabel: reject`, `CompletedByUser: Arshdeep Singh`, and the reviewer comment.
- `uip maestro case instance variables dde02258...` returned the structured `HitlTask`, `Action: reject`, reviewer comment, assigned/completed user metadata, task source metadata, timestamps, and `TaskCompletedOutputsVariable.SimpleApprovalApp`.
- Safari initially still showed the task in `Pending` after CLI completion; after a browser refresh, Action Center moved task `4295299` to `Completed`, showed `(reject)` in the task header, disabled approve/reject, and displayed the reviewer comment.
- The case completed at `2026-06-25T13:17:32.2491173Z`.

Result:

- G-001: PARTIAL. A single case query reconstructs package version, ordered runtime elements, stage/task state, task source linkage, human action, timestamps, and structured task return. It still does not natively reconstruct all domain audit fields in one Case view/query unless the proof-critical evidence payloads are carried as explicit custom task/audit data; implement custom audit events for evidence state, raw agent event, policy decision, block reason, and policy versions.
- G-002: PARTIAL/PASS for explicit metadata pinning. Case package version pinning is observed through direct process creation and `PackageKey`; interpretation and decision policy versions persist inside the explicit task payload. Native active-case policy migration semantics are not proven, so active cases must remain explicitly pinned and migrations must be custom audited.
- G-003: PASS for Action Center mechanics and structured return; PARTIAL for final reviewer legibility. The reviewer can see content, evidence packet, raw agent output, comment, approve/reject controls, and the case receives structured return. The policy decision field is persisted but mislabeled/not legible in the generated page, so the final demo should repair the Action page label/binding or use a custom evidence-packet view.
- G-004: PASS for persistence and API-level visibility of raw recommendation before override; PARTIAL for reviewer UI display of the policy decision. The same live task persisted a raw `AgentInterpretationEvent` recommending `closure_candidate` and a linked `PolicyDecisionEvent` overriding to `verify_telemetry` for `missing_authoritative_signal`. The Action Center page showed the raw recommendation but not the policy decision value under a usable label.

Decision impact:

- Maestro Case remains viable as the primary track.
- Proceed with a UiPath-grounded implementation slice only if it preserves explicit audit payloads and does not rely on generated Action Center labels for the final proof beat.
- Use direct process/package version pinning for validation and demo repeatability.
- Repair or replace the generated evidence-packet page before final demo polish.

Product feedback:

- PF-009 through PF-014 are strengthened with live package/runtime evidence.
- Add a new Action Center/CLI completion note under PF-013 or a follow-up entry for API persistence versus UI label mismatch.

Evidence:

- `docs/validation/artifacts/2026-06-25/g003-case-102-running-hitl-inprogress.png`
- `docs/validation/artifacts/2026-06-25/g003-case-102-action-history-empty-hitl-inprogress.png`
- `docs/validation/artifacts/2026-06-25/g003-action-center-task-renders-unassigned-fields-null.png`
- `docs/validation/artifacts/2026-06-25/g004-action-center-raw-recommendation-visible-task-4295299.png`
- `docs/validation/artifacts/2026-06-25/g004-action-center-policy-field-mislabeled-task-4295299.png`
- `docs/validation/artifacts/2026-06-25/g004-action-center-stale-pending-after-cli-complete-task-4295299.png`
- `docs/validation/artifacts/2026-06-25/g004-action-center-completed-reject-task-4295299.png`

## 2026-06-25 19:05 IST - Wave 07 Live Generated Payload Run

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- UiPath CLI authenticated for `arshgill6120@gmail.com`.
- Orchestrator folder key `9d7ae568-d60e-4395-94d7-db115bfb25de`, folder ID `7978263`.
- Case package feed ID `831bf59a-a3f1-4aa8-8890-f01b857c18f3`.
- Generated local payload source: `python -m service_recovery_core.evals --uipath-payload-scenario E-002 --output eval_results/uipath_action_payload_E002.json`.
- Uploaded package: `Solution.caseManagement.Maestro.Case:1.0.4`.
- Updated validation process: `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`.
- Live case instance/job key: `3af41e1d-8b04-4eba-aa5e-a95c5c673730`.
- Live case external ID: `CASE-693863006`.
- Action Center task ID: `4300080`, task key `77261fcd-d77a-411d-91df-070797dd761c`.

Steps:

1. Exported the local E-002 missing-authoritative-telemetry scenario into the UiPath Action Center payload shape.
2. Repacked the known-good `1.0.3` Case package as `1.0.4`, changing only the package version and `HitlTaskArguments` / Case task input values to the generated E-002 payload.
3. Uploaded `1.0.4` to the solution package feed.
4. Observed that default `uip or packages get Solution.caseManagement.Maestro.Case:1.0.4` could not find the package, while `--feed-id 831bf59a-a3f1-4aa8-8890-f01b857c18f3` did find it.
5. Observed that `uip or processes create ... --package-version 1.0.4` failed prerequisite validation even though the feed-scoped package read succeeded.
6. Updated existing validation process `9a7eb300-7b16-4856-b14f-d6f2da3dbe61` to `1.0.4` with `uip or processes update-version ... --package-version 1.0.4`.
7. Verified process readback: `ProcessVersion: 1.0.4`, `AutoUpdate: false`.
8. Verified process version history contained explicit `1.0.3` and `1.0.4` entries.
9. Started a fresh case job from the updated pinned process.
10. Read Action Center task `4300080` before human action and verified the generated payload.
11. Assigned task `4300080` to `arshgill6120@gmail.com`, completed it with `--action reject`, and verified task/case completion.

Observed:

- `uip or packages upload ... --feed-id 831bf59a-a3f1-4aa8-8890-f01b857c18f3` returned package `Solution.caseManagement.Maestro.Case:1.0.4`.
- Feed-scoped package read returned `PackageType: CaseManagement`, `ProjectType: CaseManagement`, `PackageVersion: 1.0.4`, and `IsActive: true`.
- Default package read did not see the same package, and process creation did not expose a feed selector.
- `uip or processes update-version` succeeded and produced explicit version history for the existing process.
- `uip maestro case instance get 3af41e1d...` returned `PackageKey: Solution.caseManagement.Maestro.Case:1.0.4`, `PackageVersion: 1.0.4`, and later `LatestRunStatus: Completed`.
- `uip tasks get 4300080` before completion returned:
  - `RawAgentRecommendation` with `event_id: AIE-E002`, `interpretation_policy_version: ip-v1`, and `recommended_next_stage: closure_candidate`.
  - `PolicyDecisionJson` with `event_id: PDE-E-002`, `links_to: AIE-E002`, `decision_policy_version: dp-v1`, `decision: override_recommendation`, `from_recommended_stage: closure_candidate`, `to_stage: verify_telemetry`, and `block_reason: missing_authoritative_signal`.
  - `EvidencePacketJson` with `business_state: green`, `derived_evidence_state: missing_pending`, and `closure_block_reason: missing_authoritative_signal`.
- Initial task completion failed with `This action is no longer assigned to you` because the task was `Unassigned`; assigning it to the logged-in user first resolved the lifecycle.
- Task `4300080` completed with `Action: reject` at `2026-06-25T13:34:53.493Z`.
- Case `3af41e1d...` completed at `2026-06-25T13:35:08.0998188Z`.

Result:

- Wave 07 first slice: PASS for live UiPath-visible generated payload propagation. The payload used in Action Center came from the local eval exporter rather than hand-written demo data.
- G-002 strengthened: process `AutoUpdate: false`, case `PackageVersion: 1.0.4`, and version history explicitly records movement from `1.0.3` to `1.0.4`.
- G-004 strengthened: raw local-agent recommendation and final policy decision are visible in the same pre-human task payload and remain separate linked JSON events.
- G-003 strengthened for lifecycle: unassigned Action tasks require assignment before CLI completion, then return structured action/comment.
- G-001 remains PARTIAL for native one-query domain audit: explicit payloads make reconstruction possible, but the native case surface still does not provide a dedicated domain audit timeline without custom audit fields/events.

Product feedback:

- PF-013 updated by the unassigned task lifecycle observation.
- PF-017 added for feed-scoped package visibility and process-binding mismatch.

## 2026-06-25 19:13 IST - Wave 07 Live Contradiction Route Run

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- UiPath CLI authenticated for `arshgill6120@gmail.com`.
- Orchestrator folder key `9d7ae568-d60e-4395-94d7-db115bfb25de`, folder ID `7978263`.
- Case package feed ID `831bf59a-a3f1-4aa8-8890-f01b857c18f3`.
- Generated local payload source: `python -m service_recovery_core.evals --uipath-payload-scenario E-004 --output eval_results/uipath_action_payload_E004.json`.
- Uploaded package: `Solution.caseManagement.Maestro.Case:1.0.5`.
- Updated validation process: `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`.
- Live case instance/job key: `60e52ca5-6891-45b4-9e98-e1b08a984f06`.
- Live case external ID: `CASE-693865376`.
- Action Center task ID: `4300219`, task key from task list for job `60e52ca5-6891-45b4-9e98-e1b08a984f06`.

Steps:

1. Exported the local E-004 contradiction scenario into the UiPath Action Center payload shape.
2. Repacked the known-good `1.0.4` Case package as `1.0.5`, changing only package version/release notes and the Case task payload values.
3. Uploaded `1.0.5` to solution feed `831bf59a-a3f1-4aa8-8890-f01b857c18f3`.
4. Verified feed-scoped package read for `Solution.caseManagement.Maestro.Case:1.0.5`.
5. Updated existing validation process to `1.0.5` and verified `AutoUpdate: false`.
6. Verified process version history now contains explicit `1.0.3`, `1.0.4`, and `1.0.5` entries.
7. Started fresh case job `60e52ca5-6891-45b4-9e98-e1b08a984f06`.
8. Read task `4300219` before human action and asserted the contradiction payload fields.
9. Assigned task `4300219` to `arshgill6120@gmail.com`, completed it with `--action reject`, and verified task/case completion.

Observed:

- `uip maestro case instance get 60e52ca5...` returned `PackageKey: Solution.caseManagement.Maestro.Case:1.0.5`, `PackageVersion: 1.0.5`, and later `LatestRunStatus: Completed`.
- `uip tasks get 4300219` before completion returned:
  - `RawAgentRecommendation` with `event_id: AIE-E004`, `interpretation_policy_version: ip-v1`, and `recommended_next_stage: closure_candidate`.
  - `PolicyDecisionJson` with `event_id: PDE-E-004`, `links_to: AIE-E004`, `decision_policy_version: dp-v1`, `decision: require_human_review`, `from_recommended_stage: closure_candidate`, `to_stage: human_review`, and `block_reason: source_contradiction`.
  - `EvidencePacketJson` with `business_state: green`, `derived_evidence_state: contradicting`, `closure_block_reason: source_contradiction`, and fresh authoritative `network_telemetry.service_live_status = not_live`.
- Task `4300219` was initially `Unassigned`; assignment to the logged-in user succeeded.
- Task `4300219` completed with `Action: reject` at `2026-06-25T13:43:16.503Z`.
- Case `60e52ca5...` completed at `2026-06-25T13:43:29.3270546Z`.

Result:

- G-005 soft gate: PASS at API/persistence level for distinct 2A and 2B routes.
  - E-002 missing authoritative telemetry routes to `verify_telemetry` with `decision: override_recommendation` and `block_reason: missing_authoritative_signal`.
  - E-004 fresh authoritative contradiction routes to `human_review` with `decision: require_human_review` and `block_reason: source_contradiction`.
- Second proof beat: PASS at API/persistence level. The same canonical green business fixture persisted fresh authoritative network telemetry contradiction and escalated to human review.
- G-003 remains PARTIAL for reviewer UI legibility until `PolicyDecisionJson` binding is repaired; API data is correct.
- G-001 remains PARTIAL for native one-query domain audit; explicit payloads now carry both missing/stale and contradiction proof beats, but native Case still lacks a domain-specific audit timeline.

Decision impact:

- Continue with Maestro Case as primary track.
- Next validation should repair generated Action Center binding for `PolicyDecisionJson` or create a custom evidence-packet view before demo polish.
- The contradiction route is ready to become the second main demo beat after UI legibility is repaired.

## 2026-06-25 19:25 IST - Custom Audit Bundle Implementation Checkpoint

Environment:

- Local Python environment.
- No new UiPath cloud mutation in this checkpoint.
- Grounded in prior live UiPath findings from package `1.0.4` / task `4300080` and package `1.0.5` / task `4300219`.

Steps:

1. Added `service_recovery_core.audit_bundle.build_case_audit_bundle`.
2. Added `python -m service_recovery_core.evals --audit-bundle-scenario <ID>` to export a one-object domain audit bundle.
3. Generated local audit bundles for E-002 missing authoritative telemetry and E-004 source contradiction.
4. Ran targeted audit/payload tests, full unit tests, and the local eval baseline.
5. Updated architecture docs to map the bundle to G-001/G-002/G-003/G-004.

Observed:

- E-002 bundle contains:
  - `audit_contract_version: service-recovery-audit-v1`.
  - `evidence_state.business_state: green`.
  - `evidence_state.derived_evidence_state: missing_pending`.
  - `evidence_state.closure_block_reason: missing_authoritative_signal`.
  - `policy_versions.interpretation_policy_version: ip-v1`.
  - `policy_versions.decision_policy_version: dp-v1`.
  - raw `AgentInterpretationEvent` with `recommended_next_stage: closure_candidate`.
  - linked `PolicyDecisionEvent` with `decision: override_recommendation`, `from_recommended_stage: closure_candidate`, `to_stage: verify_telemetry`, and `links_to: AIE-E002`.
  - ordered events: EvidenceStateEvent, AgentInterpretationEvent, PolicyDecisionEvent, HumanReviewEvent.
- E-004 bundle contains:
  - `evidence_state.business_state: green`.
  - `evidence_state.derived_evidence_state: contradicting`.
  - `evidence_state.closure_block_reason: source_contradiction`.
  - linked policy decision `require_human_review` to `human_review`.
  - reviewer options including `open_investigation`.
- Contradiction reviewer content now explicitly says fresh authoritative telemetry contradicts the business state.

Result:

- G-001: still PARTIAL natively, but the custom audit fallback is now concrete and test-covered. A single `service-recovery-audit-v1` bundle reconstructs the domain fields that native Case history did not expose in one view/query.
- G-002: strengthened locally. The bundle pins interpretation and decision policy versions at top level and inside linked events.
- G-003: strengthened locally. The bundle has a structured `reviewer_packet` with evidence table, raw agent recommendation, policy decision, block reason, recommended options, and rendering status.
- G-004: strengthened locally. The bundle preserves raw agent recommendation and final policy decision as separate linked events.
- This checkpoint does not claim new live UiPath validation. It converts prior live platform facts into a grounded implementation artifact.

Commands run:

- `python -m unittest tests.test_audit_bundle tests.test_uipath_payload`
- `python -m service_recovery_core.evals --audit-bundle-scenario E-002 --output eval_results/audit_bundle_E002.json`
- `python -m service_recovery_core.evals --audit-bundle-scenario E-004 --output eval_results/audit_bundle_E004.json`
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`

Decision impact:

- Use `service-recovery-audit-v1` as the implementation contract for custom Case/Data Fabric/Data Service audit storage unless a later native Maestro Case audit view proves the same domain reconstruction.
- Next live UiPath slice should store or surface this bundle through the chosen UiPath path, then repair or replace the generated Action Center reviewer UI.

Product feedback:

- Strengthens PF-015. The platform can orchestrate the workflow, but builders need a native domain audit/event inspector for linked agent, policy, evidence, and human events.

## 2026-06-25 19:35 IST - Static Evidence Packet Renderer

Environment:

- Local Python and Playwright.
- No new UiPath cloud mutation in this checkpoint.

Steps:

1. Added `service_recovery_core.evidence_packet_view.render_evidence_packet_html`.
2. Added `python -m service_recovery_core.evals --evidence-packet-html-scenario <ID>`.
3. Generated static reviewer packet HTML artifacts for E-002 and E-004.
4. Captured Playwright screenshots for E-004 at desktop and mobile viewport sizes.
5. Ran targeted tests, full unit tests, local eval baseline, and Playwright visibility checks.

Observed:

- `docs/demo/artifacts/evidence_packet_E002.html` renders the missing authoritative telemetry proof beat.
- `docs/demo/artifacts/evidence_packet_E004.html` renders the contradiction proof beat.
- E-004 desktop screenshot shows:
  - case/service identity,
  - business state `green`,
  - evidence state `contradicting`,
  - block reason `source_contradiction`,
  - raw agent recommendation `closure_candidate`,
  - final policy decision `require_human_review` to `human_review`,
  - evidence table with fresh authoritative `network_telemetry` value `not_live`,
  - reviewer options including `open_investigation`,
  - audit event order from EvidenceStateEvent through HumanReviewEvent.
- Playwright visibility checks passed for desktop and mobile.

Result:

- G-003: strengthened with a custom evidence-packet fallback. Action Center remains the validated task lifecycle, but this renderer gives a legible reviewer packet if generated Action Center UI continues to hide `PolicyDecisionJson`.
- G-004: strengthened for demo visibility. The raw agent recommendation and policy decision are visibly separate on one screen.
- G-006: PARTIAL/PASS for custom demo surface. The renderer shows severity-adjacent evidence state, route, block reason, history order, and evidence table, but it is not yet embedded in UiPath Case App.
- This does not claim native Action Center rendering is repaired.

Evidence:

- `docs/demo/artifacts/evidence_packet_E002.html`
- `docs/demo/artifacts/evidence_packet_E004.html`
- `docs/demo/artifacts/evidence_packet_E004_desktop.png`
- `docs/demo/artifacts/evidence_packet_E004_mobile.png`

Commands run:

- `python -m service_recovery_core.evals --evidence-packet-html-scenario E-002 --output docs/demo/artifacts/evidence_packet_E002.html`
- `python -m service_recovery_core.evals --evidence-packet-html-scenario E-004 --output docs/demo/artifacts/evidence_packet_E004.html`
- Playwright Chromium screenshot/visibility script for desktop and mobile.
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`

Decision impact:

- Keep this renderer as the demo fallback if Action Center binding repair is not reliable.
- Next live UiPath work should either embed/surface this packet in Case App/custom UI or repair the generated Action Center binding.

Product feedback:

- Strengthens PF-013: we now have a concrete comparison artifact showing the fields that the generated Action Center UI should have rendered legibly.

## 2026-06-25 21:01 IST - Data Fabric Audit Storage Preparation

Environment:

- UiPath CLI authenticated to org `keepingitlowkey`, tenant `DefaultTenant`.
- Data Fabric CLI surface inspected read-only.
- No live Data Fabric schema or record mutation was performed in this checkpoint.

Gate/wave:

- G-001: Native Case State / Audit Reconstruction.
- G-002: Policy Version Pinning.
- G-008: CLI/coding-agent lifecycle support.

Assumption tested:

- If native Maestro Case history remains insufficient for one-query domain audit reconstruction, Data Fabric can serve as the durable UiPath-accessible storage path for `service-recovery-audit-v1` bundles.

Steps:

1. Confirmed `uip df` command availability.
2. Ran a read-only entity listing for native Data Fabric entities.
3. Added a proposed `ServiceRecoveryAuditBundle` entity schema.
4. Added a local exporter for Data Fabric record bodies from the same audit bundle used by the evidence packet renderer.
5. Generated an E-004 contradiction record body with the live Case/task/package references from package `1.0.5`.

Observed:

- `uip df entities list --native-only --output json` returned success with an empty entity list: `{"Result":"Success","Code":"EntityList","Data":[]}`.
- `uip df` is available even though `uip tools list --output json` did not list a `data-fabric-tool` entry in the inspected output.
- The proposed schema is stored at `docs/architecture/data_fabric/service_recovery_audit_bundle_entity.json`.
- `python -m service_recovery_core.evals --data-fabric-record-scenario E-004` emits fields for:
  - case/service/scenario identity,
  - evidence state and block reason,
  - interpretation and decision policy versions,
  - live source Case instance key `60e52ca5-6891-45b4-9e98-e1b08a984f06`,
  - live source task ID `4300219`,
  - package version `1.0.5`,
  - raw agent event JSON,
  - policy decision event JSON,
  - reviewer packet JSON,
  - full audit bundle JSON.

Result:

- G-001: PARTIAL but materially advanced. A concrete Data Fabric storage path now exists as a proposed tenant schema plus insert-ready record body; live entity creation/query-back still requires explicit approval because it changes tenant schema.
- G-002: strengthened. The proposed record stores `interpretation_policy_version` and `decision_policy_version` as first-class fields and inside linked event JSON.
- G-004: unchanged PASS/PARTIAL from prior live task payload evidence; this checkpoint prepares durable storage for the same linked raw/final event pair.
- G-008: strengthened. The CLI can inspect Data Fabric and the repo can generate record bodies for a UiPath storage command, but no live insert has been run yet.

Commands run:

- `uip df --help`
- `uip tools list --output json`
- `uip df entities list --native-only --output json`
- `uip df entities create --help`
- `uip df records insert --help`
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- `python -m service_recovery_core.evals --data-fabric-record-scenario E-004 --output eval_results/data_fabric_record_E004.json`

Decision impact:

- Use Data Fabric as the preferred durable custom-audit storage candidate if the user approves live schema creation.
- Do not mark native G-001 as PASS: the platform still needs explicit domain audit state outside the native case runtime trail.

Product feedback:

- PF-018 added for Data Fabric CLI discovery mismatch: `uip df` is usable, but `uip tools list` did not expose the corresponding tool entry during discovery.

Next:

- Ask for explicit approval to create the live Data Fabric entity `ServiceRecoveryAuditBundle` in org `keepingitlowkey`, tenant `DefaultTenant`.
- If approved, create the entity, insert the E-004 record, query/read it back, update G-001/G-002 evidence, then commit/push the live validation checkpoint.

## 2026-06-25 21:08 IST - Live Data Fabric Entity Created / Insert Blocked

Environment:

- UiPath CLI authenticated to org `keepingitlowkey`, tenant `DefaultTenant`.
- User approved creating the live Data Fabric entity.
- Tenant schema mutation performed: created `ServiceRecoveryAuditBundle`.

Gate/wave:

- G-001: Native Case State / Audit Reconstruction.
- G-002: Policy Version Pinning.
- G-008: CLI/coding-agent lifecycle support.

Assumption tested:

- Data Fabric can store a durable one-query audit bundle for the E-004 contradiction proof beat.

Steps:

1. Created the Data Fabric entity from `docs/architecture/data_fabric/service_recovery_audit_bundle_entity.json`.
2. Read the schema back by entity ID.
3. Generated the E-004 audit record from the local eval exporter.
4. Attempted record insertion using:
   - `--file eval_results/data_fabric_record_E004.json`,
   - `--body` with the same full object,
   - a minimal required-field object,
   - a `{"Data": {...}}` wrapper,
   - field UUID keys,
   - an array containing the minimal object.
6. Attempted `uip df records import` with a CSV generated from the same E-004 record.
7. Listed records after the failed insert/import attempts.
5. Listed records after the failed insert attempts.

Observed:

- Entity creation succeeded:
  - entity name: `ServiceRecoveryAuditBundle`,
  - entity ID: `328ef8b6-ab70-f111-ac9a-002248a16d28`.
- `uip df entities get 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json` returned the created schema, including required fields such as `case_id`, `interpretation_policy_version`, `decision_policy_version`, JSON payload fields, and system fields.
- `uip df entities get ServiceRecoveryAuditBundle --output json` failed with `The value 'ServiceRecoveryAuditBundle' is not valid`; ID-based lookup works but name-based lookup does not.
- Record insertion failed every tested payload shape with:
  - `Required field "case_id" (3c8ef8b6-ab70-f111-ac9a-002248a16d28) is not provided and there is no default.`
- The debug log showed the CLI parsed a `--body` containing `case_id`, but the service still reported the required field as missing.
- CSV import returned `RecordsImported` with `TotalRecords: 1`, `InsertedRecords: 0`, and an `ErrorFileLink`, so the fallback import path also did not persist the audit record.
- `uip df records list 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json` returned success with `TotalCount: 0`.

Result:

- G-001: PARTIAL. Data Fabric schema creation/readback is validated, but record storage/query-back is blocked by CLI/API payload mapping. Native Case audit remains insufficient by itself; Data Fabric remains viable only after insert format is resolved or replaced by another storage path.
- G-002: PARTIAL/PASS for schema capability. Data Fabric can define first-class fields for both policy versions, but no live record has persisted them yet.
- G-004: unchanged from prior live task validation. The created schema can hold separate raw agent and policy decision JSON fields, but insert failed before persistence.
- G-008: strengthened and product-feedback-worthy. The CLI can create/read entity schema, but record insertion did not accept documented field-name JSON payloads.

Commands run:

- `uip df entities create ServiceRecoveryAuditBundle --file docs/architecture/data_fabric/service_recovery_audit_bundle_entity.json --output json`
- `uip df entities get ServiceRecoveryAuditBundle --output json`
- `uip df entities list --output json`
- `uip df entities get 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json`
- `python -m service_recovery_core.evals --data-fabric-record-scenario E-004 --output eval_results/data_fabric_record_E004.json`
- `uip df records insert 328ef8b6-ab70-f111-ac9a-002248a16d28 --file eval_results/data_fabric_record_E004.json --output json`
- `uip df records insert 328ef8b6-ab70-f111-ac9a-002248a16d28 --body <full-record-json> --output json`
- `uip df records insert 328ef8b6-ab70-f111-ac9a-002248a16d28 --body <minimal-required-fields-json> --output json`
- `uip df records insert 328ef8b6-ab70-f111-ac9a-002248a16d28 --body <wrapped-data-json> --output json`
- `uip df records insert 328ef8b6-ab70-f111-ac9a-002248a16d28 --body <field-id-keyed-json> --output json`
- `uip df records insert 328ef8b6-ab70-f111-ac9a-002248a16d28 --body <array-json> --output json`
- `uip df records import 328ef8b6-ab70-f111-ac9a-002248a16d28 --file tmp/data_fabric_record_E004.csv --output json`
- `uip df records list 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json`

Decision impact:

- Keep `ServiceRecoveryAuditBundle` as the preferred Data Fabric schema only if record insertion can be resolved quickly.
- Add a fallback branch: store the audit bundle as a UiPath-accessible artifact or Case custom payload while keeping the schema as proof of intended durable storage.
- Treat Data Fabric record insert as blocked until a working payload shape or platform fix is found.

Product feedback:

- PF-018 strengthened by name-vs-ID lookup behavior.
- PF-019 added for Data Fabric record insert rejecting documented field-name payloads even though the parsed body contains required fields.

Next:

- Try official docs/API or inspect the import error file if accessible without secrets.
- If record insertion remains blocked, use a file artifact or Case custom payload for final G-001 audit storage and document Data Fabric as a platform limitation for this build.

## 2026-06-25 21:17 IST - Orchestrator Bucket Audit Artifact Fallback

Environment:

- UiPath Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`.
- Folder key `9d7ae568-d60e-4395-94d7-db115bfb25de`.
- UiPath CLI `uip` authenticated as `arshgill6120@gmail.com`.

Gate/wave:

- G-001: Native Case State / Audit Reconstruction.
- G-002: Policy Version Pinning.
- G-004: Agent Recommendation Visible Before Override.
- G-008: CLI/coding-agent lifecycle support.

Assumption tested:

- If native Case history is insufficient and Data Fabric record insert is blocked, a UiPath-accessible Orchestrator storage bucket can hold one `service-recovery-audit-v1` object that reconstructs the domain proof beat without manual log archaeology.

Steps:

1. Listed existing Orchestrator storage buckets for the validation folder.
2. Generated the E-004 contradiction audit bundle artifact.
3. Created storage bucket `service-recovery-audit-validation`.
4. Uploaded `service_recovery_audit_bundle_E004.json` to bucket path `audit/service_recovery_audit_bundle_E004.json`.
5. Listed bucket files and confirmed the uploaded JSON file metadata.
6. Downloaded the same bucket file to `eval_results/downloaded_audit_bundle_E004.json`.
7. Byte-compared the downloaded file against the committed source artifact.
8. Extracted proof-critical fields from the JSON artifact.

Observed:

- Bucket creation succeeded:
  - name: `service-recovery-audit-validation`,
  - bucket key: `dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb`,
  - bucket ID: `177034`.
- Bucket upload succeeded for:
  - path: `audit/service_recovery_audit_bundle_E004.json`,
  - content type: `application/json`,
  - size: `6412` bytes.
- Bucket list returned the uploaded file at `/audit/service_recovery_audit_bundle_E004.json`.
- Bucket download succeeded and `cmp` returned `bucket-download-matches`.
- The artifact SHA-256 is `3d02852775cb8e6a3c3c451553a22c5c5afe38848853f48e9f4f5a506b83a05e`.
- The JSON artifact reconstructs:
  - `audit_contract_version: service-recovery-audit-v1`,
  - raw agent event `AIE-E004` with `recommended_next_stage: closure_candidate`,
  - policy decision event `PDE-E-004` linked to `AIE-E004`,
  - `decision: require_human_review`,
  - `from_recommended_stage: closure_candidate`,
  - `to_stage: human_review`,
  - `block_reason: source_contradiction`,
  - `interpretation_policy_version: ip-v1`,
  - `decision_policy_version: dp-v1`,
  - event order: evidence state, agent interpretation, policy decision, human review.

Result:

- G-001: PARTIAL natively, PASS for custom UiPath-accessible audit artifact fallback. Native Case state still does not by itself provide a clean one-query domain audit, and Data Fabric record storage remains blocked. Orchestrator bucket storage does prove a live UiPath-hosted, downloadable one-object audit artifact for the contradiction proof beat.
- G-002: PASS for explicit artifact-level policy version pinning. The artifact stores both policy versions with the linked events. Native active-case migration semantics remain custom and must be represented by an explicit audited migration event.
- G-004: PASS for artifact persistence of raw recommendation before policy override. The uploaded object preserves separate linked `AgentInterpretationEvent` and `PolicyDecisionEvent` data rather than only final routed state.
- G-008: PASS/PARTIAL. CLI lifecycle now includes bucket create, upload, list, download, and verification. It is a real build-lifecycle operation, not a mock.

Commands run:

- `uip or buckets list --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json`
- `python -m service_recovery_core.evals --audit-bundle-scenario E-004 --output docs/validation/artifacts/2026-06-25/service_recovery_audit_bundle_E004.json`
- `uip or buckets create service-recovery-audit-validation --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --description "Validation audit bundle artifacts for UiPath AgentHack service recovery" --output json`
- `uip or bucket-files upload dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb audit/service_recovery_audit_bundle_E004.json --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --file docs/validation/artifacts/2026-06-25/service_recovery_audit_bundle_E004.json --content-type application/json --output json`
- `uip or bucket-files list dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json`
- `uip or bucket-files download dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb audit/service_recovery_audit_bundle_E004.json --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --destination eval_results/downloaded_audit_bundle_E004.json --output json`
- `cmp -s docs/validation/artifacts/2026-06-25/service_recovery_audit_bundle_E004.json eval_results/downloaded_audit_bundle_E004.json && echo bucket-download-matches`
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`

Evidence:

- `docs/validation/artifacts/2026-06-25/service_recovery_audit_bundle_E004.json`
- `docs/validation/artifacts/2026-06-25/orchestrator_bucket_audit_artifact_E004_manifest.json`
- live bucket key `dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb`
- live bucket path `audit/service_recovery_audit_bundle_E004.json`

Decision impact:

- Use Orchestrator bucket audit artifacts as the current validated fallback for the final audit view if Data Fabric record insertion remains blocked.
- Keep native Case history for runtime lifecycle evidence: package, job, stage/task order, task status, timestamps, and reviewer return.
- Keep the custom audit bundle as the domain audit object that proves evidence state, policy versions, raw agent recommendation, final policy decision, closure block reason, human action, and ordered event chain.

Product feedback:

- No new negative PF entry for buckets. Bucket create/upload/list/download worked cleanly through CLI and should be cited as a positive "what worked well" item.
- PF-019 remains the active blocker for Data Fabric record insertion.

## 2026-06-25 21:28 IST - Action Center E-004 Completed Task UI Recheck

Environment:

- Safari authenticated to UiPath Action Center.
- Org `keepingitlowkey`, tenant `DefaultTenant`.
- Completed task URL: `https://cloud.uipath.com/keepingitlowkey/DefaultTenant/actions_/tasks/4300219`.

Gate/wave:

- G-003: Human Evidence Packet.
- G-004: Agent Recommendation Visible Before Override.

Assumption tested:

- A completed E-004 Action Center task can serve as the final reviewer-visible evidence packet for the contradiction route.

Steps:

1. Used Computer Use to inspect the current Safari Action Center tab.
2. Reloaded the page after a session-timeout overlay.
3. Selected completed task `4300219`, linked to case instance `60e52ca5-6891-45b4-9e98-e1b08a984f06`.
4. Inspected the generated completed-task form.
5. Captured a screenshot.

Observed:

- Action Center recovered after reload and listed completed tasks `4295185`, `4295299`, `4300080`, and `4300219`.
- Task `4300219` opened as `Review service recovery evidence #4300219 (reject)`.
- The completed-task UI showed the reviewer comment:
  - `Wave 07 E-004 validation: generated local eval payload preserved closure_candidate raw recommendation, detected fresh authoritative network telemetry contradiction, and routed to human_review for source_contradiction; reviewer rejects closure and opens investigation.`
- The generated UI still showed `Unable to render image`.
- `Content`, `Evidence Packet Json`, and `Raw Agent Recommendation` labels were visible, but their values were not visible in the completed-task form.
- The policy field still rendered as `Unnamed String 1` / `Unnamed string 1`.

Result:

- G-003: PARTIAL. Action Center is validated for task lifecycle, completion state, reviewer comment visibility, and structured return through APIs/case variables. The generated reviewer UI is not sufficient for final demo evidence-packet legibility.
- G-004: PASS through persisted task/API/audit artifact data, but PARTIAL through generated Action Center UI because the raw/policy proof fields are not readable in the completed-task form.

Decision impact:

- Activate D-009 fallback: use Action Center for human-task mechanics and structured reviewer return, but use the custom evidence-packet/audit-bundle surface for final demo legibility.

Evidence:

- `docs/validation/artifacts/2026-06-25/g003-action-center-e004-completed-generated-ui-empty-fields.png`

Product feedback:

- PF-013 strengthened as a repeated generated Action Center field rendering/binding issue.

## 2026-06-25 23:58 IST - Test Manager Eval Crossover

Environment:

- UiPath org `keepingitlowkey`, tenant `DefaultTenant`.
- UiPath CLI `uip` authenticated as `arshgill6120@gmail.com`.
- Test Manager project created for validation: `Service Recovery Eval Validation`.
- Project key: `SREV`.
- Project ID: `1281f516-2c82-0000-9e76-0b49cf9a9990`.

Gate/wave:

- G-007: Test Cloud / Eval Crossover.

Assumption tested:

- The local E-001 through E-009 eval scenarios can be represented honestly in UiPath Test Manager without claiming unsupported automation.

Steps:

1. Ran `uip login status --output json`.
2. Probed Test Manager CLI surface with `uip tm testcases --help --output json`.
3. Listed existing Test Manager projects with `uip tm project list --output json`.
4. Created project `SREV`.
5. Re-ran the local eval baseline with `python -m service_recovery_core.evals --output eval_results/local_baseline.json`.
6. Created nine Test Manager test cases for E-001 through E-009.
7. Created test set `SREV:9`.
8. Added all nine test cases to `SREV:9`.
9. Read back the project, test cases, test set, and test-set membership.
10. Used Computer Use to inspect the current Safari UiPath tab; it remained on Action Center task `4300219` and confirmed existing G-003 generated UI legibility limitations.

Observed:

- `uip login status` returned `Status: Logged in`, org `keepingitlowkey`, tenant `DefaultTenant`.
- `uip tm testcases --help --output json` returned `Result: Success`, confirming the post-rename `testcases` command surface.
- Initial `uip tm project list --output json` returned an empty `Data` list.
- Project creation succeeded:
  - `ProjectKey: SREV`,
  - `Id: 1281f516-2c82-0000-9e76-0b49cf9a9990`,
  - `Name: Service Recovery Eval Validation`.
- Local eval baseline passed 9/9.
- Test set creation succeeded:
  - `TestSetKey: SREV:9`,
  - `Id: 6881c763-b871-0200-165b-0b49cf9ac490`.
- Test-set membership readback returned all nine scenarios:
  - E-001: `SREV:3`,
  - E-002: `SREV:1`,
  - E-003: `SREV:2`,
  - E-004: `SREV:4`,
  - E-005: `SREV:5`,
  - E-006: `SREV:6`,
  - E-007: `SREV:7`,
  - E-008: `SREV:8`,
  - E-009: `SREV:10`.
- Created test cases are manual Test Manager cases. `IsAutomated` read back as `false` for each case.
- Manual execution creation succeeded:
  - `ExecutionId: d50a7be6-35ed-1100-95aa-0b49cf9b8cad`,
  - `TestSetKey: SREV:9`,
  - initial `Status: Pending`,
  - start time `2026-06-25T18:33:27.985Z`.
- All nine manual test case logs were finished with:
  - `Result: Passed`,
  - `HasError: false`,
  - `ExecutedBy: arshgill6120@gmail.com`,
  - detail link to `docs/validation/TEST_MANAGER_MAPPING.md` at commit `e7b881d`.
- Execution aggregate readback reported:
  - `Passed: 9`,
  - `Failed: 0`,
  - `None: 0`,
  - `ExecutionType: Manual`,
  - `IsRunningAutomated: false`.
- Top-level execution status still read back as `Running`; `uip tm wait --timeout 30` timed out with last status `Running`.

Result:

- G-007: PASS for live UiPath Test Manager representation of E-001 through E-009.
- G-007: PASS/PARTIAL for manual Test Manager execution. The execution contains nine passed manual test case logs, but the aggregate execution status remains `Running`.
- G-007: PARTIAL for automated Test Cloud crossover. The eval suite is represented in Test Manager as manual cases and grouped in a test set, but no automated Test Manager execution or Orchestrator test automation link has been created.

Evidence:

- `docs/validation/TEST_MANAGER_MAPPING.md`.
- Test Manager project `SREV`.
- Test set `SREV:9`.
- Manual execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad`.
- Local eval output `eval_results/local_baseline.json`.

Decision impact:

- It is now fair to select/report Test Cloud/Test Manager participation only as a live Test Manager mapping unless an automated execution is added later.
- Keep the final survey guardrail: do not claim automated Test Cloud validation yet.
- Next G-007 step, if time allows, is to resolve why the manual execution aggregate remains `Running` after all case logs passed, then decide whether to add a real automation link from Test Manager to an Orchestrator test package.

Product feedback:

- PF-020 added for Test Manager eval onboarding: CLI project/case/test-set lifecycle worked, but importing an eval suite from JSON/JUnit-style output still requires custom scripting/manual object creation.
- PF-021 added for manual execution status clarity: all test case logs can pass while the aggregate execution remains `Running` and wait times out.
