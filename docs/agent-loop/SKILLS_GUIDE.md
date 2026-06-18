# Skills Guide

Repo-local skills live in `.agents/skills/`.

## Available Local Skills

| Skill | Use |
| --- | --- |
| `uipath-service-recovery-architect` | Architecture, policy, schema, scope, workflow decisions. |
| `uipath-service-recovery-builder` | Implementation, fixtures, schemas, local simulation, UI, runbooks. |
| `uipath-service-recovery-validator` | UiPath validation, evals, demo readiness, submission readiness. |

## Expected Usage

Future agents should load the narrowest skill for the active task, then read the listed required files. Skills are not substitutes for current repo context.

## Skill Format

Each skill uses:

- YAML front matter with `name` and `description`,
- clear trigger/use case,
- required reading,
- checklist or workflow,
- reporting requirements.
