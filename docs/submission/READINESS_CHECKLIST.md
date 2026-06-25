# Submission Readiness Checklist

Status: current evidence map for final submission and future agents. Do not mark an item stronger than the evidence listed here.

## Core Validation

| Requirement | Status | Evidence | Remaining caution |
| --- | --- | --- | --- |
| Local unit tests pass. | PASS | `python -m unittest discover -s tests` passed 27 tests on 2026-06-26. | Re-run before final submission if code changes. |
| Local eval suite E-001 through E-009 passes. | PASS | `python -m service_recovery_core.evals --output eval_results/local_baseline.json` passed 9/9. | Re-run before final submission if fixtures/policy change. |
| Repeatable E-002/E-004 proof artifacts exist. | PASS | `scripts/run_demo.sh --with-local-checks --no-uipath-next-steps`; `docs/demo/artifacts/demo_proof_manifest.json`. | Script is local/default-safe; it does not start live cases. |
| UiPath Labs access is confirmed. | PASS | Org `keepingitlowkey`, tenant `DefaultTenant`, user `arshgill6120@gmail.com` in validation logs. | Do not store credentials or tokens. |
| Maestro Case access is confirmed. | PASS | Wave 01 and live Case validation entries in `docs/validation/VALIDATION_RESULTS.md`. | Native Case history is not full domain audit by itself. |

## Hard Gates

| Gate | Result | Evidence | Implementation decision |
| --- | --- | --- | --- |
| G-001 Native Case State / Audit Reconstruction | PARTIAL natively; PASS with custom UiPath-hosted audit artifact fallback | `docs/validation/VALIDATION_GATES.md`; Orchestrator bucket artifact `audit/service_recovery_audit_bundle_E004.json`; `docs/demo/artifacts/service_recovery_audit_bundle_E004.json` | Use `service-recovery-audit-v1` bundle in Orchestrator bucket for one-object domain audit proof. |
| G-002 Policy Version Pinning | PASS for explicit package/process/artifact pinning | Process readback/version history; payload/audit fields `interpretation_policy_version` and `decision_policy_version` | Represent policy migrations as explicit audited events. |
| G-003 Human Evidence Packet | PASS for Action Center lifecycle/structured return; PARTIAL for generated UI legibility | Live tasks `4300080`, `4300219`; `docs/demo/artifacts/evidence_packet_E002.html`; `docs/demo/artifacts/evidence_packet_E004.html` | Use Action Center for lifecycle and custom packet for judge-readable proof. |
| G-004 Agent Recommendation Visible Before Override | PASS for persistence/API/audit visibility; PARTIAL for generated UI display | Live E-002/E-004 task payloads; audit bundle AIE/PDE linkage; evidence packet comparison panels | Do not depend on generated Action Center UI to show the boundary. |

## Soft Gates

| Gate | Result | Evidence | Remaining caution |
| --- | --- | --- | --- |
| G-005 Distinct 2A/2B routing | PASS | E-002 route `verify_telemetry`; E-004 route `human_review`; live tasks and local artifacts | Keep both beats on same green business fixture with only authoritative signal changed. |
| G-006 Demo surface visibility | PASS for custom packet; PARTIAL for generated Action Center UI | `evidence_packet_E002_desktop.png`; `evidence_packet_E004_desktop.png`; PF-013 | Use custom packet as primary visual surface. |
| G-007 Test Cloud/Test Manager crossover | PARTIAL/PASS for manual Test Manager representation | Project `SREV`, test set `SREV:9`, manual execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad`, mapping doc | Do not claim automated Test Cloud execution. |
| G-008 Coding-agent/CLI bonus | PASS for CLI-assisted lifecycle artifacts | `uip` CLI validation, package/process/task/bucket/test-manager commands in logs, `scripts/run_demo.sh` | If shown live, run readback commands deliberately and log new evidence. |

## Product Feedback Award

| Requirement | Status | Evidence | Remaining caution |
| --- | --- | --- | --- |
| Product feedback captured during UiPath interactions. | PASS | PF-001 through PF-022 in `docs/product/PRODUCT_FEEDBACK_AWARD.md`. | Add new PF entries only for newly observed UiPath behavior. |
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
| E-002 evidence packet | Ready | `docs/demo/artifacts/evidence_packet_E002.html` |
| E-004 evidence packet | Ready | `docs/demo/artifacts/evidence_packet_E004.html` |
| Audit proof manifest | Ready | `docs/demo/artifacts/demo_proof_manifest.json` |

## Do Not Claim

- Automated Test Cloud execution.
- Data Fabric audit record persistence.
- Generated Action Center UI is final-demo ready.
- Native Case history alone passes G-001.
- Terminal Case job completion for E-002/E-004 while jobs still read `Running`.
- Real telecom production integrations.
- LLM final closure authority.
- Generic agent governance platform positioning.

## Final Manual Inputs

- Team name.
- Story-sharing preference.
- Any fresh live E-002/E-004 case/task IDs if rerun after this checklist.
