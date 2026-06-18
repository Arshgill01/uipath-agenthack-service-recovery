---
name: uipath-service-recovery-architect
description: Use when making architecture, policy, schema, Maestro Case, eval, or scope decisions for this UiPath AgentHack service recovery repo.
---

# UiPath Service Recovery Architect Skill

Use this skill before changing architecture docs, schemas, policy rules, workflow stages, eval strategy, or scope boundaries.

## Required Reading

Read these first:

- `AGENTS.md`
- `PROJECT_BRIEF.md`
- `docs/architecture/ARCHITECTURE.md`
- `docs/architecture/AGENT_CONTRACT.md`
- `docs/architecture/POLICY_MODEL.md`
- `docs/architecture/CASE_WORKFLOW.md`
- `docs/validation/VALIDATION_GATES.md`
- `docs/decisions/DECISIONS.md`

## Non-Negotiable Architecture

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

Do not weaken this boundary.

## Architecture Review Checklist

- Does agent output remain structured?
- Does policy avoid parsing prose?
- Does closure require fresh authoritative evidence?
- Does missing/stale evidence route differently from contradiction?
- Can the demo show agent recommendation before policy override?
- Are policy versions pinned or explicitly migrated?
- Are proposed policy changes eval-backed and human-approved?
- Is the change still business-centric and tied to MTTR/SLA/wrongful closure/audit completeness?

## Decision Logging

Every material decision must be appended to `docs/decisions/DECISIONS.md`.

Use:

```md
## D-XXX: Title

Decision:

Rationale:

Status:
```
