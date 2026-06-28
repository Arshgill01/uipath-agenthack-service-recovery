# Platform Integration Proof Map

Date: 2026-06-28.

Purpose: make the UiPath platform-depth story reviewable from one place. This map ties the repo's local deterministic proof, UiPath-native runtime proof, and judge-readable packet proof into one chain without overstating the validated boundaries.

Read this with:

- [SUBMISSION_BRIEF.md](SUBMISSION_BRIEF.md)
- [READINESS_CHECKLIST.md](READINESS_CHECKLIST.md)
- [DEMO_SAFE_PROOF_RUNBOOK.md](../demo/DEMO_SAFE_PROOF_RUNBOOK.md)
- [VALIDATION_RESULTS.md](../validation/VALIDATION_RESULTS.md)

## Claim Boundary

The submission claim is:

> UiPath Maestro Case is the orchestration boundary for dynamic telecom service-recovery exceptions. Agents produce structured recommendations, deterministic policy decides allowed routing, Action Center handles human review lifecycle, and UiPath-hosted audit/eval surfaces preserve the evidence trail.

Do not claim:

- automated Test Cloud execution,
- generated Action Center UI as the final judge-facing evidence surface,
- native Maestro Case history alone as the full domain audit,
- real telecom production integrations,
- LLM or coding-agent authority over final closure.

## Three Proof Layers

| Layer | What it is | Primary artifacts | Final-demo role |
| --- | --- | --- | --- |
| Native UiPath proof | Live or CLI-readback evidence from Maestro Case, Action Center, Orchestrator, Data Fabric, Test Manager, and UiPath CLI. | `docs/validation/VALIDATION_RESULTS.md`, `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`, `docs/validation/artifacts/2026-06-27/` | Proves this is connected to UiPath platform surfaces. |
| Custom judge-readable proof | HTML packets, screenshots, and audit bundles generated from the same policy/evidence contract used for UiPath payloads. | `docs/demo/artifacts/evidence_packet_E002.html`, `docs/demo/artifacts/evidence_packet_E004.html`, `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html`, screenshots, audit bundles | Gives judges a readable view of fields the generated Action Center UI did not render safely. |
| Local deterministic policy proof | Unit tests, evals, fixtures, exported payloads, and policy-improvement artifacts. | `tests/`, `fixtures/eval_scenarios.json`, `service_recovery_core/`, `docs/demo/artifacts/policy_improvement_E008.json`, `scripts/run_submission_check.sh` | Proves the architecture boundary is repeatable and regression-checked without live tenant mutation. |

## End-To-End Proof Chain

1. Track and platform intent are locked in [TRACK_SELECTION_DECISION.md](TRACK_SELECTION_DECISION.md): primary track is UiPath Maestro Case; Test Manager supports eval proof only.
2. Local eval scenarios E-002 and E-004 use the same green business fixture. Only authoritative telemetry/inventory changes.
3. `service_recovery_core` exports three connected proof shapes for each core scenario:
   - Action Center payload: `docs/demo/artifacts/action_payload_E002.json`, `docs/demo/artifacts/action_payload_E004.json`
   - durable audit bundle: `docs/demo/artifacts/service_recovery_audit_bundle_E002.json`, `docs/demo/artifacts/service_recovery_audit_bundle_E004.json`
   - judge-readable packet: `docs/demo/artifacts/evidence_packet_E002.html`, `docs/demo/artifacts/evidence_packet_E004.html`
4. Maestro Case package/process runs carried the exported payloads into Action Center tasks:
   - E-002 missing telemetry: case/job `3af41e1d-8b04-4eba-aa5e-a95c5c673730`, task `4300080`, package `1.0.4`
   - E-004 contradiction: case/job `60e52ca5-6891-45b4-9e98-e1b08a984f06`, task `4300219`, package `1.0.5`
   - runtime label repair recheck: case/job `9eb64f9f-6613-48f7-b452-215085d8c67b`, task `4333536`, package `1.0.6`
5. Action Center task readback proves human lifecycle and structured return, while API payloads preserve the raw Agent Interpretation Event and linked Policy Decision Event.
6. Orchestrator process/package readback proves explicit package/process pinning with `AutoUpdate: false`; bucket file `audit/service_recovery_audit_bundle_E004.json` proves an alternate UiPath-hosted full-payload audit artifact.
7. Data Fabric V2 record `F9D838CE-4671-F111-AC9A-0022489A9A06` in entity `ServiceRecoveryAuditBundleV2` proves queryable full-payload audit readback for E-004.
8. Test Manager project `SREV`, test set `SREV:9`, and terminal manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` represent E-001 through E-009 with 9/9 passed logs.
9. `scripts/run_submission_check.sh` verifies the local proof set without starting live UiPath cases, completing live tasks, or calling Gemini/Vertex.

## Core Scenario Proof

| Beat | Same business fixture | Agent recommendation | Policy decision | UiPath proof | Judge-readable proof | Caveat |
| --- | --- | --- | --- | --- | --- | --- |
| 2A missing/stale evidence | CRM/order/billing/support green; authoritative telemetry missing or stale. | `closure_candidate` | `override_recommendation`, route `verify_telemetry`, reason `missing_authoritative_signal` or `stale_authoritative_signal` | Task `4300080`; case/job `3af41e1d-8b04-4eba-aa5e-a95c5c673730`; package `1.0.4`; `docs/demo/artifacts/action_payload_E002.json` | `docs/demo/artifacts/evidence_packet_E002.html`, `docs/demo/artifacts/evidence_packet_E002_desktop.png`, `docs/demo/artifacts/service_recovery_audit_bundle_E002.json` | Generated Action Center UI is not the final readable packet. |
| 2B contradiction | Same green business fixture; fresh authoritative telemetry says not live or inventory contradicts. | `closure_candidate` | `require_human_review`, route `human_review`, reason `source_contradiction` | Task `4300219`; case/job `60e52ca5-6891-45b4-9e98-e1b08a984f06`; package `1.0.5`; Data Fabric record `F9D838CE-4671-F111-AC9A-0022489A9A06`; bucket path `audit/service_recovery_audit_bundle_E004.json` | `docs/demo/artifacts/evidence_packet_E004.html`, `docs/demo/artifacts/evidence_packet_E004_desktop.png`, `docs/demo/artifacts/evidence_packet_E004_mobile.png`, `docs/demo/artifacts/service_recovery_audit_bundle_E004.json` | Native Case history remains partial for full domain audit. |
| E-003 live/adversarial LLM | Stale authoritative telemetry with unstructured note pressure. | Live Gemini can recommend `closure_candidate`; adversarial path records structured disagreement. | Deterministic policy overrides or routes to `human_review` with `high_interpretation_disagreement`. | Optional live Vertex artifacts only; not required for closure authority. | `docs/demo/artifacts/llm_interpreter_E003_live.json`, `docs/demo/artifacts/llm_interpreter_E003_adversarial_live.json`, `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` and screenshots | LLM output remains advisory and schema-validated. |
| E-008 learning loop | Repeated usefulness failure rather than a customer closure path. | Agent usefulness degrades through low confidence despite sufficient signal. | Proposal-only improvement case; no policy auto-promotion. | Test Manager maps E-008 as part of `SREV:9`. | `docs/demo/artifacts/policy_improvement_E008.json` | Human approval and eval pass are required before promotion. |

## Native UiPath Surface Map

| UiPath surface | Exact proof | What it proves | Caveat / final use |
| --- | --- | --- | --- |
| Maestro Case | Case/job IDs `3af41e1d-8b04-4eba-aa5e-a95c5c673730`, `60e52ca5-6891-45b4-9e98-e1b08a984f06`, `9fc6fece-55ed-4fb2-b11a-6c96f7a3314e`, `9eb64f9f-6613-48f7-b452-215085d8c67b`; validation log entries in [VALIDATION_RESULTS.md](../validation/VALIDATION_RESULTS.md). | Case runtime exists, package versions are visible, stage/task lifecycle can be read back, and fresh package `1.0.6` reached terminal completion. | Native Case history alone is not the complete domain audit. Pair with Data Fabric or bucket audit. |
| Action Center | Tasks `4300080`, `4300219`, `4333536`; `uip tasks get` readbacks in validation logs; `TaskSource.SourceName: CaseManagement`; structured action/comment return. | Human review task lifecycle, assignment, completion, reviewer comment, and structured return work through UiPath. | Generated page rendering hid/mislabeled `PolicyDecisionJson`; use custom packet for judge readability. |
| Orchestrator | Process key `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`; folder key `9d7ae568-d60e-4395-94d7-db115bfb25de`; package versions `1.0.3` through `1.0.6`; bucket `dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb`; bucket path `audit/service_recovery_audit_bundle_E004.json`. | Package/process pinning, `AutoUpdate: false`, job starts/readback, and UiPath-hosted audit-bundle storage. | Orchestrator is the package/audit host, not the decision engine. |
| Data Fabric | Entity `ServiceRecoveryAuditBundleV2` (`35e8f6c7-4671-f111-ac9a-002248a16d28`); record `F9D838CE-4671-F111-AC9A-0022489A9A06`; read-only reconfirmation in `docs/validation/artifacts/2026-06-27/data_fabric_readback_diagnostics_probe.md`. | Queryable full-payload audit readback for E-004, including `CaseId`, policy versions, closure block reason, raw AIE JSON, linked PDE JSON, reviewer packet, and audit bundle. | PascalCase V2 schema is the validated path. Legacy snake_case entity remains product-feedback evidence only. |
| Test Manager | Project `SREV`; test set `SREV:9`; terminal manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11`; JUnit export `docs/validation/artifacts/test-manager-results/Service_Recovery_E_001_through_E_009_Baseline___20260626_1017.xml`; read-only 2026-06-27 probe in `docs/validation/artifacts/2026-06-27/pf-workstream-c/README.md`. | E-001 through E-009 are represented in UiPath Test Manager with 9/9 passed manual logs and terminal `Status: Finished`. | This is manual Test Manager evidence, not automated Test Cloud execution. |
| UiPath CLI | `uip` readback commands captured in [DEMO_SAFE_PROOF_RUNBOOK.md](../demo/DEMO_SAFE_PROOF_RUNBOOK.md), [VALIDATION_RESULTS.md](../validation/VALIDATION_RESULTS.md), and 2026-06-27 command artifacts. | Platform interactions are reproducible and auditable through commands, not only screenshots. | Prefer read-only checks for final review unless new live IDs are intentionally needed. |

## Custom Judge-Readable Proof Map

| Artifact | Use in review/demo | Underlying platform connection |
| --- | --- | --- |
| `docs/demo/artifacts/evidence_packet_E002.html` | Shows missing/stale authoritative evidence, raw `closure_candidate`, policy override, and route to `verify_telemetry`. | Same fields exported into Action Center payload `action_payload_E002.json` and live task `4300080`. |
| `docs/demo/artifacts/evidence_packet_E004.html` | Shows fresh contradiction, severity, human review route, raw recommendation, linked policy decision, and block reason. | Same fields exported into Action Center payload `action_payload_E004.json`, live task `4300219`, Data Fabric V2, and Orchestrator bucket audit bundle. |
| `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` | Shows optional LLM/adversarial interpretation with deterministic policy control. | Derived from live Gemini/Vertex JSON artifact, still routed by local policy. |
| `docs/demo/artifacts/service_recovery_audit_bundle_E002.json` and `docs/demo/artifacts/service_recovery_audit_bundle_E004.json` | Machine-readable one-object audit reconstruction for the core beats. | E-004 bundle is the object uploaded/read from Orchestrator bucket and persisted through Data Fabric V2. |
| `docs/demo/artifacts/demo_proof_manifest.json` | Quick index of the generated E-002/E-004 payload, audit, packet, recommendation, decision, block reason, and route. | Generated by `python -m service_recovery_core.demo_proof`. |

## Local Deterministic Policy Proof Map

| Local proof | What it proves | Guardrail |
| --- | --- | --- |
| `python -m unittest discover -s tests` | Core validators, policy behavior, packet generation, and LLM/adversarial helpers are covered by unit tests. | Passing locally does not replace UiPath runtime proof. |
| `python -m service_recovery_core.evals --output eval_results/local_baseline.json` | E-001 through E-009 pass the deterministic eval suite. | E-002/E-004 must remain fixture variants, not unrelated examples. |
| `scripts/run_demo.sh` | Regenerates E-002/E-004 payloads, audit bundles, packets, and proof manifest without starting live UiPath work by default. | Live next-step commands are printed for deliberate use only. |
| `scripts/run_submission_check.sh` | Non-mutating final sanity check for tests, evals, proof artifacts, proof strings, and wrapper syntax. | Does not validate fresh live tenant state. |
| `docs/demo/artifacts/policy_improvement_E008.json` | Proves governed learning: proposed diff, eval result, pending human approval, `not_promoted`, and active-case pinning. | No policy auto-promotion is claimed. |

## Reviewer Walkthrough

For a final reviewer or judge:

1. Open [SUBMISSION_BRIEF.md](SUBMISSION_BRIEF.md) for the short story.
2. Open this proof map to see how each UiPath surface connects to the core architecture boundary.
3. Open `docs/demo/artifacts/evidence_packet_E002.html` and `docs/demo/artifacts/evidence_packet_E004.html` to compare the two same-fixture proof beats.
4. Inspect `docs/demo/artifacts/service_recovery_audit_bundle_E004.json` and the Data Fabric V2 validation entries for full-payload audit reconstruction.
5. Inspect Test Manager evidence for `SREV:9` and execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` only as manual eval representation.
6. Run `scripts/run_submission_check.sh` from repo root for a non-mutating local readiness check.
