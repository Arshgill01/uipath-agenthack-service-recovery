# Demo-Safe Proof Runbook

This runbook turns the validated UiPath platform facts into repeatable demo operations.

It is intentionally conservative:

- Action Center proves human-task lifecycle and structured reviewer return.
- Custom evidence-packet HTML proves judge-readable evidence, agent recommendation, policy decision, and route.
- Orchestrator bucket audit bundle proves durable UiPath-hosted one-object audit reconstruction.
- Generated Action Center UI is not used as the final evidence-packet surface unless repaired and revalidated.

## Current Live References

UiPath context:

- Org: `keepingitlowkey`
- Tenant: `DefaultTenant`
- User: `arshgill6120@gmail.com`
- Orchestrator folder key: `9d7ae568-d60e-4395-94d7-db115bfb25de`
- Process key: `9a7eb300-7b16-4856-b14f-d6f2da3dbe61`
- Audit bucket key: `dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb`
- Audit bucket path: `audit/service_recovery_audit_bundle_E004.json`

Validated live proof beats:

| Beat | Scenario | Case/job key | Action task | Package version | Route |
| --- | --- | --- | --- | --- | --- |
| 2A | E-002 missing authoritative telemetry | `3af41e1d-8b04-4eba-aa5e-a95c5c673730` | `4300080` | `1.0.4` | `verify_telemetry` |
| 2B | E-004 fresh authoritative contradiction | `60e52ca5-6891-45b4-9e98-e1b08a984f06` | `4300219` | `1.0.5` | `human_review` |

Test Manager:

- Project key: `SREV`
- Test set key: `SREV:9`
- Terminal manual execution: `40a1b334-5df8-1100-0a4b-0b49d0564f11`
- Result artifact: `docs/validation/artifacts/test-manager-results/Service_Recovery_E_001_through_E_009_Baseline___20260626_1017.xml`
- Readback nuance: the first manual execution `d50a7be6-35ed-1100-95aa-0b49cf9b8cad` stayed `Running` after direct finish calls. The repaired run used explicit `testcaselog start` before `testcaselog finish` for each case and reached `Status: Finished`.
- Repeatable wrapper: `scripts/run_test_manager_manual_eval.sh` prints the exact dry-run command sequence by default; add `--execute` only when intentionally creating a fresh live Test Manager manual execution.

## Proof Beat Contract

Use the same canonical green business fixture for 2A and 2B:

- CRM/order: green / active
- Billing: green / clear
- Support note: green / resolved
- Agent recommendation: `closure_candidate`

Change only authoritative evidence:

- 2A: authoritative telemetry is missing or stale.
- 2B: authoritative telemetry or inventory is fresh but contradicts the green business state.

Expected policy outcomes:

- 2A: policy overrides closure to `verify_telemetry` or retry with SLA, reason `missing_authoritative_signal` or `stale_authoritative_signal`.
- 2B: policy escalates to `human_review` or exception investigation, reason `source_contradiction`, elevated severity.

Non-negotiable proof:

- Raw Agent Interpretation Event stays separate from Policy Decision Event.
- Policy event links back to the raw agent event.
- Policy decision, not the agent, controls routing.
- Closure is blocked unless fresh authoritative telemetry satisfies policy.

## Local Artifact Generation

Run from repo root.

Default repeatable demo preparation:

```sh
scripts/run_demo.sh
```

This is the safest operator entry point. It regenerates and verifies the E-002/E-004 Action Center payloads, audit bundles, evidence-packet HTML, and proof manifest, then prints the live UiPath readback/upload commands to run manually. It does not start new live cases, complete live tasks, or mutate the tenant by default.

Run the full local validation set before recording or submission:

```sh
scripts/run_demo.sh --with-local-checks
```

Dry-run the validated Test Manager manual execution lifecycle:

```sh
scripts/run_test_manager_manual_eval.sh
```

Create a fresh live Test Manager manual execution only when a new G-007 evidence ID is intentionally needed:

```sh
scripts/run_test_manager_manual_eval.sh --execute
```

Suppress UiPath next-step commands when only refreshing local artifacts:

```sh
scripts/run_demo.sh --no-uipath-next-steps
```

The underlying commands are:

```sh
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
python -m service_recovery_core.demo_proof --output-dir docs/demo/artifacts
python -m service_recovery_core.demo_proof --output-dir docs/demo/artifacts --verify-only
```

The demo proof helper generates and verifies:

- `docs/demo/artifacts/action_payload_E002.json`
- `docs/demo/artifacts/action_payload_E004.json`
- `docs/demo/artifacts/service_recovery_audit_bundle_E002.json`
- `docs/demo/artifacts/service_recovery_audit_bundle_E004.json`
- `docs/demo/artifacts/evidence_packet_E002.html`
- `docs/demo/artifacts/evidence_packet_E004.html`
- `docs/demo/artifacts/demo_proof_manifest.json`

Generate the governed learning-loop artifact:

```sh
python -m service_recovery_core.evals \
  --policy-improvement-artifact-scenario E-008 \
  --output docs/demo/artifacts/policy_improvement_E008.json
```

Show `policy_improvement_E008.json` during the eval/learning-loop beat to prove the system proposes a diff, records eval results, keeps `approval_status: pending_human_approval`, keeps `promotion_status: not_promoted`, proposes `ip-v2-proposed`, and leaves active cases pinned until an explicit migration event.

It fails if the raw agent recommendation, policy decision, route, block reason, or AIE/PDE linkage drifts from the proof-beat contract.

## Coding-Agent Proof Beat

The AgentHack rules and forum Q&A require coding-agent use to be documented and visible for bonus points.

Show these during the demo:

- `README.md` coding-agent section.
- `docs/submission/CODING_AGENT_PROOF_LOG.md`.
- `git log --oneline --max-count=5`.
- `scripts/run_submission_check.sh` passing, or the most recent saved output from the recording run.

Suggested narration:

> Codex was used as the coding agent to build the core, evals, UiPath validation runbooks, and product-feedback evidence. UiPath remains the orchestration and governance layer; Codex is build-time assistance, not runtime closure authority.

Do not imply that Codex, Gemini, or any LLM makes final closure decisions.

## Optional Live LLM Interpretation

The default proof artifacts are deterministic so tests and evals are repeatable. For the strongest demo beat, run the optional Gemini-backed interpreter to create the raw Agent Interpretation Event from unstructured notes, then let deterministic policy accept or override it.

Auth is environment-based; do not store keys or project IDs in the repo.

Default wrapper:

```sh
scripts/run_llm_demo.sh
```

If auth is unavailable, the wrapper writes `eval_results/llm_interpreter_E003.json` with `status: blocked` and exits `2`. Do not treat that as a live LLM validation.

Validated live artifact:

- `docs/demo/artifacts/llm_interpreter_E003_live.json`
- Model used for the captured run: `gemini-2.5-flash` on Vertex AI.
- Observed beat: Gemini emitted a valid Agent Interpretation Event with `recommended_next_stage: closure_candidate`; policy emitted `decision: override_recommendation`, `to_stage: verify_telemetry`, and reason `stale_authoritative_signal`.

API-key path:

```sh
GEMINI_API_KEY=... scripts/run_llm_demo.sh \
  --scenario-id E-003 \
  --model gemini-3-flash
```

Vertex AI path:

```sh
scripts/run_llm_demo.sh \
  --scenario-id E-003 \
  --model gemini-3-flash \
  --project YOUR_GOOGLE_CLOUD_PROJECT_ID \
  --location us-central1
```

Adversarial advocate/skeptic path:

```sh
scripts/run_llm_demo.sh \
  --scenario-id E-003 \
  --model gemini-3-flash \
  --project YOUR_GOOGLE_CLOUD_PROJECT_ID \
  --location us-central1 \
  --adversarial \
  --output eval_results/llm_interpreter_E003_adversarial.json \
  --evidence-packet-output docs/demo/artifacts/evidence_packet_E003_adversarial_live.html
```

Expected proof beat:

- The LLM reads technician/customer/support text and emits a schema-validated Agent Interpretation Event.
- The event may include urgency, customer impact, evidence gaps, recommended actions, reviewer questions, and an operator note.
- In the stale-telemetry scenario, the LLM can recommend `closure_candidate`; policy then overrides to `verify_telemetry` with `stale_authoritative_signal`.
- In adversarial mode, two structured LLM calls interpret the same evidence as resolution advocate and closure skeptic. A high disagreement score becomes structured policy input and can route to `human_review` with `high_interpretation_disagreement`.
- If `--evidence-packet-output` is set, the wrapper renders the successful governed LLM JSON into the same judge-facing evidence-packet HTML used by the deterministic proof packets.
- If auth is missing, the command returns JSON with `status: blocked` and the required next step.
- If the provider call works but the model output violates the local agent contract, the command returns JSON with `status: invalid_llm_output`; do not use that run as proof until it validates.

Individual generation commands are available for inspection or partial refresh.

Generate UiPath Action Center payloads:

```sh
python -m service_recovery_core.evals \
  --uipath-payload-scenario E-002 \
  --output docs/demo/artifacts/action_payload_E002.json

python -m service_recovery_core.evals \
  --uipath-payload-scenario E-004 \
  --output docs/demo/artifacts/action_payload_E004.json
```

Generate durable audit bundles:

```sh
python -m service_recovery_core.evals \
  --audit-bundle-scenario E-002 \
  --output docs/demo/artifacts/service_recovery_audit_bundle_E002.json

python -m service_recovery_core.evals \
  --audit-bundle-scenario E-004 \
  --output docs/demo/artifacts/service_recovery_audit_bundle_E004.json
```

Generate judge-readable evidence packets:

```sh
python -m service_recovery_core.evals \
  --evidence-packet-html-scenario E-002 \
  --output docs/demo/artifacts/evidence_packet_E002.html

python -m service_recovery_core.evals \
  --evidence-packet-html-scenario E-004 \
  --output docs/demo/artifacts/evidence_packet_E004.html
```

Verify the proof-critical fields:

```sh
jq -r '[.case_id,.agent_interpretation_event.recommended_next_stage,.policy_decision_event.decision,.policy_decision_event.from_recommended_stage,.policy_decision_event.to_stage,.policy_decision_event.block_reason,.policy_decision_event.links_to] | @tsv' \
  docs/demo/artifacts/service_recovery_audit_bundle_E002.json \
  docs/demo/artifacts/service_recovery_audit_bundle_E004.json

jq -r '[(.RawAgentRecommendation|fromjson).recommended_next_stage,(.PolicyDecisionJson|fromjson).decision,(.PolicyDecisionJson|fromjson).from_recommended_stage,(.PolicyDecisionJson|fromjson).to_stage,(.PolicyDecisionJson|fromjson).block_reason,(.PolicyDecisionJson|fromjson).links_to] | @tsv' \
  docs/demo/artifacts/action_payload_E002.json \
  docs/demo/artifacts/action_payload_E004.json

rg -n "closure_candidate|override_recommendation|require_human_review|verify_telemetry|human_review|missing_authoritative_signal|source_contradiction" \
  docs/demo/artifacts/evidence_packet_E002.html \
  docs/demo/artifacts/evidence_packet_E004.html
```

Optional screenshot capture:

```sh
npx playwright screenshot \
  --viewport-size=1440,1100 \
  file://$PWD/docs/demo/artifacts/evidence_packet_E002.html \
  docs/demo/artifacts/evidence_packet_E002_desktop.png

npx playwright screenshot \
  --viewport-size=1440,1100 \
  file://$PWD/docs/demo/artifacts/evidence_packet_E004.html \
  docs/demo/artifacts/evidence_packet_E004_desktop.png

npx playwright screenshot \
  --viewport-size=1440,1100 \
  file://$PWD/docs/demo/artifacts/evidence_packet_E003_adversarial_live.html \
  docs/demo/artifacts/evidence_packet_E003_adversarial_desktop.png

npx playwright screenshot \
  --viewport-size=390,900 \
  file://$PWD/docs/demo/artifacts/evidence_packet_E003_adversarial_live.html \
  docs/demo/artifacts/evidence_packet_E003_adversarial_mobile.png
```

## UiPath CLI Readback Checks

Confirm login:

```sh
uip login status --output json
```

Read the pinned process:

```sh
uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json

uip or processes version-history 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 \
  --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de \
  --output json
```

Read Action Center task state when validating a run:

```sh
uip tasks get 4300080 --output json
uip tasks get 4300219 --output json
```

Read live case/job state:

```sh
uip or jobs get 3af41e1d-8b04-4eba-aa5e-a95c5c673730 --output json
uip or jobs get 60e52ca5-6891-45b4-9e98-e1b08a984f06 --output json
uip or jobs history 60e52ca5-6891-45b4-9e98-e1b08a984f06 --output json
```

Observed readback on 2026-06-26:

- `processes get` infers folder by process key and rejects `--folder-key`; `version-history` accepts `--folder-key`.
- Current process readback: `ProcessVersion: 1.0.5`, `AutoUpdate: false`, `IsLatestVersion: false`.
- Version history shows `1.0.3`, `1.0.4`, and `1.0.5`.
- E-002 task `4300080` and E-004 task `4300219` read back as completed `AppTask` records with `Action: reject`, reviewer comments, `FolderId: 7978263`, and `TaskSource.SourceName: CaseManagement`.
- E-002 and E-004 jobs still read back as `State: Running` after task completion; use task completion plus audit bundle as proof of reviewer action, and do not claim terminal case-job completion unless a fresh job reaches a terminal state.

Expected proof fields in task or payload readback:

- `RawAgentRecommendation` contains `recommended_next_stage: closure_candidate`.
- `PolicyDecisionJson` contains a linked policy event.
- E-002 policy event routes to `verify_telemetry`.
- E-004 policy event routes to `human_review`.
- Policy reason is `missing_authoritative_signal`, `stale_authoritative_signal`, or `source_contradiction`.

## Orchestrator Bucket Audit Proof

Upload or refresh the E-004 audit bundle:

```sh
uip or bucket-files upload \
  dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb \
  audit/service_recovery_audit_bundle_E004.json \
  --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de \
  --file docs/demo/artifacts/service_recovery_audit_bundle_E004.json \
  --content-type application/json \
  --output json
```

List bucket files:

```sh
uip or bucket-files list \
  dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb \
  --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de \
  --output json
```

Download and verify:

```sh
uip or bucket-files download \
  dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb \
  audit/service_recovery_audit_bundle_E004.json \
  --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de \
  --destination eval_results/downloaded_audit_bundle_E004.json \
  --output json

cmp -s \
  docs/demo/artifacts/service_recovery_audit_bundle_E004.json \
  eval_results/downloaded_audit_bundle_E004.json \
  && echo bucket-download-matches
```

Expected audit fields:

- `audit_contract_version: service-recovery-audit-v1`
- `agent_interpretation_event.recommended_next_stage: closure_candidate`
- `policy_decision_event.links_to` points to the agent event.
- `policy_decision_event.from_recommended_stage: closure_candidate`
- `policy_decision_event.to_stage: human_review` for E-004.
- `evidence_state.closure_block_reason: source_contradiction` for E-004.
- `policy_versions.interpretation_policy_version: ip-v1`
- `policy_versions.decision_policy_version: dp-v1`

## Demo Operator Flow

Use [DEMO_STORYBOARD.md](DEMO_STORYBOARD.md) for the sub-five-minute recording script. This runbook is the operational backup for the screens and commands in that script.

For recording day, pre-stage the following and avoid live mutation unless a new proof ID is intentionally needed:

| Stage | Open / verify | Purpose |
| --- | --- | --- |
| UiPath platform proof | Maestro Case process/case surface, Action Center tasks `4300080` and `4300219`, Orchestrator bucket/process readback, Test Manager `SREV` | Shows the solution running through UiPath platform surfaces. |
| 2A proof | `docs/demo/artifacts/evidence_packet_E002.html` | Shows raw `closure_candidate` overridden to `verify_telemetry`. |
| 2B proof | `docs/demo/artifacts/evidence_packet_E004.html` | Shows same green fixture escalated to `human_review` because authoritative evidence contradicts. |
| LLM usefulness proof | `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` | Shows agent interpretation and disagreement as structured policy input, not final authority. |
| Eval/learning proof | `docs/demo/artifacts/policy_improvement_E008.json` and Test Manager `SREV` | Shows E-001 through E-009 discipline and no auto-promotion. |
| Coding-agent proof | `README.md`, `docs/submission/CODING_AGENT_PROOF_LOG.md`, terminal validation output | Shows Codex build-time contribution without weakening runtime governance. |

The shortest safe recording path is:

1. Show the canonical green business fixture.
2. Show 2A local and/or live evidence:
   - business state green,
   - telemetry missing/stale,
   - raw agent recommends `closure_candidate`,
   - policy overrides to `verify_telemetry`,
   - case routes to verification/retry instead of closure.
3. Reset narrative to the same green fixture.
4. Show 2B:
   - only authoritative telemetry/inventory changes,
   - fresh authoritative contradiction appears,
   - raw agent still recommends `closure_candidate`,
   - policy routes to `human_review`,
   - custom evidence packet shows elevated exception packet.
5. Show Action Center task lifecycle/reviewer return as platform proof.
6. Show Orchestrator bucket artifact readback as durable audit proof.
7. Show Test Manager `SREV` as manual eval coverage proof with terminal execution `40a1b334-5df8-1100-0a4b-0b49d0564f11`.

## Do Not Claim

- Do not claim generated Action Center UI is final-demo ready.
- Do not claim native Case history alone passes G-001.
- Do not claim automated Test Cloud execution.
- Do not claim real telecom integrations.
- Do not pitch the product as a generic agent governance platform.

## Reset / Rebuild Checklist

Before a demo dry run:

```sh
git status --short --branch
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
python -m service_recovery_core.evals --evidence-packet-html-scenario E-002 --output docs/demo/artifacts/evidence_packet_E002.html
python -m service_recovery_core.evals --evidence-packet-html-scenario E-004 --output docs/demo/artifacts/evidence_packet_E004.html
python -m service_recovery_core.evals --audit-bundle-scenario E-004 --output docs/demo/artifacts/service_recovery_audit_bundle_E004.json
```

After a demo dry run:

- Record commands and observed UiPath IDs in `docs/logs/BUILD_LOG.md`.
- Add product feedback only for new, concrete UiPath observations.
- If live artifacts changed, commit the runbook/log update and push.
