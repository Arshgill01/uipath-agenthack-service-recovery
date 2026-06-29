# Wave 42 Worker A Claim Audit

Date: 2026-06-29.

Scope: strict read-only audit of the strongest product-feedback claims against live CLI readbacks and existing artifacts. No live cases were started, no tasks were completed, and no UiPath tenant resources were created, updated, or deleted.

Environment:

- Repository: `/Users/arshdeepsingh/Developer/uipath-agenthack-service-recovery`
- UiPath CLI: `1.195.1`
- Auth readback: `Logged in`
- Org: `keepingitlowkey`
- Tenant: `DefaultTenant`
- User/session: `arshgill6120@gmail.com`

## Commands Run

```sh
uip --version
uip login status --output json
uip tasks get 4300080 --output json
uip tasks get 4300219 --output json
uip tasks get 4333536 --output json
uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json
uip or processes version-history 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json
uip or packages get Solution.caseManagement.Maestro.Case:1.0.4 --output json
uip or packages get Solution.caseManagement.Maestro.Case:1.0.4 --feed-id 831bf59a-a3f1-4aa8-8890-f01b857c18f3 --output json
uip df entities list --native-only --output json
uip df records get 35e8f6c7-4671-f111-ac9a-002248a16d28 F9D838CE-4671-F111-AC9A-0022489A9A06 --output json
uip df records get 328ef8b6-ab70-f111-ac9a-002248a16d28 DA42769C-33B7-4701-A266-019F032AF376 --output json
uip tm testcases --help --output json
uip tm project list --filter SREV --output json
uip tm testsets list --project-key SREV --include-last-execution --output json
uip tm executions get-stats --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --output json
uip tm report get --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --output json
uip or folders list --output json
uip tm testcases list-automations --project-key SREV --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip or packages get ServiceRecoveryEvalProcessProbe:0.0.3 --output json
uip or packages get ServiceRecoveryEvalProcessProbe:0.0.2 --output json
uip maestro case instance get 3af41e1d-8b04-4eba-aa5e-a95c5c673730 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case instance get 60e52ca5-6891-45b4-9e98-e1b08a984f06 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case instance get 9eb64f9f-6613-48f7-b452-215085d8c67b --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case instance get 9fc6fece-55ed-4fb2-b11a-6c96f7a3314e --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case processes diagnose 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case registry list --output json
uip maestro case registry get e08ea52f-ad42-41db-a6bc-50471bd25511 --output json
uip maestro case registry get 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
uip maestro case tasks describe --type action --id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
uip tasks users 7978263 --output json
uip tools list --output json
uip is connectors list --output json
```

## Claim Matrix

| Claim / PF IDs | Command or artifact checked | Observed result | Status | Exact wording change if needed |
| --- | --- | --- | --- | --- |
| PF-003: Actions/Action Center was not initially enabled and needed a clearer readiness path. | Existing screenshots in `docs/validation/artifacts/2026-06-24/`; `uip tasks users 7978263 --output json`; `uip tasks get ...`; `uip tools list --output json`. | Current task APIs and user listing work, and `tasks-tool` is installed. The original not-enabled state is historical artifact-backed, not reproducible now because Actions has been enabled. | Confirm as historical/resolved setup feedback. | Keep wording as "was not enabled at first" and "later enabled"; do not imply the tenant is still blocked. |
| PF-006/PF-013: Action app schema included proof-critical fields, but generated/runtime UI binding was not reliable. | `uip maestro case tasks describe --type action --id 9eeb...`; `uip tasks get 4333536`; existing `ACTION_CENTER_UI_REPAIR_ASSESSMENT.md` and `product_feedback_action_binding_probe.md`. | `tasks describe` still exposes `Content`, `EvidencePacketJson`, `RawAgentRecommendation`, `PolicyDecisionJson`, and `Comment`. Runtime task `4333536` still shows `AppId: ID5c...`, `AppVersion: 1`, and the reviewer comment says the generated runtime UI still rendered `Unnamed String 1`. Completed task readback today no longer exposes proof-critical input fields beyond reviewer comment/metadata. | Confirm core issue; downgrade any broad "task API currently returns all policy fields on completed tasks" wording. | Say "the schema and task-creation/readback artifacts preserved the fields, and the custom/Data Fabric proof surfaces preserve them durably; completed task readback today mainly exposes lifecycle/comment metadata." |
| PF-007: Missing Action task `Title` passed too late and failed at runtime. | Existing incident screenshot and `product_feedback_phase2_scratch_case_probe.md`; no new mutation. | Existing scratch probe shows `tasks add` allowed an Action task without `--task-title`; `case validate` found "A required field is empty" but did not name `Title`; solution dry-run/upload accepted the invalid scratch solution. | Confirm from artifact, not freshly rerun. | Keep as artifact-backed. Prefer "required field such as Title" over "the validator never catches Title"; Case validate caught a generic required-field issue but packaging/upload did not enforce the same readiness contract. |
| PF-015/G-001: Native Case history alone is not full domain audit; Data Fabric V2/custom audit path supplies full payload proof. | `uip df records get 35e8... F9D838...`; `uip maestro case instance get 9fc6...`; artifact audit bundle. | V2 record returns first-class fields for E-004: `CaseId CASE-BG-CONTRA`, `ScenarioId E-004`, `DerivedEvidenceState contradicting`, `ClosureBlockReason source_contradiction`, policy versions, source case/task, package `1.0.6`, and non-empty AIE/PDE/audit JSON lengths. Raw JSON readback includes `closure_candidate`, `require_human_review`, and `source_contradiction`. | Confirm. | No weakening needed. Continue saying native Case is partial and Data Fabric V2/custom audit is the full-payload path. |
| PF-017: Package/feed/process binding diagnostics were inconsistent. | `uip or packages get Solution.caseManagement.Maestro.Case:1.0.4` with and without feed; `uip or processes get`; `version-history`. | Default package lookup returns `HTTP 404: Package not found`; the same version succeeds with feed `831bf59a...`. Process `9a7e...` now reads `ProcessVersion: 1.0.6`, `AutoUpdate: false`, and version history shows `1.0.3` through `1.0.6`. | Confirm. | No weakening needed. Keep "requires feed-aware readback and version-history verification." |
| PF-019/PF-023: Legacy snake_case Data Fabric path was unreliable; PascalCase V2 is validated. | `uip df entities list --native-only`; `uip df records get` for V2 and legacy IDs. | Entity list confirms both schemas. V2 record reads back full custom fields and payloads. Legacy record lookup with corrected entity ID now returns `Record not found`, not the older "system-fields-only" behavior. | Confirm V2; downgrade live-current legacy claim. | Say "legacy snake_case behavior was observed in earlier artifacts; current live readback no longer finds that legacy record. Do not use legacy path as current proof." |
| PF-020/PF-021: Test Manager manual eval representation is terminal with 9/9 passed. | `uip tm project list`; `testsets list`; `executions get-stats`; `report get`. | Project `SREV` exists; test set `SREV:9` last status `Finished`; execution `40a1...` has `Passed: 9`, `Failed: 0`, `None: 0`, `Status: Finished`, `ExecutionType: Manual`, `IsRunningAutomated: false`, 100% report pass rate. | Confirm strongly. | No weakening needed. Keep explicit "manual Test Manager execution, not automated Test Cloud." |
| PF-024: Automated Test Cloud execution is not proven; automation discovery/linking remains unclaimed. | `uip tm testcases --help`; `uip or packages get ServiceRecoveryEvalProcessProbe:0.0.2/0.0.3`; `uip tm testcases list-automations --folder-key 9d7ae...`. | CLI exposes automation-link/run commands; probe packages are Orchestrator-visible as inactive process packages; automation discovery against the Solution folder returned HTTP 400 `Internal Server Error`. No automated execution was run. | Confirm non-claim; strengthen diagnostics evidence. | Say "automated Test Cloud execution remains unclaimed; a read-only automation discovery probe returned a generic internal error rather than a linkable automation target." |
| PF-026: Case process diagnostics are insufficient for human-review readiness. | `uip maestro case processes diagnose 9a7e...`; existing `product_feedback_readiness_probe.md`. | Fresh diagnose still fails with `UnknownError`, `Error diagnosing process`, `summaries.find is not a function` for the current process. | Confirm strongly. | No weakening needed. This is current live evidence. |
| PF-027: Reviewer readiness discovery is split across surfaces. | `uip tasks users 7978263`; `uip tools list`; existing readiness probe. | Correct positional `tasks users 7978263` returns reviewer user `Arshdeep` / username `arshgill6120@gmail.com`; tool list shows `tasks-tool`; no single readiness command connects services, folder, reviewer, Action app binding, and package version. | Confirm. | No weakening needed. Keep as "needs cross-surface readiness report," not "no individual readiness data exists." |
| PF-028: Case validate, solution dry-run, and Studio Web upload did not share one readiness contract for scratch human-review Case. | `product_feedback_phase2_scratch_case_probe.md`; no new mutation. | Existing scratch probe shows `case validate` failed, `solution pack --dry-run` reported valid, and `solution upload` succeeded for the same invalid scratch human-review solution. | Confirm from artifact, not freshly rerun. | No weakening needed, but keep "scratch probe" context. |
| Current completion status of older E-002/E-004 cases. | `uip maestro case instance get 3af41e...`; `uip maestro case instance get 60e52...`; `uip tasks get 4300080`; `uip tasks get 4300219`. | E-002 and E-004 instances now read `LatestRunStatus: Completed`; tasks are completed AppTasks with `reject` comments. | Upgrade old caution. | Any remaining "do not claim terminal completion for older E-002/E-004 jobs while they still read Running" should be revised to "fresh 2026-06-29 readback shows these case instances completed; still avoid native-history-alone audit claims." |
| Optional external evidence / Integration Service context. | `uip is connectors list --output json`. | Integration Service connector catalog is accessible and returns connectors. No real telecom OSS/BSS connection was probed or claimed. | Confirm boundary. | Keep saying synthetic telecom systems; optional external Google Sheet evidence is an external evidence-source simulator, not real telecom integration. |

## Recommended Product Feedback Copy Adjustments

1. Keep the primary Q11 Human-Review Readiness Check thesis. The live readbacks support it.
2. In Q10/Q12, avoid saying completed `uip tasks get` always returns the full proof-critical input payload. More precise wording: "Task schema and prior task/artifact readbacks preserved the fields, while completed task readback now mainly proves lifecycle/comment metadata; Data Fabric V2/custom packets are the durable full-payload proof."
3. Update stale caution language that older E-002/E-004 case instances were still running. Fresh `uip maestro case instance get` readbacks show `LatestRunStatus: Completed` for `3af41e1d-8b04-4eba-aa5e-a95c5c673730` and `60e52ca5-6891-45b4-9e98-e1b08a984f06`.
4. Keep the legacy Data Fabric snake_case issue as historical/product-feedback evidence, but do not imply the specific legacy record is still readable today. The V2 record remains the final proof path.
5. Strengthen PF-024 wording slightly: the current read-only Test Manager automation discovery probe returned a generic HTTP 400/internal-error response, while Orchestrator package readback still sees the probe package. This supports the "automation discovery diagnostics" feedback and preserves the automated Test Cloud non-claim.

## Bottom Line

The feedback copy is broadly accurate and appropriately cautious. The strongest live-confirmed claims are Data Fabric V2 audit readback, Test Manager manual execution, package/feed/process readback, Case diagnose failure, Action task lifecycle, reviewer availability, and the absence of automated Test Cloud proof. The only meaningful wording downgrades are around completed Action task payload visibility and current readability of the legacy Data Fabric record.
