# Action Center Generated UI Repair Assessment

Date: 2026-06-26

Purpose: determine whether PF-013 can be repaired safely from the repository artifacts, or whether the final demo should continue using the custom evidence packet as the judge-readable surface.

## Current Finding

The generated Action Center page is not safely repairable from committed repository source today, and the latest label-only Studio Web repair did not propagate to the Case-bound runtime task.

The Studio Web designer exposes the broken generated label and its `Text` property. A label-only repair was applied and published as `SimpleApprovalApp` version `1.0.1`; the Studio preview showed `Policy Decision Json:` instead of `Unnamed String 1:`. A fresh package `1.0.6` Case Instance then created task `4333536`, and Action Center runtime still rendered `Unnamed String 1:` / `Unnamed string 1` even though `uip tasks get` returned a correct `PolicyDecisionJson` payload.

Use Action Center for lifecycle, assignment, completion, reviewer comment, and structured return. Use the custom evidence packet/Data Fabric/bucket audit surfaces for judge-readable proof.

## Evidence Inspected

Downloaded UiPath app package paths:

- `tmp/uipath-downloads/maestro-case-current/SimpleApprovalApp/`
- `tmp/uipath-downloads/maestro-case-pack-experiment/SimpleApprovalApp/`

Relevant files:

- `tmp/uipath-downloads/maestro-case-current/SimpleApprovalApp/project.uiproj`
- `tmp/uipath-downloads/maestro-case-current/SimpleApprovalApp/.app/schemas/schema-5e4cfd91-d8f9-46f7-83da-fdb3572e6ece.json`
- `tmp/uipath-downloads/maestro-case-current/SimpleApprovalApp/.app/models/models-IDeb3af66806404a4eaa3b9049014bb4d0.json`
- `tmp/uipath-downloads/maestro-case-current/SimpleApprovalApp/.app/*.dll`

## Observed Structure

`project.uiproj` identifies `SimpleApprovalApp` as a `WebApp`, not a checked-in coded app source tree.

The Action schema includes the expected input fields:

- `Content`
- `EvidencePacketJson`
- `RawAgentRecommendation`
- `PolicyDecisionJson`

The generated form model includes visible controls for:

- `Content`
- `EvidencePacketJson`
- `RawAgentRecommendation`
- `UnnamedString1`

The downloaded app also contains compiled form assemblies such as:

- `Apps.form.FeedbackSubmissionPagePage.gwg341SrS3gg.dll`
- `Apps.form.FeedbackSubmissionPagePage.Expressions.hlA749gmHN19twwd2tYmHr2.dll`

## Interpretation

The proof-critical field is present in the Action schema and task payload contract, but the generated form control is named `UnnamedString1` instead of `PolicyDecisionJson`.

This matches live Action Center observations:

- task APIs preserved `PolicyDecisionJson`,
- the generated runtime page rendered the policy field as `Unnamed String 1`,
- completed-task UI repeated blank/unreadable proof fields.

Because the reviewer page is represented by generated model JSON plus compiled DLL artifacts rather than a clear checked-in app source file, a repo-only patch would be speculative and unvalidated.

## Decision

Do not spend more submission-critical time trying to repair the generated Action Center page from local package artifacts or label-only Studio edits unless one of these becomes available:

- an editable Studio Web/Coded App source path with explicit control binding support,
- a documented `uip` command that updates generated Action app field bindings,
- a documented way to bind the republished app version back into the Case package/process,
- enough time to repair field binding, republish/repackage, and re-run a fresh live Action Center task end to end.

Keep PF-013 as product feedback and keep the custom evidence packet as the final proof surface.

## Product Feedback Implication

PF-013 is stronger after this inspection:

- the schema is correct,
- backend/task payload persistence is correct,
- generated UI naming/binding loses the proof-critical display name,
- the downloadable package does not expose an obvious safe source-level repair path.

Suggested product improvement: generated Action app artifacts should include a field-binding inspector and repair path that maps every action schema field to its rendered control name, binding expression, runtime visibility, and validation status.

## Follow-Up Repair Probes

### 2026-06-26 16:55 UTC - Coded App CLI / Studio Web Pull Probe

Assumption tested:

- The generated `SimpleApprovalApp` might still be retrievable as editable coded-app source through `uip codedapp pull`, allowing a source-level repair of the `PolicyDecisionJson` binding.

Commands and observations:

- `uip codedapp --help --output json` showed `init`, `push`, `pull`, `pack`, `publish`, and `deploy` surfaces.
- `uip codedapp build --help --output json` returned `unknown command 'build'`; build remains a project-local npm concern for coded apps, not a `uip` subcommand.
- `uip codedapp pull --help --output json` confirmed pull requires a Studio Web `--project-id`.
- `tmp/uipath-downloads/maestro-case-pack-experiment/SolutionStorage.json` identifies `SimpleApprovalApp` project ID `986ee0c8-915c-4569-8df9-a74b454589a9`.
- `uip codedapp pull --project-id 986ee0c8-915c-4569-8df9-a74b454589a9 --target-dir tmp/uipath-codedapp-pull-simpleapproval --verbose --output json` failed with: `The project you are pulling is not supported. Only Studio Web coded app projects can be pulled. Please check that you have the correct project ID.`

Interpretation:

- `SimpleApprovalApp` is a generated Studio Web app/action app artifact, not a supported coded-app source project for the current `uip codedapp pull` path.
- A source-level CLI repair is not available from the current project shape.

### 2026-06-26 16:58 UTC - Safari Dashboard Probe

Assumption tested:

- The existing logged-in Safari session might expose a direct, low-risk route from Automation Cloud home to the `SimpleApprovalApp` designer.

Observed:

- Safari is authenticated on `cloud.uipath.com/keepingitlowkey/portal_/home`.
- The Automation Cloud home page lists `SimpleApprovalApp` under `Automations > Draft projects in Studio Web`.
- The same page also shows the historical Test Manager recent execution as `Running`, while the validated terminal run is documented through CLI/JUnit evidence.
- Clicking the `SimpleApprovalApp` accessibility node from this dashboard state did not navigate to an editable designer during this pass.

Interpretation:

- Browser access is available, but this snapshot did not expose a deterministic edit/publish/revalidate route for repairing the generated Action Center UI.
- Starting manual UI edits without a clear publish and fresh task validation path would risk stale/unverifiable changes.

Updated decision:

- Keep generated Action Center UI repair as an honest remaining partial.
- Do not attempt speculative local model/DLL edits.
- Continue using custom evidence packet plus Data Fabric V2/bucket audit proof as the final judge-readable path.

### 2026-06-26 17:25 UTC - Safari Studio Designer Repair And Publish Probe

Assumption tested:

- The logged-in Safari session might expose the generated Action app designer and allow direct repair of the `Unnamed String 1` label.

Observed:

- Safari is authenticated on the Studio Web designer URL for `SimpleApprovalApp` project `986ee0c8-915c-4569-8df9-a74b454589a9`.
- The page title is `SimpleApprovalApp - Main.xaml - UiPath Studio`.
- The app preview visibly contains:
  - `Content:`
  - `Evidence Packet Json:`
  - `Raw Agent Recommendation:`
  - `Unnamed String 1:`
  - `Comment`
  - `Approve` / `Reject`
- Selecting `Unnamed String 1:` opens the properties panel for `Label - Label4`.
- The properties panel exposes a `Text` property with value `"Unnamed String 1:"`.
- The same designer still shows the July 22 local UiPath Assistant migration prompt for RPA/app editing and debugging.
- Initial macOS `osascript` input was blocked, but Computer Use keyboard actions were then used to edit the expression.
- `Label4.Text` was changed from `"Unnamed String 1:"` to `"Policy Decision Json:"`.
- The stale duplicate expression editor was canceled so it did not revert the saved value.
- The Studio preview updated and now shows `Policy Decision Json:` in the policy-field position.
- Publishing was started from the visible `Publish` control.
- The publish dialog used default personal workspace scope with version `1.0.1`.
- Studio reported `Published v1.0.1`, `arshgill6120@gmail.com's workspace`, and snackbar text `Solution package created and deployed Package name: Solution ver. 1.0.1`.
- Change history now shows `Published v1.0.1` with a `View package` link.

Interpretation:

- PF-013 is more precise now: the generated app is not pullable as coded-app source through CLI, but Studio Web can expose and repair the broken label at design time.
- A label-only repair improves Studio preview legibility, but it is not enough to claim G-003/G-004 generated Action Center UI PASS until a fresh task proves the corrected label and policy decision value render correctly in Action Center after publish/deploy.

Updated decision:

- Keep generated Action Center UI legibility as PARTIAL/FAILED for the proof-critical policy field after runtime revalidation.
- Do not treat label-only Studio Web edits as sufficient. The next feasible repair would need to prove a deeper field binding/version propagation path, then start another fresh Case/AppTask.
- Keep the custom evidence packet as the judge-facing surface.

### 2026-06-26 14:40 UTC - Fresh Runtime Recheck After Publish

Assumption tested:

- A fresh Case/AppTask after the `SimpleApprovalApp` version `1.0.1` publish might render the corrected `Policy Decision Json:` label and the policy decision value.

Commands and observations:

- `uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json` returned `ProcessVersion: 1.0.6` and `AutoUpdate: false`.
- `uip or jobs start 9A7EB300-7B16-4856-B14F-D6F2DA3DBE61 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --jobs-count 1 --reference action-label-runtime-recheck-1-0-6-20260626 --output json` created Case Instance/job `9eb64f9f-6613-48f7-b452-215085d8c67b`.
- `uip tasks list --folder-id 7978263 --output-filter "[?CreatorJobKey=='9eb64f9f-6613-48f7-b452-215085d8c67b']"` found task `4333536`.
- `uip tasks get 4333536 --folder-id 7978263 --output json` returned correct `Data.PolicyDecisionJson` with `decision: require_human_review`, `from_recommended_stage: closure_candidate`, `to_stage: human_review`, `links_to: AIE-E004`, and `block_reason: source_contradiction`.
- Safari Action Center runtime for task `4333536` rendered `Unnamed String 1:` and value `Unnamed string 1`, not `Policy Decision Json:` and not the policy decision JSON.
- The task was completed with `reject`; Case Instance `9eb64f9f-6613-48f7-b452-215085d8c67b` later read back `LatestRunStatus: Completed`.

Interpretation:

- The Studio Web preview/publish improved the designer view only, or did not update the Case-bound runtime app version used by this package/process path.
- The proof-critical data is still preserved in APIs and audit artifacts; the generated Action Center runtime remains unsuitable as the final judge-readable surface.
