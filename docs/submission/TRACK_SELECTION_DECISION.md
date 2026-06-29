# Track Selection Decision

Date: 2026-06-27.

Decision: submit the project under **UiPath Maestro Case**.

Confidence: high.

## Source Criteria

Official Devpost track guidance:

| Track | Official fit | Repo fit |
| --- | --- | --- |
| UiPath Maestro Case | Dynamic, exception-heavy casework; stages; handoffs between agents, robots, and people; humans in charge at key decision points; unpredictable paths emerging as work unfolds. | Strong fit. Service recovery routes differently based on missing, stale, contradictory, or adversarial evidence. Human review handles high-impact exceptions. |
| UiPath Maestro BPMN | Predictable end-to-end process in BPMN 2.0; clear tasks, decisions, and handoffs in a defined flow. | Weak fit. The project is not centered on a validated BPMN 2.0 process artifact, and the main story is dynamic exception handling rather than a predictable sequence. |
| UiPath Test Cloud | Agents that redesign software testing: requirements-to-tests, fragile test detection, automation repair, risk/coverage/change-based test orchestration. | Supporting fit only. The repo uses evals and Test Manager manual evidence, but the business solution is telecom service recovery, not a testing product. |

## Why Maestro Case Is The Right Track

The project's core proof is case-centric:

- same green business state can route to different outcomes depending on authoritative evidence,
- missing/stale telemetry routes to controlled verification/retry,
- fresh contradiction routes to human exception review,
- raw agent recommendation and final policy decision are separate events,
- Maestro Case and Action Center enforce lifecycle, review, and routing,
- humans own exceptions and reviewer return is structured.

This is exactly the "unpredictable paths that emerge as the work unfolds" pattern from Devpost.

## Why Not Pivot

### Do not pivot to Maestro BPMN

Reasons:

- no validated BPMN 2.0 runtime solution is the core artifact,
- BPMN would weaken the story by implying a predictable process,
- current UiPath evidence and product feedback are mainly Case / Action Center / audit readiness,
- forum evidence shows publishing/package issues around Maestro artifacts, so a late BPMN pivot would add risk without improving fit.

### Do not pivot to Test Cloud

Reasons:

- Test Manager validation is manual representation and terminal manual execution, not automated Test Cloud execution,
- the repo has honest eval evidence but not a Test Cloud-centered agent product,
- claiming Test Cloud as primary would overstate the validated surface.

## How To Advertise The Build

Primary:

> Track 1: UiPath Maestro Case. Telecom service-recovery case management for dynamic exceptions where agents interpret messy evidence, deterministic policy decides whether closure is safe, and humans review high-impact contradictions.

Supporting:

- Test Manager manual eval representation proves regression discipline.
- Orchestrator/Data Fabric prove audit/version evidence.
- Codex/coding-agent logs prove the coding-agent bonus.
- Best Product Feedback is supported by PF-001 through PF-029 and forum-aligned product insights.

## Submission Copy Guardrails

Say:

- "UiPath Maestro Case is the orchestration boundary."
- "Action Center handles human task lifecycle and structured return."
- "Test Manager represents the eval suite manually."
- "Codex was used as the coding agent and is documented in the README/proof log."

Do not say:

- "Automated Test Cloud execution."
- "Final demo relies on generated Action Center UI."
- "Native Case history alone reconstructs the full domain audit."
- "This is a BPMN process submission."
- "The LLM owns final closure authority."
