# Wave 01: Platform Access And Inventory

## Goal

Confirm baseline access and repo readiness.

## Inputs

- GitHub repo.
- UiPath Automation Cloud / AgentHack Labs access.
- Local machine with Node/npm and target coding agent.

## Tasks

- Confirm repo remote and default branch.
- Confirm UiPath tenant and Labs invite.
- Confirm access to Maestro, Maestro Case, Studio Web, Action Center, Test Cloud, Integration Service, Orchestrator.
- Install or verify `@uipath/cli`.
- Run `uip --version` and `uip login` if appropriate.
- Try `uip skills install --agent codex`.
- Record all access gaps.

## Outputs

- Updated [docs/validation/VALIDATION_RESULTS.md](../docs/validation/VALIDATION_RESULTS.md).
- Updated [docs/logs/RISK_REGISTER.md](../docs/logs/RISK_REGISTER.md).

## Validation

- Exact commands and screenshots/notes captured.

## Exit Criteria

- Access status is known; no hidden platform assumptions remain about login/labs.
