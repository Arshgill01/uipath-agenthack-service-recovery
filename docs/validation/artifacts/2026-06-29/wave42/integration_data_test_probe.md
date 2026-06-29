# Wave 42 Worker C - Integration Service / Data Fabric / Test Manager Probe

Date: 2026-06-29  
Worker: C  
Scope: read-only UiPath CLI research for Integration Service, Data Fabric, and Test Manager feedback evidence.

## Objective

Run strict read-only commands against the live UiPath tenant to verify whether existing feedback claims around Data Fabric, Test Manager, and Integration Service are accurate, need downgrading, or should be extended.

## Environment

- CLI: `uip --version` -> `1.195.1`.
- Auth: `uip login status --output json` returned `Logged in`.
- Org: `keepingitlowkey`.
- Tenant: `DefaultTenant`.
- User context: existing CLI session; no new login, connection, entity, record, test case, or execution was created.

## Summary Verdict

Existing product-feedback boundaries are accurate.

- PF-018 should remain framed as historical/improved: `uip tools list` now shows `data-fabric-tool`, `integrationservice-tool`, and `test-manager-tool`.
- PF-019/PF-023 remain accurate: PascalCase Data Fabric V2 is valid proof storage; legacy snake_case records remain feedback evidence only.
- PF-020/PF-021 remain accurate: Test Manager has a terminal manual execution with 9/9 passed logs, and the older execution still shows the manual-lifecycle ambiguity.
- PF-024 remains accurate: no automated Test Cloud execution is proven; automation discovery still returns no Shared-folder automations and an opaque Solution-folder HTTP 400.
- Integration Service can discover Google Sheets and HTTP connector/activity/resource surfaces, but no connections exist. This supports optional future integration work only; it does not justify claiming a real external integration in the submission.

## Commands And Observations

### CLI Tool Discovery

Commands:

```sh
uip --version
uip login status --output json
uip tools list --output json
uip tools search data --output json
uip tools search test --output json
uip tools search integration --output json
```

Observed:

- `uip --version` returned `1.195.1`.
- Login status returned `Logged in` for org `keepingitlowkey`, tenant `DefaultTenant`.
- `uip tools list` included:
  - `data-fabric-tool` version `1.195.0`, prefix `df`.
  - `integrationservice-tool` version `1.195.0`, prefix `is`.
  - `test-manager-tool` version `1.195.0`, prefix `tm`.
- `uip tools search data/test/integration` returned newer available `1.196.0` versions and `1.197.0-preview.59`.

Feedback impact:

- Confirms PF-018 as improved/resolved on current CLI. Do not describe Data Fabric CLI discovery as a current blocker.

### Data Fabric Entity And Record Readback

Commands:

```sh
uip df entities list --native-only --output json --output-filter "[?Name=='ServiceRecoveryAuditBundle' || Name=='ServiceRecoveryAuditBundleV2'].{Name:Name,Id:Id,RecordCount:RecordCount,FieldNames:Fields[].Name}"
uip df entities get 35e8f6c7-4671-f111-ac9a-002248a16d28 --output json --output-filter "{Name:Name,Id:Id,Fields:Fields[].{Name:Name,Type:FieldDataType.Name,Required:IsRequired,System:IsSystemField}}"
uip df entities get 328ef8b6-ab70-f111-ac9a-002248a16d28 --output json --output-filter "{Name:Name,Id:Id,Fields:Fields[].{Name:Name,Type:FieldDataType.Name,Required:IsRequired,System:IsSystemField}}"
uip df records get 35e8f6c7-4671-f111-ac9a-002248a16d28 F9D838CE-4671-F111-AC9A-0022489A9A06 --output json
uip df records get 328ef8b6-ab70-f111-ac9a-002248a16d28 DA42769C-33B7-4701-A266-019F032AF376 --output json
uip df records query 35e8f6c7-4671-f111-ac9a-002248a16d28 --body '{"selectedFields":["CaseId","ScenarioId","DerivedEvidenceState","ClosureBlockReason","PackageVersion","AuditBundleJson"],"filterGroup":{"logicalOperator":0,"queryFilters":[{"fieldName":"CaseId","operator":"=","value":"CASE-BG-CONTRA"}]}}' --limit 5 --output json
uip df records query 328ef8b6-ab70-f111-ac9a-002248a16d28 --body '{"selectedFields":["Id","case_id","scenario_id"],"filterGroup":{"logicalOperator":0,"queryFilters":[{"fieldName":"Id","operator":"=","value":"DA42769C-33B7-4701-A266-019F032AF376"}]}}' --limit 5 --output json
```

Observed:

- Current native entity IDs:
  - `ServiceRecoveryAuditBundle`: `328ef8b6-ab70-f111-ac9a-002248a16d28`, `RecordCount: 30`.
  - `ServiceRecoveryAuditBundleV2`: `35e8f6c7-4671-f111-ac9a-002248a16d28`, `RecordCount: 1`.
- `ServiceRecoveryAuditBundleV2` has PascalCase custom fields including `CaseId`, `ScenarioId`, `DerivedEvidenceState`, `ClosureBlockReason`, `RawAgentEventJson`, `PolicyDecisionEventJson`, `ReviewerPacketJson`, and `AuditBundleJson`.
- V2 record `F9D838CE-4671-F111-AC9A-0022489A9A06` returned the full custom domain payload:
  - `CaseId: CASE-BG-CONTRA`.
  - `ScenarioId: E-004`.
  - `DerivedEvidenceState: contradicting`.
  - `ClosureBlockReason: source_contradiction`.
  - `PackageVersion: 1.0.6`.
  - parseable JSON strings for raw agent event, policy decision event, reviewer packet, and audit bundle.
- V2 query by `CaseId = CASE-BG-CONTRA` returned one item with the selected custom fields and full `AuditBundleJson`.
- Legacy record `DA42769C-33B7-4701-A266-019F032AF376` returned only system fields through `records get`.
- Legacy query by record `Id` returned the record but still only projected `Id`; selected custom snake_case fields were absent.
- Querying old `CaseId`/`case_id` value `CASE-E004-LIVE` returned no records in both entities. The validated V2 proof record currently uses `CASE-BG-CONTRA`.

Feedback impact:

- Confirms PF-019/PF-023.
- No downgrade needed to the final G-001 proof path as long as the submission claims only PascalCase V2 Data Fabric readback.
- Update any stale reference that says the V2 record uses `CASE-E004-LIVE`; the current live record uses `CASE-BG-CONTRA`.
- Keep the legacy snake_case entity as product-feedback evidence, not as proof storage.

### Test Manager Manual Eval Mapping And Automation Boundary

Commands:

```sh
uip tm testcases --help --output json
uip tm project list --filter SREV --output json
uip tm testsets list --project-key SREV --filter SREV:9 --include-last-execution --output json
uip tm testsets list-testcases --project-key SREV --test-set-key SREV:9 --output json
uip tm executions get-stats --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --output json
uip tm report get --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --output json
uip tm executions testcaselogs list --project-key SREV --execution-id 40a1b334-5df8-1100-0a4b-0b49d0564f11 --output json
uip tm executions list --project-key SREV --limit 5 --output json
uip or folders list --output json --output-filter "[].{DisplayName:DisplayName,Key:Key,Id:Id,FullyQualifiedName:FullyQualifiedName,FolderType:FolderType}"
uip tm testcases list-automations --project-key SREV --folder-key 555d3f16-a106-4946-a934-4bede4789be7 --output json
uip tm testcases list-automations --project-key SREV --folder-key 555d3f16-a106-4946-a934-4bede4789be7 --package-name ServiceRecoveryEvalProcessProbe --output json
uip tm testcases list-automations --project-key SREV --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
```

Observed:

- `uip tm testcases --help` confirms the current plural `testcases` command surface.
- Project `SREV` exists and is active.
- Test set `SREV:9` read back with `LastExecutionStatus: Finished` and `LastExecutionAt: 2026-06-26T10:19:58.490Z`.
- `SREV:9` contains the expected nine test cases for E-001 through E-009.
- Execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` readback:
  - `Passed: 9`.
  - `Failed: 0`.
  - `None: 0`.
  - `ExecutionType: Manual`.
  - `IsRunningAutomated: false`.
  - `Status: Finished`.
- `uip tm report get` returned `TotalTests: 9`, `Passed: 9`, `Failed: 0`, `PassRate: 100`.
- Test case logs for execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` each returned `Result: Passed`, `ExecutionType: Manual`, and `ExecutedBy: arshgill6120@gmail.com`.
- `uip tm executions list --project-key SREV --limit 5` still shows the earlier manual execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad` with `Passed: 9`, `ExecutionType: Manual`, but `Status: Running`, while the later terminal execution is `Finished`.
- `uip or folders list` returned four folder keys but the selected display/name fields were null for this command shape, so folder identity requires prior notes or a different lookup.
- `list-automations` in Shared folder `555d3f16-a106-4946-a934-4bede4789be7` returned `Data: []`.
- `list-automations` in the same Shared folder filtered by `ServiceRecoveryEvalProcessProbe` also returned `Data: []`.
- `list-automations` in Solution folder `9d7ae568-d60e-4395-94d7-db115bfb25de` returned HTTP 400 with `Internal Server Error`.

Feedback impact:

- Confirms PF-020/PF-021/PF-024 exactly.
- Do not claim automated Test Cloud execution.
- The older still-running manual execution remains valid lifecycle feedback; the terminal execution remains valid manual proof.
- Potential minor addition: folder list readback can expose keys without human-readable names under this output-filter shape, which makes automation-discovery diagnostics harder. Keep this as supporting detail under PF-024 rather than a new headline PF.

### Integration Service Discovery For Optional External Evidence

Commands:

```sh
uip is --help --output json
uip is connectors --help --output json
uip is connections --help --output json
uip is activities --help --output json
uip is connectors list --help --output json
uip is connections list --help --output json
uip is connectors list --search google --output json
uip is connectors list --filter google --output json
uip is connectors list --filter sheets --output json
uip is connectors list --filter http --output json
uip is connectors list --filter csv --output json
uip is connections list --output json
uip is connections list --all-folders --output json
uip is connectors get uipath-google-sheets --output json
uip is connectors get uipath-uipath-http --output json
uip is activities list uipath-google-sheets --output json
uip is activities list uipath-uipath-http --output json
uip is resources --help --output json
uip is resources list uipath-google-sheets --output json
uip is resources list uipath-uipath-http --output json
uip is connections list uipath-google-sheets --all-folders --output json
uip is connections list uipath-uipath-http --all-folders --output json
```

Observed:

- `uip is` exposes connectors, connections, activities, resources, triggers, and webhooks.
- `uip is connectors list` uses `--filter`, not `--search`. The attempted `--search` commands returned `unknown option '--search'`.
- `uip is connectors list --filter google` returned Google connector entries including Google Sheets, Google Drive, Gmail, Google Vertex, and others.
- `uip is connectors list --filter sheets` returned Google Sheets with key `uipath-google-sheets`.
- `uip is connectors list --filter http` returned HTTP connector key `uipath-uipath-http` and HTTP Webhook key `uipath-http-webhook`.
- `uip is connectors list --filter csv` returned no connectors.
- `uip is connections list --output json` and `--all-folders` returned no connections.
- `uip is connections list uipath-google-sheets --all-folders` and `uip is connections list uipath-uipath-http --all-folders` returned no connections for those connectors.
- `uip is connectors get uipath-google-sheets` returned a connector description and `AuthenticationType: oauth2`, `HasEvents: Yes`, but `Active: No`, `CatalogActive: No`, `DocumentationUrl: No documentation`.
- `uip is connectors get uipath-uipath-http` returned `AuthenticationType: oauth2`, `HasEvents: No`, `HasMethods: No`, `DocumentationUrl: No documentation`.
- Google Sheets activities include `ReadRange`, `ReadCell`, `ListAllRecords`, `GetRecord`, `InsertRecord`, `UpdateRecord`, and write/delete operations.
- HTTP activities include `HTTP Request`.
- Google Sheets resources list includes `SpreadsheetRows`, `ReadRange`, `ReadCell`, `WriteRange`, `Spreadsheet`, and other spreadsheet resources.
- HTTP resources list includes `http-request`.
- Resource list commands warn: `Results may not include custom objects. Use --connection-id for connection-specific data.`

Feedback impact:

- This supports the optional external-evidence-source story only as a discoverable Integration Service path, not as a completed integration.
- Do not claim real Google Sheets/HTTP integration until a connection is created, used, and read back.
- Candidate product-feedback addition: connector discovery is useful, but `connectors get` returning `DocumentationUrl: No documentation` for Google Sheets/HTTP and inactive catalog state makes it harder for a hackathon builder to turn discovery into a low-risk connection workflow. A readiness check could include "connector exists, no connection configured, docs/deep-link unavailable, OAuth required."
- Candidate runbook correction: use `uip is connectors list --filter ...`, not `--search`.

## Recommended Product Feedback Changes

Do not broadly rewrite the feedback. The current top thesis remains correct.

Recommended small changes:

1. PF-018 / survey challenge wording: keep "Data Fabric CLI discovery mismatch" as historical/improved, because current `uip tools list` exposes Data Fabric, Integration Service, and Test Manager tools.
2. PF-019/PF-023 / audit proof wording: explicitly say the validated V2 record currently reads back as `CaseId: CASE-BG-CONTRA`, not `CASE-E004-LIVE`.
3. PF-024 / Test Manager automation wording: keep the automated Test Cloud boundary strict. Fresh readbacks again show manual execution only and no discoverable automation target.
4. Integration Service / external evidence wording: add a careful optional note that Google Sheets and HTTP connector/activity/resource surfaces are discoverable through CLI, but this tenant has no configured connections, so the project must not claim a real Integration Service-backed external evidence source.
5. Q11 readiness-check recommendation: add "connector exists but no connection configured; connector documentation/deep-link unavailable; required OAuth connection missing" as one possible readiness-check item if space allows.

## Claims Not Supported By This Probe

- Automated Test Cloud execution.
- A real Google Sheets/HTTP Integration Service integration.
- Real telecom OSS/BSS integration.
- Legacy snake_case Data Fabric entity as full audit proof.
- Native Case history alone as full G-001 audit proof.

