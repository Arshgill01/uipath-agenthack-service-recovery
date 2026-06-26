# Candidate Branch Review

Status: current merge-readiness review for candidate work produced outside `master`.

Reviewed on: 2026-06-26.

Base reviewed: `master` at `80afa5c`.

## Summary

Do not merge the candidate branches wholesale.

`master` already contains the stronger LLM/adversarial implementation: bounded repair loop, strict closure-candidate validation, adversarial policy signal, evidence-packet rendering, live Vertex artifacts, and submission sanity checks. The LLM candidate branch is older and would regress those guarantees.

The UI candidate branch has some useful spacing and visual hierarchy ideas, but it predates the current adversarial packet, imports external Google Fonts, and pushes the evidence packet toward a warm decorative theme that is less operational than the current telecom service-recovery proof surface.

## Branch Verdicts

| Branch | Verdict | Reason |
| --- | --- | --- |
| `feature/llm-engine-adv` (`7179637`) | Reject as direct merge; cherry-pick nothing without re-review. | It includes a committed `test_output.log`, weakens `closure_candidate` confidence validation for adversarial payloads, and is behind the current `master` LLM implementation. |
| `feature/ui-design` (`74c09fb`) | Rework/cherry-pick only. | It touches only `service_recovery_core/evidence_packet_view.py`, but drops the current adversarial section if merged as-is and adds external font dependency/theme choices that are not demo-critical. |
| `feature/service-recovery-combined` (`34d18cc`) | Do not merge. | Combined branch inherits the risks above and should not override the already validated mainline proof path. |

## LLM Review Notes

Observed diff:

- `scripts/run_llm_demo.sh`
- `service_recovery_core/agent_validator.py`
- `service_recovery_core/enums.py`
- `service_recovery_core/evidence_packet_view.py`
- `service_recovery_core/llm_interpreter.py`
- `service_recovery_core/policy.py`
- `service_recovery_core/uipath_payload.py`
- `tests/test_llm_interpreter.py`
- `test_output.log`

Merge blockers:

- `service_recovery_core/agent_validator.py` changes the closure-candidate confidence rule so adversarial payloads can keep `closure_candidate` with confidence below `0.75`. This conflicts with `docs/architecture/AGENT_CONTRACT.md`, which states adversarial mode does not relax validation.
- The branch contains `test_output.log` with failing test output and should not be committed to the product branch.
- The branch has less complete LLM behavior than `master`; current mainline already repairs observed live schema drift and validates live adversarial artifact rendering.

What to preserve:

- The advocate/skeptic concept is already preserved on `master`.
- The structured disagreement signal is already preserved on `master`.
- The evidence-packet adversarial panel is already preserved on `master`.

## UI Review Notes

Observed diff:

- `service_recovery_core/evidence_packet_view.py`

Merge blockers:

- The branch version predates the current adversarial packet code and would remove or conflict with `Adversarial dual interpretation` rendering.
- The CSS uses `@import` from Google Fonts. Evidence packets should remain self-contained and reliable offline during judging or recording.
- The palette and copy comments lean into a decorative Japanese-paper concept. The current product should read as telecom service recovery operations: clear, authoritative, and audit-focused.
- The branch adds hover motion and decorative shadows across dense proof panels. That is not necessary for a recorded audit surface and increases screenshot variability.

Reusable ideas:

- Slightly stronger table spacing.
- More deliberate route-banner treatment.
- Compact rectangular status chips.
- More visible side-by-side agent/policy comparison.

Implementation rule:

If UI polish continues, apply these ideas manually to the current `master` renderer and verify desktop/mobile screenshots. Do not merge the branch file over current mainline.

## Validation Performed

Commands:

- `git status --short --branch`
- `git log --oneline -5`
- `git worktree list`
- `git branch --all --verbose --no-abbrev`
- `git diff --stat master...feature/llm-engine-adv`
- `git log --oneline master..feature/llm-engine-adv`
- `git diff --name-status master...feature/llm-engine-adv`
- `git diff master...feature/llm-engine-adv -- service_recovery_core/llm_interpreter.py service_recovery_core/policy.py service_recovery_core/agent_validator.py service_recovery_core/enums.py tests/test_llm_interpreter.py`
- `git show feature/llm-engine-adv:test_output.log`
- `git diff --stat master...feature/ui-design`
- `git log --oneline master..feature/ui-design`
- `git diff --name-status master...feature/ui-design`
- `git diff master...feature/ui-design -- service_recovery_core/evidence_packet_view.py`
- `scripts/run_submission_check.sh`
- `git diff --check`

Results:

- PASS: `scripts/run_submission_check.sh` passed on current `master` with 39 tests and proof artifact checks.
- PASS: `git diff --check` passed before this review document was added.
- Review finding: candidate branches are not direct-merge safe.

## Next Loop

Use `docs/plans/LONG_RUNNING_AGENTIC_LOOP_RUNBOOK.md` as the operating loop. The next high-value implementation chunk is selective evidence-packet polish on current `master`, not branch merging.

Acceptance criteria for that chunk:

- preserve adversarial rendering,
- preserve raw AIE and linked PDE side by side,
- keep the packet self-contained with no external assets,
- run `scripts/run_submission_check.sh`,
- regenerate and visually inspect desktop/mobile screenshots if renderer CSS changes.
