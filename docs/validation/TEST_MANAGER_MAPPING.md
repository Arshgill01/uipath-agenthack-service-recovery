# Test Manager Eval Mapping

This file records the live UiPath Test Manager representation of the local service-recovery eval suite.

## 2026-06-25 23:58 IST - Live Mapping

Environment:

- UiPath org: `keepingitlowkey`
- Tenant: `DefaultTenant`
- Test Manager project: `Service Recovery Eval Validation`
- Project key: `SREV`
- Project ID: `1281f516-2c82-0000-9e76-0b49cf9a9990`
- Test set: `Service Recovery E-001 through E-009 Baseline`
- Test set key: `SREV:9`
- Test set ID: `6881c763-b871-0200-165b-0b49cf9ac490`
- Initial manual execution ID: `d50a7be6-35ed-1100-95aa-0b49cf9b8cad`
- Terminal manual execution ID: `40a1b334-5df8-1100-0a4b-0b49d0564f11`

Scope:

- This is a live Test Manager representation of the local eval scenarios.
- The test cases are manual Test Manager cases today.
- Automated Test Cloud execution is not claimed yet.
- The source of truth for pass/fail remains:
  - `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- Latest Test Manager manual evidence is terminal execution `40a1b334-5df8-1100-0a4b-0b49d0564f11`, which reached `Status: Finished` with 9/9 passed logs.

## Scenario Mapping

| Eval | Test Manager key | Test case ID | Expected policy outcome |
| --- | --- | --- | --- |
| E-001 | `SREV:3` | `a219914a-fdf8-0a00-6bb1-0b49cf9aa802` | Fresh aligned telemetry allows `closure_candidate`; policy accepts recommendation. |
| E-002 | `SREV:1` | `ee12563e-fbf8-0a00-2871-0b49cf9aa7f4` | Missing authoritative telemetry overrides `closure_candidate` to `verify_telemetry`. |
| E-003 | `SREV:2` | `6d62f1b1-fcf8-0a00-61c0-0b49cf9aa7ff` | Stale authoritative telemetry overrides `closure_candidate` to `verify_telemetry`. |
| E-004 | `SREV:4` | `a6c525ac-fef8-0a00-6ae2-0b49cf9aa805` | Fresh authoritative contradiction requires `human_review` with elevated severity. |
| E-005 | `SREV:5` | `ab0b0937-fff8-0a00-e67d-0b49cf9abc79` | High-impact exception remains out of closure and routes to `dispatch_followup`. |
| E-006 | `SREV:6` | `0b8206a1-00f9-0a00-7910-0b49cf9abc7e` | Missing signal blocks closure while already in `verify_telemetry`. |
| E-007 | `SREV:7` | `c7f17b11-01f9-0a00-287e-0b49cf9abcbc` | Invalid agent output is overridden and routed to `verify_telemetry`. |
| E-008 | `SREV:8` | `a20fe8f8-02f9-0a00-ec41-0b49cf9abce1` | Low confidence blocks closure and records a usefulness incident. |
| E-009 | `SREV:10` | `ac219460-03f9-0a00-9bff-0b49cf9ac487` | Raw `closure_candidate` recommendation persists separately from policy override to `verify_telemetry`. |

## Readback Evidence

Commands used:

- `uip login status --output json`
- `uip tm testcases --help --output json`
- `uip tm project list --output json`
- `uip tm project create --name "Service Recovery Eval Validation" --project-key SREV --description "AgentHack service-recovery eval mapping for E-001 through E-009; validation-scoped project created by Codex on 2026-06-25." --output json`
- `uip tm testcases create --project-key SREV ... --output json`
- `uip tm testsets create --project-key SREV --name "Service Recovery E-001 through E-009 Baseline" --description "Manual Test Manager representation of local eval suite. Automation linkage is not yet claimed; source of truth remains python -m service_recovery_core.evals." --output json`
- `uip tm testcases add --test-set-key SREV:9 --test-case-keys SREV:1,SREV:2,SREV:3,SREV:4,SREV:5,SREV:6,SREV:7,SREV:8,SREV:10 --output json`
- `uip tm project list --filter SREV --output json`
- `uip tm testcases list --project-key SREV --output json`
- `uip tm testsets list --project-key SREV --include-last-execution --output json`
- `uip tm testsets list-testcases --project-key SREV --test-set-key SREV:9 --output json`
- `uip tm testsets run --test-set-key SREV:9 --execution-type manual --output json`
- `uip tm testcaselog finish --project-key SREV --execution-id d50a7be6-35ed-1100-95aa-0b49cf9b8cad --test-case-id ... --result Passed --has-error false --executed-by arshgill6120@gmail.com --detail-link https://github.com/Arshgill01/uipath-agenthack-service-recovery/blob/e7b881d/docs/validation/TEST_MANAGER_MAPPING.md --run-id 1 --is-post-condition-met true --output json`
- `uip tm executions list --project-key SREV --output json`
- `uip tm executions testcaselogs list --project-key SREV --execution-id d50a7be6-35ed-1100-95aa-0b49cf9b8cad --output json`
- `uip tm wait --project-key SREV --execution-id d50a7be6-35ed-1100-95aa-0b49cf9b8cad --timeout 30 --output json`

Observed:

- Test Manager CLI auth succeeded for org `keepingitlowkey`, tenant `DefaultTenant`.
- Test Manager initially returned an empty project list.
- Project `SREV` was created and read back as active.
- Nine test cases were created and read back.
- Test set `SREV:9` was created and read back.
- `SREV:9` read back with all nine expected test cases attached.
- Manual execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad` was created for test set `SREV:9`.
- All nine manual test case logs were marked `Passed` with `has-error: false`, executor `arshgill6120@gmail.com`, and detail link back to this mapping artifact.
- Execution aggregate readback reported `Passed: 9`, `Failed: 0`, `None: 0`, `ExecutionType: Manual`, and `IsRunningAutomated: false`.
- The same aggregate readback still reported top-level `Status: Running`; `uip tm wait --timeout 30` timed out with last status `Running`.

Result:

- G-007: PASS for live Test Manager representation of E-001 through E-009 as manual test cases.
- G-007: PASS/PARTIAL for manual Test Manager execution: all nine test case logs are passed, but the top-level execution status remains `Running`.
- G-007: PARTIAL for automated Test Cloud crossover because no automated Test Manager execution was created or linked to an Orchestrator test automation.

## 2026-06-26 15:50 UTC - Terminal Manual Execution Rerun

Purpose:

- Resolve whether the non-terminal aggregate status was a hard Test Manager limitation or a lifecycle issue in the first manual execution.

Commands used:

- `uip tm testsets run --test-set-key SREV:9 --execution-type manual --output json`
- `uip tm testcaselog start --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --test-case-id ... --run-id 1 --output json`
- `uip tm testcaselog finish --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --test-case-id ... --result Passed --has-error false --executed-by arshgill6120@gmail.com --detail-link https://github.com/Arshgill01/uipath-agenthack-service-recovery/blob/master/docs/validation/TEST_MANAGER_MAPPING.md --run-id 1 --is-post-condition-met true --output json`
- `uip tm executions get-stats --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --output json`
- `uip tm wait --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --timeout 10 --output json`
- `uip tm report get --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --output json`
- `uip tm result download --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --result-path docs/validation/artifacts/test-manager-results --output json`

Observed:

- Fresh manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` was created for test set `SREV:9`.
- Each manual test case log was explicitly started and then finished as passed.
- Execution aggregate readback reported `Passed: 9`, `Failed: 0`, `None: 0`, `ExecutionType: Manual`, `IsRunningAutomated: false`, and `Status: Finished`.
- `uip tm wait` returned `WaitComplete` with terminal status `Finished`.
- `uip tm report get` returned `TotalTests: 9`, `Passed: 9`, `Failed: 0`, `PassRate: 100`.
- `uip tm result download` wrote JUnit XML to `docs/validation/artifacts/test-manager-results/Service_Recovery_E_001_through_E_009_Baseline___20260626_1017.xml`.
- CLI telemetry/AppInsights flush warnings appeared during several commands but did not prevent Test Manager operations from succeeding.

Result:

- G-007: PASS for manual Test Manager representation and terminal manual execution/report/export.
- G-007: PARTIAL only for automated Test Cloud crossover because no automated Test Manager execution or Orchestrator test automation link has been created.
- PF-021 remains useful feedback because direct `finish` calls can create passed child logs while leaving the aggregate execution `Running`; the verified workaround is to call `testcaselog start` before `testcaselog finish` for each manual case.

## 2026-06-26 16:33 UTC - Automated Execution Feasibility Probe

Purpose:

- Work the remaining automated Test Cloud/Test Manager blocker instead of leaving it as an untried caveat.

Commands used:

- `uip login status --output json`
- `uip tm testcases --help --output json`
- `uip tm testcases link-automation --help --output json`
- `uip tm testcases run --help --output json`
- `uip or folders list --output json`
- `uip or processes list --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json`
- `uip or processes list --folder-key 555d3f16-a106-4946-a934-4bede4789be7 --output json`
- `uip or packages list --search Test --output json`
- `uip or packages list --search Solution --output json`
- `uip tm testcases list-automations --project-key SREV --folder-key 555d3f16-a106-4946-a934-4bede4789be7 --output json`
- `uip tm testcases list-automations --project-key SREV --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json`
- `uip tm testcases list-automations --project-key SREV --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --package-name Solution --output json`
- `uip tm testcases list-automations --project-key SREV --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --package-name Test --output json`

Observed:

- CLI auth remained valid for org `keepingitlowkey`, tenant `DefaultTenant`.
- `uip tm testcases link-automation` and `uip tm testcases run --execution-type automated` are supported CLI surfaces.
- Shared folder `555d3f16-a106-4946-a934-4bede4789be7` had no processes and `list-automations` returned an empty list.
- Solution folder `9d7ae568-d60e-4395-94d7-db115bfb25de` had Case/BPMN/WebApp processes, but no obvious test automation process.
- Default package-feed searches for `Test` and `Solution` returned zero packages.
- `list-automations` against the Solution folder returned HTTP 400 with `Internal Server Error` both unfiltered and filtered by `Solution`/`Test`.

Result:

- G-007 remains PASS for terminal manual Test Manager representation/execution/report/JUnit export.
- G-007 remains PARTIAL for automated Test Cloud execution. This was actively probed, not ignored: the tenant/folder evidence does not expose a ready test automation target to link and run.
- Product feedback PF-024 was added for opaque automation discovery failure in a Solution folder.

## 2026-06-26 14:55 UTC - Automated Execution Follow-Up

Purpose:

- Test whether the automated execution blocker is only missing folder assignment or also missing linked automation/package selection.

Commands used:

- `uip tm testsets run --test-set-key SREV:9 --execution-type automated --wait --timeout 90 --poll-interval 15 --output json`
- `uip tm project set-default-folder --project-key SREV --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json`
- `uip tm project set-default-folder --project-key SREV --folder-key 555d3f16-a106-4946-a934-4bede4789be7 --output json`
- `uip tm testsets run --test-set-key SREV:9 --execution-type automated --wait --timeout 90 --poll-interval 15 --output json`

Observed:

- Automated `SREV:9` run without folder assignment failed with `Please assign a folder to the test set or at the project level to start the execution.`
- `uip tm testsets update --help` exposes name/description only, so the CLI did not provide a test-set folder-binding path.
- Setting the project default folder to the `Solution` folder failed with HTTP 500 `Internal Server Error`.
- Setting the project default folder to Standard `Shared` succeeded.
- Automated `SREV:9` run after the Shared default folder assignment failed with `No Automatic package selection could be done for test set to execute.`

Result:

- G-007 automated execution remains PARTIAL and should not be claimed.
- The blocker is now better bounded: folder assignment is required, Standard `Shared` can satisfy that prerequisite, but the test set still lacks a discoverable/linked automation package.
- The `SREV` project default folder is currently set to Standard `Shared` as the only folder assignment path that succeeded through the CLI.
