# Product Feedback Phase 2 Scratch Case Probe

Date: 2026-06-27

Scope:

- Run one deeper scratch UiPath product probe.
- Preserve existing submission resources.
- Use prefix `PFPROBE-20260627-` for created resources.

Environment:

- UiPath CLI: `1.195.1`.
- Org: `keepingitlowkey`.
- Tenant: `DefaultTenant`.
- User: `arshgill6120@gmail.com`.

Scratch artifacts:

- Local solution folder: `tmp/product-feedback-probes/PFPROBE-20260627-human-review`.
- Local Case project: `tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case`.
- Studio Web scratch solution: `PFPROBE-20260627-human-review`.
- Studio Web solution ID: `d897e886-da98-4e73-6caf-08ded37985a5`.
- Studio Web project ID: `c577c2db-ec94-4ec6-86b0-2c65c6b15393`.
- Studio Web designer URL returned by CLI: `https://cloud.uipath.com/keepingitlowkey/studio_/designer/c577c2db-ec94-4ec6-86b0-2c65c6b15393?solutionId=d897e886-da98-4e73-6caf-08ded37985a5`.

Commands and observations:

1. Confirmed auth:

   ```sh
   uip login status --output json
   ```

   Observed authenticated Labs context for org `keepingitlowkey`, tenant `DefaultTenant`.

2. Checked scratch namespace and pulled registry metadata:

   ```sh
   uip maestro case registry pull --output json
   uip maestro case registry search PFPROBE --output json
   uip maestro case registry search SimpleApprovalApp --output json
   ```

   Observed `registry pull` loaded 2291 nodes and 2 action apps. Search for `PFPROBE` returned 0, as expected. Search for `SimpleApprovalApp` returned 0 even though the pulled `action-apps-index.json` contained `SimpleApprovalApp` entries.

3. Created scratch solution and Case project:

   ```sh
   cd tmp/product-feedback-probes
   uip solution init PFPROBE-20260627-human-review --output json
   cd PFPROBE-20260627-human-review
   uip maestro case init PFPROBE-20260627-human-review-case --output json
   ```

   Observed local solution and Case project creation. The generated `entry-points.json` referenced `/content/caseplan.json.bpmn#trigger_1`, but no `content/caseplan.json` existed yet.

4. Tried validating and adding a task before creating the missing Case definition:

   ```sh
   uip maestro case validate tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case/content/caseplan.json --output json
   uip maestro case tasks add tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case/content/caseplan.json Stage_1 --type action --display-name "PFPROBE Human Review Missing Title" --task-type-id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --recipient arshgill6120@gmail.com --output json
   ```

   Both commands failed because `content/caseplan.json` was absent. This is a new-builder scaffold/discovery issue rather than a submission blocker.

5. Created the missing scratch Case definition and required stage:

   ```sh
   mkdir -p tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case/content
   uip maestro case cases add --name "PFPROBE-20260627 Human Review Case" --file tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case/content/caseplan.json --case-app-enabled --description "Scratch human-review readiness probe" --output json
   uip maestro case stages add tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case/content/caseplan.json --label "Human Review" --is-required --output json
   ```

   Observed Case ID `case-MFZe3pKuV9`, trigger ID `trigger_1`, and stage ID `Stage_PxZpVH`.

6. Added a scratch Action task without a task title:

   ```sh
   uip maestro case tasks add tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case/content/caseplan.json Stage_PxZpVH --type action --display-name "PFPROBE Human Review Missing Title" --task-type-id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --recipient arshgill6120@gmail.com --output json
   ```

   Observed success and task ID `tDE6A9MfL`. The command allowed an Action task without `--task-title`.

7. Inspected concrete Action app schema:

   ```sh
   uip maestro case tasks describe --type action --id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
   ```

   Observed input fields `Content`, `EvidencePacketJson`, `RawAgentRecommendation`, `PolicyDecisionJson`, and `Comment`; outputs included `Comment`, `Action`, `hitlTask`, and `Error`.

8. Validated the scratch Case:

   ```sh
   uip maestro case validate tmp/product-feedback-probes/PFPROBE-20260627-human-review/PFPROBE-20260627-human-review-case/content/caseplan.json --output json
   ```

   Observed validation failure with 4 errors and 2 warnings:

   - `Case has no completion rules`
   - `A required field is empty in 'PFPROBE Human Review Missing Title'`
   - `Stage has no entry rules`
   - `This stage has no completion rules`
   - `Task has no entry rules`
   - `Case has no stage with a Case Entered entry rule`

   The required-field error did not name `Title`.

9. Checked task update affordances:

   ```sh
   uip maestro case tasks update --help
   ```

   Observed update flags for display name, name, folder path, run-once behavior, description, and requiredness, but no visible `--task-title` repair flag.

10. Ran solution resource refresh and dry-run pack:

   ```sh
   uip solution resource refresh --solution-folder tmp/product-feedback-probes/PFPROBE-20260627-human-review --output json
   uip solution pack tmp/product-feedback-probes/PFPROBE-20260627-human-review --dry-run --output json
   ```

   Observed resource refresh success and `uip solution pack --dry-run` returning `Status: Valid`, despite the Case-level validation failure above.

11. Uploaded the scratch solution:

   ```sh
   uip solution upload tmp/product-feedback-probes/PFPROBE-20260627-human-review --output json
   ```

   Observed `Uploaded successfully`, `ErrorList: []`, and Studio Web designer URL for scratch solution `PFPROBE-20260627-human-review`.

Result:

- PASS for one deeper scratch product probe.
- A scratch local Case solution and scratch Studio Web solution were created using the required prefix.
- No existing submission resources were modified.
- New product feedback signal: Case-level validation, solution dry-run packaging, and Studio Web upload/import did not share one consistent readiness/preflight contract for a human-review Case with missing required Action task title and missing rules.

Decision impact:

- Strengthens the primary Best Product Feedback recommendation: add a Maestro Case human-review readiness/preflight path that runs before deployment/upload and names exact required fields, app bindings, reviewer readiness, and rule gaps.
- Does not change demo validation claims. Generated Action Center UI remains non-final for the judge proof surface, automated Test Cloud execution remains unclaimed, and existing submission resources remain untouched.
