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
