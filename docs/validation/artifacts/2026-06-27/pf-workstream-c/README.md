# Product Feedback Workstream C Probe

Date: 2026-06-27.

Scope: read-only Test Manager / Test Cloud eval-import and automation-discovery diagnostics for product-feedback evidence.

Environment:

- UiPath CLI: `1.195.1`
- Org: `keepingitlowkey`
- Tenant: `DefaultTenant`
- User: `arshgill6120@gmail.com`

Guardrails observed:

- Existing `SREV` project/test set/cases were inspected read-only only.
- No Test Manager object, package, process, case, or tenant setting was created, updated, linked, run, or deleted.
- No automated Test Cloud execution is claimed.
- Scratch `PFPROBE-20260627-` Test Manager resources were not needed because the read-only probes answered the assigned queue.

Key observations:

- `SREV:9` still reads back with latest execution status `Finished` at `2026-06-26T10:19:58.490Z`.
- `uip tm executions list` still shows the older direct-finish execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad` as `Running` with 9 passed logs, while terminal execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` is `Finished` with 9 passed logs.
- The local CLI surface exposes manual object creation, requirement export, result download, attachment download, and automation linking/discovery commands, but no CLI import command for local eval JSON/JUnit into Test Manager cases/test sets.
- Official Test Manager documentation exposes UI import flows for manual test cases from Excel and Orchestrator test sets from Orchestrator, but this probe found no documented direct import path for this repo's local eval JSON/JUnit output into Test Manager cases/test sets.
- `uip or packages list --search ServiceRecoveryEvalProcessProbe` shows package `ServiceRecoveryEvalProcessProbe:0.0.3` as latest, `PackageType: Process`, and `IsActive: false`.
- `uip tm testcases list-automations` against Standard `Shared` returns `Data: []`, including when filtered to `ServiceRecoveryEvalProcessProbe`.
- `--log-level debug` shows CLI/tool loading and project resolution, but no reason why the package is not Test Manager-visible.
- `uip or processes list --folder-key Shared` returns no processes. A guessed `--search` option failed; `uip or processes list --help` shows the correct filter is `--name`.

Command artifact index:

- `01-login-status.txt`: authenticated org/tenant readback.
- `02` through `08`: Test Manager SREV project, test set, execution, stats, and log readback.
- `09` through `15`: Test Manager command-surface import/export/result/attachment help.
- `16` through `18`: Orchestrator folder/package readback.
- `19` through `21`: Test Manager automation discovery/link/run help.
- `22` through `27`: automation discovery and process diagnostic readback.
- `28` through `30`: package/process CLI diagnostic shape checks.

Result:

- Product feedback PF-020, PF-021, and PF-024 are strengthened with fresh 2026-06-27 read-only evidence.
- No new PF ID was created because the observations are repeat sightings of existing issue classes.
