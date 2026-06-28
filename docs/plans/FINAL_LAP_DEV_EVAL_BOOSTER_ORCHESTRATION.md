# Final-Lap Dev/Eval Booster Orchestration

Date: 2026-06-28.

Objective: improve the final submission with real code, generated artifacts, and eval/verifier coverage while preserving the validated claim boundaries. This plan is the main-thread control plane for parallel worker threads and final integration review.

## Risk Classification

Do not try to "resolve" these by weakening the architecture:

- Real telecom integrations: intentional non-goal. The submission uses honest simulated telecom systems.
- LLM or Codex closure authority: intentional non-goal. Agents recommend; deterministic policy decides; humans own high-impact exceptions.

Reducible only with fresh proof:

- Automated Test Cloud execution: may be claimed only after a successful UiPath automated execution and readback. Until then, the validated claim is local eval plus Test Manager manual representation/execution.
- Generated Action Center UI final-demo readiness: may be claimed only after a fresh runtime task shows proof-critical fields with readable labels. Until then, Action Center proves lifecycle and structured return, while custom packets are judge-readable.
- Native Maestro Case history alone as full G-001 audit proof: currently partial. Full audit proof remains Data Fabric V2 and Orchestrator bucket custom payload readback.

## Active Workstreams

| Workstream | Thread | Goal | Acceptance |
| --- | --- | --- | --- |
| Policy boundary eval hardening | `019f0de4-fe5e-7770-883a-e7ebbb4fef50` | Add a deterministic local eval report for source authority, override persistence, confidence guardrails, and fixture discipline. | Code/tests pass and `run_submission_check.sh` regenerates the report under `/tmp`. |
| Test Manager bridge | `019f0de4-fe5e-7770-883a-e7d8a01763c5` | Recheck automated Test Cloud feasibility read-only, then strengthen the manual Test Manager evidence bridge if automation remains unproven. | Verifier joins local eval JSON, exported JUnit, and execution stats while preserving the non-automated claim boundary. |
| Action Center UI claim hardening | `019f0de4-ff7f-75e2-9692-f78c66e89aa5` | Determine whether generated UI readiness can be reduced without mutation; otherwise harden custom proof verification. | Submission verifier parses payload/audit/HTML proof and keeps generated UI readiness partial unless a fresh task proves repair. |
| Judge-facing proof index | `019f0de5-0010-7473-ad0e-6d2d89166ce3` | Generate one compact proof index from existing artifacts for demo navigation and inspection. | Generated HTML is tested, checked by Python verifier, and wired into demo/submission scripts. |

## Main-Thread Review Rules

For each worker output:

1. Inspect changed files and claim language before accepting code.
2. Prefer code, tests, generated artifacts, and machine-readable verifier output over docs-only improvements.
3. Do not merge live-tenant mutations unless the pass condition, rollback/non-deletion note, and product-feedback impact are documented first.
4. Resolve shared-script edits manually, especially `scripts/run_submission_check.sh`.
5. Run targeted tests before the full submission check.
6. Log validation using exact commands; do not claim a proof surface passed unless the command or live run was performed.

## Integration Checklist

- `python -m unittest tests.test_policy_state_eval tests.test_test_manager_bridge tests.test_submission_proof tests.test_proof_index`
- `python -m service_recovery_core.evals --policy-boundary-report --output /tmp/service_recovery_policy_boundary_report.json`
- `python -m service_recovery_core.test_manager_bridge --eval-results /tmp/service_recovery_local_baseline.json --junit docs/validation/artifacts/test-manager-results/Service_Recovery_E_001_through_E_009_Baseline___20260626_1017.xml --execution-stats docs/validation/artifacts/2026-06-28/test-manager-feasibility-spike/04-tm-terminal-execution-stats.json --output /tmp/service_recovery_test_manager_bridge.json`
- `python -m service_recovery_core.proof_index --artifact-dir docs/demo/artifacts --verify-only`
- `git diff --check`
- `rg -n "^(<<<<<<<|=======|>>>>>>>)" . -g '!docs/research/artifacts/**' -g '!docs/validation/artifacts/**' -g '!eval_results/local_baseline.json'`
- `scripts/run_submission_check.sh`
