# Wave 42 Worker B - Maestro / Action Center / Solution Readiness Probe

Date: 2026-06-29 IST

Worker scope: read-only/live CLI and local artifact probes for Maestro Case, Action Center tasks, and UiPath Solution readiness. No jobs/cases were started, no tasks were completed, and no cloud resources were published/uploaded/deployed by this lane.

## Executive Finding

The current feedback thesis is accurate and should be kept: Maestro Case already has useful validators, task metadata, registry, task lifecycle, process/package, and solution packaging surfaces, but builders still lack a single cross-surface human-review readiness contract that answers whether a Case human-review path will actually run and be audit-ready before runtime.

This probe strengthens the thesis in three places:

- The Action schema and task metadata correctly expose `PolicyDecisionJson`, but the runtime Case tasks still bind to the older Action app deployment. Schema correctness alone does not prove generated Action Center UI readiness.
- The newer `Solution.webApp.SimpleApprovalApp:1.0.1` package is present and latest, but the known post-publish runtime task `4333536` still used app system name `ID5c3f0a11590d4fdab3c22de72f4ff443` / version `1`. A readiness report should show which app deployment/version a Case package will instantiate.
- Local validations disagree by surface: `uip maestro case validate` rejects downloaded/extracted Case `caseplan.json` files as not a known Case Management JSON version, while `uip solution pack --dry-run` proceeds into the solution and fails later on the generated web app with `Activity is valid only inside Trigger Scope`. A readiness report should reconcile Case validation, Solution packaging, and generated app validation into one actionable result.

## Environment

- CLI: `uip --version` -> `1.195.1`
- Login: `uip login status --output json` -> logged in to `https://cloud.uipath.com`, org `keepingitlowkey`, tenant `DefaultTenant`
- Read-only folder/process context:
  - Folder key: `9d7ae568-d60e-4395-94d7-db115bfb25de`
  - Folder id: `7978263`
  - Case process key: `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`
- Known Action tasks inspected:
  - `4300080` for E-002
  - `4300219` for E-004
  - `4333536` for the post-label-publish runtime recheck

## Commands Run

### Auth and CLI surface

```sh
uip --version
uip login status --output json
uip solution init --help --output json
uip maestro case registry --help --output json
uip maestro case processes --help --output json
```

Observed:

- CLI is available as `1.195.1`.
- Login is live for org `keepingitlowkey`, tenant `DefaultTenant`.
- `uip solution init --help` confirms the post-rename `solution init` surface and describes AI-agent briefing files generated for new solutions.
- `uip maestro case registry` exposes `pull`, `list`, `search`, `get`, `get-connector`, and `get-connection`.
- `uip maestro case processes` exposes `list`, `incidents`, `diagnose`, and `error-codes`.

### Case validation and solution dry-run packaging

```sh
uip maestro case validate tmp/uipath-case-packages/extracted-1.0.6/content/caseplan.json --output json
uip maestro case validate "tmp/uipath-downloads/maestro-case-current/Maestro Case/caseplan.json" --output json
uip solution pack tmp/uipath-downloads/maestro-case-current --dry-run --output json
uip solution resource list --solution-folder tmp/uipath-downloads/maestro-case-current --source local --output json
```

Observed:

- Both Case validation commands failed with:
  - `JSON is not a valid Case Management JSON of any known version.`
- The Solution dry-run pack did not stop at that same Case-validation message. It restored/read solution resources and then failed while validating/building `SimpleApprovalApp`:
  - `Activity is valid only inside Trigger Scope`
  - `Solution pack failed: Activity is valid only inside Trigger Scope`
- `uip solution resource list` successfully listed 13 local resources, including multiple `SimpleApprovalApp` app/appVersion/package/process resources, `Maestro Case`, and `Maestro BPMN`.

Interpretation:

- This confirms a real cross-surface readiness gap. The individual surfaces exist, but their results are not normalized into a single builder-facing readiness report that says which part fails and what will happen at upload/pack/runtime.
- It supports PF-009, PF-026, and PF-028.

### Action registry search and version binding

```sh
uip maestro case registry list --output json --output-filter "Resources[?DeploymentTitle=='SimpleApprovalApp' || Name=='SimpleApprovalApp' || contains(Name || '', 'SimpleApprovalApp') || contains(DeploymentTitle || '', 'SimpleApprovalApp')].{Id:Id,Name:Name,ResourceType:ResourceType,DeploymentTitle:DeploymentTitle,SemVersion:SemVersion,SystemName:SystemName,Folder:DeploymentFolder.FullyQualifiedName,DateDeployed:DateDeployed}"
uip maestro case registry search SimpleApprovalApp --output json
uip maestro case registry get e08ea52f-ad42-41db-a6bc-50471bd25511 --output json
uip maestro case registry get 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
uip maestro case tasks describe --type action --id e08ea52f-ad42-41db-a6bc-50471bd25511 --output json
uip maestro case tasks describe --type action --id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
```

Observed:

- Registry list found two `SimpleApprovalApp` deployments:
  - `e08ea52f-ad42-41db-a6bc-50471bd25511`, `SemVersion: 1.0.0`, `SystemName: ID5c3f0a11590d4fdab3c22de72f4ff443`, folder `arshgill6120@gmail.com's workspace/Solution`
  - `9eeb93b2-11d3-4bfb-b7d6-29879226f242`, `SemVersion: 1.0.1`, `SystemName: IDb707cd2abbdd42178b415f7341a65f13`, folder `arshgill6120@gmail.com's workspace/Solution 1`
- `uip maestro case registry search SimpleApprovalApp` returned `ResultCount: 0` even though `registry list` and `registry get` found the matching action apps.
- `registry get` for both IDs returned action-app resources.
- `tasks describe --type action` for both IDs exposed the expected inputs:
  - `Content`
  - `EvidencePacketJson`
  - `RawAgentRecommendation`
  - `PolicyDecisionJson`
  - `Comment`
- `tasks describe --type action` also exposed structured outputs including `Comment`, `Action`, `hitlTask`, and `Error`.

Interpretation:

- PF-006 should remain accurate: the schema/task metadata includes `PolicyDecisionJson`, so the problem is not simply that the field is missing from the action contract.
- PF-013 should remain accurate and be even more precise: runtime generated UI/readiness depends on generated control binding and the Case-bound app deployment/version, not just task schema.
- PF-028 should mention that registry `search` still misses a concrete app discoverable via `list`/`get`.

### Solution resource and package readbacks for Action app versioning

```sh
uip solution resource get e08ea52f-ad42-41db-a6bc-50471bd25511 --solution-folder tmp/uipath-downloads/maestro-case-current --output json
uip solution resource get 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --solution-folder tmp/uipath-downloads/maestro-case-current --output json
uip or packages get Solution.webApp.SimpleApprovalApp:1.0.0 --feed-id 831bf59a-a3f1-4aa8-8890-f01b857c18f3 --output json
uip or packages get Solution.webApp.SimpleApprovalApp:1.0.1 --feed-id 831bf59a-a3f1-4aa8-8890-f01b857c18f3 --output json
```

Observed:

- The downloaded solution resource for `e08...` resolves to:
  - `Name: SimpleApprovalApp_1`
  - `AppSystemName: ID5c3f0a11590d4fdab3c22de72f4ff443`
  - `Version: 1.0.0`
  - `ActionSchema` includes `PolicyDecisionJson`
  - `ResourceOverwrite.ValidationError.Message.Key: ResourceNotFoundInRCS`
- The remote/newer app resource `9eeb...` resolves to:
  - `Name: SimpleApprovalApp`
  - `AppSystemName: IDb707cd2abbdd42178b415f7341a65f13`
  - `ActionSchema` includes `PolicyDecisionJson`
  - dependency package `Solution.webApp.SimpleApprovalApp:1.0.1`
- Package readback confirms:
  - `Solution.webApp.SimpleApprovalApp:1.0.0` exists, active, not latest.
  - `Solution.webApp.SimpleApprovalApp:1.0.1` exists, active, latest.

Interpretation:

- This supports the feedback that builders need a visible binding/version inspector. A newer Action app package can be latest in the feed while the existing Case-bound task path still uses an older app deployment/system name.
- It supports PF-013 and PF-017. It also gives Q11 a concrete pass/fail example: "Case-bound Action app deployment is older than the latest published Action app package."

### Action Center task readbacks

```sh
uip tasks get 4300080 --folder-id 7978263 --output json
uip tasks get 4300219 --folder-id 7978263 --output json
uip tasks get 4333536 --folder-id 7978263 --output json
uip tasks users 7978263 --output json
```

Observed:

- All three tasks read back as `Completed`, `Type: AppTask`, `Action: reject`, with title `Review service recovery evidence`.
- Task `4300080` has `CreatorJobKey: 3af41e1d-8b04-4eba-aa5e-a95c5c673730`.
- Task `4300219` has `CreatorJobKey: 60e52ca5-6891-45b4-9e98-e1b08a984f06`.
- Task `4333536` has `CreatorJobKey: 9eb64f9f-6613-48f7-b452-215085d8c67b`.
- All three completed tasks report `AppTasksMetadata.AppId: ID5c3f0a11590d4fdab3c22de72f4ff443` and `AppVersion: 1`.
- Task `4333536` completed output `Data` contains only the reviewer `Comment`; it does not expose the original `PolicyDecisionJson` input in the same post-completion readback.
- `uip tasks users 7978263` found one assignable user: `arshgill6120@gmail.com` / `Arshdeep Singh`.

Interpretation:

- This confirms Action Center lifecycle and structured reviewer return.
- It preserves the generated UI non-claim: `4333536` still points at the older app system name even though a newer package exists.
- It adds nuance for PF-015/PF-027: after completion, the task endpoint is not a complete one-query domain audit source for the original evidence packet. The custom audit bundle/Data Fabric path remains necessary.

### Case process and instance diagnostics

```sh
uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json
uip maestro case processes diagnose 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case processes list --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case processes incidents 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case processes error-codes 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case instance get 9eb64f9f-6613-48f7-b452-215085d8c67b --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case instance get 60e52ca5-6891-45b4-9e98-e1b08a984f06 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case instance variables-all 9eb64f9f-6613-48f7-b452-215085d8c67b --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json --output-filter "keys(@)"
uip maestro case instance element-executions 9eb64f9f-6613-48f7-b452-215085d8c67b --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
```

Observed:

- `uip or processes get` returns process name `Maestro Case G004 1.0.3 Evidence Validation`, `ProcessVersion: 1.0.6`, and `AutoUpdate: false`; the narrowed readback did not expose folder/package fields.
- `uip maestro case processes diagnose` failed with:
  - `Error diagnosing process`
  - `summaries.find is not a function`
- `uip maestro case processes list --folder-key ...` returned `Data: []` in this session even though `or processes get` and `instance get` could read the known process/instances by key.
- `incidents` and `error-codes` returned empty arrays for the current process key.
- `instance get` for `9eb64...` returned `LatestRunStatus: Completed`, `PackageVersion: 1.0.6`.
- `instance get` for `60e52...` returned `LatestRunStatus: Completed`, `PackageVersion: 1.0.5`.
- `element-executions` for `9eb64...` returned `Data: []`.
- `variables-all` returned a top-level `Variables` key only under the narrow output filter used.

Interpretation:

- PF-026 remains accurate: Case/process diagnostics are not yet reliable enough to serve as a single readiness or post-run audit view.
- The instance readbacks confirm completion/package version, but not enough by themselves for full G-001 domain audit proof.
- Keep the current claim boundary: native Case history/readbacks are partial; Data Fabric V2 and custom audit bundles own the full payload proof.

## PF Confirmation Matrix

| PF | Result | Notes |
| --- | --- | --- |
| PF-006 | Confirmed | `tasks describe --type action` exposes `PolicyDecisionJson`; problem is generated UI/control binding and runtime rendering, not missing action schema. |
| PF-007 | Confirmed by prior evidence; not re-mutated | This lane did not create a missing-title task. Existing evidence remains valid; this probe adds that preflight must include binding/version and post-completion audit behavior too. |
| PF-013 | Strengthened | Runtime task `4333536` used old `AppId`/version while `1.0.1` is latest. Keep generated Action Center UI as non-demo-safe until a fresh task proves stable rendering. |
| PF-017 | Strengthened | Package `1.0.1` exists and is latest, but Case-bound runtime path still used older app deployment. Feed/package visibility is not the same as runtime binding readiness. |
| PF-026 | Confirmed | `processes diagnose` still fails with `summaries.find is not a function`; process list with folder key returned empty while keyed process/instance reads worked. |
| PF-027 | Strengthened | `tasks users` can identify assignable reviewer, but completed task readback does not reconstruct original evidence inputs; readiness should include reviewer eligibility plus audit evidence availability. |
| PF-028 | Strengthened | Registry `search SimpleApprovalApp` returned zero despite `list`/`get` finding two deployments. Case validate and Solution pack dry-run still expose different failure modes. |

## Recommended Feedback Changes

Do not add a broad new claim. Instead, tighten Q10/Q11 with these evidence-backed refinements:

1. In the Action Center/UI binding bullet, say that both `1.0.0` and `1.0.1` action deployments expose `PolicyDecisionJson` in task metadata, but known runtime Case tasks still used the older `AppId`/version. This is stronger than saying only that a label rendered badly.
2. In the readiness-check recommendation, include an explicit pass/fail item: "Case-bound Action app deployment/version matches the intended published Action app, and every schema input has a rendered runtime control with readable label and value."
3. In the audit/readback section, mention that after task completion, `uip tasks get` returns reviewer output/comment and task metadata but not necessarily the original full evidence inputs through the same endpoint. This supports the custom audit bundle/Data Fabric V2 path without overclaiming native task history.
4. In the registry/discovery bullet, keep the existing `registry search` gap: `registry search SimpleApprovalApp` returned zero while `registry list/get` found the action apps.
5. Preserve all existing non-claims:
   - no automated Test Cloud execution claimed,
   - no generated Action Center UI final-demo readiness claimed,
   - no native Case history alone as full G-001 proof,
   - no real telecom OSS/BSS integration,
   - no LLM/Codex runtime closure authority.

## No Product Feedback Docs Edited

Per Worker B scope, this lane did not edit `docs/product/*`. The orchestrator should decide whether to merge the recommended Q10/Q11 refinements into the survey copy.
