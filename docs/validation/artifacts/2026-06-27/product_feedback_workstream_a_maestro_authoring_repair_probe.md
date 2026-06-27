# Product Feedback Workstream A - Maestro Case Human-Review Authoring Repair Probe

Date: 2026-06-27 19:54 IST.

Scope:

- Continue Product Feedback Evidence Workstream A for Maestro Case human-review authoring/readiness.
- Inspect existing scratch solution `PFPROBE-20260627-human-review` without mutating it.
- Create a separate scratch repair solution with the required `PFPROBE-20260627-` prefix.
- Compare readiness signals across Case validation, solution dry-run, Studio Web upload/import, and download/export round trip.

Environment:

- UiPath CLI: `1.195.1`.
- Org: `keepingitlowkey`.
- Tenant: `DefaultTenant`.
- User: `arshgill6120@gmail.com`.
- Browser screenshot: Safari was logged into the UiPath Labs account and loaded the repaired scratch Studio Web designer. After Computer Use system access was enabled, the first-run Case Management modal was dismissed and the unobstructed Case plan canvas was captured. Screenshot artifact: `docs/validation/artifacts/2026-06-27/pfprobe-human-review-repair-studio-safari.png`.

## Existing Scratch Inspection

Commands:

```sh
uip login status --output json
uip solution download d897e886-da98-4e73-6caf-08ded37985a5 -d tmp/product-feedback-probes-existing --extract -n PFPROBE-20260627-human-review-existing --output json
uip solution project list --output json
uip maestro case validate tmp/product-feedback-probes-existing/PFPROBE-20260627-human-review-existing/PFPROBE-20260627-human-review-case/caseplan.json --output json
uip maestro case cases get tmp/product-feedback-probes-existing/PFPROBE-20260627-human-review-existing/PFPROBE-20260627-human-review-case/caseplan.json --output json
uip maestro case stages get tmp/product-feedback-probes-existing/PFPROBE-20260627-human-review-existing/PFPROBE-20260627-human-review-case/caseplan.json Stage_PxZpVH --output json
uip maestro case tasks get tmp/product-feedback-probes-existing/PFPROBE-20260627-human-review-existing/PFPROBE-20260627-human-review-case/caseplan.json Stage_PxZpVH tDE6A9MfL --output json
```

Key observed output:

```json
{
  "Result": "Success",
  "Code": "SolutionDownload",
  "Data": {
    "Status": "Solution exported successfully",
    "SolutionId": "d897e886-da98-4e73-6caf-08ded37985a5",
    "ExtractedTo": ".../tmp/product-feedback-probes-existing/PFPROBE-20260627-human-review-existing"
  }
}
```

```text
Found 4 error(s) and 2 warning(s):
  - [error] [nodes[root]] Case has no completion rules
  - [error] [nodes[Stage_PxZpVH]] A required field is empty in 'PFPROBE Human Review Missing Title'
  - [warning] [nodes[Stage_PxZpVH]] Stage has no entry rules
  - [warning] [nodes[Stage_PxZpVH]] This stage has no completion rules
  - [error] [nodes[Stage_PxZpVH]] Task has no entry rules
  - [error] [(root)] Case has no stage with a Case Entered entry rule
```

Observed:

- The existing scratch Studio Web solution was exportable by CLI and contained one CaseManagement project.
- Exported `caseplan.json` still failed `uip maestro case validate` before runtime with the same missing-rule errors and the generic required-field message.
- `tasks get` for `tDE6A9MfL` showed `EvidencePacketJson`, `RawAgentRecommendation`, and `PolicyDecisionJson` inputs, but did not show a `TaskTitle` value.
- Missing case/stage/task rules are visible before runtime through `uip maestro case validate`.
- Missing Action task Title is only visible before runtime as a generic required-field validation error; the message does not name `Title`.

## New Scratch Repair Path

Scratch resources:

- Local solution: `tmp/product-feedback-probes/PFPROBE-20260627-human-review-repair`.
- Local Case project: `tmp/product-feedback-probes/PFPROBE-20260627-human-review-repair/PFPROBE-20260627-human-review-repair-case`.
- Studio Web solution: `PFPROBE-20260627-human-review-repair`.
- Solution ID: `74018a7a-e09c-43b3-6d15-08ded37985a5`.
- Project ID: `79f8d37b-f33e-42ba-b777-eabde556bc5e`.

Commands:

```sh
uip solution init PFPROBE-20260627-human-review-repair --output json
uip maestro case init PFPROBE-20260627-human-review-repair-case --output json
mkdir -p PFPROBE-20260627-human-review-repair-case/content
uip maestro case cases add --name "PFPROBE-20260627 Human Review Repair Case" --file PFPROBE-20260627-human-review-repair-case/content/caseplan.json --case-app-enabled --description "Scratch human-review repair probe" --output json
uip maestro case stages add PFPROBE-20260627-human-review-repair-case/content/caseplan.json --label "Human Review" --is-required --output json
uip maestro case tasks add PFPROBE-20260627-human-review-repair-case/content/caseplan.json Stage_SCER4c --type action --display-name "PFPROBE Human Review Missing Title" --task-type-id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --recipient arshgill6120@gmail.com --output json
uip maestro case validate PFPROBE-20260627-human-review-repair-case/content/caseplan.json --output json
uip maestro case stage-entry-conditions add PFPROBE-20260627-human-review-repair-case/content/caseplan.json Stage_SCER4c --display-name "Case entered" --rule-type case-entered --output json
uip maestro case tasks remove PFPROBE-20260627-human-review-repair-case/content/caseplan.json Stage_SCER4c tvWLIAj8L --output json
uip maestro case tasks add PFPROBE-20260627-human-review-repair-case/content/caseplan.json Stage_SCER4c --type action --display-name "PFPROBE Human Review With Title" --task-type-id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --recipient arshgill6120@gmail.com --task-title "PFPROBE Human Review Evidence" --output json
uip maestro case task-entry-conditions add PFPROBE-20260627-human-review-repair-case/content/caseplan.json Stage_SCER4c tzLMka9e1 --display-name "Stage entered" --rule-type current-stage-entered --output json
uip maestro case stage-exit-conditions add PFPROBE-20260627-human-review-repair-case/content/caseplan.json Stage_SCER4c --display-name "Required tasks complete" --type exit-only --marks-stage-complete true --rule-type required-tasks-completed --output json
uip maestro case case-exit-conditions add PFPROBE-20260627-human-review-repair-case/content/caseplan.json --display-name "Required stages complete" --marks-case-complete true --rule-type required-stages-completed --output json
uip maestro case validate PFPROBE-20260627-human-review-repair-case/content/caseplan.json --output json
uip maestro case tasks update PFPROBE-20260627-human-review-repair-case/content/caseplan.json Stage_SCER4c tzLMka9e1 --is-required --output json
uip maestro case validate PFPROBE-20260627-human-review-repair-case/content/caseplan.json --output json
uip solution resource refresh --solution-folder tmp/product-feedback-probes/PFPROBE-20260627-human-review-repair --output json
uip solution pack tmp/product-feedback-probes/PFPROBE-20260627-human-review-repair --dry-run --output json
uip solution upload tmp/product-feedback-probes/PFPROBE-20260627-human-review-repair --output json
uip solution download 74018a7a-e09c-43b3-6d15-08ded37985a5 -d tmp/product-feedback-probes-repair-export --extract -n PFPROBE-20260627-human-review-repair-export --output json
uip maestro case validate tmp/product-feedback-probes-repair-export/PFPROBE-20260627-human-review-repair-export/PFPROBE-20260627-human-review-repair-case/caseplan.json --output json
```

Key observed output:

```text
Found 4 error(s) and 2 warning(s):
  - [error] [nodes[root]] Case has no completion rules
  - [error] [nodes[Stage_SCER4c]] A required field is empty in 'PFPROBE Human Review Missing Title'
  - [warning] [nodes[Stage_SCER4c]] Stage has no entry rules
  - [warning] [nodes[Stage_SCER4c]] This stage has no completion rules
  - [error] [nodes[Stage_SCER4c]] Task has no entry rules
  - [error] [(root)] Case has no stage with a Case Entered entry rule
```

```text
Found 1 error(s) and 0 warning(s):
  - [error] [nodes[Stage_SCER4c]] Stage exit rule 'Required tasks complete' has no task(s) marked as required
```

```json
{
  "Result": "Success",
  "Code": "CaseValidate",
  "Data": {
    "Status": "Valid"
  }
}
```

```json
{
  "Result": "Success",
  "Code": "TaskFound",
  "Data": {
    "Task": {
      "DisplayName": "PFPROBE Human Review With Title",
      "Type": "action",
      "Data": {
        "TaskTitle": "PFPROBE Human Review Evidence"
      },
      "IsRequired": true
    }
  }
}
```

```json
{
  "Result": "Success",
  "Code": "SolutionPack",
  "Data": {
    "Package": "PFPROBE-20260627-human-review-repair@1.0.0",
    "DryRun": true,
    "Status": "Valid"
  }
}
```

```json
{
  "Result": "Success",
  "Code": "SolutionUpload",
  "Data": {
    "Status": "Uploaded successfully",
    "SolutionId": "74018a7a-e09c-43b3-6d15-08ded37985a5",
    "DesignerUrl": "https://cloud.uipath.com/keepingitlowkey/studio_/designer/79f8d37b-f33e-42ba-b777-eabde556bc5e?solutionId=74018a7a-e09c-43b3-6d15-08ded37985a5"
  }
}
```

Observed:

- The repair path for a missing Action task title is not an in-place `tasks update`; `tasks update --help` does not expose `--task-title`.
- The least-mutating CLI repair found in this run was remove/re-add the Action task with `--task-title`, then set requiredness and add rules.
- `uip maestro case validate` gave the strongest readiness signal. It caught the invalid baseline, narrowed the remaining issue after the first repair pass, and returned `Status: Valid` after requiredness was added.
- `uip solution pack --dry-run` returned `Status: Valid` for the repaired scratch, matching Case validation in the repaired case but not distinguishing the earlier invalid scratch from upload/import readiness.
- `uip solution upload` returned `Uploaded successfully` and `ErrorList: []` for the repaired scratch, just as it had for the invalid scratch.
- The uploaded repaired solution round-tripped through `uip solution download --extract` and still passed `uip maestro case validate`.

Result:

- PASS for evidence gathering.
- PASS for creating a separate scratch repair solution with `PFPROBE-20260627-` prefix.
- PASS for a local repair path that makes the scratch Case pass `uip maestro case validate`.
- PARTIAL for Studio Web designer validation/readiness: CLI upload/import accepted both invalid and valid scratch definitions. Safari loaded the repaired scratch designer and the screenshot shows the repaired Case plan canvas with Trigger 1, the Human Review stage, and the repaired human-review task. This proves Studio Web could open the repaired scratch, but no separate Studio Web readiness/preflight warning surface was observed.

Decision impact:

- Strengthens PF-028 rather than creating a new product-feedback class.
- The product feedback recommendation should explicitly ask for one shared Maestro Case human-review preflight used by Case validate, solution dry-run, and Studio Web upload/import.
- The recommendation should also ask for an in-place Action task `Title` repair affordance or field-specific guidance when `TaskTitle` is missing.
- This probe does not change submission guardrails: no automated Test Cloud execution is claimed, generated Action Center UI is still not treated as final-demo ready, native Case history alone is not claimed for G-001, and no submission process/package/case/task/Data Fabric/Test Manager baseline object was mutated.
