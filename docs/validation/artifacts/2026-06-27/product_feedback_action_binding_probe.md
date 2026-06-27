# Product Feedback Action Binding Probe

Date: 2026-06-27.

Scope:

- Workstream B: Action Center / generated Action app binding evidence.
- Read-only inspection only.
- Preserve existing submission Case processes, tasks, packages, Action apps, Data Fabric entities, Test Manager baseline objects, and tenant-wide settings.
- Determine whether current CLI/API evidence can diagnose Action schema field -> generated control -> runtime task field mapping and Case-bound Action app version without starting a submission case.

Environment:

- UiPath CLI: `1.195.1`.
- Org: `keepingitlowkey`.
- Tenant: `DefaultTenant`.
- User: `arshgill6120@gmail.com`.
- Existing process inspected: `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`.
- Existing task inspected: `4333536`.
- Existing case instance inspected: `9eb64f9f-6613-48f7-b452-215085d8c67b`.

## Commands

```sh
uip --version
uip login status --output json
uip maestro case tasks describe --type action --id 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
uip tasks get 4333536 --folder-id 7978263 --output json
uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json
uip maestro case instance variables 9eb64f9f-6613-48f7-b452-215085d8c67b --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case tasks describe --help
uip maestro case registry search 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
uip maestro case registry search SimpleApprovalApp --output json
uip tasks get 4300219 --folder-id 7978263 --output json
uip maestro case registry --help
uip apps --help
uip codedapp pull --help
uip maestro case registry get 9eeb93b2-11d3-4bfb-b7d6-29879226f242 --output json
uip maestro case registry get ID5c3f0a11590d4fdab3c22de72f4ff443 --output json
uip maestro case registry get IDb707cd2abbdd42178b415f7341a65f13 --output json
uip maestro case registry get eca298e8-78e8-40d2-8610-946f5145aa9a --output json
uip maestro case registry list --output json
uip maestro case registry get e08ea52f-ad42-41db-a6bc-50471bd25511 --output json
uip maestro case tasks describe --type action --id e08ea52f-ad42-41db-a6bc-50471bd25511 --output json
uip maestro case registry list --output-filter "Resources[?ResourceType=='action-apps' || Id=='e08ea52f-ad42-41db-a6bc-50471bd25511' || Id=='9eeb93b2-11d3-4bfb-b7d6-29879226f242'].{Id:Id,DeploymentTitle:DeploymentTitle,SemVersion:SemVersion,SystemName:SystemName,Folder:DeploymentFolder.FullyQualifiedName,DateDeployed:DateDeployed}" --output json
uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json --output-filter "{Key:Key,Name:Name,ProcessVersion:ProcessVersion,AutoUpdate:AutoUpdate,FolderKey:FolderKey,FolderPath:FolderPath}"
```

## Key Observations

- `tasks describe` for both known `SimpleApprovalApp` action-app IDs exposes the expected schema inputs: `Content`, `EvidencePacketJson`, `RawAgentRecommendation`, `PolicyDecisionJson`, and `Comment`.
- Those schema inputs include empty `ElementId` values. The command exposes the data contract, but not the generated page control names or rendered labels.
- The `hitlTask` output schema describes `AppTasksMetadata.AppId`, `AppVersion`, `AppProcessKey`, and `FolderKey`, but this is a runtime task output shape, not a pre-runtime Case/process binding readback.
- `uip tasks get 4333536` and `uip maestro case instance variables 9eb64f9f-6613-48f7-b452-215085d8c67b` show runtime `AppTasksMetadata.AppId: ID5c3f0a11590d4fdab3c22de72f4ff443` and `AppVersion: 1` after task creation.
- `uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61` shows Case package/process version `1.0.6` and `AutoUpdate: false`, but does not show the Action app ID/version the Case will instantiate.
- `uip maestro case registry list` shows two `SimpleApprovalApp` deployments:

  ```json
  [
    {
      "Id": "9eeb93b2-11d3-4bfb-b7d6-29879226f242",
      "DeploymentTitle": "SimpleApprovalApp",
      "SemVersion": "1.0.1",
      "SystemName": "IDb707cd2abbdd42178b415f7341a65f13",
      "Folder": "arshgill6120@gmail.com's workspace/Solution 1",
      "DateDeployed": "2026-06-26T10:52:54.243Z"
    },
    {
      "Id": "e08ea52f-ad42-41db-a6bc-50471bd25511",
      "DeploymentTitle": "SimpleApprovalApp",
      "SemVersion": "1.0.0",
      "SystemName": "ID5c3f0a11590d4fdab3c22de72f4ff443",
      "Folder": "arshgill6120@gmail.com's workspace/Solution",
      "DateDeployed": "2026-06-24T20:04:43.425Z"
    }
  ]
  ```

- The fresh runtime recheck task `4333536` used `SystemName` `ID5c3f0a11590d4fdab3c22de72f4ff443`, which maps to the older `SimpleApprovalApp` deployment in folder `Solution` with `SemVersion: 1.0.0`, not the later `SemVersion: 1.0.1` deployment in folder `Solution 1`.
- `registry get` works when called with the action-app resource IDs `9eeb93b2-11d3-4bfb-b7d6-29879226f242` and `e08ea52f-ad42-41db-a6bc-50471bd25511`, but not with runtime `SystemName` values or `ActionDefinitionId` values.
- `registry search SimpleApprovalApp` and `registry search 9eeb93b2-11d3-4bfb-b7d6-29879226f242` returned zero results, even though `registry get` and `registry list` could expose those resources.
- `uip apps --help` is not a current CLI surface.
- `uip codedapp pull --help` exists, but the earlier validated pull attempt against the generated app project failed because generated Action apps are not supported coded-app source projects.

## Probe Queue Result

1. Existing read-only evidence confirms the proof-critical fields are present in schema/task API data, while the generated Action Center UI previously rendered `PolicyDecisionJson` as `Unnamed String 1`.
2. Current CLI/API surfaces partially diagnose the data contract and runtime metadata, but do not expose a complete schema field -> generated control -> runtime field mapping without opening/creating a task.
3. The Action app version actually instantiated by a Case task is discoverable after runtime task creation through `AppTasksMetadata`, but this probe did not find a pre-runtime process/package command that shows which Action app deployment a Case package will instantiate.
4. No new scratch artifact was created. The read-only probes answered the binding/version diagnostic question, and a scratch authoring probe had already been run as `PFPROBE-20260627-human-review`; another scratch case would add tenant state without testing the missing pre-runtime binding inspector.
5. This file is the saved CLI/API evidence artifact for Workstream B under `docs/validation/artifacts/2026-06-27/`.

## Product Feedback Impact

This strengthens PF-013. The issue is not only a generated label bug. Builders also need a pre-runtime inspector that links:

- Action schema field names and display names,
- generated page controls and labels,
- persisted runtime task data fields,
- Case process/package version,
- Action app deployment ID/system name/version/folder,
- and whether a Studio Web publish is actually used by the Case-bound runtime task.

The validated submission posture is unchanged: use Action Center for lifecycle and structured reviewer return, and use the custom evidence packet/Data Fabric/bucket audit surfaces for judge-readable proof.
