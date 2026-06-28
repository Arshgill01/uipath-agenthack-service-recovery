# Wave 41: Final Substantive Differentiation Pass

## Goal

Find and implement the last high-leverage improvements that make the submission feel distinct without broadening scope or adding noise.

This wave is not for stale-doc cleanup, cosmetic refactors, or generic polishing. Useful work must strengthen one of these claims:

- Maestro Case coordinates governed telecom service recovery better than a hand-stitched workflow.
- The agent is useful but cannot close, override policy, or mutate policy.
- Missing/stale evidence and contradicting evidence route differently and visibly.
- The product-feedback story is backed by reproduced UiPath build friction and clear improvement proposals.
- The final codebase is simpler, more modular, and easier to review without weakening validated proof.

## Candidate Workstreams

1. **Novel Maestro/Policy Slice**
   - Deepen the core case behavior with a small concrete slice that judges can understand quickly.
   - Prefer evidence-state routing, adversarial interpretation disagreement, reviewer packets, policy-improvement case handoff, or SLA/impact handling.
   - Do not add real telecom integrations or let the LLM make final decisions.

2. **Eval and Proof Hardening**
   - Add scenario-level proof or regression checks that catch shallow implementations.
   - Prefer tests that assert the agent/policy boundary, route differences, audit linkage, and claim boundaries.
   - Keep Test Cloud claims manual unless a real automated path is validated.

3. **Product Feedback Research and Form Strengthening**
   - Improve the feedback thesis with current, sourced UiPath/AgentHack context and stronger Microsoft Form copy.
   - Do not paste internal PF labels into form-facing answers.
   - Separate reproduced build evidence from forum context and from product recommendations.

4. **Codex/Coding-Agent Bonus Evidence**
   - Strengthen proof that Codex materially helped build, validate, and document the project.
   - Prefer concrete logs, branches, commits, prompts, and demo beats.
   - Do not imply Codex has runtime closure authority.

5. **Simplification and Core Code Quality**
   - Reduce complexity in the local core where it improves reviewability.
   - Prefer boring names, smaller functions, stronger tests, and removal of noise introduced by earlier waves.
   - Do not refactor validated proof paths unless tests and submission checks remain green.

## Review Standard

Useful changes should be merged only if they:

- improve a judge-visible or validation-visible claim,
- preserve all existing claim boundaries,
- pass targeted validation,
- update required logs,
- avoid broad speculative abstractions.

Shallow changes should be rejected or sent back for another pass.

## Validation

Run targeted tests for changed code. Before merging to `master`, run:

```bash
scripts/run_submission_check.sh
```

Document any skipped live UiPath or Gemini operation explicitly.
