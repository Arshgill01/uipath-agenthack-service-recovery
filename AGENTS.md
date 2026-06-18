# AGENTS.md

This repository is the scaffold and build home for the UiPath AgentHack service-recovery project.

## Mission

Build a working UiPath AgentHack submission for **Maestro Case**:

> A telecom/broadband service activation and restoration exception workflow that proves governed agentic recovery under missing, stale, or contradicting authoritative evidence.

The system must show that agents are useful, but not trusted blindly:

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

## Current Locked Direction

- Primary track: Maestro Case.
- Supporting proof layers: Test Cloud/eval harness, UiPath CLI/coding-agent bonus, optional BPMN/API Workflow subprocesses.
- Domain: telecom/broadband service activation/restoration exceptions.
- Core failure primitive: CRM/order/billing/support note look green, but authoritative network telemetry is missing, stale, or contradicting service-live state.
- Business impact: service continuity, SLA/MTTR reduction, fewer wrongful closures, fewer repeat contacts, fewer service credits, better audit completeness.
- External systems are simulated unless real UiPath connectors are trivial and low-risk.

## Hard Rules

- Do not turn this into a generic AI governance platform.
- Do not build real telecom integrations.
- Do not let the LLM directly close cases, override policy, or mutate production policy.
- Do not bury the agent/policy boundary in prose. Enforce it with structured schemas and visible audit events.
- Do not claim validation unless the exact command or UiPath run was performed.
- Do not add speculative abstractions. Build the smallest concrete version that proves the architecture.
- Do not weaken closure requirements to make a demo pass.
- Do not treat a simulated system as a real telecom system. Label simulations honestly.

## Agent Work Loop

Every substantial agent run must follow this loop:

1. **Orient**: read this file, [PROJECT_BRIEF.md](PROJECT_BRIEF.md), [docs/architecture/ARCHITECTURE.md](docs/architecture/ARCHITECTURE.md), [docs/validation/VALIDATION_GATES.md](docs/validation/VALIDATION_GATES.md), and the current wave file.
2. **Plan**: state the exact wave/task, affected files, assumptions, and validation command(s).
3. **Act**: make the smallest scoped change that advances the wave.
4. **Observe**: run targeted validation and capture results.
5. **Reflect**: update the relevant log with decisions, blockers, and next steps.
6. **Stop or continue**: only continue if the next step is still within the active wave and validation state is understood.

This mirrors current agent-loop practice: plan-act-observe-reflect with explicit stopping conditions, traces/logs, evals, and guardrails as first-class execution logic.

## Required Logs

Update these as work proceeds:

- [docs/logs/BUILD_LOG.md](docs/logs/BUILD_LOG.md): what changed, commands run, validation status.
- [docs/decisions/DECISIONS.md](docs/decisions/DECISIONS.md): material architecture/product decisions.
- [docs/research/RESEARCH_LOG.md](docs/research/RESEARCH_LOG.md): source-backed research and platform findings.
- [docs/validation/VALIDATION_RESULTS.md](docs/validation/VALIDATION_RESULTS.md): UiPath Labs validation outcomes.
- [docs/logs/RISK_REGISTER.md](docs/logs/RISK_REGISTER.md): open risks and mitigations.

## Definition Of Done For Any Wave

- Requested scope is implemented or clearly blocked.
- Relevant docs/logs are updated.
- Validation was run, or the reason it could not be run is documented.
- No unrelated refactors.
- No hidden assumptions about UiPath platform behavior.
- Final response includes changed files, commands run, pass/fail status, and open risks.

## File Ownership Guide

- Root docs define repo-wide intent and operating rules.
- `docs/architecture/` defines system shape and contracts.
- `docs/validation/` defines platform and build verification gates.
- `docs/product/` defines business narrative, metrics, and demo requirements.
- `docs/agent-loop/` defines how future agents should work.
- `waves/` is the phase-by-phase execution plan.
- `.agents/skills/` contains local skills future agents may load for this repository.

## Before Scaffolding Code

Do not start application code until these are answered or consciously waived:

- Maestro Case native state/audit reconstruction.
- Policy version pinning strategy.
- Human evidence packet UI strategy.
- Agent recommendation visible before policy override.

See [docs/validation/VALIDATION_GATES.md](docs/validation/VALIDATION_GATES.md).
