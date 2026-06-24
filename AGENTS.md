# AGENTS.md

Repository operating rules for agents building the UiPath AgentHack service-recovery project.

## Mission

Build a working **UiPath AgentHack Maestro Case** submission:

> Telecom/broadband service activation and restoration exception handling, proving governed agentic recovery when authoritative evidence is missing, stale, or contradicting business-system state.

Architecture thesis:

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

## Winning Posture

- Primary target: Grand Prize.
- Primary track: Maestro Case, unless platform validation disproves feasibility.
- Special-award targets: Best Demo/Presentation, Best Cross-Platform Integration, and especially **Best Product Feedback**.
- Product feedback is not an afterthought. Every UiPath Labs friction point, confusing doc, missing feature, workaround, bug, rough edge, and improvement idea must be captured while it is fresh.

## Current Status

- Local provisional core exists and is committed.
- Local tests/evals should pass:
  - `python -m unittest discover -s tests`
  - `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- UiPath CLI was installed locally in a prior run as `uip` version `1.196.0`.
- A prior Wave 01 attempt was blocked at `portal_/missingaccount`; if the user now has working Labs access, rerun Wave 01 before continuing.
- Hard UiPath gates G-001 through G-004 are still the next critical checkpoint unless newer validation results prove otherwise.

If this status conflicts with newer entries in `docs/validation/VALIDATION_RESULTS.md`, `docs/logs/BUILD_LOG.md`, or `docs/decisions/DECISIONS.md`, trust the newer dated evidence and update this section in the same commit.

## Non-Negotiables

- Do not turn this into a generic AI governance platform.
- Do not build real telecom integrations; use honest simulated systems unless a real connector is trivial and low-risk.
- Do not let the LLM close cases, override policy, override source-of-truth hierarchy, or mutate production policy.
- Agent output must be structured. Policy must not parse prose.
- Extracted claims from notes/messages never override authoritative structured evidence.
- Closure requires fresh authoritative telemetry.
- Missing/stale evidence and contradicting evidence must route differently.
- Raw agent recommendation and final policy decision must persist as separate linked events.
- Do not claim validation unless the exact command or UiPath run was performed.

## Required Work Loop

For every substantial run:

1. **Orient**: read this file, `PROJECT_BRIEF.md`, `PLAN.md`, active wave file, and relevant architecture/validation docs.
2. **Plan**: state the wave/gate, assumption being tested, files likely affected, and validation command(s).
3. **Act**: make the smallest scoped change or validation run.
4. **Observe**: capture exact command output, UiPath behavior, screenshots/notes if relevant.
5. **Evaluate**: compare observed behavior against the documented pass condition.
6. **Log**: update required docs before finishing.
7. **Commit/push**: commit meaningful checkpoints so other agents see the same state.

Stop instead of improvising if access is blocked, a hard gate fails, platform behavior contradicts the architecture, or implementation would begin before required validation.

## Required Logs

Update these as applicable:

- `docs/logs/BUILD_LOG.md`: changes, commands, validation status.
- `docs/validation/VALIDATION_RESULTS.md`: UiPath/platform/eval results.
- `docs/logs/RISK_REGISTER.md`: open risks and mitigations.
- `docs/decisions/DECISIONS.md`: material decisions.
- `docs/research/RESEARCH_LOG.md`: new sourced research.
- `docs/product/PRODUCT_FEEDBACK_AWARD.md`: all UiPath product feedback evidence.

`AGENTS.md` is the control file future agents will follow. Edit it only for durable operating rules or major status changes; keep it concise.

## Immediate Priority

If UiPath Labs access is now working, run:

1. Wave 01: platform access and inventory.
2. G-001: Native Case State / Audit Reconstruction.
3. G-002: Policy Version Pinning.
4. G-003: Human Evidence Packet.
5. G-004: Agent Recommendation Visible Before Override.

Do not start broad UiPath implementation until G-001 through G-004 are PASS/PARTIAL with documented implications or explicitly waived in `docs/decisions/DECISIONS.md`.

## Product Feedback Award Discipline

The team wants to seriously compete for the **Best Product Feedback** award.

During every UiPath interaction, capture:

- product surface and exact workflow,
- what worked,
- what failed or confused the builder,
- expected behavior vs observed behavior,
- workaround used,
- severity/impact on hackathon build,
- concrete product improvement suggestion,
- screenshots or artifact references if available.

High-quality feedback is specific, reproducible, impact-oriented, and fair. Do not rant. Do not invent issues. Separate user error, documentation ambiguity, missing access, product limitation, and actual defect.

## Definition Of Done

A wave is done only when:

- requested scope is implemented or clearly blocked,
- required logs are updated,
- validation was run or the reason it could not run is documented,
- no unrelated refactors were made,
- assumptions are explicit,
- changes are committed and pushed when meaningful.

Final reports must include: what changed, commands run, pass/fail status, files updated, commit hash if pushed, and open risks.
