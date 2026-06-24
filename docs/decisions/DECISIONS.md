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

Decision: If Action Center cannot render the evidence packet clearly, use a Case App/custom evidence-packet view even if Action Center technically works.

Rationale: Demo legibility matters. The human reviewer must see evidence, agent output, policy decision, block reason, and allowed actions.

Status: Accepted, pending validation.

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

Status: Accepted for the current spike. Revisit only if Actions is enabled or a different tenant is provided.

## D-014: Maestro Case Spike Scope

Decision: Continue with focused Maestro Case validation only; do not start broad product implementation until a live case instance proves or rejects G-001, G-002, and G-004, and G-003 has a documented Action Center enablement or Case App/custom packet path.

Rationale: Automation Cloud, Maestro, Studio Web, and Maestro Case project creation are confirmed, but the hard gates require live state/audit/version/override evidence. Creating a validation-scoped `Maestro BPMN` solution and `Maestro Case` project is not enough to prove audit reconstruction or human evidence packet behavior.

Status: Accepted.
