# Submission Readiness Checklist

Status: current evidence map for final submission and future agents. Do not mark an item stronger than the evidence listed here.

Objective-level audit: [OBJECTIVE_COMPLETION_AUDIT.md](../validation/OBJECTIVE_COMPLETION_AUDIT.md).

## Core Validation

| Requirement | Status | Evidence | Remaining caution |
| --- | --- | --- | --- |
| Local unit tests pass. | PASS | `python -m unittest discover -s tests` passed 43 tests on 2026-06-26. | Re-run before final submission if code changes. |
| Local eval suite E-001 through E-009 passes. | PASS | `python -m service_recovery_core.evals --output eval_results/local_baseline.json` passed 9/9. | Re-run before final submission if fixtures/policy change. |
| Repeatable E-002/E-004 proof artifacts exist. | PASS | `scripts/run_demo.sh --with-local-checks --no-uipath-next-steps`; `docs/demo/artifacts/demo_proof_manifest.json`. | Script is local/default-safe; it does not start live cases. |
| Optional real LLM interpretation path exists. | PASS with live Vertex run | `scripts/run_llm_demo.sh --scenario-id E-003 --model gemini-2.5-flash --project <project> --location us-central1 --output eval_results/llm_interpreter_E003_live.json`; committed artifact `docs/demo/artifacts/llm_interpreter_E003_live.json` | Re-run if model, prompt, Google project, or ADC environment changes before recording. |
| Optional adversarial LLM interpretation path exists. | PASS with live Vertex run | Unit tests cover advocate/skeptic interpretation, repair of schema/semantic drift, disagreement scoring, policy route to `human_review`, and evidence-packet display. Live artifact: `docs/demo/artifacts/llm_interpreter_E003_adversarial_live.json`. | Re-run before final recording if prompt, model, scoring, Google project, or ADC environment changes. |
| Non-mutating submission sanity check exists. | PASS | `scripts/run_submission_check.sh` runs tests, evals, existing artifact verification, script syntax checks, and proof-string checks without live UiPath/Vertex calls. | Use before final submission and after any code or artifact change. |
| UiPath Labs access is confirmed. | PASS | Org `keepingitlowkey`, tenant `DefaultTenant`, user `arshgill6120@gmail.com` in validation logs. | Do not store credentials or tokens. |
| Maestro Case access is confirmed. | PASS | Wave 01 and live Case validation entries in `docs/validation/VALIDATION_RESULTS.md`. | Native Case history is not full domain audit by itself. |

## Hard Gates

| Gate | Result | Evidence | Implementation decision |
| --- | --- | --- | --- |
| G-001 Native Case State / Audit Reconstruction | PARTIAL natively; PASS with Data Fabric V2 and Orchestrator bucket full-payload fallbacks | Data Fabric entity `ServiceRecoveryAuditBundleV2` record `F9D838CE-4671-F111-AC9A-0022489A9A06` queries by `CaseId` and returns parseable AIE/PDE/audit JSON; Orchestrator bucket artifact `audit/service_recovery_audit_bundle_E004.json` | Native Case history is still not the full domain audit by itself. Use Data Fabric V2 or bucket artifact as the full-payload audit proof. |
| G-002 Policy Version Pinning | PASS for explicit package/process/artifact pinning | Process readback/version history; payload/audit fields `interpretation_policy_version` and `decision_policy_version` | Represent policy migrations as explicit audited events. |
| G-003 Human Evidence Packet | PASS for Action Center lifecycle/structured return; PARTIAL for generated UI legibility | Live tasks `4300080`, `4300219`; `docs/demo/artifacts/evidence_packet_E002.html`; `docs/demo/artifacts/evidence_packet_E004.html`; generated UI repair assessment `docs/validation/ACTION_CENTER_UI_REPAIR_ASSESSMENT.md` | Use Action Center for lifecycle and custom packet for judge-readable proof. |
| G-004 Agent Recommendation Visible Before Override | PASS for persistence/API/audit visibility; PARTIAL for generated UI display | Live E-002/E-004 task payloads; audit bundle AIE/PDE linkage; evidence packet comparison panels | Do not depend on generated Action Center UI to show the boundary. |

## Soft Gates

| Gate | Result | Evidence | Remaining caution |
| --- | --- | --- | --- |
| G-005 Distinct 2A/2B routing | PASS | E-002 route `verify_telemetry`; E-004 route `human_review`; live tasks and local artifacts | Keep both beats on same green business fixture with only authoritative signal changed. |
| G-006 Demo surface visibility | PASS for custom packet; PARTIAL for generated Action Center UI | `evidence_packet_E002_desktop.png`; `evidence_packet_E004_desktop.png`; `evidence_packet_E003_adversarial_desktop.png`; PF-013 | Use custom packet as primary visual surface. |
| G-007 Test Cloud/Test Manager crossover | PASS for manual Test Manager representation/execution; PARTIAL for automated Test Cloud | Project `SREV`, test set `SREV:9`, terminal manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11`, mapping doc, JUnit export `docs/validation/artifacts/test-manager-results/Service_Recovery_E_001_through_E_009_Baseline___20260626_1017.xml`; automation-discovery and package-probe evidence in `docs/validation/TEST_MANAGER_MAPPING.md` including `ServiceRecoveryEvalProcessProbe:0.0.2/0.0.3` | Do not claim automated Test Cloud execution. |
| G-008 Coding-agent/CLI bonus | PASS for CLI-assisted lifecycle artifacts | `uip` CLI validation, package/process/task/bucket/test-manager commands in logs, `scripts/run_demo.sh` | If shown live, run readback commands deliberately and log new evidence. |

## Product Feedback Award

| Requirement | Status | Evidence | Remaining caution |
| --- | --- | --- | --- |
| Product feedback captured during UiPath interactions. | PASS | PF-001 through PF-025 in `docs/product/PRODUCT_FEEDBACK_AWARD.md`. | Add new PF entries only for newly observed UiPath behavior. |
| Feedback is curated into final answer material. | PASS | `docs/product/FEEDBACK_AWARD_APPENDIX.md`; `docs/product/FEEDBACK_SURVEY_COPY_READY.md`. | Team name and story-sharing preference still need user confirmation. |
| Feedback separates user/access/docs/product defects. | PASS | Feedback matrix classifications and confidence fields. | Keep fair language; do not turn workarounds into unsupported defect claims. |

## Submission Artifacts

| Artifact | Status | Path |
| --- | --- | --- |
| Project brief | Ready | `PROJECT_BRIEF.md` |
| Submission brief | Ready | `docs/submission/SUBMISSION_BRIEF.md` |
| Feedback answer bank | Ready except user fields | `docs/product/FEEDBACK_SURVEY_COPY_READY.md` |
| Demo-safe runbook | Ready | `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md` |
| Repeatable proof wrapper | Ready | `scripts/run_demo.sh` |
| Repeatable Test Manager manual eval wrapper | Ready | `scripts/run_test_manager_manual_eval.sh` |
| Submission sanity check | Ready | `scripts/run_submission_check.sh` |
| E-002 evidence packet | Ready | `docs/demo/artifacts/evidence_packet_E002.html` |
| E-004 evidence packet | Ready | `docs/demo/artifacts/evidence_packet_E004.html` |
| E-002/E-004 desktop screenshots | Ready | `docs/demo/artifacts/evidence_packet_E002_desktop.png`; `docs/demo/artifacts/evidence_packet_E004_desktop.png` |
| Audit proof manifest | Ready | `docs/demo/artifacts/demo_proof_manifest.json` |
| Live LLM proof artifact | Ready | `docs/demo/artifacts/llm_interpreter_E003_live.json` |
| Live adversarial LLM proof artifact | Ready | `docs/demo/artifacts/llm_interpreter_E003_adversarial_live.json` |
| Live adversarial LLM evidence packet | Ready | `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` |
| Live adversarial packet screenshots | Ready | `docs/demo/artifacts/evidence_packet_E003_adversarial_desktop.png`; `docs/demo/artifacts/evidence_packet_E003_adversarial_mobile.png` |
| Action Center UI repair assessment | Ready | `docs/validation/ACTION_CENTER_UI_REPAIR_ASSESSMENT.md` |

## Do Not Claim

- Automated Test Cloud execution.
- Generated Action Center UI is final-demo ready.
- Native Case history alone passes G-001.
- Terminal completion for older E-002/E-004 jobs; only the fresh package `1.0.6` Case Instance completion is claimed.
- Real telecom production integrations.
- LLM final closure authority.
- Generic agent governance platform positioning.

## Final Manual Inputs

- Team name.
- Story-sharing preference.
- Any fresh live E-002/E-004 case/task IDs if rerun after this checklist.
- Google Cloud project ID or Gemini API key environment setup if rerunning the optional live LLM interpreter.
