# ClearPath Recovery

Governed telecom service recovery with UiPath Maestro Case.

ClearPath Recovery is a UiPath AgentHack Maestro Case submission for broadband activation and restoration exceptions. It proves a practical enterprise pattern: agents interpret ambiguous service evidence, deterministic policy decides what is allowed, Maestro Case routes the work, and humans own high-impact exceptions.

The project is intentionally focused. It is not a generic AI governance platform, and it does not claim real production telecom integrations. The telecom systems are simulated so the submission can concentrate on the hard workflow problem: preventing unsafe closure when business systems look resolved but authoritative service evidence is missing, stale, or contradictory.

## The Problem

Telecom recovery workflows often fail after the case appears clean on paper:

- CRM says the customer is active.
- The order system says activation is complete.
- Billing says the account is ready.
- A support note suggests closure.
- But fresh network telemetry or inventory evidence may still show that service is not working.

A naive agent can make that worse by confidently recommending closure from the cleanest text field. ClearPath demonstrates the safer pattern:

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

## What It Proves

The core proof uses the same green business fixture and changes only the authoritative evidence.

| Beat | Business state | Authoritative evidence | Raw agent recommendation | Policy outcome | Route |
| --- | --- | --- | --- | --- | --- |
| E-002 missing/stale evidence | CRM, order, billing, and support note look resolved | Network telemetry is missing or stale | `closure_candidate` | Closure blocked because required authoritative evidence is not fresh | `verify_telemetry` |
| E-004 contradiction | Same green business fixture | Fresh telemetry or inventory contradicts business state | `closure_candidate` | Human review required because authoritative evidence disagrees | `human_review` |

The important boundary is that the raw Agent Interpretation Event is stored separately from the final Policy Decision Event. Judges and reviewers can see what the agent recommended, why policy overrode it, which evidence source caused the block, and what must be true before closure is safe.

## Architecture

ClearPath has three layers of proof:

| Layer | Purpose | Key artifacts |
| --- | --- | --- |
| Native UiPath proof | Shows the solution is connected to UiPath platform surfaces. | Maestro Case runs, Action Center task readback, Orchestrator package/process/bucket evidence, Data Fabric V2 audit readback, Test Manager manual execution logs. |
| Judge-readable proof | Makes the policy/evidence boundary easy to inspect. | Evidence packet HTML/screenshots, proof index, audit bundles, action payload JSON. |
| Local deterministic proof | Keeps the behavior repeatable without mutating a live tenant. | Unit tests, eval suite E-001 through E-009, fixtures, submission verifier, demo wrappers. |

Runtime flow:

1. CRM, order, billing, support notes, telemetry, and inventory evidence are collected.
2. The agent interprets messy text into a closed-schema Agent Interpretation Event.
3. Deterministic policy checks source authority, freshness, contradiction, confidence, and policy version.
4. Maestro Case routes to telemetry verification, human review, or policy-safe closure.
5. Action Center handles reviewer lifecycle when escalation is required.
6. Data Fabric V2, Orchestrator bucket artifacts, and local audit bundles preserve the proof trail.

## UiPath Platform Use

| UiPath surface | How ClearPath uses it | Validated boundary |
| --- | --- | --- |
| Maestro Case | Primary orchestration boundary for dynamic exception-heavy service recovery. | Case lifecycle and package/runtime validation are proven; native Case history alone is not claimed as complete domain audit. |
| Action Center | Human task lifecycle, reviewer action/comment, and structured return. | Lifecycle and structured return are proven; generated Action Center UI is not used as the final judge-readable packet because field rendering was partially unsuitable. |
| Orchestrator | Package/process/job readback, version pinning, and bucket-backed audit artifact storage. | Used as platform proof and durable audit-artifact host. |
| Data Fabric V2 | Queryable full-payload audit readback for E-004. | PascalCase V2 schema is the validated path. |
| Test Manager | Manual representation of eval scenarios E-001 through E-009. | 9/9 manual execution evidence is captured; automated Test Cloud execution is not claimed. |
| UiPath CLI | Repeatable readback, validation, diagnostics, and evidence capture. | Used for reproducible proof instead of screenshot-only claims. |

## Repository Map

| Path | Purpose |
| --- | --- |
| `service_recovery_core/` | Deterministic recovery core, policy engine, eval runner, LLM adapters, packet/audit generation. |
| `fixtures/eval_scenarios.json` | E-001 through E-009 service-recovery scenarios. |
| `tests/` | Unit tests for policy, schema validation, proof generation, and supporting utilities. |
| `docs/demo/artifacts/` | Generated evidence packets, screenshots, action payloads, audit bundles, proof manifest, and learning-loop artifact. |
| `docs/submission/` | Devpost story, submission brief, proof map, readiness checklist, coding-agent proof, and upload bundle. |
| `docs/validation/` | Validation gates, UiPath readback notes, Test Manager mapping, and objective completion audit. |
| `docs/product/` | Product-feedback award evidence and final feedback copy. |
| `scripts/` | Repeatable demo, submission, deck, and validation helpers. |

## Quick Start

Use Python 3.11+ from the repository root.

```sh
python -m pip install .
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
scripts/run_submission_check.sh
```

Expected baseline:

- Unit tests pass.
- E-001 through E-009 pass 9/9.
- `scripts/run_submission_check.sh` completes without mutating live UiPath state.

## Demo Commands

Regenerate local E-002/E-004 proof artifacts without starting live UiPath work:

```sh
scripts/run_demo.sh --with-local-checks
```

Run the non-mutating final submission proof check:

```sh
scripts/run_submission_check.sh
```

Optional live Gemini/Vertex interpretation can be refreshed only when local ADC/API access is intentionally available:

```sh
scripts/run_llm_demo.sh --evidence-packet-output docs/demo/artifacts/evidence_packet_E003_adversarial_live.html
```

## Key Proof Artifacts

| Artifact | What to inspect |
| --- | --- |
| `docs/demo/artifacts/evidence_packet_E002.html` | Missing/stale authoritative evidence blocks closure and routes to `verify_telemetry`. |
| `docs/demo/artifacts/evidence_packet_E004.html` | Fresh contradiction escalates to `human_review`. |
| `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` | Optional live Gemini/Vertex advocate/skeptic disagreement, still controlled by deterministic policy. |
| `docs/demo/artifacts/service_recovery_audit_bundle_E004.json` | One-object audit reconstruction for the contradiction path. |
| `docs/demo/artifacts/demo_proof_manifest.json` | Machine-readable index of generated proof artifacts. |
| `docs/demo/artifacts/policy_improvement_E008.json` | Governed learning-loop artifact where policy improvement remains proposal-only. |
| `docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md` | End-to-end map from local deterministic proof to UiPath-native proof. |
| `docs/submission/CODING_AGENT_PROOF_LOG.md` | Auditable Codex coding-agent proof. |

## Validation Status

Current validated baseline:

- Local unit tests: 46+ tests passing in the maintained baseline.
- Local evals: E-001 through E-009 passing 9/9.
- UiPath Labs validation ran against org `keepingitlowkey`, tenant `DefaultTenant`.
- Action Center lifecycle and structured reviewer return are validated.
- Data Fabric V2 stores and reads back the E-004 full-payload audit record.
- Orchestrator bucket audit artifact is available as an alternate full-payload proof path.
- Test Manager project `SREV`, test set `SREV:9`, and terminal manual execution represent E-001 through E-009 with 9/9 passed logs.

Read the detailed status in:

- `docs/validation/VALIDATION_RESULTS.md`
- `docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md`
- `docs/submission/READINESS_CHECKLIST.md`

## Honest Boundaries

ClearPath is designed to be reviewable without overclaiming:

- The telecom systems are simulated fixtures, not production OSS/BSS integrations.
- The optional external evidence-source path is a systems-of-record simulator, not real carrier integration.
- The LLM can recommend and explain, but it cannot close cases, override policy, or mutate production policy.
- Codex was used for build-time implementation, validation, and documentation support; it is not runtime authority.
- Generated Action Center UI is not presented as the final readable evidence packet.
- Native Maestro Case history alone is not claimed as the complete domain audit.
- Test Manager evidence is manual representation/execution, not automated Test Cloud execution.

## Coding-Agent Disclosure

Codex as the coding agent was used for build-time implementation, validation loops, UiPath CLI investigation, product-feedback evidence gathering, and submission documentation.

The proof is intentionally auditable from the repository:

- `docs/submission/CODING_AGENT_PROOF_LOG.md`
- `docs/submission/coding_agent_evidence_manifest.json`
- `docs/logs/BUILD_LOG.md`
- `scripts/run_submission_check.sh`
- Codex-prefixed branches and workstream history

The runtime safety boundary remains unchanged: deterministic policy, UiPath Maestro Case routing, Action Center accountability, and human review own the governed recovery path.

## Product Feedback

The strongest product recommendation from the build is a Maestro Case Human-Review Readiness Check: a preflight and auditability contract for human-review cases that validates tenant services, roles, task schemas, generated page bindings, case/action mappings, package versions, reviewer visibility, and audit coverage before live runtime.

Supporting docs:

- `docs/product/PRODUCT_FEEDBACK_AWARD.md`
- `docs/product/FEEDBACK_AWARD_APPENDIX.md`
- `docs/product/FEEDBACK_SURVEY_FINAL_DRAFT.md`

## License

MIT.
