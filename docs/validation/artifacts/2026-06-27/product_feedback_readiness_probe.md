# Product Feedback Readiness Probe

Date: 2026-06-27.

Environment:

- UiPath CLI `1.195.1`.
- Org `keepingitlowkey`.
- Tenant `DefaultTenant`.
- User `arshgill6120@gmail.com`.
- No scratch resources created; read-only CLI probe only.

## Commands

```sh
uip login status --output json
uip login tenant list --output json
uip or folders list --output json
uip maestro case --help
uip maestro case validate --help
uip maestro case tasks describe --help
uip maestro case processes list --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case process list --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json --log-level debug
uip maestro case processes diagnose 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case processes diagnose 320c067a-27b9-4c2f-8b26-f6ee38ad97cc --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case processes incidents 320c067a-27b9-4c2f-8b26-f6ee38ad97cc --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip maestro case processes error-codes 320c067a-27b9-4c2f-8b26-f6ee38ad97cc --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de --output json
uip tasks users --folder-id 7978263 --output json
uip tasks users 7978263 --output json
uip tasks list --folder-id 7978263 --limit 10 --output json
uip platform tenants --help
uip tools list --output json
```

## Key Observations

- Auth and tenant context are valid: `LoginStatus` returned `Logged in`, org `keepingitlowkey`, tenant `DefaultTenant`.
- `uip maestro case processes list` returned existing Case process summaries and counts, including process `9a7eb300-7b16-4856-b14f-d6f2da3dbe61` with package versions `1.0.3` through `1.0.6`.
- The singular `uip maestro case process list` command failed with only `Response returned an error code` and `Request was rejected - check flag values and inputs`, while the plural `processes list` command succeeded.
- `uip maestro case processes diagnose` failed for both a healthy/current process and an older faulted process with `UnknownError`, `Error diagnosing process`, and `summaries.find is not a function`.
- `uip maestro case processes incidents` returned `Data: []` for the older faulted process, while `error-codes` returned `170000 / Failure in the AppTasks request`.
- The Case CLI exposes `validate` for local case JSON and `tasks describe` for task metadata, but the observed help does not advertise a readiness check for Actions service availability, required Action task `Title`, generated Action page binding, app version propagation, package/feed binding, or reviewer visibility before runtime.
- `uip tasks users --folder-id 7978263` failed because `tasks users` expects positional `<folder-id>`, while `tasks list` and `tasks get` use `--folder-id`.
- Corrected `uip tasks users 7978263` succeeded and returned reviewer user `Arshdeep Singh`, ID `14338019`.
- `uip platform tenants --help` exposes tenant licensing only; it does not expose a tenant-service readiness list for Actions/Action Center even though `uip tools list` shows the `tasks-tool`.

## Product Feedback Impact

These observations strengthen the existing primary recommendation: Maestro Case needs a human-review readiness/preflight path that verifies services, roles, Action app schema binding, required task fields, package version/feed binding, and diagnostic readability before a live Case run.
