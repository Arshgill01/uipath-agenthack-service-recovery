# Feedback Survey Copy-Ready Bank

Status: evidence-backed answer bank for the final UiPath product feedback form. Fill owner/team/share fields manually at submission time.

Source files:

- `docs/product/PRODUCT_FEEDBACK_AWARD.md`
- `docs/product/FEEDBACK_AWARD_APPENDIX.md`
- `docs/product/FEEDBACK_SURVEY_DRAFT.md`
- `docs/product/FEEDBACK_SURVEY_FINAL_DRAFT.md`
- `docs/validation/VALIDATION_RESULTS.md`
- `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`

## Fields That Need User Confirmation

| Question | Current value |
| --- | --- |
| First name | `Arshdeep` |
| Last name | `Singh` |
| Team name | needs user confirmation |
| Email | `arshgill6120@gmail.com` |
| Story sharing preference | needs user confirmation |

## Recommended Choices

| Question | Recommended answer | Why |
| --- | --- | --- |
| Overall satisfaction with AgentHack | `Somewhat satisfied` | The platform enabled a real Maestro Case + Action Center + Orchestrator proof, but setup, diagnostics, and generated Action app issues slowed validation. |
| Categories | `UiPath Maestro Case`; include `UiPath Test Cloud` only if the final submission wants to cite the validated Test Manager manual mapping. | Maestro Case is the primary validated track; Test Manager was represented manually, not automated. |
| Overall satisfaction with UiPath Platform | `Somewhat satisfied` | Strong primitives, but first-time builder readiness and runtime diagnostics need work. |
| Ease of build | `Somewhat difficult` | The architecture mapped well; the difficult part was proving tenant/service readiness, package/version binding, Action Center rendering, and audit readback. |

## Q7 - Briefly Describe Your Use Case

We built a telecom/broadband service activation and restoration exception workflow in UiPath Maestro Case. The problem is that CRM, order, billing, and support notes can all look green while authoritative network telemetry is missing, stale, or contradicts the business state. An agent interprets ambiguous evidence into structured signals, but deterministic policy makes the closure and routing decision. The proof preserves the raw agent recommendation separately from the final policy decision: when the agent recommends `closure_candidate` but telemetry is missing, policy overrides to `verify_telemetry`; when fresh authoritative telemetry contradicts the green business state, policy escalates to `human_review` with an evidence packet. We also validated an optional live Gemini/Vertex path, including an adversarial advocate/skeptic interpretation where policy escalated because structured interpretation disagreement crossed threshold.

Evidence:

- `docs/demo/artifacts/evidence_packet_E002.html`
- `docs/demo/artifacts/evidence_packet_E004.html`
- `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html`
- `docs/demo/artifacts/demo_proof_manifest.json`
- Live E-002 task `4300080`; live E-004 task `4300219`.

## Q10 - Challenges Encountered

The hardest part was turning a first-time Maestro Case build into a repeatable, observable runtime proof. The policy engine and evals were straightforward; the slower work was validating platform readiness and runtime behavior.

Specific challenges:

- Actions/Action Center was required for human review but was not enabled for the tenant at first. The disabled-service page did not show the exact admin enablement path we later used.
- Human-review authoring exposed the right primitives, but the generated Action app flow did not make schema-to-page binding, required task fields, or structured return mapping obvious.
- A required Action task `Title` field passed deployment but failed at live runtime, so the missing field was discovered only after starting a case.
- The generated reviewer page hid or mislabeled a proof-critical field: `PolicyDecisionJson` persisted correctly in task/API data but rendered as `Unnamed String 1`.
- Package/feed/process diagnostics required extra work. A package could be read with `--feed-id`, while default lookup and direct process creation could not bind the same version.
- Native Case history and task APIs can reconstruct operational flow, but a clean domain audit for evidence state, raw agent recommendation, policy decision, policy versions, block reason, and human action still required explicit custom audit artifacts.
- Data Fabric entity create/readback worked, but the first snake_case entity could not map the required `case_id` field despite multiple valid-looking JSON shapes. A PascalCase V2 schema later solved the full-payload audit storage/readback path and sharpened the product feedback around field-name lifecycle consistency.
- Test Manager could represent the eval suite as manual cases and passed logs, but it was not a one-step import from the local eval result. A first direct-finish execution stayed `Running`; the corrected start-then-finish lifecycle produced terminal manual execution `40a1b334-5df8-1100-0a4b-0b49d0564f11` with 9/9 passed logs and JUnit export. Automated Test Cloud execution still needs a real automation target.

Evidence:

- PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-019, PF-020, PF-021, PF-022, PF-023, PF-024, PF-025.

## Q11 - One Thing To Change

Add a Maestro Case human-review readiness and preflight path.

Before a builder publishes or runs a Case with a human review step, UiPath should verify:

- tenant services and roles: Actions, Action Center, Orchestrator, Test Manager, Integration Service, Data Service/Data Fabric,
- required Action task fields such as Title,
- schema-to-generated-page binding for every input/output property,
- Case variable to Action input mapping,
- Action output to Case variable mapping,
- package/feed binding and the package version the next process run will use,
- process `AutoUpdate` and package-version readback,
- native audit coverage versus required custom audit events.

This would have shortened our slowest loops: enabling Actions, diagnosing generated Action page binding, fixing runtime-only task field failures, proving package version pinning, and deciding where to store audit evidence. Maestro Case is strongest when it coordinates agents, systems, and people; those workflows need a preflight that proves the reviewer will see the right evidence before a live case starts.

Evidence:

- PF-003, PF-006, PF-007, PF-013, PF-017.

## Q12 - What Surprised You / Advice To Another Developer

The positive surprise was that the UiPath primitives were closer to our architecture than expected. Maestro Case gave the long-running case shell, Action Center gave real human task lifecycle, Orchestrator gave process/package/job controls and bucket storage, and task APIs preserved structured payloads well enough to prove the boundary between raw agent recommendation and final policy decision.

The advice to another developer is to validate hard gates early with API readback and committed proof artifacts, not only with the designer or generated UI. Confirm tenant services, Action Center rendering, package version readback, task return shape, audit reconstruction, and any live LLM proof path before polishing the app. In our build, the backend task data preserved the policy payload correctly even when the generated reviewer UI hid it, so API readback and repeatable local checks were essential.

Evidence:

- `scripts/run_demo.sh`
- `scripts/run_submission_check.sh`
- `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`
- PF-013, PF-015, PF-017, PF-022.

## Q13 - What Maestro Simplified

We used Maestro Case as the orchestration boundary for governed service-recovery exceptions. Without Maestro, we would have had to stitch together case state, stage routing, agent interpretation, deterministic policy decisions, human task assignment, reviewer comments, process/package versioning, runtime timestamps, and audit artifacts across separate tools.

In the validated proof beats, the raw agent event recommended `closure_candidate`, while policy either overrode to `verify_telemetry` for missing authoritative telemetry or escalated to `human_review` for fresh contradiction. Action Center handled the human lifecycle, Orchestrator exposed package/process/job and audit artifact operations, and explicit audit bundles reconstructed the domain event chain. The product improvement request is to make that domain audit timeline native: linked agent interpretation, policy decision, evidence state, block reason, human action, timestamps, and policy/package versions in one Case view or query.

Evidence:

- Live E-002 task `4300080`, case `3af41e1d-8b04-4eba-aa5e-a95c5c673730`.
- Live E-004 task `4300219`, case `60e52ca5-6891-45b4-9e98-e1b08a984f06`.
- Orchestrator bucket audit artifact `audit/service_recovery_audit_bundle_E004.json`.
- PF-015, PF-022.

## Do Not Claim

- Automated Test Cloud execution.
- Legacy snake_case Data Fabric audit persistence. Use the validated PascalCase `ServiceRecoveryAuditBundleV2` path for queryable E-004 audit readback.
- Generated Action Center UI is final-demo ready.
- Native Case history alone passes the domain audit gate.
- Terminal Case job completion for E-002/E-004 while jobs still read `Running`.
- A generic agent governance platform; the product is telecom/broadband service recovery.
