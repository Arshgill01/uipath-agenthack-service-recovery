# Final Video Script Plan

Date: 2026-06-30.

Objective: produce a detailed, word-for-word final demo video script that can be recorded one-to-one, stays under the five-minute Devpost limit, and matches the current ClearPath Recovery submission artifacts.

## Scope

- Create the main script in `docs/demo/FINAL_VIDEO_MAIN_SCRIPT.md`.
- Anchor the recording to the 13-page main deck, UiPath platform surfaces, evidence packets, eval/learning-loop artifact, product-feedback proof, coding-agent proof, and final validation output.
- Preserve validated claim boundaries: no automated Test Cloud claim, no generated Action Center UI readiness claim, no real telecom integration claim, no native Case-history-only audit claim, and no LLM/Codex runtime authority claim.

## Inputs Read

- `AGENTS.md`
- `PROJECT_BRIEF.md`
- `PLAN.md`
- `docs/validation/VALIDATION_GATES.md`
- `docs/validation/EVAL_PLAN.md`
- `docs/demo/DEMO_STORYBOARD.md`
- `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`
- `docs/submission/SUBMISSION_BRIEF.md`
- `docs/submission/READINESS_CHECKLIST.md`
- `docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md`
- `docs/submission/CODING_AGENT_DEMO_BEAT_CHECKLIST.md`
- `docs/submission/presentation_deck/organizer_template_adaptation_guide.md`
- `docs/submission/presentation_deck/governed_service_recovery_kami_deck.html`
- `docs/product/FEEDBACK_AWARD_APPENDIX.md`
- `waves/38_demo_video_script.md`
- `waves/39_final_validation.md`

## Verification Loop

1. Pass 1: structural coverage against deck, storyboard, and required proof beats.
2. Pass 2: claim-boundary audit against readiness/proof-map non-claims.
3. Pass 3: timing and delivery audit for a natural spoken five-minute script.
4. Pass 4: artifact/path audit plus repo validation.

## Validation Commands

- `rg` scans over the script for required and forbidden claim language.
- `git diff --check`
- `scripts/run_submission_check.sh`

## Acceptance

- Script gives exact screen/deck timing and word-for-word narration.
- Script includes visible instructions for what to point at on each proof surface.
- Script keeps one canonical story: agents interpret, policy decides, Maestro routes, humans own exceptions.
- Script is detailed enough to record from directly, without sounding robotic.
