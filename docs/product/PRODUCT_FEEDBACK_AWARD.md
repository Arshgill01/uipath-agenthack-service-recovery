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
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-24 21:40 IST Zen Session Maestro Case Designer Checkpoint.
- Commands/logs: see `docs/validation/VALIDATION_RESULTS.md`, 2026-06-25 01:11 IST G-003 Human Action Placeholder Inserted.

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
