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

- Local service-recovery core exists and is committed.
- Local tests/evals should pass:
  - `python -m unittest discover -s tests`
  - `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- Current local validation baseline is 39 unit tests and E-001 through E-009 passing 9/9.
- UiPath CLI is installed locally as `uip` version `1.196.0`.
- UiPath Labs access is working for org `keepingitlowkey`, tenant `DefaultTenant`, user `arshgill6120@gmail.com`.
- Live validation has answered the hard gates with implementation implications:
  - G-001: native Case runtime audit is PARTIAL; custom `service-recovery-audit-v1` bundle stored in Orchestrator bucket is the validated one-object audit fallback.
  - G-002: PASS for explicit package/process/artifact policy-version pinning; native active-case migration must be represented as an explicit custom audit event.
  - G-003: PASS for Action Center lifecycle and structured reviewer return; PARTIAL for generated Action Center UI legibility. Use custom evidence-packet/audit surface for the final demo.
  - G-004: PASS for persisted raw Agent Interpretation Event and linked Policy Decision Event; PARTIAL only for generated Action Center display.
- Soft gates now have evidence:
  - G-005: live E-002/E-004 runs prove distinct missing/stale versus contradiction routes.
  - G-007: Test Manager project `SREV`, test set `SREV:9`, and manual execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad` represent E-001 through E-009; all manual logs passed, but the aggregate execution remained `Running`.
- Demo-safe proof path:
  - Action Center = lifecycle, assignment, reviewer action/comment, structured return.
  - Custom evidence packet = judge-readable proof surface.
  - Orchestrator bucket audit bundle = durable UiPath-hosted audit proof.
  - Do not rely on the generated Action Center page as the final evidence-packet UI unless repaired and revalidated.
- Repeatable local proof commands:
  - `scripts/run_demo.sh` regenerates/verifies E-002/E-004 proof artifacts without starting live UiPath work by default.
  - `scripts/run_llm_demo.sh --evidence-packet-output ...` can produce a fresh governed Gemini/Vertex JSON artifact and evidence-packet HTML when ADC/API auth is intentionally available.
  - `scripts/run_submission_check.sh` is the non-mutating final sanity check for tests, evals, committed proof artifacts, proof strings, and wrapper syntax.
- Live Gemini/Vertex proof artifacts exist:
  - `docs/demo/artifacts/llm_interpreter_E003_live.json`
  - `docs/demo/artifacts/llm_interpreter_E003_adversarial_live.json`
  - `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html`
  - `docs/demo/artifacts/evidence_packet_E003_adversarial_desktop.png`
  - `docs/demo/artifacts/evidence_packet_E003_adversarial_mobile.png`

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

The hard gates are answered enough to proceed with the validated demo-safe proof path. The local proof path is now repeatable. Next work should preserve the validated proof set and only run fresh live UiPath or Gemini operations when new IDs/artifacts are intentionally needed:

1. Run `scripts/run_submission_check.sh` before final submission and after any code/artifact change.
2. Keep the canonical green business fixture stable, changing only authoritative telemetry/inventory state between 2A and 2B.
3. Use the custom evidence packets and screenshots as the primary judge-readable surface.
4. Continue product-feedback logging during every UiPath interaction.

Do not restart broad platform validation unless new platform behavior contradicts the current evidence or a remaining partial item becomes demo-critical.

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
