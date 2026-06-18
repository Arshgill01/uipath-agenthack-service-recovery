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
