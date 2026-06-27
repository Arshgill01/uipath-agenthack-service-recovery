# Coding-Agent Proof Log

Status: active submission evidence log.

Purpose: satisfy the AgentHack coding-agent bonus requirement by documenting which coding agent was used, how it contributed, and what verifiable evidence exists in the repo.

## Summary

Coding agent used: Codex.

Role in project:

- designed and implemented the local service-recovery core,
- built deterministic policy/eval/test scaffolding,
- generated evidence-packet and audit artifacts,
- drove UiPath CLI validation and readback loops,
- captured product-feedback evidence and submission runbooks,
- created the final readiness, demo, and feedback documentation.

Human role:

- selected business direction,
- challenged shallow agent work,
- prioritized real UiPath product evidence,
- approved architecture constraints and final positioning,
- owns team name, story-sharing preference, and final submission decisions.

## Evidence Inventory

| Evidence | What it proves | Path / reference |
| --- | --- | --- |
| Repository commit history | Codex-authored checkpoints across core, evals, demo artifacts, product feedback, and submission docs. | `git log --oneline` |
| Build log | Agentic work loops, validation commands, and checkpoints. | `docs/logs/BUILD_LOG.md` |
| Product-feedback workstream plan | Codex-managed multi-thread evidence gathering after user correction. | `docs/plans/PRODUCT_FEEDBACK_EVIDENCE_WORKSTREAM_PLAN.md` |
| Forum research artifacts | Codex scraped and analyzed official/forum evidence for track and bonus alignment. | `docs/research/artifacts/2026-06-27/` |
| Submission sanity script | Codex-maintained non-mutating validation wrapper. | `scripts/run_submission_check.sh` |
| Evals and tests | Codex-built regression proof for policy boundary and agent usefulness. | `tests/`, `service_recovery_core/evals.py` |

## Prompt / Thread Evidence

| Date | Thread / branch | Agent task | Output |
| --- | --- | --- | --- |
| 2026-06-27 | `master`, commits `45374ba`, `378d6d9` | Improve competition readiness: governed learning-loop artifact, demo proof, eval guardrails. | `docs/demo/artifacts/policy_improvement_E008.json`, updated demo/readiness docs, 46 tests passing. |
| 2026-06-27 | `codex/product-feedback-evidence-sprint`, commits `92868f3`, `f4ff3e6` | Gather fresh UiPath product-feedback evidence. | PF-026, PF-027, PF-028 and scratch Case evidence artifacts. |
| 2026-06-27 | `master`, commit `c5509ed` | Correct shallow one-probe workflow and create sustained evidence workstreams. | `docs/plans/PRODUCT_FEEDBACK_EVIDENCE_WORKSTREAM_PLAN.md`, four worktree evidence threads queued. |
| 2026-06-27 | `codex/forum-track-research` | Scrape forum/Devpost/winner evidence and lock track/coding-agent documentation. | This log, track decision memo, forum research digest, README coding-agent section. |
| 2026-06-27 | `codex/pf-evidence-maestro-authoring`, commits `c0f1432`, `732de38` | Gather Maestro Case human-review authoring/readiness evidence. | PF-028 repair probe, Studio Web screenshots, validation/build log entries. |
| 2026-06-27 | `codex/pf-evidence-action-binding`, commit `8a72ea1` | Gather Action Center generated-app binding/version evidence. | PF-013 binding probe showing runtime used older app deployment while newer designer version existed. |
| 2026-06-27 | `codex/pf-evidence-test-manager`, commit `27bb351` | Gather Test Manager eval-import and automation-discovery evidence. | PF-020, PF-021, PF-024 strengthened; terminal manual execution preserved; automated Test Cloud remains unclaimed. |
| 2026-06-27 | `codex/pf-evidence-data-fabric`, commit `d7a0a5c` | Gather Data Fabric audit-readback diagnostics. | PF-018 improved for current CLI discovery; PF-019/PF-023 strengthened; V2 audit proof path reconfirmed. |

## Demo Beat To Include

Use a short 10 to 20 second beat in the five-minute video:

1. Show the GitHub README section naming Codex as the coding agent.
2. Show `docs/submission/CODING_AGENT_PROOF_LOG.md`.
3. Show a terminal running `scripts/run_submission_check.sh` or the final passed output.
4. State: "Codex helped build the code, evals, UiPath validation runbooks, and product-feedback evidence, but deterministic policy remains the runtime decision authority."

## Guardrails

Do not imply:

- Codex is part of the runtime closure authority.
- Codex mutates production policy.
- Coding-agent usage replaces UiPath orchestration.

The submission claim is:

> Codex accelerated build, validation, and documentation. UiPath remains the orchestration and governance layer for the solution.
