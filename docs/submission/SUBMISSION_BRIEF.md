# Submission Brief

Status: concise, evidence-backed source for Devpost-style project copy. This is not a demo video script.

Readiness checklist: [READINESS_CHECKLIST.md](READINESS_CHECKLIST.md).

Track decision: [TRACK_SELECTION_DECISION.md](TRACK_SELECTION_DECISION.md).

Coding-agent proof: [CODING_AGENT_PROOF_LOG.md](CODING_AGENT_PROOF_LOG.md).

## One-Line Pitch

UiPath Maestro Case for telecom service recovery: agents interpret messy evidence, deterministic policy decides whether closure is safe, and human reviewers handle high-impact exceptions with an auditable evidence packet.

## Three-Paragraph Pitch

Telecom service recovery often fails when business systems look clean while the customer still lacks working service. CRM, order, billing, and support notes may all say the case is ready to close, but authoritative network telemetry may be missing, stale, or contradicting the business state. This project prevents unsafe closure in that exact service-activation/restoration workflow.

The architecture keeps the agent useful without giving it final authority. The agent emits a structured Agent Interpretation Event, including a raw `closure_candidate` recommendation when business systems look green. A deterministic policy layer then evaluates source authority, freshness, contradiction, confidence, and policy version. The final Policy Decision Event is separate, linked to the raw agent event, and controls routing. Missing/stale authoritative telemetry routes to verification or retry; fresh contradiction escalates to human review.

The UiPath implementation uses Maestro Case and Action Center for lifecycle and human-task proof, Orchestrator for package/process/job and audit artifact operations, Test Manager for eval-suite representation, and a custom evidence packet for the judge-readable proof surface. The hard platform gates are answered: native Case audit is partial, but a UiPath-hosted audit bundle gives one-object domain reconstruction; policy version pinning is explicit; Action Center lifecycle and structured return work; and the raw agent recommendation remains visible separately from the policy override.

## What Is Real

- Local engine with deterministic policy, structured agent validation, state transitions, audit bundles, UiPath payload generation, and evidence-packet rendering.
- Optional Gemini-backed LLM interpreter validated through live Vertex runs; it reads unstructured notes/messages and emits the same schema-validated Agent Interpretation Event plus urgency, customer impact, evidence gaps, recommended actions, reviewer questions, and operator note.
- Optional adversarial Gemini interpretation path validated through a live Vertex run: resolution advocate recommended `closure_candidate`, closure skeptic recommended `verify_telemetry`, disagreement reached `0.712`, and deterministic policy routed to `human_review` with `high_interpretation_disagreement`.
- 46 unit tests passing.
- E-001 through E-009 eval suite passing 9/9.
- Live UiPath Labs validation in org `keepingitlowkey`, tenant `DefaultTenant`.
- Live Action Center tasks for E-002 and E-004.
- Live Orchestrator bucket audit artifact for E-004.
- Test Manager project/test-set/manual logs representing E-001 through E-009.
- `scripts/run_demo.sh` repeatably regenerates and verifies the local E-002/E-004 proof artifacts.
- `scripts/run_submission_check.sh` verifies the local submission proof set without starting live UiPath cases or live LLM calls.

## Core Proof Beats

| Beat | Fixture | Agent recommendation | Policy outcome | Route |
| --- | --- | --- | --- | --- |
| 2A | CRM/order/billing/support green; authoritative telemetry missing/stale | `closure_candidate` | `override_recommendation` with `missing_authoritative_signal` or `stale_authoritative_signal` | `verify_telemetry` |
| 2B | Same green business fixture; fresh authoritative telemetry contradicts | `closure_candidate` | `require_human_review` with `source_contradiction` | `human_review` |

## UiPath Surfaces Used

- Maestro Case: case lifecycle, stage/task orchestration, runtime case validation.
- Action Center: human task assignment, completion, reviewer comment, structured return.
- Orchestrator: package/process/version/job readback and bucket-backed audit artifact.
- Test Manager: eval-suite representation through manual test cases, set, terminal manual execution, report, and JUnit export.
- UiPath CLI: repeatable readback and validation operations.

## Track And Bonus Positioning

- Primary track: UiPath Maestro Case.
- Reason: the solution is dynamic, exception-heavy casework where routes emerge from evidence freshness and contradiction state, not a predictable BPMN sequence.
- Supporting surfaces: Test Manager for eval representation, Data Fabric/Orchestrator for audit proof, Action Center for human review lifecycle.
- Coding-agent bonus: Codex was used to build and validate the repo; proof is documented in `README.md` and `docs/submission/CODING_AGENT_PROOF_LOG.md`.

Devpost-ready coding-agent paragraph:

> We used Codex as the coding agent throughout the build: it helped implement the local service-recovery core, deterministic policy tests, eval harness, evidence-packet renderer, UiPath CLI validation loops, product-feedback evidence logs, and final submission docs. The proof is auditable in GitHub through the README coding-agent section, `docs/submission/CODING_AGENT_PROOF_LOG.md`, `docs/logs/BUILD_LOG.md`, Codex-prefixed branches/workstreams, and the non-mutating `scripts/run_submission_check.sh` validation wrapper. Codex was build-time assistance only; it is not part of runtime case closure authority, does not mutate production policy, and does not replace UiPath Maestro Case orchestration, Action Center accountability, deterministic policy, or human review.

## Evidence Links

- Repeatable local proof: `scripts/run_demo.sh`
- Non-mutating submission check: `scripts/run_submission_check.sh`
- Demo runbook: `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`
- E-002 packet: `docs/demo/artifacts/evidence_packet_E002.html`
- E-004 packet: `docs/demo/artifacts/evidence_packet_E004.html`
- Proof manifest: `docs/demo/artifacts/demo_proof_manifest.json`
- Optional LLM interpreter: `service_recovery_core/llm_interpreter.py`
- Live LLM proof artifact: `docs/demo/artifacts/llm_interpreter_E003_live.json`
- Live adversarial LLM proof artifact: `docs/demo/artifacts/llm_interpreter_E003_adversarial_live.json`
- Live adversarial evidence packet: `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html`
- Governed learning-loop artifact: `docs/demo/artifacts/policy_improvement_E008.json`
- Validation results: `docs/validation/VALIDATION_RESULTS.md`
- Product feedback answer bank: `docs/product/FEEDBACK_SURVEY_COPY_READY.md`
- Track decision: `docs/submission/TRACK_SELECTION_DECISION.md`
- Coding-agent proof log: `docs/submission/CODING_AGENT_PROOF_LOG.md`
- Forum/Devpost research digest: `docs/research/AGENTHACK_FORUM_RESEARCH.md`

## Honest Boundaries

- The telecom systems are simulated fixtures, not production integrations.
- Native Maestro Case history is not claimed as a complete domain audit by itself.
- Generated Action Center UI is not the final judge-facing evidence surface because it hid or mislabeled proof-critical fields during validation.
- Data Fabric V2 full-payload persistence is validated for E-004 through JSON insert/query/readback using PascalCase fields. The legacy snake_case `ServiceRecoveryAuditBundle` entity remains a product-feedback finding because its custom fields did not populate or read back correctly.
- Test Manager validation is manual execution/report/export, not automated Test Cloud execution.
- A fresh Case Instance on package `1.0.6` reached terminal lifecycle completion (`LatestRunStatus: Completed`) after the unbound placeholder task was made optional. Do not generalize this to older E-002/E-004 jobs.
- Coding-agent usage is build-time assistance and documentation/validation support, not runtime case authority.
