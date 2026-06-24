# Build Log

Append one entry per substantial agent run.

## Template

### YYYY-MM-DD HH:MM - Agent / Wave

What changed:

- ...

Commands run:

- `...`

Validation:

- PASS / FAIL / PARTIAL

Product feedback:

- PF-XXX / none

Open risks:

- ...

Next:

- ...

## 2026-06-18 - Scaffolding Setup

What changed:

- Created initial repository scaffolding documents.
- Added operating rules, project brief, high-level plan, research log, decision log, architecture/validation/doc directories, local skills directory, and wave plan skeleton.

Commands run:

- See final report for this run.

Validation:

- Pending final structure scan.

Open risks:

- UiPath Labs platform assumptions remain unvalidated.

### 2026-06-18 20:10 IST - Agent / Waves 07-14, 22

What changed:

- Selected dependency-free Python local core stack.
- Added package foundation, `.env.example`, JSON eval fixtures, schema validators, agent output validator, deterministic reconciliation/closure policy, local case state machine, and eval runner.
- Added unit tests for evidence/case schemas, invalid agent outputs, canonical business-green fixture discipline, closure blocking, distinct missing/stale vs contradiction routes, event persistence, and eval baseline.
- Represented E-008 usefulness degradation as an eval incident and E-009 override persistence as linked agent/policy events.

Commands run:

- `python -m unittest`
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- `python -m pip install -e .`
- `python -m pip install .`
- `python -m compileall service_recovery_core tests`

Validation:

- PASS: `python -m pip install .`
- PASS: `python -m compileall service_recovery_core tests`
- PASS: `python -m unittest discover -s tests` ran 16 tests.
- PASS: `python -m service_recovery_core.evals --output eval_results/local_baseline.json` passed 9/9 eval scenarios.
- PARTIAL: `python -m unittest` ran 0 tests because explicit discovery is required.
- FAIL: `python -m pip install -e .` failed in this Python 3.9/older pip environment because editable install invoked a Python environment without `pip`; non-editable local install passed.

Open risks:

- UiPath Labs hard gates G-001 through G-004 remain unvalidated.
- Local case state machine and audit events are provisional and not yet mapped to Maestro Case native state/history.
- Test Cloud integration is not implemented; the eval harness is local and portable.

Next:

- Do not start UiPath implementation waves until Labs access is granted and hard gates are run or explicitly waived.

### 2026-06-24 14:16 IST - Agent / Wave 01

What changed:

- Re-ran local repo validation before platform access work.
- Installed and verified the UiPath CLI package.
- Attempted UiPath Automation Cloud access through controlled Chromium and Safari without handling credentials.
- Recorded Wave 01 as partial because login reached `portal_/missingaccount` rather than an accessible tenant.

Commands run:

- `git status --short --branch`
- `git log --oneline -5`
- `git remote -v`
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- `command -v uip && uip --version`
- `npm view @uipath/cli version bin --json`
- `node --version && npm --version`
- `npm install -g @uipath/cli@1.196.0`
- `uip --version`
- `agent-browser --session-name uipath-labs open https://cloud.uipath.com`
- `agent-browser --session-name uipath-labs --headed open https://cloud.uipath.com`
- `open -na Safari https://cloud.uipath.com`
- `osascript -e 'tell application "Safari" to if (count of windows) > 0 then return URL of current tab of front window & "\n" & name of current tab of front window'`
- `uip login`

Validation:

- PASS: `python -m unittest discover -s tests` ran 16 tests.
- PASS: `python -m service_recovery_core.evals --output eval_results/local_baseline.json` passed 9/9 eval scenarios.
- PASS: `uip --version` returned `1.196.0` after installing `@uipath/cli@1.196.0`.
- PARTIAL: Wave 01 local/CLI inventory completed, but UiPath product-surface inventory could not be completed.
- NOT RUN: G-001 through G-004 because Automation Cloud access landed at `portal_/missingaccount`.

Open risks:

- UiPath Labs account/tenant access is not usable yet for validation.
- Maestro, Maestro Case, Studio Web, Action Center, Test Cloud/Test Manager, Integration Service, and Orchestrator access remain unconfirmed.

Next:

- Resolve UiPath Labs org/tenant assignment for the logged-in Google account.
- Re-run Wave 01 inventory after Automation Cloud opens inside an accessible tenant.
- Continue with G-001 only after Maestro Case access is confirmed.

### 2026-06-24 20:30 IST - Agent / Wave 01 Rerun, G-001/G-003 Stop

What changed:

- Re-ran local validation and UiPath Labs access inventory using Safari and the authorized Google account.
- Confirmed Automation Cloud org `keepingitlowkey`, tenant `DefaultTenant`, user `Arshdeep Singh`.
- Confirmed Maestro, Studio Web, Maestro Case project creation, Orchestrator presence, Data Fabric listing, Integration Service listing, Test Manager listing, Agents listing, and CLI availability.
- Captured screenshots under `docs/validation/artifacts/2026-06-24/`.
- Added product feedback entries PF-002 and PF-003.
- Documented Actions / Action Center as not enabled for the tenant.

Commands run:

- `git status --short --branch`
- `git log --oneline -5`
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- `command -v uip && uip --version && git remote -v`
- `uip --help`
- `uip skills --help`
- `screencapture -x docs/validation/artifacts/2026-06-24/...`

Validation:

- PASS: `python -m unittest discover -s tests` ran 16 tests.
- PASS: `python -m service_recovery_core.evals --output eval_results/local_baseline.json` passed 9/9 eval scenarios.
- PARTIAL/PASS: Wave 01 access inventory now confirms Automation Cloud, Maestro, Studio Web, Maestro Case project creation, and product launcher surfaces.
- PARTIAL: G-001/G-002/G-004 are not fully run because no live case instance/audit reconstruction was executed.
- BLOCKED/PARTIAL: G-003 through Action Center because Actions is not enabled for `DefaultTenant`.

Product feedback:

- PF-002
- PF-003

Open risks:

- Actions / Action Center service enablement blocks Action Center evidence-packet validation.
- Native audit reconstruction remains unproven until a live case instance runs.
- Test Manager is visible but has no accessible projects yet.

Next:

- Decide whether to request Actions enablement or use Case App/custom evidence packet.
- Run a minimal live Maestro Case instance through at least two stages before broad implementation.

### 2026-06-24 20:33 IST - Agent / Actions Blocker Investigation

What changed:

- Investigated the `Actions is not enabled for this tenant` blocker.
- Confirmed official UiPath docs say Actions is enabled from `Admin > Tenants > Edit Services > Actions > Save`.
- Confirmed `uip` CLI authentication works for `arshgill6120@gmail.com`.
- Confirmed CLI exposes tenant license management but not tenant service enablement.
- Attempted Admin/Tenants UI inspection; Safari automation did not render a usable tenants table.
- Updated validation results and PF-003 with the blocker root cause and next action.

Commands run:

- `uip user --output json`
- `uip user --help`
- `uip platform --help`
- `uip platform tenants --help`
- `uip platform tenants list --output json`
- `uip platform tenants licenses --help`
- `uip platform licenses --help`
- `uip platform tenants licenses get --help`
- `uip config --help`

Validation:

- PASS: CLI auth confirmed current user `arshgill6120@gmail.com`.
- PARTIAL: blocker root cause narrowed to tenant service enablement.
- BLOCKED: no service change made; Admin/Tenants UI was not usable through Safari automation and enabling services requires explicit approval.

Product feedback:

- PF-003

Open risks:

- Actions remains disabled for `DefaultTenant`.
- Admin/Tenants page may have a rendering or automation-accessibility issue in Safari.

Next:

- If the user approves and the Admin UI becomes usable, enable Actions from `Admin > Tenants > DefaultTenant > Edit Services`.
- Otherwise send a support/hackathon request asking UiPath to enable Actions for org `keepingitlowkey`, tenant `DefaultTenant`, citing session ID `32e450e2-89ca-4a80-a0c9-16df19a3d6b4`.

### 2026-06-24 21:08 IST - Agent / Actions Enabled

What changed:

- Used Admin `DefaultTenant > Services > Add services` after explicit user approval.
- Selected only `Actions` and added it to the tenant.
- Verified the direct Actions route now opens as `Inbox - Action Center`.
- Captured before/after screenshots for the service list and Action Center inbox.

Commands run:

- `screencapture -x docs/validation/artifacts/2026-06-24/actions-admin-services-list.png`
- `screencapture -x docs/validation/artifacts/2026-06-24/actions-enabled-inbox.png`

Validation:

- PASS: Actions service availability is unblocked for `keepingitlowkey / DefaultTenant`.
- PARTIAL: G-003 still requires a real human review task with structured evidence packet and structured return.

Product feedback:

- PF-003

Open risks:

- Action Center rendering quality and structured return behavior remain unvalidated.
- Live Maestro Case audit reconstruction is still unproven.

Next:

- Create or trigger a minimal human review task and validate G-003 evidence-packet requirements.

### 2026-06-24 21:40 IST - Agent / Zen Case Designer Checkpoint

What changed:

- Verified Action Center in the logged-in Zen/cmux browser session.
- Opened Studio Web solution `Maestro BPMN` in Zen.
- Added/opened a real `Maestro Case` project and `Case plan`.
- Captured Case JSON/code-view metadata and observed Case task types.
- Identified the current G-003 friction: `Human action` appears in the task picker, but did not activate through click/Return/accessibility in this session.

Commands run:

- `git status --short --branch`
- `git log --oneline -3`
- `git ls-remote --heads origin master`
- `screencapture -x docs/validation/artifacts/2026-06-24/actions-enabled-inbox-zen.png`
- `screencapture -x docs/validation/artifacts/2026-06-24/g001-maestro-case-json-code-view.png`

Validation:

- PASS: repository is clean and `origin/master` points to `f9388b6`.
- PASS: Action Center opens in Zen as `Inbox - Action Center`.
- PARTIAL: Maestro Case design surfaces are confirmed, but no live case instance has run.
- PARTIAL: G-003 remains unproven because no real human action task/evidence packet was created.

Product feedback:

- PF-004

Open risks:

- Runtime audit reconstruction remains unproven.
- Active-case policy version pinning remains unproven.
- Action Center evidence-packet rendering remains unproven.
- The Case task picker may require a manual gesture, different browser interaction, or undocumented setup.

Next:

- Add a minimal human action task to the Case plan.
- Publish/debug the smallest case instance.
- Inspect case history/state and Action Center task rendering before implementing broader flows.

### 2026-06-25 01:11 IST - Agent / G-003 Human Action Placeholder

What changed:

- Reopened the real Maestro Case plan in Zen.
- Inserted `Human action (placeholder)` under `Stage 1` through `Add first task > Human action > Human action placeholder`.
- Confirmed Case JSON/code view remains available and exposes case metadata, but did not save any JSON edits.
- Captured a canvas screenshot showing the inserted placeholder task.

Commands run:

- `git status --short --branch`
- `rg -n "2026-06-24|G-003|PF-004|Current status|hard gates|Action Center|Human action" ...`
- `screencapture -x docs/validation/artifacts/2026-06-25/g003-human-action-placeholder-canvas.png`

Validation:

- PARTIAL: G-003 now has a real Human action placeholder inserted in Studio Web.
- NOT PASS: evidence-packet fields, reviewer outcomes, and structured return to the case have not been validated.
- SAFETY: an accidental malformed JSON editor text entry was discarded; `Save` was disabled and no malformed JSON was saved.

Product feedback:

- PF-004 updated.

Open risks:

- Action Center rendering quality and structured return behavior remain unvalidated.
- Task-level Human action configuration did not surface clearly from selecting the placeholder in this observation.
- Runtime case execution/publish/debug remains unvalidated.

Next:

- Use `Create new Action app` or the supported task configuration path to build a minimal evidence packet.
- Publish/debug the smallest case instance and inspect Action Center plus case history.
