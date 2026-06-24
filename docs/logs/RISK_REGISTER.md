# Risk Register

| ID | Risk | Impact | Likelihood | Mitigation | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R-001 | Maestro Case native state/history is insufficient for audit reconstruction. | High | Medium | Validate early; use Data Fabric/Data Service or custom audit events if needed. | Platform spike agent | Open |
| R-002 | Policy version pinning is not natively supported. | Medium | High | Store policy versions as explicit case metadata and audit migration events. | Platform spike agent | Open |
| R-003 | Action Center cannot render evidence packet clearly. | Medium | Medium | Use Case App/custom evidence-packet view. | UX/build agent | Open |
| R-004 | Raw agent recommendation cannot be shown before policy override. | High | Medium | Persist agent interpretation event separately from policy decision event. | Architecture/build agent | Open |
| R-005 | Test Cloud integration is too heavy for the build timeline. | Medium | Medium | Use a lightweight eval harness and document Test Cloud mapping; integrate if feasible. | Eval agent | Open |
| R-006 | Agent outputs invalid/low-confidence too often. | High | Medium | Add eval scenarios, schema validation, usefulness incident, and governed improvement loop. | Agent/eval agent | Open |
| R-007 | Demo becomes too complex for five minutes. | High | Medium | Keep demo to 2A, 2B, unstructured-route change, eval artifact, business metrics. | Demo agent | Open |
| R-008 | Platform access/lab readiness blocks build. | High | Medium | Validate access before code; keep local simulation path. | Platform spike agent | Open |

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
