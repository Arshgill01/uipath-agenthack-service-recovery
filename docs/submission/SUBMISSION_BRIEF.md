# Submission Brief

Status: concise, evidence-backed source for Devpost-style project copy. This is not a demo video script.

Readiness checklist: [READINESS_CHECKLIST.md](READINESS_CHECKLIST.md).

Track decision: [TRACK_SELECTION_DECISION.md](TRACK_SELECTION_DECISION.md).

Coding-agent proof: [CODING_AGENT_PROOF_LOG.md](CODING_AGENT_PROOF_LOG.md).

Platform integration proof map: [PLATFORM_INTEGRATION_PROOF_MAP.md](PLATFORM_INTEGRATION_PROOF_MAP.md).

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
- Coding-agent bonus: Codex was used to build and validate the repo; proof is documented in `README.md`, `docs/submission/CODING_AGENT_PROOF_LOG.md`, and `docs/submission/coding_agent_evidence_manifest.json`.

Devpost-ready coding-agent paragraph:

> We used Codex as the coding agent throughout the build: it helped implement the local service-recovery core, deterministic policy tests, eval harness, evidence-packet renderer, UiPath CLI validation loops, product-feedback evidence logs, and final submission docs. The proof is auditable in GitHub through the README coding-agent section, `docs/submission/CODING_AGENT_PROOF_LOG.md`, `docs/submission/coding_agent_evidence_manifest.json`, `docs/logs/BUILD_LOG.md`, Codex-prefixed branches/workstreams, and the non-mutating `scripts/run_submission_check.sh` validation wrapper. Codex was build-time assistance only; it is not part of runtime case closure authority, does not mutate production policy, and does not replace UiPath Maestro Case orchestration, Action Center accountability, deterministic policy, or human review.

## Devpost Final Copy Blocks

Use this section as the final copy/checklist when filling Devpost. Keep field text short enough to scan; link to repo docs for depth.

| Devpost / judging area | Copy or checklist |
| --- | --- |
| Project title | Recommended: `Governed Telecom Service Recovery with UiPath Maestro Case`. Fallback if keeping the repo name: `UiPath AgentHack Service Recovery`. |
| Track | `UiPath Maestro Case`. Do not select Maestro BPMN. Select Test Cloud only as a supporting category if the form allows it without implying automated Test Cloud execution. |
| Problem | Telecom service recovery often closes cases because CRM/order/billing/support notes look green while authoritative network telemetry is missing, stale, or contradictory. Wrong closure drives repeat contacts, SLA breaches, service credits, churn risk, and weak audit trails. |
| What it does | The solution runs a service-recovery case through structured agent interpretation, deterministic policy reconciliation, Maestro Case routing, Action Center human review, and durable audit evidence. It proves two high-risk paths: missing/stale authoritative evidence routes to verification, while fresh contradiction escalates to human review. |
| How it works | The agent emits a schema-validated Agent Interpretation Event, including the raw `closure_candidate` recommendation. Policy then checks source authority, freshness, contradiction, confidence, and pinned policy versions. The final Policy Decision Event is separate, linked to the agent event, and controls the next stage. |
| UiPath platform use / Platform Usage | Maestro Case is the orchestration boundary; Action Center handles reviewer lifecycle and structured return; Orchestrator stores package/process/version and bucket audit proof; Data Fabric V2 stores queryable full-payload audit evidence; Test Manager represents the E-001 through E-009 eval suite; UiPath CLI provides repeatable validation/readback. |
| Agentic behavior | The agent interprets messy technician, customer, and support context into structured signals. Optional Gemini/Vertex proof shows live LLM interpretation, including advocate/skeptic disagreement. The LLM never owns closure; deterministic policy does. |
| Human-in-the-loop | High-impact contradictions route to Action Center human review with structured reviewer action/comment. The final video should show Action Center lifecycle or readback plus the custom evidence packet for readable proof. |
| Business Impact & Adoption Potential | Impact areas: lower wrongful closure rate, fewer repeat contacts, faster path to correct remediation, SLA breach reduction, lower service-credit exposure, and stronger audit completeness for regulated service operations. |
| Technical Execution, Feasibility & Versatility | Evidence: 46 unit tests, E-001 through E-009 passing, repeatable `scripts/run_submission_check.sh`, E-002/E-004 proof artifacts, live UiPath task IDs, Data Fabric V2 audit readback, Orchestrator bucket audit artifact, and explicit honest boundaries. |
| Completeness of Delivery | Public repo has MIT license, README/setup, UiPath component list, coding-agent disclosure, proof logs, demo runbook, submission checklist, product feedback docs, and repeatable local validation scripts. |
| Creativity & Innovation | The novel boundary is not "AI closes the case"; it is governed service recovery where agents propose, policy decides, Maestro routes, humans own exceptions, and explanations/audit are generated once and reused across proof surfaces. |
| Presentation | Follow `docs/demo/DEMO_STORYBOARD.md`. Keep the video under five minutes, show the solution running, show UiPath surfaces, show the AIE/PDE boundary, and stop by 4:55. |
| Product feedback / Best Product Feedback | Mention the strongest recommendation: add a Maestro Case human-review readiness preflight covering tenant services/roles, Action task required fields, generated Action app binding, input/output mappings, package/feed versioning, and audit readiness. Source docs: `docs/product/FEEDBACK_SURVEY_FINAL_DRAFT.md` and `docs/product/FEEDBACK_AWARD_APPENDIX.md`. |
| Coding-agent bonus | `Codex was used as the coding agent to build the local core, evals, UiPath validation runbooks, evidence packets, product-feedback evidence, and final submission pack. It is documented in README, docs/submission/CODING_AGENT_PROOF_LOG.md, and docs/submission/coding_agent_evidence_manifest.json. Codex is build-time assistance; UiPath and deterministic policy remain runtime authority.` |
| Screenshots/images to upload | Prefer: `docs/demo/artifacts/evidence_packet_E002_desktop.png`, `docs/demo/artifacts/evidence_packet_E004_desktop.png`, `docs/demo/artifacts/evidence_packet_E003_adversarial_desktop.png`, plus one UiPath platform screenshot if captured during recording. |
| Repository link check | Ensure the submitted repository is public, includes `LICENSE` with MIT text, and the README points to setup, UiPath components, coding-agent use, and validation commands. |
| Presentation deck link check | Upload/share the deck with public or jury-access permissions. The deck should mirror the video: problem, UiPath architecture, 2A/2B contrast, eval/learning loop, product feedback, coding-agent proof, business impact. |

## Evidence Links

- Repeatable local proof: `scripts/run_demo.sh`
- Non-mutating submission check: `scripts/run_submission_check.sh`
- Platform integration proof map: `docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md`
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
- Coding-agent evidence manifest: `docs/submission/coding_agent_evidence_manifest.json`
- Coding-agent demo beat checklist: `docs/submission/CODING_AGENT_DEMO_BEAT_CHECKLIST.md`
- Optional external evidence-source proof: `docs/demo/artifacts/external_evidence_source_proof.json`
- Forum/Devpost research digest: `docs/research/AGENTHACK_FORUM_RESEARCH.md`

## Honest Boundaries

- The telecom systems are simulated fixtures, not production integrations. The optional external evidence-source proof uses a live-style CRM/billing/inventory/network/dispatch evidence simulator and must not be described as production telecom OSS/BSS access.
- Native Maestro Case history is not claimed as a complete domain audit by itself.
- Generated Action Center UI is not the final judge-facing evidence surface because it hid or mislabeled proof-critical fields during validation.
- Data Fabric V2 full-payload persistence is validated for E-004 through JSON insert/query/readback using PascalCase fields. The legacy snake_case `ServiceRecoveryAuditBundle` entity remains a product-feedback finding because its custom fields did not populate or read back correctly.
- Test Manager validation is manual execution/report/export, not automated Test Cloud execution.
- A fresh Case Instance on package `1.0.6` reached terminal lifecycle completion (`LatestRunStatus: Completed`) after the unbound placeholder task was made optional. Do not generalize this to older E-002/E-004 jobs.
- Coding-agent usage is build-time assistance and documentation/validation support, not runtime case authority.
