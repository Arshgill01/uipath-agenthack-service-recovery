# Agentic Loop Competition Improvement Plan

Date: 2026-06-27.

Purpose: convert the current repository, validation evidence, and UiPath AgentHack rules into a focused improvement loop. This plan treats "moves" from the voice note as agentic loops. RAM is not relevant.

## Current Read

The project is not a blank prototype. It already has a working local service-recovery core, live UiPath validation evidence, custom proof artifacts, and curated product-feedback material.

The strongest architecture remains:

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

This is a strong fit for Track 1, UiPath Maestro Case. The public Devpost framing asks for real working solutions on UiPath Automation Cloud, UiPath as the execution/orchestration layer, dynamic casework for Maestro Case, human control, exception handling, and visible platform usage. The repo's validated demo-safe path maps to that directly:

- Maestro Case / Action Center: lifecycle, task assignment, reviewer action/comment, structured return.
- Custom evidence packet: judge-readable proof where generated Action Center UI was not reliable.
- Data Fabric V2 and Orchestrator bucket: UiPath-hosted audit proof.
- Test Manager: honest manual eval representation, not automated Test Cloud execution.
- UiPath CLI/Codex workflow: coding-agent bonus evidence.

## What Is Actually Strong

1. The core boundary is implemented, not just narrated.
   `service_recovery_core/agent_validator.py`, `policy.py`, `state_machine.py`, and `audit_bundle.py` preserve separate Agent Interpretation Events and Policy Decision Events.

2. The most important demo contrast is crisp.
   E-002/E-003/E-004 use the same green business fixture and differ on authoritative telemetry. Missing/stale evidence routes to verification; contradiction routes to human review.

3. Product feedback is unusually evidence-backed.
   PF-001 through PF-025 separate access friction, UX/docs issues, product defect candidates, platform limitations, workarounds, and proof impact. The strongest award claim is the Maestro Case human-review readiness/preflight recommendation.

4. The live UiPath story is honest.
   The repo does not overclaim native Case audit, generated Action Center UI, or automated Test Cloud. That restraint is a competitive advantage because the feedback is credible.

5. The optional LLM path strengthens the architecture.
   The Gemini/Vertex interpreter and adversarial advocate/skeptic path add modern agentic behavior without letting the LLM close cases or mutate policy.

## Gaps That Matter

These are the gaps worth improving. Everything else is lower leverage.

1. Demo proof needs one sharper "why UiPath" moment.
   The custom packet is readable, but the final narrative should make the UiPath role unmistakable: Maestro Case owns the work lifecycle; Action Center owns human accountability; Data Fabric/Orchestrator own audit evidence; Test Manager owns eval representation.

2. Product feedback can be made more award-shaped.
   The raw feedback is strong, but the final survey should lead with one unifying recommendation, then support it with concrete PF evidence. Avoid listing every issue equally.

3. The learning loop artifact is still more design than product moment.
   E-008 generates a usefulness incident, and `docs/architecture/POLICY_IMPROVEMENT_LOOP.md` describes the governance loop. A judge-facing artifact should show a policy improvement case with trigger, proposed diff, eval result, human approval status, and next policy version.

4. Eval breadth is adequate but not "max confidence."
   Nine scenarios cover the core beats. Additional evals should be added only if they support the demo story: stale-but-green closure pressure, contradiction plus customer pressure, and generated Action Center/UI fallback proof.

5. Submission copy had one stale fact.
   `docs/submission/SUBMISSION_BRIEF.md` said 39 tests while current validation reports 43.

## Loop Mechanism

Use one competition-improvement loop at a time:

1. Goal: select one outcome that improves judging odds.
2. Evidence: identify the repo files, validation facts, and Devpost criterion it touches.
3. Move: make the smallest change that can improve that outcome.
4. Verify: run targeted validation first, then `scripts/run_submission_check.sh` when artifacts or final copy change.
5. Reflect: update build log, risk/validation/product-feedback docs only if the evidence changed.
6. Gate: continue only if the change improves at least one of demo clarity, platform usage depth, product-feedback quality, eval confidence, or submission accuracy.

Stop if a move would weaken the policy boundary, invent unvalidated UiPath claims, add generic platform scope, mutate live UiPath tenant state without intent, or create broad code churn.

## Priority Moves

### Move 1: Feedback Award Finalization

Outcome: make the Best Product Feedback submission read like a single high-impact product insight, not a complaint inventory.

Files likely affected:

- `docs/product/FEEDBACK_SURVEY_FINAL_DRAFT.md`
- `docs/product/FEEDBACK_SURVEY_COPY_READY.md`
- `docs/product/FEEDBACK_AWARD_APPENDIX.md`

Acceptance:

- One primary recommendation: Maestro Case human-review readiness/preflight.
- Supporting evidence cites PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, and PF-019/PF-023 as secondary audit/storage support.
- Positive platform findings remain visible.
- No automated Test Cloud, native Case full-audit, or generated Action Center final-UI claim is introduced.

Validation:

- `rg -n "automated Test Cloud|generated Action Center UI is final|native Case history alone|generic governance" docs/product docs/submission`
- `scripts/run_submission_check.sh`

### Move 2: Judge-Facing Learning Loop Artifact

Outcome: turn E-008 and the policy improvement loop into a visible governed-learning proof.

Files likely affected:

- `service_recovery_core/evals.py`
- `service_recovery_core/evidence_packet_view.py` or a small new renderer if existing packet shape should remain stable
- `docs/architecture/POLICY_IMPROVEMENT_LOOP.md`
- tests under `tests/`
- demo artifacts under `docs/demo/artifacts/`

Acceptance:

- A policy improvement artifact exists with trigger, sample cases, proposed change type, proposed diff summary, eval result, approval status, current policy version, and proposed next version.
- The artifact does not auto-promote policy.
- Unit tests assert that E-008 generates the artifact and keeps active cases pinned.

Validation:

- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- `scripts/run_submission_check.sh`

### Move 3: Demo Proof Tightening

Outcome: make the five-minute demo easier to follow without adding new platform claims.

Files likely affected:

- `docs/demo/DEMO_STORYBOARD.md`
- `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`
- `docs/submission/SUBMISSION_BRIEF.md`
- evidence packet renderer only if proof-critical UI text is unclear

Acceptance:

- The demo explicitly shows: AIE closure recommendation, PDE override, final route, policy versions, evidence state, UiPath surface responsibility.
- 2A and 2B remain tied to the same green business fixture.
- The adversarial LLM beat is supplemental, not a replacement for E-002/E-004 UiPath proof.

Validation:

- `python -m service_recovery_core.demo_proof --output-dir docs/demo/artifacts --verify-only`
- `scripts/run_submission_check.sh`

### Move 4: Targeted Eval Hardening

Outcome: add only evals that improve confidence in the current story.

Candidate evals:

- Contradiction plus customer pressure still routes to human review; pressure never overrides telemetry.
- Stale telemetry plus high-confidence LLM closure still routes to verification.
- Policy improvement artifact remains proposal-only until approved.

Acceptance:

- New evals are named and mapped in `docs/validation/EVAL_PLAN.md`.
- No generic failure taxonomy expansion.
- Tests stay focused and readable.

Validation:

- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`

## Recommendation

Do the moves in this order:

1. Feedback Award Finalization.
2. Judge-Facing Learning Loop Artifact.
3. Demo Proof Tightening.
4. Targeted Eval Hardening.

Do not restart broad UiPath validation. Run fresh live UiPath or Gemini work only when a new final artifact or ID is intentionally needed.
