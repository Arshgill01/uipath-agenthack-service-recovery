# Coding-Agent Proof Log

Status: final-lap submission evidence artifact.

Purpose: document the coding-agent bonus claim in a way judges can audit from GitHub and Devpost without trusting narration.

## Claim

Coding agent used: Codex.

Codex was used as a build-time coding agent for repository implementation, validation loops, UiPath CLI investigation, documentation, and submission packaging. Codex is not part of the runtime case authority. The runtime boundary remains:

> Agent interpretation is structured input. Deterministic policy decides allowed actions. UiPath Maestro Case routes the case. Humans own high-impact exceptions.

## Human And Agent Responsibilities

| Area | Human-owned decision | Codex contribution | Evidence |
| --- | --- | --- | --- |
| Product direction | Telecom service activation/restoration exception handling; primary track is Maestro Case. | Turned the direction into scoped docs, fixtures, policy/eval model, runbooks, and track evidence. | `PROJECT_BRIEF.md`, `PLAN.md`, `docs/submission/TRACK_SELECTION_DECISION.md`, `docs/research/AGENTHACK_FORUM_RESEARCH.md` |
| Safety boundary | LLM/Codex must not close cases, mutate production policy, or override source-of-truth hierarchy. | Encoded the boundary in tests, evals, proof artifacts, and do-not-claim docs. | `tests/`, `docs/validation/EVAL_PLAN.md`, `docs/submission/READINESS_CHECKLIST.md`, `docs/submission/SUBMISSION_BRIEF.md` |
| UiPath platform claims | Keep only evidence-backed claims; do not overclaim native audit, generated Action Center UI, or automated Test Cloud. | Ran CLI/readback loops, captured PASS/PARTIAL results, and wrote product-feedback evidence. | `docs/validation/VALIDATION_RESULTS.md`, `docs/product/PRODUCT_FEEDBACK_AWARD.md`, `docs/logs/BUILD_LOG.md` |
| Final submission packaging | Choose final Devpost story, video, team name, and survey choices. | Prepared README, proof log, Devpost-ready copy, readiness checklist, and demo beat. | `README.md`, this file, `docs/submission/SUBMISSION_BRIEF.md`, `docs/demo/DEMO_STORYBOARD.md` |

## Evidence Inventory

| Evidence | What it proves | Audit path |
| --- | --- | --- |
| README coding-agent section | Judges can find the claim from the GitHub front door. | `README.md` |
| This proof log | Names Codex, work performed, human boundaries, and proof paths. | `docs/submission/CODING_AGENT_PROOF_LOG.md` |
| Build log | Records agent work loops, commands, validation, and risks over time. | `docs/logs/BUILD_LOG.md` |
| Commit history | Shows a dense sequence of implementation, validation, proof, and workstream checkpoints. Commits use the repository's configured git identity, so use commit messages, branch names, and build-log entries together. | `git log --oneline --decorate --max-count=40` |
| Codex-prefixed branches/worktrees | Shows parallel coding-agent workstreams for forum research and product-feedback evidence. | `git branch --all --verbose --no-abbrev` |
| Local validation wrapper | Proves the current submission proof set can be checked without live tenant mutation. | `scripts/run_submission_check.sh` |
| Demo proof wrapper | Regenerates/verifies E-002/E-004 local proof artifacts. | `scripts/run_demo.sh` |
| Product-feedback workstream plan | Shows Codex was used to coordinate sustained evidence-gathering work rather than one shallow probe. | `docs/plans/PRODUCT_FEEDBACK_EVIDENCE_WORKSTREAM_PLAN.md` |
| Forum/Devpost research artifacts | Shows Codex gathered external submission/bonus requirements and preserved local scrape artifacts. | `docs/research/AGENTHACK_FORUM_RESEARCH.md`, `docs/research/artifacts/2026-06-27/` |

## Auditable Commit And Branch Evidence

These are representative local checkpoints visible in git history. They are not the full history.

| Date | Branch / commit | Codex-assisted work | Output |
| --- | --- | --- | --- |
| 2026-06-26 | `b7477e1` | Live Gemini interpreter proof hardening. | `docs/demo/artifacts/llm_interpreter_E003_live.json`, `scripts/run_llm_demo.sh` |
| 2026-06-26 | `c4c83ae` | Submission sanity wrapper. | `scripts/run_submission_check.sh` |
| 2026-06-26 | `8de69a3` | Terminal manual Test Manager execution repair. | `docs/validation/TEST_MANAGER_MAPPING.md`, JUnit evidence under `docs/validation/artifacts/test-manager-results/` |
| 2026-06-26 | `efa567e` | Data Fabric V2 audit-readback validation. | `docs/architecture/data_fabric/service_recovery_audit_bundle_v2_entity.json`, validation/readiness updates |
| 2026-06-27 | `45374ba`, `378d6d9` | Governed learning-loop artifact and demo/eval guardrail tightening. | `docs/demo/artifacts/policy_improvement_E008.json`, 46-test baseline |
| 2026-06-27 | `codex/forum-track-research`, `9f106e2` | Forum/Devpost research, track lock, first coding-agent proof package. | `docs/research/AGENTHACK_FORUM_RESEARCH.md`, `docs/submission/TRACK_SELECTION_DECISION.md`, this log |
| 2026-06-27 | `codex/product-feedback-evidence-sprint`, `92868f3`, `f4ff3e6` | Product-feedback evidence sprint. | PF-026, PF-027, PF-028, validation artifacts |
| 2026-06-27 | `codex/pf-evidence-maestro-authoring`, `c0f1432`, `732de38` | Maestro Case authoring/readiness evidence. | Scratch Case validation and Studio Web screenshot evidence |
| 2026-06-27 | `codex/pf-evidence-action-binding`, `8a72ea1` | Action Center generated-app binding/version evidence. | PF-013 strengthened with runtime/deployment evidence |
| 2026-06-27 | `codex/pf-evidence-test-manager`, `27bb351` | Test Manager eval-import and automation-discovery evidence. | PF-020, PF-021, PF-024 strengthened |
| 2026-06-27 | `codex/pf-evidence-data-fabric`, `d7a0a5c` | Data Fabric audit-readback diagnostics. | PF-018/PF-019/PF-023 updates, V2 readback reconfirmed |
| 2026-06-28 | `5eb0a85` | Integrated parallel evidence workstreams into `master`. | Current proof baseline before this final-lap pass |
| 2026-06-28 | `codex/final-demo-devpost-pack` | Prepare final-lap demo and Devpost submission pack. | Timed recording run-of-show, Devpost judging/copy checklist, pre-recording validation checklist, and build-log validation entry. |

Reproduce the local view:

```sh
git log --oneline --decorate --max-count=40
git branch --all --verbose --no-abbrev
```

## What Codex Helped Build

- Local service-recovery core: schemas, deterministic policy, state transitions, audit bundles, UiPath payload exporter, and evidence-packet renderer.
- Evals and tests: E-001 through E-009, hardening tests, invalid-output checks, override-persistence checks, and proof artifact verification.
- UiPath validation loops: Maestro Case, Action Center, Orchestrator bucket audit, Data Fabric V2 readback, Test Manager manual eval representation, and CLI diagnostics.
- Demo/submission artifacts: `scripts/run_demo.sh`, `scripts/run_submission_check.sh`, evidence packets, readiness checklist, submission brief, demo storyboard, and product-feedback answer material.
- Product-feedback evidence: PF-001 through PF-028, including parallel Codex worktrees for Maestro authoring, Action binding, Test Manager, and Data Fabric.

## Safety Boundaries For Devpost And Video

Do not imply:

- Codex is part of the runtime closure path.
- Codex mutates production policy.
- An LLM can close a case or override deterministic policy.
- Coding-agent usage replaces UiPath orchestration, Action Center accountability, or human review.

Use this wording:

> Codex helped build, test, validate, and document the solution. UiPath remains the runtime orchestration and governance layer, and deterministic policy owns closure decisions.

## Demo Beat

Use 10 to 20 seconds in the five-minute video:

1. Show the README coding-agent section.
2. Show this proof log and the commit/branch evidence table.
3. Show a terminal running `scripts/run_submission_check.sh` or its final passed output.
4. Say the boundary sentence above.

## Current Validation

Before citing this proof package as final, run:

```sh
git diff --check
scripts/run_submission_check.sh
```

Record the exact pass/fail result in `docs/logs/BUILD_LOG.md`.
