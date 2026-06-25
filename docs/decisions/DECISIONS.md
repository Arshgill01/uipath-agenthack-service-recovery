# Decision Log

Use this as an append-only record. Do not rewrite history; add superseding decisions when needed.

## D-001: Primary Track

Decision: Use Maestro Case as primary track unless UiPath Labs validation fails.

Rationale: The project thesis is dynamic, exception-heavy, long-running case recovery with human accountability and auditability. This is the strongest fit for Maestro Case.

Status: Accepted, pending platform validation.

## D-002: Domain

Decision: Use telecom/broadband service activation/restoration exceptions.

Rationale: The domain is business-centric, technically rich, and validated by UiPath's One NZ Maestro case study while leaving differentiation headroom around safe exception governance, missing/stale evidence, contradictions, and policy override.

Status: Accepted.

## D-003: Core Architecture Boundary

Decision:

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

Rationale: This preserves agent usefulness while preventing probabilistic outputs from directly making high-impact closure decisions.

Status: Accepted.

## D-004: External Systems

Decision: Simulate CRM/order, billing, network telemetry, inventory/activation, dispatch notes, and customer/support messages.

Rationale: The judging value is orchestration/governance, not real telecom access. Honest simulation reduces risk and keeps the build focused.

Status: Accepted.

## D-005: Evidence States

Decision: Use four evidence states:

- confirmed aligned,
- missing/pending,
- contradicting,
- authoritative source unavailable/stale.

Rationale: Missing evidence, stale evidence, and contradictory evidence require different operational responses.

Status: Accepted.

## D-006: Policy Versioning

Decision: Active cases stay pinned to their interpretation and decision policy versions by default. Migration requires an explicit audit event.

Rationale: Silent policy changes mid-case weaken auditability.

Status: Accepted, implementation method pending validation.

## D-007: Learning Loop

Decision: Agents may propose policy/schema/prompt improvements but may not apply them directly. Proposed changes require eval/regression pass and human approval before promotion.

Rationale: This gives governed learning without self-mutating production rules.

Status: Accepted.

## D-008: Test Cloud / Eval Crossover

Decision: Use Test Cloud or a UiPath-compatible eval harness to validate agent usefulness, confidence calibration, schema validity, and policy regressions.

Rationale: This supports cross-platform integration and prevents the agent from being merely conservative or decorative.

Status: Accepted, implementation method pending validation.

## D-009: Action Center Fallback

Decision: Use Action Center for human-task lifecycle and structured reviewer return, but use a Case App/custom evidence-packet or audit-bundle view for the final demo surface unless the generated Action Center page is repaired.

Rationale: Demo legibility matters. The human reviewer must see evidence, agent output, policy decision, block reason, and allowed actions.

Status: Accepted and activated. Live tasks `4295299` and `4300219` proved Action Center task mechanics and reviewer comments, but the generated page rendered the policy field as `Unnamed String 1` and left proof-critical evidence/raw/policy values blank or unreadable in the completed-task UI. Use the custom packet/audit surface for legibility while keeping Action Center as the human-in-the-loop mechanism.

## D-010: Product Narrative Boundary

Decision: Pitch this as a concrete telecom service-recovery solution whose architecture can generalize, not as a generic governance platform.

Rationale: The data model contains reusable internal concepts, but the hackathon judging requires a real business problem. A generic platform pitch would conflict with the scope boundary and weaken business impact.

Status: Accepted.

## D-011: Override Persistence As Eval Requirement

Decision: Eval scenarios must assert that raw agent recommendations and policy decisions persist as linked events, not only that the final route is correct.

Rationale: The visible policy override is the central proof that agents advise while policy decides. An implementation that discards the raw recommendation can appear correct while failing the architecture.

Status: Accepted.

## D-012: Local Provisional Core Stack

Decision: Use a dependency-free Python package with JSON fixtures, standard-library validators, `unittest` tests, and a small CLI-style eval runner for Waves 07-14 and 22.

Rationale: UiPath Labs access is pending, so the immediate build needs portable domain fixtures, deterministic policy behavior, and repeatable evals without assuming Maestro Case or Test Cloud APIs. Python standard library code keeps the local core easy to inspect and later map to UiPath artifacts.

Status: Accepted for local/provisional core. Revisit after UiPath Labs validation.

## D-013: Action Center Availability During Labs Spike

Decision: Treat Action Center/Actions as unavailable for the current `keepingitlowkey` / `DefaultTenant` validation run, and do not claim G-003 pass through Action Center.

Rationale: On 2026-06-24 20:30 IST, the Actions route redirected to `portal_/unregistered?serviceType=actions&organizationName=keepingitlowkey&tenantName=defaulttenant` and displayed `Actions is not enabled for this tenant` with session ID `32e450e2-89ca-4a80-a0c9-16df19a3d6b4`.

Status: Superseded. Actions was later enabled for `DefaultTenant`, and live Action Center task lifecycle/structured return is validated. The remaining G-003 caveat is generated UI legibility, covered by D-009.

## D-014: Maestro Case Spike Scope

Decision: Continue with focused Maestro Case validation only; do not start broad product implementation until a live case instance proves or rejects G-001, G-002, and G-004, and G-003 has a documented Action Center enablement or Case App/custom packet path.

Rationale: Automation Cloud, Maestro, Studio Web, and Maestro Case project creation are confirmed, but the hard gates require live state/audit/version/override evidence. Creating a validation-scoped `Maestro BPMN` solution and `Maestro Case` project is not enough to prove audit reconstruction or human evidence packet behavior.

Status: Superseded by live validation. G-001 through G-004 are answered with PASS/PARTIAL implications; proceed with the demo-safe proof path rather than broad implementation against unvalidated assumptions.

## D-015: Explicit Case Package Pinning And Custom Audit Payloads

Decision: Use explicit Case package version pinning plus custom structured audit/event payloads as the current implementation plan. Create direct processes with a chosen `--package-version` and `--no-auto-update`; treat active cases as pinned to their starting package, interpretation policy, and decision policy unless an explicit migration event is recorded.

Rationale: Live validation shows the Case process package is visible on case instances through `PackageKey`, and direct process creation can pin package versions. It also showed that the original solution-created process stayed on package `1.0.0` with `AutoUpdate` false despite an update command reporting success, so implicit update/migration is not reliable enough for the audit story. Separately, Action Center AppTask can return structured output into case variables, and raw agent recommendation plus final policy decision can be represented as separate structured HITL payload fields. Custom payloads preserve the required architecture boundary even if native Case history is incomplete.

Status: Accepted as the current implementation plan. Package `1.0.3` live validation proved task payload persistence and structured human return, including the raw agent recommendation and linked policy override decision. Reviewer page legibility still needs repair because the generated Action Center page rendered `PolicyDecisionJson` as `Unnamed String 1`.

## D-016: Demo-Safe Proof Path

Decision: Build the final proof path from the validated components:

- Action Center owns human task lifecycle and structured reviewer return.
- Custom evidence packet owns judge-readable proof of evidence state, raw agent recommendation, policy decision, block reason, recommended options, and route.
- Orchestrator bucket audit bundle owns durable UiPath-hosted domain audit evidence.
- Generated Action Center UI is not used as the final evidence-packet surface unless repaired and revalidated.

Rationale: Live validation answered the hard gates with partial native support. Native Case and Action Center provide the orchestration and human-review mechanics, but generated Action Center rendering hid or mislabeled proof-critical fields. The custom evidence packet and bucket-backed audit artifact preserve the architecture boundary without weakening the platform story or pretending the generated UI is demo-ready.

Status: Accepted as the implementation plan for the next build wave.
