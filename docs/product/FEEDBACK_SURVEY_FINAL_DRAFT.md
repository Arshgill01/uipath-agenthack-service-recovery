# UiPath Product Feedback Survey Final Draft

Status: near-final answer draft. User-owned identity fields still need confirmation before submission.

Source of truth:

- `docs/product/PRODUCT_FEEDBACK_AWARD.md`
- `docs/product/FEEDBACK_AWARD_APPENDIX.md`
- `docs/product/FEEDBACK_SURVEY_COPY_READY.md`
- `docs/validation/VALIDATION_RESULTS.md`

## 1. What's your first name?

Arshdeep

## 2. What's your last (family) name?

Singh

## 3. What's the name of your team?

Needs user confirmation.

## 4. Add here your email address.

arshgill6120@gmail.com

## 5. Please rate your overall satisfaction with UiPath AgentHack.

Recommended choice: Somewhat satisfied.

Reasoning: UiPath gave us enough real platform surface to validate a governed Maestro Case workflow end to end: Maestro Case, Action Center lifecycle, Orchestrator package/process/bucket operations, Test Manager manual eval representation, and CLI readback. We are not choosing "Very satisfied" because first-time tenant readiness, generated Action app binding, runtime validation, package/feed diagnostics, and native audit reconstruction all required workarounds.

Evidence: PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-019, PF-022.

## 6. Which categories did you compete in AgentHack?

Recommended selections:

- UiPath Maestro Case
- UiPath Test Cloud, only if we want to cite the validated Test Manager manual mapping honestly

Do not select UiPath Maestro BPMN unless a real BPMN artifact is built and validated.

## 7. Please briefly describe your use case.

We built a telecom/broadband service activation and restoration exception workflow in UiPath Maestro Case. The risk we modeled is common in service operations: CRM, order, billing, and support notes can all look green while authoritative network telemetry is missing, stale, or contradicts the business state.

Our agent reads messy technician notes, customer messages, and support context into a structured Agent Interpretation Event. The agent can recommend `closure_candidate`, but it does not get final authority. A deterministic policy layer checks evidence authority, freshness, contradiction, confidence, and pinned policy versions before routing the case. If authoritative telemetry is missing or stale, policy overrides closure and routes to `verify_telemetry`; if fresh authoritative telemetry contradicts the green business state, policy escalates to `human_review` with an evidence packet.

The proof preserves the raw agent recommendation separately from the final Policy Decision Event, so the demo can show exactly where AI interpretation ends and governed closure control begins. We also validated an optional live Gemini/Vertex interpretation path, including an adversarial advocate/skeptic interpretation where the advocate recommended closure, the skeptic found unresolved risk, and deterministic policy escalated because the structured disagreement score crossed threshold.

Evidence: `docs/demo/artifacts/evidence_packet_E002.html`, `docs/demo/artifacts/evidence_packet_E004.html`, `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html`, `docs/demo/artifacts/demo_proof_manifest.json`, PF-015.

## 8. Please indicate your overall satisfaction with the UiPath Platform.

Recommended choice: Somewhat satisfied.

The platform primitives were strong. Maestro Case fit the architecture, Action Center handled human task lifecycle after enablement, Orchestrator gave package/process/job and bucket artifact operations, and Test Manager could represent the eval suite. The friction was not conceptual fit; it was the lack of guided readiness and diagnostics across services, generated Action app fields, required task inputs, package/feed binding, and domain audit reconstruction.

## 9. How easy was it to build your solution?

Recommended choice: Somewhat difficult.

The local policy/eval layer was straightforward. The difficult part was proving the platform behavior live and repeatably: enabling Actions, mapping human-review evidence fields, finding a runtime-only missing Action task Title, resolving package/feed/version behavior, proving task return shape, keeping Case job claims honest, and iterating from a blocked legacy Data Fabric entity to a validated PascalCase V2 audit record.

Evidence: PF-003, PF-006, PF-007, PF-013, PF-017, PF-019, PF-022, PF-023.

## 10. What challenges did you encounter while building the solution?

The hardest part was turning a first-time Maestro Case build into a repeatable, observable runtime proof.

The major challenge classes were:

- Tenant and service readiness: Actions was required for human review but was not enabled for the tenant initially. The disabled-service page did not show the exact admin path we later used to enable it.
- Human-review authoring: Studio Web exposed the right Case and Action primitives, but the Human action flow did not clearly guide evidence-packet input mapping, output mapping, or reviewer return.
- Generated reviewer UI: `PolicyDecisionJson` persisted correctly through task/API data, but the generated Action Center page rendered that proof-critical field as `Unnamed String 1` and repeated blank/unreadable fields in a completed E-004 task.
- Runtime validation: deployment succeeded even when a required Action task `Title` was missing. The first actionable error appeared only after a live case faulted at runtime.
- Package/feed/process diagnostics: a package uploaded to the solution feed and could be read with `--feed-id`, while default lookup and direct process creation could not bind the same version.
- Audit reconstruction: native Case/task history plus APIs can reconstruct operational flow, but a clean domain audit for evidence state, policy versions, raw recommendation, policy decision, block reason, human action, and timestamps still required explicit custom audit artifacts.
- Data Fabric persistence: entity create/readback worked, snake_case JSON insert/update could not map required custom fields despite valid-looking payloads, and the later CSV-created row could not expose custom payload fields through CLI readback. A PascalCase V2 schema then solved the full-payload storage/readback path and gave us a useful product-feedback insight: field names accepted at schema creation should work consistently across insert/update/query/get or be rejected up front.
- Test Manager eval mapping: project, cases, test set, and manual pass logs worked, but E-001 through E-009 had to be represented manually. A first execution stayed `Running` after direct child-log finishes; a later explicit start-then-finish lifecycle reached terminal `Status: Finished` with 9/9 passed logs and JUnit export. Automated Test Cloud execution remained unclaimable after a concrete package probe: Orchestrator accepted `ServiceRecoveryEvalProcessProbe:0.0.2/0.0.3` and exposed an entry point, but Test Manager discovery returned no automations and direct linking failed with `Test ... not found in package`.

Evidence: PF-003, PF-004, PF-006, PF-007, PF-013, PF-015, PF-017, PF-019, PF-020, PF-021, PF-022, PF-023, PF-024, PF-025.

## 11. If you had to change one thing about the UiPath Platform experience, what would it be and why?

Add a Maestro Case human-review readiness and preflight path.

Before a builder publishes or starts a Case with a human review step, UiPath should verify tenant services and roles, Actions/Action Center availability, required Action task fields such as Title, schema-to-page binding for every input/output property, Case variable to Action input mapping, Action output to Case variable mapping, package/feed binding, package version readback, and audit readiness.

This one improvement would have shortened our slowest loops: enabling Actions, diagnosing generated Action page binding, fixing runtime-only required-field failures, proving package version pinning, and deciding where to store audit evidence. Maestro Case is most valuable when it coordinates agents, systems, and people; those workflows need a preflight that proves the reviewer will see the right evidence before a live case starts.

Evidence: PF-003, PF-006, PF-007, PF-013, PF-017.

## 12. What surprised you the most? What would you tell another developer?

The positive surprise was that the UiPath primitives were closer to our target architecture than expected. Maestro Case gave the long-running case shell, Action Center gave real human task lifecycle, Orchestrator gave package/process/job and audit artifact operations, and task APIs preserved structured payloads well enough to prove the boundary between raw agent recommendation and final policy decision.

The advice to another developer is to validate hard gates early with API readback and committed proof artifacts, not only with the designer or generated UI. Confirm tenant services, Action Center rendering, task return shape, package version readback, audit reconstruction, and any live LLM proof path before polishing the app. In our build, the backend task data preserved the policy payload correctly even when the generated reviewer UI hid it, so API readback and repeatable local checks were essential.

Evidence: `scripts/run_submission_check.sh`, PF-013, PF-015, PF-016, PF-017, PF-022.

## 13. What did you build with Maestro that would have been a mess to stitch together without it?

We used Maestro Case as the orchestration boundary for governed service-recovery exceptions. Without Maestro, we would have had to stitch together case state, stage routing, agent interpretation, deterministic policy decisions, human task assignment, reviewer comments, process/package versioning, runtime timestamps, and audit artifacts across separate tools.

In our validated proof beats, the raw agent event recommended `closure_candidate`, while policy either overrode to `verify_telemetry` for missing authoritative telemetry or escalated to `human_review` for fresh contradiction. Action Center handled the human lifecycle, Orchestrator exposed package/process/job and audit artifact operations, and explicit audit bundles reconstructed the domain event chain.

The product improvement request is to make that domain audit timeline native: linked agent interpretation, policy decision, evidence state, block reason, human action, timestamps, and policy/package versions in one Case view or query.

Evidence: live E-002 task `4300080`, live E-004 task `4300219`, Orchestrator bucket audit artifact `audit/service_recovery_audit_bundle_E004.json`, PF-015, PF-022.

## 14. Can we share your story?

Needs user confirmation.

Options:

- Yes, you can use my name, title, and company in UiPath marketing materials.
- Yes, but please show me the final version before publishing.
- Use my story without my name.
- No. Please keep this private for the UiPath team's internal reference only.

## Claims To Avoid

- Do not claim automated Test Cloud execution. The validated Test Manager path is manual; the RPA package probe did not produce a Test Manager-visible automation target.
- Claim Data Fabric full-payload persistence only for the validated PascalCase V2 path; do not use the legacy snake_case entity as proof.
- Do not claim generated Action Center UI is final-demo ready.
- Do not claim native Case history alone passes G-001.
- Do not claim terminal completion for older E-002/E-004 jobs while their job readback remains `Running`; claim only the fresh package `1.0.6` Case Instance completion if cited.
- Do not frame the project as a generic agent governance platform.
