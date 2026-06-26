# Long-Running Agentic Loop Runbook

Status: active operating runbook for multi-hour improvement chunks.

Objective: improve the validated service-recovery submission through sustained, verifiable work loops that preserve the architecture boundary, improve judge-facing proof, and keep product-feedback evidence fresh.

## Current Baseline

- Hard gates G-001 through G-004 have enough live UiPath evidence to proceed on the demo-safe proof path.
- Action Center proves task lifecycle and structured reviewer return.
- Custom evidence packets are the judge-readable proof surface.
- Orchestrator bucket audit bundles are the durable UiPath-hosted audit fallback.
- Generated Action Center UI is not final-demo safe unless repaired and revalidated.
- Local E-001 through E-009 evals pass.
- Live Gemini/Vertex standard and adversarial LLM paths are validated, including the live `high_interpretation_disagreement` artifact.
- Branches `feature/llm-engine-adv`, `feature/ui-design`, and `feature/service-recovery-combined` are review inputs only; do not merge them wholesale.

## Work Loop

Run one substantial chunk at a time. A chunk should target 2 to 4 hours unless a stop condition is hit.

1. Orient
   - Read `AGENTS.md`, `PROJECT_BRIEF.md`, `PLAN.md`, `docs/submission/READINESS_CHECKLIST.md`, and the files touched by the chunk.
   - Check `git status --short --branch`.
   - Treat uncommitted changes as someone else's work unless you made them in the current loop.

2. Select one winning outcome
   - Pick one outcome: demo clarity, repeatability, product feedback quality, cross-platform proof, eval confidence, or submission accuracy.
   - State likely files and exact validation commands before editing.

3. Act in narrow slices
   - Preserve: agents interpret, policy decides, Maestro routes, humans own high-impact exceptions.
   - Keep raw Agent Interpretation Event and linked Policy Decision Event separate.
   - Keep E-002 and E-004 on the same canonical green business fixture, changing only authoritative telemetry or inventory evidence.
   - Do not add generic platform features.

4. Verify before broadening
   - Run targeted tests first.
   - Run broader gates before committing behavior or artifact changes.
   - For UiPath claims, require live readback, screenshots, task IDs, case/job IDs, or committed artifact evidence.

5. Log
   - Update `docs/logs/BUILD_LOG.md` for substantial work.
   - Update `docs/validation/VALIDATION_RESULTS.md` for new UiPath or eval validation.
   - Update `docs/product/PRODUCT_FEEDBACK_AWARD.md` for every new UiPath interaction.
   - Update `docs/logs/RISK_REGISTER.md` when risk changes.
   - Update `docs/decisions/DECISIONS.md` only for material decisions.

6. Commit and push
   - Run `git diff --check`.
   - Run the selected validation commands.
   - Inspect `git diff --stat` and `git status --short`.
   - Commit meaningful checkpoints and push.

## Standard Validation Set

Use this set for behavior, policy, demo artifact, or submission-readiness changes:

```sh
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
python -m service_recovery_core.demo_proof --output-dir docs/demo/artifacts --verify-only
bash -n scripts/run_llm_demo.sh
git diff --check
```

Use this for live adversarial LLM readback when prompt/model/scoring changes:

```sh
scripts/run_llm_demo.sh \
  --scenario-id E-003 \
  --model gemini-2.5-flash \
  --project project-61c59251-6618-46b7-a8c \
  --location us-central1 \
  --adversarial \
  --output eval_results/llm_interpreter_E003_adversarial_live.json
```

Promote the live output only if it validates and shows:

- advocate recommendation `closure_candidate`,
- skeptic recommendation different from advocate,
- disagreement score at or above `0.60`,
- policy reason `high_interpretation_disagreement`,
- final route `human_review`.

## Acceptance Gates

### A. Architecture Boundary

Accept only if:

- agent output remains structured,
- policy does not parse prose,
- source-of-truth hierarchy is preserved,
- closure requires fresh authoritative telemetry,
- missing/stale evidence and contradiction route differently,
- active cases remain pinned to policy versions unless explicitly migrated.

Stop if an edit lets the LLM close cases, mutate policy, override authoritative evidence, or hide the raw recommendation.

### B. Demo Proof

Accept only if:

- E-002 shows green business state, missing/stale authoritative telemetry, raw `closure_candidate`, policy override, and route to verification/retry.
- E-004 uses the same green business fixture, fresh authoritative contradiction, elevated severity, and human review.
- Evidence packets show raw AIE, linked PDE, block reason, route, policy versions, and audit order.
- Mobile and desktop packet checks do not hide proof-critical fields.

### C. UiPath Evidence

Accept only if:

- live claims cite command output, screenshots, task IDs, process IDs, bucket paths, or committed validation logs,
- Test Manager claims remain manual representation unless automated execution is actually validated,
- Data Fabric persistence is not claimed without successful insert and readback,
- product feedback is fair, specific, reproducible, and evidence-backed.

### D. Submission Quality

Accept only if the chunk makes the submission more likely to win by improving at least one:

- judge-readable proof,
- repeatable demo execution,
- product feedback award material,
- cross-platform integration evidence,
- eval/regression confidence,
- final copy accuracy.

## Priority Chunks

1. Demo proof hardening
   - Improve evidence-packet clarity and verification for E-002/E-004.
   - Preserve adversarial rendering and table responsiveness.
   - Do not depend on generated Action Center UI.

2. Product feedback award polish
   - Curate PF entries into survey-ready, high-impact product feedback.
   - Separate access confusion, docs ambiguity, product limitation, and defect.
   - Preserve what worked, not just failures.

3. Live UiPath rerun safety
   - Make read-only validation commands explicit.
   - Mark every tenant-mutating step.
   - Capture required evidence before claiming live status.

4. Adversarial LLM proof polish
   - Re-run live Vertex only if prompt/model/scoring changes.
   - Keep repair bounded and validator strict.
   - Render a dedicated adversarial packet only if it becomes part of the final demo.

5. Submission narrative accuracy
   - Keep the story telecom service recovery, not a generic governance platform.
   - Make the core beat: AI interprets, policy governs, Maestro routes, human reviews exceptions.

## Stop Conditions

Stop and report if:

- a hard architecture boundary is contradicted,
- UiPath auth/session is unavailable for a required live validation,
- a hard gate changes from pass/partial to fail,
- generated Action Center UI becomes the only available proof surface,
- tests/evals fail and the cause is not understood,
- the next step would mutate UiPath tenant services or credentials without explicit user approval.
