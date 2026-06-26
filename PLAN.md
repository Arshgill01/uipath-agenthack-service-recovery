# High-Level Plan

This is the human-readable main plan for the repository. Detailed execution is in [waves/](waves/).

## Goal

Create a working UiPath AgentHack submission that proves governed agentic service recovery using Maestro Case, simulated telecom systems, structured agent interpretation, deterministic policy enforcement, human exception review, audit logging, eval-backed agent usefulness checks, and a governed policy-improvement loop.

## Build Strategy

1. Preserve the validated UiPath platform facts and do not reopen broad gate validation without new contradictory evidence.
2. Keep deterministic policy separate from agent/LLM interpretation.
3. Use Action Center for human-task lifecycle and structured return.
4. Use custom evidence packets/screenshots for judge-readable proof.
5. Use Orchestrator bucket artifacts for durable UiPath-hosted domain audit reconstruction.
6. Use local evals, Test Manager manual mapping, and `scripts/run_submission_check.sh` for repeatable validation.
7. Use the optional Gemini/Vertex interpreter only as a structured recommendation source, never as final closure authority.
8. Polish submission and feedback assets around observed platform facts.

## Workstreams

| Workstream | Purpose | Primary docs |
| --- | --- | --- |
| Platform validation | Prove what UiPath Labs actually supports | [docs/validation/VALIDATION_GATES.md](docs/validation/VALIDATION_GATES.md) |
| Domain model | Represent case, evidence, policy, audit, evals | [docs/architecture/DATA_MODEL.md](docs/architecture/DATA_MODEL.md) |
| Agent interpretation | Convert unstructured text into structured signals | [docs/architecture/AGENT_CONTRACT.md](docs/architecture/AGENT_CONTRACT.md) |
| Policy engine | Decide allowed actions and block unsafe closure | [docs/architecture/POLICY_MODEL.md](docs/architecture/POLICY_MODEL.md) |
| Case orchestration | Enforce stages, routes, human review | [docs/architecture/CASE_WORKFLOW.md](docs/architecture/CASE_WORKFLOW.md) |
| Evals/Test Cloud | Validate agent usefulness and policy regressions | [docs/validation/EVAL_PLAN.md](docs/validation/EVAL_PLAN.md) |
| Demo/submission | Tell the story clearly | [docs/demo/DEMO_STORYBOARD.md](docs/demo/DEMO_STORYBOARD.md) |
| Product feedback | Capture specific UiPath feedback for the feedback award | [docs/product/PRODUCT_FEEDBACK_AWARD.md](docs/product/PRODUCT_FEEDBACK_AWARD.md) |

## Execution Order

Use [waves/00_WAVES_INDEX.md](waves/00_WAVES_INDEX.md). Do not skip validation waves unless explicitly documented.

Initial validation waves are complete enough to proceed with the demo-safe proof path:

1. Use `scripts/run_submission_check.sh` before final submission and after any change.
2. Use `scripts/run_demo.sh` to regenerate/verify E-002/E-004 proof artifacts.
3. Use `scripts/run_llm_demo.sh --evidence-packet-output ...` only when intentionally refreshing the live Gemini/Vertex proof.
4. Keep fresh live UiPath reruns scoped to new IDs/artifacts that are explicitly needed.
5. Keep product-feedback updates tied to newly observed platform behavior.

## Current Highest-Risk Assumptions

- Maestro Case native state/history is not sufficient alone for one-view domain audit reconstruction; use the Orchestrator `service-recovery-audit-v1` fallback.
- Generated Action Center UI is not reliable enough as the judge-facing packet; use the custom packet/screenshots.
- Active-case policy migration remains an explicit custom audit-event concern.
- Test Cloud/Test Manager validation is manual mapping plus passed logs, not automated Test Cloud execution.
- Fresh live reruns mutate tenant state and need explicit intent/logging.

## Quality Bar

This project should feel like a production-shaped architecture compressed into a hackathon build. It does not need production infrastructure, but it must avoid toy behavior:

- no happy-path-only demo,
- no unstructured LLM outputs driving policy,
- no hidden closure decisions,
- no fake auditability,
- no unexplained rule changes.
