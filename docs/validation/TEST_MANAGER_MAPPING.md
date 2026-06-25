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

Scope:

- This is a live Test Manager representation of the local eval scenarios.
- The test cases are manual Test Manager cases today.
- Automated Test Cloud execution is not claimed yet.
- The source of truth for pass/fail remains:
  - `python -m service_recovery_core.evals --output eval_results/local_baseline.json`

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

Observed:

- Test Manager CLI auth succeeded for org `keepingitlowkey`, tenant `DefaultTenant`.
- Test Manager initially returned an empty project list.
- Project `SREV` was created and read back as active.
- Nine test cases were created and read back.
- Test set `SREV:9` was created and read back.
- `SREV:9` read back with all nine expected test cases attached.

Result:

- G-007: PASS for live Test Manager representation of E-001 through E-009 as manual test cases.
- G-007: PARTIAL for automated Test Cloud crossover because no automated Test Manager execution was created or linked to an Orchestrator test automation.
