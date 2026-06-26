# Action Center Generated UI Repair Assessment

Date: 2026-06-26

Purpose: determine whether PF-013 can be repaired safely from the repository artifacts, or whether the final demo should continue using the custom evidence packet as the judge-readable surface.

## Current Finding

The generated Action Center page is not safely repairable from committed repository source today.

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

Do not spend more submission-critical time trying to repair the generated Action Center page from local package artifacts unless one of these becomes available:

- an editable Studio Web/Coded App source path with explicit control binding support,
- a documented `uip` command that updates generated Action app field bindings,
- enough time to repair in Studio UI and re-run a fresh live Action Center task end to end.

Keep PF-013 as product feedback and keep the custom evidence packet as the final proof surface.

## Product Feedback Implication

PF-013 is stronger after this inspection:

- the schema is correct,
- backend/task payload persistence is correct,
- generated UI naming/binding loses the proof-critical display name,
- the downloadable package does not expose an obvious safe source-level repair path.

Suggested product improvement: generated Action app artifacts should include a field-binding inspector and repair path that maps every action schema field to its rendered control name, binding expression, runtime visibility, and validation status.
