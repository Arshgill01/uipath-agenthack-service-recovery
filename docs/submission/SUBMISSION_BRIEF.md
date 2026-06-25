# Submission Brief

Status: concise, evidence-backed source for Devpost-style project copy. This is not a demo video script.

Readiness checklist: [READINESS_CHECKLIST.md](READINESS_CHECKLIST.md).

## One-Line Pitch

UiPath Maestro Case for telecom service recovery: agents interpret messy evidence, deterministic policy decides whether closure is safe, and human reviewers handle high-impact exceptions with an auditable evidence packet.

## Three-Paragraph Pitch

Telecom service recovery often fails when business systems look clean while the customer still lacks working service. CRM, order, billing, and support notes may all say the case is ready to close, but authoritative network telemetry may be missing, stale, or contradicting the business state. This project prevents unsafe closure in that exact service-activation/restoration workflow.

The architecture keeps the agent useful without giving it final authority. The agent emits a structured Agent Interpretation Event, including a raw `closure_candidate` recommendation when business systems look green. A deterministic policy layer then evaluates source authority, freshness, contradiction, confidence, and policy version. The final Policy Decision Event is separate, linked to the raw agent event, and controls routing. Missing/stale authoritative telemetry routes to verification or retry; fresh contradiction escalates to human review.

The UiPath implementation uses Maestro Case and Action Center for lifecycle and human-task proof, Orchestrator for package/process/job and audit artifact operations, Test Manager for eval-suite representation, and a custom evidence packet for the judge-readable proof surface. The hard platform gates are answered: native Case audit is partial, but a UiPath-hosted audit bundle gives one-object domain reconstruction; policy version pinning is explicit; Action Center lifecycle and structured return work; and the raw agent recommendation remains visible separately from the policy override.

## What Is Real

- Local engine with deterministic policy, structured agent validation, state transitions, audit bundles, UiPath payload generation, and evidence-packet rendering.
- 27 unit tests passing.
- E-001 through E-009 eval suite passing 9/9.
- Live UiPath Labs validation in org `keepingitlowkey`, tenant `DefaultTenant`.
- Live Action Center tasks for E-002 and E-004.
- Live Orchestrator bucket audit artifact for E-004.
- Test Manager project/test-set/manual logs representing E-001 through E-009.
- `scripts/run_demo.sh` repeatably regenerates and verifies the local E-002/E-004 proof artifacts.

## Core Proof Beats

| Beat | Fixture | Agent recommendation | Policy outcome | Route |
| --- | --- | --- | --- | --- |
| 2A | CRM/order/billing/support green; authoritative telemetry missing/stale | `closure_candidate` | `override_recommendation` with `missing_authoritative_signal` or `stale_authoritative_signal` | `verify_telemetry` |
| 2B | Same green business fixture; fresh authoritative telemetry contradicts | `closure_candidate` | `require_human_review` with `source_contradiction` | `human_review` |

## UiPath Surfaces Used

- Maestro Case: case lifecycle, stage/task orchestration, runtime case validation.
- Action Center: human task assignment, completion, reviewer comment, structured return.
- Orchestrator: package/process/version/job readback and bucket-backed audit artifact.
- Test Manager: eval-suite representation through manual test cases, set, and passed logs.
- UiPath CLI: repeatable readback and validation operations.

## Evidence Links

- Repeatable local proof: `scripts/run_demo.sh`
- Demo runbook: `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`
- E-002 packet: `docs/demo/artifacts/evidence_packet_E002.html`
- E-004 packet: `docs/demo/artifacts/evidence_packet_E004.html`
- Proof manifest: `docs/demo/artifacts/demo_proof_manifest.json`
- Validation results: `docs/validation/VALIDATION_RESULTS.md`
- Product feedback answer bank: `docs/product/FEEDBACK_SURVEY_COPY_READY.md`

## Honest Boundaries

- The telecom systems are simulated fixtures, not production integrations.
- Native Maestro Case history is not claimed as a complete domain audit by itself.
- Generated Action Center UI is not the final judge-facing evidence surface because it hid or mislabeled proof-critical fields during validation.
- Data Fabric audit record persistence is not claimed; Orchestrator bucket artifact storage is the validated fallback.
- Test Manager validation is manual mapping/logging, not automated Test Cloud execution.
- E-002/E-004 Case jobs still read back as `Running`, so the submission should claim Action Center task lifecycle and audit proof, not terminal Case job completion.
