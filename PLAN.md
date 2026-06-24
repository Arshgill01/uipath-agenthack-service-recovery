# High-Level Plan

This is the human-readable main plan for the repository. Detailed execution is in [waves/](waves/).

## Goal

Create a working UiPath AgentHack submission that proves governed agentic service recovery using Maestro Case, simulated telecom systems, structured agent interpretation, deterministic policy enforcement, human exception review, audit logging, eval-backed agent usefulness checks, and a governed policy-improvement loop.

## Build Strategy

1. Validate UiPath platform assumptions before committing code shape.
2. Build a minimal local simulation of telecom systems and policy logic.
3. Implement structured agent interpretation with schema validation.
4. Implement deterministic reconciliation and policy decisions.
5. Map the local workflow to Maestro Case stages and human review.
6. Add eval scenarios and agent usefulness checks.
7. Add governed policy-improvement artifacts.
8. Polish demo, documentation, and Devpost submission assets.

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

Immediate next work is validation, not product implementation:

1. Wave 01: platform access and inventory.
2. Wave 02: Maestro Case state/audit spike.
3. Wave 03: policy version pinning spike.
4. Wave 04: human evidence packet spike.
5. Wave 05: raw agent recommendation before policy override.

## Current Highest-Risk Assumptions

- Maestro Case native state/history may not be sufficient for one-view audit reconstruction.
- Action Center may not render the evidence packet clearly enough for the demo.
- Policy version pinning may need to be implemented as explicit metadata, not native behavior.
- Showing raw agent recommendation before policy override may require deliberate event logging or custom UI.
- Test Cloud/eval integration may need to be represented as a lightweight harness if full integration is too heavy.

## Quality Bar

This project should feel like a production-shaped architecture compressed into a hackathon build. It does not need production infrastructure, but it must avoid toy behavior:

- no happy-path-only demo,
- no unstructured LLM outputs driving policy,
- no hidden closure decisions,
- no fake auditability,
- no unexplained rule changes.
