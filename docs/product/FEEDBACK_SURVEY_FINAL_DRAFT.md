# UiPath Product Feedback Survey Final Draft

Status: near-final answer draft. User-owned identity fields still need confirmation before submission.

This is the cleaner one-form draft for the Microsoft Form. It should be copied as prose, not as an evidence index. Internal PF labels are kept only in the traceability section at the bottom and should not be pasted into the form unless UiPath asks for proof references.

Source of truth:

- `docs/product/PRODUCT_FEEDBACK_AWARD.md`
- `docs/product/FEEDBACK_AWARD_APPENDIX.md`
- `docs/product/FEEDBACK_SURVEY_COPY_READY.md`
- `docs/validation/VALIDATION_RESULTS.md`
- `docs/research/RESEARCH_LOG.md`

Use `FEEDBACK_AWARD_APPENDIX.md` as the ranked internal evidence source when checking the final form. The submitted survey should lead with the Maestro Case Human-Review Readiness Check and auditability-contract recommendation, then explain Action Center binding, native audit, package/feed, Data Fabric, and Test Manager examples in plain language.

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

Reasoning: UiPath gave us enough real platform surface to validate a governed Maestro Case workflow end to end: Maestro Case, Action Center lifecycle, Orchestrator package/process/bucket operations, Data Fabric V2 audit readback, Test Manager manual eval representation, and CLI diagnostics. We are not choosing "Very satisfied" because a first-time human-review Case build still required workarounds across tenant readiness, generated Action app binding, runtime validation, package/feed diagnostics, Data Fabric field-name behavior, and native audit reconstruction.

This rating reflects a real working proof, but also the time spent discovering tenant readiness, generated Action app binding, runtime validation, package/feed diagnostics, Data Fabric field-name behavior, and native audit reconstruction issues.

## 6. Which categories did you compete in AgentHack?

Recommended selections:

- UiPath Maestro Case
- UiPath Test Cloud, only if we want to cite the validated Test Manager manual mapping honestly

Do not select UiPath Maestro BPMN unless a real BPMN artifact is built and validated.

## 7. Please briefly describe your use case.

We built a telecom/broadband service activation and restoration exception workflow in UiPath Maestro Case. The risk we modeled is common in service operations: CRM, order, billing, and support notes can all look green while authoritative network telemetry is missing, stale, or contradicts the business state.

Our agent reads messy technician notes, customer messages, and support context into a structured Agent Interpretation Event. The agent can recommend `closure_candidate`, but it does not get final authority. A deterministic policy layer checks evidence authority, freshness, contradiction, confidence, and pinned policy versions before routing the case. If authoritative telemetry is missing or stale, policy overrides closure and routes to `verify_telemetry`; if fresh authoritative telemetry contradicts the green business state, policy escalates to `human_review` with an evidence packet.

The proof preserves the raw agent recommendation separately from the final Policy Decision Event, so the demo can show exactly where AI interpretation ends and governed closure control begins. We also validated an optional live Gemini/Vertex interpretation path, including an adversarial advocate/skeptic interpretation where the advocate recommended closure, the skeptic found unresolved risk, and deterministic policy escalated because the structured disagreement score crossed threshold.

The build produced separate evidence packets for the missing-telemetry path, the contradiction/human-review path, and the optional adversarial Gemini/Vertex interpretation path.

## 8. Please indicate your overall satisfaction with the UiPath Platform.

Recommended choice: Somewhat satisfied.

The platform primitives were strong. Maestro Case fit the architecture, Action Center handled human task lifecycle after enablement, Orchestrator gave package/process/job and bucket artifact operations, and Test Manager could represent the eval suite. The friction was not conceptual fit; it was the lack of guided readiness and diagnostics across services, generated Action app fields, required task inputs, package/feed binding, and domain audit reconstruction.

## 9. How easy was it to build your solution?

Recommended choice: Somewhat difficult.

The local policy/eval layer was straightforward. The difficult part was proving the platform behavior live and repeatably: enabling Actions, mapping human-review evidence fields, finding a runtime-only missing Action task Title, resolving package/feed/version behavior, proving task return shape, keeping Case job claims honest, and iterating from a blocked legacy Data Fabric entity to a validated PascalCase V2 audit record.

The difficulty came from live platform proof work rather than the local policy model.

## 10. What challenges did you encounter while building the solution?

The hardest part was not the service-recovery policy model. It was turning a first-time Maestro Case human-review workflow into a repeatable, observable runtime proof.

The main pattern was clear: UiPath exposed the right primitives, but we had to discover readiness and binding gaps by combining Studio Web, Maestro Case, Action Center, Orchestrator, Data Fabric, Test Manager, and CLI readbacks instead of running one shared preflight.

The major challenge classes were:

- Tenant and service readiness: Actions was required for human review but was not enabled for the tenant initially. The disabled-service page did not show the exact admin path we later used to enable it.
- Human-review authoring and preflight: Studio Web exposed the right Case and Action primitives, but the Human action flow did not clearly guide evidence-packet input mapping, output mapping, reviewer return, required `Title`, or rule readiness. A PFPROBE scratch Case showed `uip maestro case validate` catching missing rules and a required field while `uip solution pack --dry-run` returned `Status: Valid` and `uip solution upload` accepted the same invalid scratch solution with `ErrorList: []`.
- Generated reviewer UI and binding/version visibility: `PolicyDecisionJson` persisted correctly through task/API data, but the generated Action Center page rendered that proof-critical field as `Unnamed String 1`. A later label-only Studio publish did not fix the Case-bound runtime task; read-only registry probes showed the task used an older Action app deployment while a newer deployment existed elsewhere.
- Runtime and process diagnostics: deployment succeeded even when a required Action task `Title` was missing, and `uip maestro case processes diagnose` later failed with `summaries.find is not a function` instead of producing repair guidance for the AppTasks failure family.
- Package/feed/process binding: a package uploaded to the solution feed and could be read with `--feed-id`, while default lookup and direct process creation could not bind the same version.
- Audit reconstruction: native Case/task history plus APIs can reconstruct operational flow, but a clean domain audit for evidence state, policy versions, raw recommendation, policy decision, block reason, human action, and timestamps still required explicit custom audit artifacts.
- Data Fabric persistence: entity create/readback worked, snake_case JSON insert/update could not map required custom fields despite valid-looking payloads, and the later CSV-created row could not expose custom payload fields through CLI readback. A PascalCase V2 schema then solved the full-payload storage/readback path and gave us a useful product-feedback insight: field names accepted at schema creation should work consistently across insert/update/query/get or be rejected up front.
- Test Manager eval mapping: project, cases, test set, and manual pass logs worked, but E-001 through E-009 had to be represented manually. A first execution stayed `Running` after direct child-log finishes; a later explicit start-then-finish lifecycle reached terminal `Status: Finished` with 9/9 passed logs and JUnit export. Automated Test Cloud execution remained unclaimable after a concrete package probe: Orchestrator accepted the package and exposed an entry point, but Test Manager discovery returned no automations and direct linking could not find a test in the package.

Expected behavior: before a builder publishes or starts a human-review Case, UiPath should make it clear whether the required services, reviewer visibility, Action task fields, generated Action app bindings, package/feed version, and audit path are ready.

Workaround used: we enabled Actions manually, ran Case validation separately from solution packaging, repaired or bypassed task-field problems, used CLI/API readbacks for task and package state, used custom evidence packets for readable policy proof, stored audit payloads through validated Data Fabric V2 and Orchestrator artifact paths, and kept Test Manager claims manual-only.

These were reproduced during the actual build across Maestro Case, Action Center, Orchestrator, Data Fabric, Test Manager, and the UiPath CLI. The strongest examples were not abstract: Actions tenant enablement blocked human review at first, a required task `Title` failed only at runtime, a proof-critical generated Action Center field rendered as `Unnamed String 1`, a package version was visible only with the feed specified, Data Fabric field naming/readback behavior required a V2 schema, and Test Manager could represent our evals manually but not as a discoverable automated Test Cloud execution.

## 11. If you had to change one thing about the UiPath Platform experience, what would it be and why?

Add a Maestro Case Human-Review Readiness Check: a preflight and auditability contract for Cases that route work to a human reviewer. This is the top feedback thesis from the reproduced build evidence, not a generic "add more validation" request.

UiPath already has validation, simulation, debug, testing, Actions, retry, and migration primitives. The missing layer we felt was one cross-surface report that answers: "Will this human-review Case actually work when it starts?" Before a builder publishes or starts a Case with a human review step, the readiness check should verify tenant services and roles, Actions/Action Center availability, required Action task fields such as `Title`, schema-to-page binding for every input/output property, Case variable to Action input mapping, Action output to Case variable mapping, reviewer visibility for proof-critical fields, package/feed binding, package version readback, audit readiness, and agreement between Case validation, solution dry-run packaging, and Studio Web upload/import.

The report could appear in Studio Web as `Run human-review readiness check` and in CLI as a command such as `uip maestro case preflight`. It should return specific pass/fail findings with fix links: Actions not enabled for this tenant, Action task `Title` missing, generated reviewer page has no rendered control for `PolicyDecisionJson`, the Case will instantiate an older Action app deployment than the one just repaired, package/feed lookup is resolving a different version than expected, or native Case history will not reconstruct the declared domain audit without a custom event.

The same product primitive should produce a native Case audit timeline after runtime: linked Agent Interpretation Event, Policy Decision Event, evidence state, block reason, human action/comment, timestamps, package version, and policy versions. That makes the ask one coherent contract: prove the human-review Case is ready before runtime, then prove what happened after runtime.

This one improvement would have shortened our slowest loops: enabling Actions, diagnosing generated Action page binding, fixing runtime-only required-field failures, proving package version pinning, reconciling inconsistent readiness signals, and deciding where to store audit evidence. This is not telecom-specific. Any serious Maestro Case workflow with agents, automations, humans, policy decisions, and audit obligations can fail in the same way if designer validity does not prove runtime reviewer readiness.

This recommendation comes from multiple reproduced loops, not a single bug: service enablement, Action field requirements, generated page binding, package version binding, validation/package/upload agreement, and audit-readiness proof all needed separate investigation. It also aligns with the official Maestro Case positioning: long-running, exception-heavy work with people, agents, automations, visibility, and auditability needs a readiness and auditability contract, not only runtime recovery after something fails.

## 12. What surprised you the most? What would you tell another developer?

The positive surprise was that the UiPath primitives were closer to our target architecture than expected. Maestro Case gave the long-running case shell, Action Center gave real human task lifecycle, Orchestrator gave package/process/job and audit artifact operations, and task APIs preserved structured payloads well enough to prove the boundary between raw agent recommendation and final policy decision.

The advice to another developer is to validate hard gates early with API readback and committed proof artifacts, not only with the designer or generated UI. Confirm tenant services, Action Center rendering, task return shape, package version readback, audit reconstruction, and any live LLM proof path before polishing the app. In our build, the backend task data preserved the policy payload correctly even when the generated reviewer UI hid it, so API readback and repeatable local checks were essential.

In practice, the best developer habit was to keep a repeatable local submission check and then confirm the important boundaries with live API readback.

## 13. What did you build with Maestro that would have been a mess to stitch together without it?

We used Maestro Case as the orchestration boundary for governed service-recovery exceptions. Without Maestro, we would have had to stitch together case state, stage routing, agent interpretation, deterministic policy decisions, human task assignment, reviewer comments, process/package versioning, runtime timestamps, and audit artifacts across separate tools.

In our validated proof beats, the raw agent event recommended `closure_candidate`, while policy either overrode to `verify_telemetry` for missing authoritative telemetry or escalated to `human_review` for fresh contradiction. Action Center handled the human lifecycle, Orchestrator exposed package/process/job and audit artifact operations, and explicit audit bundles reconstructed the domain event chain.

The product improvement request is to make that domain audit timeline native: linked agent interpretation, policy decision, evidence state, block reason, human action, timestamps, and policy/package versions in one Case view or query.

The strongest live proof examples were the two Action Center human-review tasks for the missing-telemetry and contradiction paths, plus the E-004 audit bundle stored as an Orchestrator artifact.

## Internal Traceability - Do Not Paste Into The Form

These labels map the final-form prose back to the detailed evidence log in `docs/product/FEEDBACK_AWARD_APPENDIX.md`.

| Form area | Internal evidence labels |
| --- | --- |
| Satisfaction rating | PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-019, PF-022, PF-026, PF-027, PF-028 |
| Use case | PF-015 plus demo evidence packets and live E-002/E-004 tasks |
| Ease of build | PF-003, PF-006, PF-007, PF-013, PF-017, PF-019, PF-022, PF-023, PF-026, PF-027, PF-028 |
| Challenges | PF-003, PF-004, PF-006, PF-007, PF-013, PF-015, PF-017, PF-019, PF-020, PF-021, PF-022, PF-023, PF-024, PF-025, PF-026, PF-027, PF-028 |
| One change | PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-026, PF-027, PF-028; secondary support from PF-019 and PF-023 |
| Surprise/advice | PF-013, PF-015, PF-016, PF-017, PF-022 plus `scripts/run_submission_check.sh` |
| Maestro value | PF-015, PF-022 plus live E-002/E-004 task and audit-bundle artifacts |

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
