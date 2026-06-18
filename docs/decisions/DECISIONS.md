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
