# Validation Results

UiPath Labs hard gate validation is in progress. Wave 01 access inventory is mostly complete; hard gates G-001 through G-004 remain PARTIAL until a real Maestro Case instance proves runtime audit, policy pinning, evidence packet, and override visibility behavior.

Use [VALIDATION_GATES.md](VALIDATION_GATES.md) for pass/fail criteria.

Until hard gates G-001 through G-004 are answered, the data model and UiPath integration map remain provisional.

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
