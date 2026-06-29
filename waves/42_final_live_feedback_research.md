# Wave 42: Final Live Feedback Research

## Goal

Run one final strict UiPath platform research pass that improves product feedback only when live commands or concrete artifact validation justify it.

This wave is not a smoke test, a doc polish pass, or a broad feature build. Useful work must either:

- verify or downgrade an existing product-feedback claim,
- discover a new high-confidence feedback claim through real UiPath CLI/browser work,
- improve the code/proof path only when a probe exposes a concrete gap,
- preserve all existing claim boundaries.

## Lanes

1. **Claim Audit Lane**
   - Recheck the strongest feedback claims PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-019, PF-020, PF-021, PF-023, PF-024, PF-026, PF-027, and PF-028.
   - Prefer live read-only CLI readbacks and existing validation artifacts.
   - Output a downgrade/confirm matrix.

2. **Maestro / Action / Solution Readiness Lane**
   - Run concrete `uip maestro case`, `uip solution`, `uip tasks`, and Orchestrator readback commands against existing scratch/downloaded artifacts and existing live resources.
   - Look for readiness-contract evidence: validate vs pack/upload agreement, Action task required fields, app version binding, process/package/feed diagnostics, Case diagnostics.
   - Do not start or complete a fresh live Case unless the orchestrator explicitly approves.

3. **Integration / Data Fabric / Test Manager Lane**
   - Run concrete `uip is`, `uip df`, `uip tm`, and Orchestrator readback commands.
   - Recheck Data Fabric V2 audit readback, legacy field-mapping caveat, Test Manager manual-vs-automated boundary, and Integration Service discoverability for optional external evidence sources.
   - Do not create/delete Data Fabric schemas or Test Manager artifacts unless the orchestrator explicitly approves.

## Claim Boundaries

- Do not claim automated Test Cloud execution unless a successful automated execution is actually run and read back.
- Do not claim generated Action Center UI final-demo readiness unless a fresh runtime task visibly renders proof-critical fields with stable labels and values.
- Do not claim native Case history alone as full G-001 proof.
- Do not claim real telecom OSS/BSS integration.
- Do not imply LLM/Codex runtime closure authority.

## Required Outputs

- New artifact notes under `docs/validation/artifacts/2026-06-29/wave42/`.
- Updates to `docs/product/PRODUCT_FEEDBACK_AWARD.md`, `docs/product/FEEDBACK_AWARD_APPENDIX.md`, and survey copy only if evidence changes the feedback.
- `docs/validation/VALIDATION_RESULTS.md` and `docs/logs/BUILD_LOG.md` entries for any accepted findings.
- Targeted tests or submission proof checks when docs/code/artifacts change.

## Validation

Before merging accepted work:

```sh
git diff --check
python3 -m service_recovery_core.submission_proof --artifact-dir docs/demo/artifacts
python3 -m unittest tests.test_submission_proof
scripts/run_submission_check.sh
```
