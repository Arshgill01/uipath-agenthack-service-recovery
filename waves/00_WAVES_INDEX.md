# Waves Index

This directory breaks the build into 40 waves. Each wave should be independently understandable by a future agent.

## How To Use

1. Read [AGENTS.md](../AGENTS.md), [PROJECT_BRIEF.md](../PROJECT_BRIEF.md), and the relevant architecture docs.
2. Check the current status table below before picking work. Do not restart completed validation waves unless new platform evidence contradicts them.
3. Run `scripts/run_submission_check.sh` before final submission and after any code/artifact change.
4. Update [docs/logs/BUILD_LOG.md](../docs/logs/BUILD_LOG.md) before finishing.
5. Do not skip hard validation waves unless explicitly waived in [docs/decisions/DECISIONS.md](../docs/decisions/DECISIONS.md).

## Current Status Overlay

The original wave files remain useful for historical intent, but the current repository state is more advanced than the initial wave order.

| Area | Current status | Evidence |
| --- | --- | --- |
| Waves 01-06 / gates G-001 through G-006 | Answered with PASS/PARTIAL implications. Do not redo broad validation without new contradictory platform behavior. | [VALIDATION_RESULTS.md](../docs/validation/VALIDATION_RESULTS.md), [OBJECTIVE_COMPLETION_AUDIT.md](../docs/validation/OBJECTIVE_COMPLETION_AUDIT.md) |
| Demo-safe proof path | Ready locally: Action Center lifecycle, custom evidence packet, Orchestrator audit bundle. | [DEMO_SAFE_PROOF_RUNBOOK.md](../docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md), `scripts/run_demo.sh` |
| Submission sanity check | Ready and non-mutating. | `scripts/run_submission_check.sh` |
| Optional live LLM proof | Gemini/Vertex standard and adversarial artifacts are committed; rerun only intentionally. | `scripts/run_llm_demo.sh`, `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` |
| Product feedback | PF-001 through PF-022 captured and curated. | [PRODUCT_FEEDBACK_AWARD.md](../docs/product/PRODUCT_FEEDBACK_AWARD.md), [FEEDBACK_SURVEY_FINAL_DRAFT.md](../docs/product/FEEDBACK_SURVEY_FINAL_DRAFT.md) |

## Wave List

| Wave | File | Goal |
| --- | --- | --- |
| 01 | [01_platform_access_and_inventory.md](01_platform_access_and_inventory.md) | Confirm accounts, labs, CLI, repo state. |
| 02 | [02_maestro_case_state_spike.md](02_maestro_case_state_spike.md) | Validate native Case state and audit reconstruction. |
| 03 | [03_policy_version_pinning_spike.md](03_policy_version_pinning_spike.md) | Validate policy version pinning strategy. |
| 04 | [04_human_evidence_packet_spike.md](04_human_evidence_packet_spike.md) | Validate Action Center/Case App evidence packet. |
| 05 | [05_agent_override_visibility_spike.md](05_agent_override_visibility_spike.md) | Validate visible raw agent recommendation before policy override. |
| 06 | [06_case_routing_visibility_spike.md](06_case_routing_visibility_spike.md) | Validate distinct 2A/2B routing and visibility. |
| 07 | [07_tech_stack_selection.md](07_tech_stack_selection.md) | Choose local app/test stack based on validation. |
| 08 | [08_repo_foundation.md](08_repo_foundation.md) | Scaffold project structure and baseline tooling. |
| 09 | [09_domain_fixtures.md](09_domain_fixtures.md) | Create simulated telecom data fixtures. |
| 10 | [10_evidence_schema.md](10_evidence_schema.md) | Implement evidence and case schemas. |
| 11 | [11_agent_schema_validator.md](11_agent_schema_validator.md) | Implement agent output schema and semantic validation. |
| 12 | [12_policy_reconciliation_core.md](12_policy_reconciliation_core.md) | Implement deterministic evidence reconciliation. |
| 13 | [13_closure_policy.md](13_closure_policy.md) | Implement closure eligibility and block reasons. |
| 14 | [14_case_state_machine.md](14_case_state_machine.md) | Implement local case state machine matching Maestro stages. |
| 15 | [15_agent_interpretation_stub.md](15_agent_interpretation_stub.md) | Build deterministic/LLM-ready agent interpretation adapter. |
| 16 | [16_unstructured_note_routing.md](16_unstructured_note_routing.md) | Prove technician note changes route. |
| 17 | [17_missing_stale_override_path.md](17_missing_stale_override_path.md) | Build 2A missing/stale evidence override path. |
| 18 | [18_contradiction_escalation_path.md](18_contradiction_escalation_path.md) | Build 2B contradiction escalation path. |
| 19 | [19_human_review_flow.md](19_human_review_flow.md) | Build human review event and evidence packet flow. |
| 20 | [20_audit_event_log.md](20_audit_event_log.md) | Build audit reconstruction and one-query/event view. |
| 21 | [21_policy_versions.md](21_policy_versions.md) | Implement interpretation/decision policy versions. |
| 22 | [22_eval_harness_baseline.md](22_eval_harness_baseline.md) | Implement 8 minimum eval scenarios. |
| 23 | [23_agent_usefulness_incident.md](23_agent_usefulness_incident.md) | Implement usefulness degradation detection. |
| 24 | [24_policy_improvement_case.md](24_policy_improvement_case.md) | Implement improvement-case artifact and diff flow. |
| 25 | [25_test_cloud_mapping.md](25_test_cloud_mapping.md) | Map/runnable evals to Test Cloud if feasible. |
| 26 | [26_uipath_cli_coding_agent_bonus.md](26_uipath_cli_coding_agent_bonus.md) | Add visible UiPath CLI/coding-agent proof. |
| 27 | [27_maestro_case_implementation.md](27_maestro_case_implementation.md) | Build Maestro Case implementation from local model. |
| 28 | [28_api_workflows_and_simulated_systems.md](28_api_workflows_and_simulated_systems.md) | Connect simulated systems through API Workflows or equivalent. |
| 29 | [29_case_app_or_review_ui.md](29_case_app_or_review_ui.md) | Build evidence packet UI. |
| 30 | [30_demo_scenario_runbook.md](30_demo_scenario_runbook.md) | Create repeatable demo runbook. |
| 31 | [31_failure_injection.md](31_failure_injection.md) | Add controlled failure/adversarial toggles. |
| 32 | [32_metrics_surface.md](32_metrics_surface.md) | Add business metric outputs. |
| 33 | [33_product_feedback_capture.md](33_product_feedback_capture.md) | Capture product feedback for award. |
| 34 | [34_security_and_secret_handling.md](34_security_and_secret_handling.md) | Check secrets, PII, simulation honesty. |
| 35 | [35_docs_for_builders.md](35_docs_for_builders.md) | Finalize builder docs and setup instructions. |
| 36 | [36_devpost_assets.md](36_devpost_assets.md) | Draft Devpost writeup structure. |
| 37 | [37_presentation_deck_outline.md](37_presentation_deck_outline.md) | Draft deck outline. |
| 38 | [38_demo_video_script.md](38_demo_video_script.md) | Draft demo video script after product exists. |
| 39 | [39_final_validation.md](39_final_validation.md) | Run full validation and fix gaps. |
| 40 | [40_submission_readiness.md](40_submission_readiness.md) | Final submission readiness checklist. |
