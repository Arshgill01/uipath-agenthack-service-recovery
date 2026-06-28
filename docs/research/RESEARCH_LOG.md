# Research Log

This log captures source-backed research and platform findings. Append as new evidence is gathered.

## Initial Research Summary

Research source folder from prior run:

- `/Users/arshdeepsingh/Developer/agenthack_research`

Key conclusions imported into this repo:

- Primary track should bias toward Maestro Case if platform validation passes.
- Maestro Case is high-upside but has Preview / Coming Soon maturity signals.
- The live Devpost deadline observed during research was June 29, 2026 at 11:45pm EDT, not June 30.
- Official rules cap a project at two prizes: one overall/track prize plus one special award.
- Coding-agent bonus is explicit and should be visible in the demo.
- LangGraph/LangChain has the strongest official external-framework path; CrewAI is official but Enterprise-gated; AutoGen was invited by Devpost but no strong first-party UiPath path was found.

## Current Loop/Agent Workflow Notes

Accessed June 18, 2026.

| Source | What it contributed | Confidence |
| --- | --- | --- |
| https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop | Traces + human/model feedback + evals can form an improvement flywheel. Relevant to policy-improvement loop and agent usefulness evals. | official-docs |
| https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html | Evaluator/reflect/refine loops use generated output, evaluation, correction, and repeated improvement. Relevant to eval-backed policy proposal flow. | official-docs |
| https://www.anthropic.com/research/building-effective-agents | Agent systems should use workflows/patterns like evaluator-optimizer where appropriate, not over-agentic complexity for its own sake. | official-docs |
| https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems | Agent loop framing: assemble context, reason/select action, execute, observe, feed back until done/stopped. | secondary/aggregator |
| https://www.arthur.ai/blog/best-practices-for-building-agents-guardrails | Guardrails should be first-class execution logic; pre/post-LLM checks and guardrail telemetry matter. Relevant to structured policy override events. | secondary/aggregator |

## Research Rules For Future Agents

- Official UiPath sources first: Devpost, docs.uipath.com, UiPath blogs, UiPath GitHub.
- Log every new source here with access date.
- Do not treat forum posts as product truth unless confirmed by official UiPath response.
- When a source is unavailable, log the failure rather than inferring.
- If a source changes prior assumptions, update [docs/decisions/DECISIONS.md](../decisions/DECISIONS.md).

## 2026-06-27 - AgentHack Forum / Devpost / Winner Research

Sources:

| Source | What it contributed | Confidence |
| --- | --- | --- |
| https://forum.uipath.com/t/uipath-agenthack-is-live-50-000-in-prizes-three-tracks-and-7-weeks-to-build/5746132 | Full public forum thread with launch post, Q&A, track guidance, coding-agent bonus clarification, Labs/Action Center/Maestro blocker reports, and product-feedback context. | official/community |
| https://uipath-agenthack.devpost.com/ | Official rules, track definitions, submission requirements, judging criteria, coding-agent bonus wording, prizes, and Best Product Feedback description. | official |
| https://forum.uipath.com/t/here-are-the-uipath-agenthack-2025-winners/3586396 | 2025 winner list and special-award pattern. | official/community |
| https://www.uipath.com/community-blog/community-news/uipath-community-annual-global-hackathon-2025 | 2025 winner/project summaries, evaluation themes, and prior winner patterns. | official |

Local digest:

- `docs/research/AGENTHACK_FORUM_RESEARCH.md`
- `docs/research/artifacts/2026-06-27/`

Decision impact:

- Confirmed primary track remains UiPath Maestro Case.
- Added `docs/submission/TRACK_SELECTION_DECISION.md`.
- Added README and `docs/submission/CODING_AGENT_PROOF_LOG.md` for coding-agent bonus proof.
- Added demo beat to show coding-agent usage without weakening the runtime governance boundary.

## 2026-06-29 - Final-Lap Product Feedback Source Refresh

Sources:

| Source | What it contributed | Confidence |
| --- | --- | --- |
| https://uipath-agenthack.devpost.com/rules | Confirms Best Product Feedback eligibility requires a complete online form with actionable comments UiPath can use, such as bug reports, UI improvements, suggested integrations, or documentation improvements. Also confirms Track 1 Maestro Case is for dynamic, exception-heavy work with stages, handoffs between agents/robots/people, and humans in charge at key decision points. | official |
| https://uipath-agenthack.devpost.com/details/tracks | Confirms strong Maestro Case submissions should show dynamic exception workflows, human-in-the-loop decisions, long-running business processes, visibility, auditability, and collaboration between humans, agents, and automations. | official |
| https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/overview | Defines Maestro as cloud-native orchestration that unifies automation, AI agents, and human interactions. Supports the submission thesis that UiPath is the orchestration boundary. | official-docs |
| https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/value-proposition | Describes Maestro as human-aware orchestration where AI agents can escalate to human-in-the-loop decisions, and Case Management supports long-running, exception-heavy work where the path evolves as new information appears. | official-docs |
| https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions | Documents tenant-level Actions enablement through Admin > Tenants > Edit Services > Actions. This supports PF-003 as an observed readiness gap, while keeping the expected enablement path grounded in official docs. | official-docs |
| https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/create-user-action | Documents App tasks in Action Center, Action controls defining input fields, and Apps as the visual task interface. Supports the Action app field-binding feedback without inventing product behavior. | official-docs |
| https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/executing-tests | Confirms Test Manager supports manual and automated executions, and that test sets are the execution unit. Supports the honest claim that our validated path is manual Test Manager execution. | official-docs |
| https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/selecting-automation | Confirms linking automations to Test Manager relies on automations published to Orchestrator and feed selection. Supports the package/feed automation-discovery feedback while preserving the non-claim around automated Test Cloud execution. | official-docs |
| https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/introduction | Confirms Data Fabric/Data Service is persistent no-code data storage for RPA projects and long-running business processes. Supports the audit-storage recommendation while keeping the snake_case behavior as reproduced build evidence only. | official-docs |
| https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-packages | Confirms Orchestrator package upload, version visibility, process upgrade, and package/version inspection concepts. Supports package/feed/process readback recommendations. | official-docs |

Decision impact:

- Strengthened `docs/product/FEEDBACK_AWARD_APPENDIX.md`, `docs/product/FEEDBACK_SURVEY_COPY_READY.md`, and `docs/product/FEEDBACK_SURVEY_FINAL_DRAFT.md` so the Microsoft Form answers stand alone.
- Kept three evidence classes separate: reproduced build evidence, official/product context, and recommended product improvements.
- No new UiPath live operation was run; this was source research plus documentation refinement.
