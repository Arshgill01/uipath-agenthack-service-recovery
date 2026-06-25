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
