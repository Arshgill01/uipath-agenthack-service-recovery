# UiPath Product Feedback Survey — Final Paste Draft

## 1. What's your first name?

Arshdeep

## 2. What's your last/family name?

Singh

## 3. What's the name of your team?

[Confirm team name before submission]

## 4. Add here your email address.

[arshgill6120@gmail.com](mailto:arshgill6120@gmail.com)

## 5. Please rate your overall satisfaction with UiPath AgentHack.

Somewhat satisfied.

UiPath gave us enough real platform surface to validate a governed Maestro Case workflow end to end: Maestro Case, Action Center lifecycle, Orchestrator package/process/bucket operations, Data Fabric V2 audit readback, Test Manager manual eval representation, and CLI diagnostics. Not "Very satisfied," because a first-time human-review Case build still required workarounds to get there — the specifics are in Q10.

## 6. Which categories did you compete in AgentHack?

UiPath Maestro Case.

We also used UiPath Test Manager/Test Cloud surfaces as supporting manual eval representation, but the project's primary submission track was Maestro Case and we are not claiming automated Test Cloud execution.

## 7. Please briefly describe your use case.

We built a telecom/broadband service activation and restoration exception workflow in UiPath Maestro Case. The scenario is a realistic service-operations failure: CRM, order, billing, and support notes can all look resolved while authoritative network telemetry is missing, stale, or contradicts that green business state.

The agent's job is interpretation, not closure. It turns messy technician notes, customer messages, and support context into a structured Agent Interpretation Event. Deterministic policy then checks evidence authority, freshness, contradictions, confidence, and pinned policy versions before deciding the route.

The demo keeps the raw agent recommendation separate from the final Policy Decision Event. In the missing/stale telemetry path, the agent can recommend `closure_candidate`, but policy overrides to `verify_telemetry`. In the contradiction path, the business fixture stays green, but fresh authoritative evidence disagrees, so policy escalates to `human_review` with an evidence packet.

We also validated an optional live Gemini/Vertex interpretation path. In an adversarial advocate/skeptic run, one interpretation pressed toward closure and another found unresolved risk; deterministic policy escalated on the disagreement signal. LLM interpretation stayed useful input, never final closure authority.

The build produced separate evidence packets for the missing-telemetry path, the contradiction/human-review path, and the optional adversarial Gemini/Vertex path.

## 8. Please indicate your overall satisfaction with the UiPath Platform.

Somewhat satisfied.

The architecture fit was real, not approximate: Maestro Case matched our orchestration boundary, Action Center matched our human-task lifecycle, Orchestrator matched our package/job/artifact needs, and Test Manager could represent our eval suite. Despite the friction, we would choose Maestro Case again for this type of work — the orchestration fit was real. The gap was that none of these surfaces gave one clear answer, before runtime, on whether a human-review Case was actually ready to ship. We had to assemble that readiness picture ourselves across multiple tools.

## 9. How easy was it to build your solution?

Somewhat difficult.

The local policy/eval layer was straightforward — that part took the time it should take. What made the build slower was a repeating loop: build a piece of the human-review Case, publish or run it, discover that one cross-product binding or assumption was not actually ready, then recover through CLI/API readback and custom evidence storage. We hit that loop on tenant service enablement, Action app field binding, package/feed version resolution, and Data Fabric schema behavior. The difficulty was proving platform behavior live and repeatably, not designing the policy model.

## 10. What challenges did you encounter while building the solution?

The hardest part was not the service-recovery policy model. It was proving that a first-time Maestro Case human-review workflow would work live, show the reviewer the right evidence, and leave behind an audit trail strong enough to explain what happened.

The UiPath primitives worked: Maestro Case gave the long-running case shell, Action Center handled human task lifecycle, Orchestrator/Data Fabric supported package and audit proof, Test Manager represented the eval suite, and the CLI gave important readbacks. The friction was that readiness proof was split across those surfaces exactly when we needed one clear answer before runtime.

Reproduced gaps, grouped by the builder question they blocked:

**1. Is this human-review Case ready to start?**

* Actions was required for human review but was not enabled for the tenant initially; the disabled-service page did not show the admin path needed to enable it.
* The generated Action app flow did not clearly guide evidence-packet input/output mapping or required task fields. A required Action task `Title` passed deployment and failed only at live runtime.
* A scratch Case probe showed `uip maestro case validate` catching an invalid Case, while `uip solution pack --dry-run` returned `Status: Valid` and `uip solution upload` accepted the same invalid solution with `ErrorList: []` — three different readiness answers for the same invalid definition.

**2. Will the reviewer see the governing decision clearly?**

* `PolicyDecisionJson` existed in the Action schema and task metadata, but the generated Action Center page rendered that proof-critical field as `Unnamed String 1`. A label-only Studio publish did not fix the Case-bound runtime task; registry probes showed the task running an older Action app deployment while a newer one existed elsewhere.
* Deployment succeeded even when a required Action task `Title` was missing, and `uip maestro case processes diagnose` later failed with `summaries.find is not a function` instead of returning repair guidance.
* A package uploaded to the solution feed could be read with `--feed-id`, while default lookup and direct process creation could not bind the same version.

**3. Can we prove what happened after runtime?**

* Native Case/task history plus APIs can reconstruct operational flow, but a clean domain audit — evidence state, policy versions, raw recommendation, policy decision, block reason, human action, and timestamps — still required explicit custom audit artifacts.
* Data Fabric entity create/readback worked, but snake_case JSON insert/update could not map required custom fields despite valid-looking payloads, and a CSV-created row could not expose custom payload fields through CLI readback. A PascalCase V2 schema solved the full-payload path. The product insight: field names accepted at schema creation should work consistently across insert/update/query/get, or be rejected up front.
* Test Manager represented our evals manually — E-001 through E-009, 9/9 passed with JUnit export — but automated Test Cloud execution stayed unclaimable: the package was visible to Orchestrator, yet Test Manager discovery found no automations and direct linking found no test in the package.
* For optional external evidence sources, connector catalog and activity discovery worked across surfaces such as Google Sheets, HTTP, Data Fabric, Orchestrator, Gmail, Slack, ServiceNow, Jira, and Salesforce, but no valid tenant connection was configured for our proof path. The product gap was distinguishing connector discoverability from runtime connection readiness and giving a direct setup/fix path. We used an honest public CSV/simulator source instead of claiming a real Integration Service integration.

## 11. If you had to change one thing about the UiPath Platform experience, what would it be and why?

Add a **Maestro Case Human-Review Readiness Check** — one preflight and auditability contract for Cases that route work to a human reviewer. Every gap in Q10 would have been caught by one report instead of discovered one at a time during live runtime recovery.

UiPath already has validation, simulation, debug, testing, Actions, retry, and migration primitives. What is missing is one report that answers two questions:

1. Before runtime: will this human-review Case actually work?
2. After runtime: can we prove what the agent recommended, what policy decided, what the human did, and which versions were active?

Before publish or start, the readiness check should verify tenant services and roles, Actions/Action Center availability, required Action task fields such as `Title`, schema-to-page binding for every input/output property, Case-variable-to-Action-input and Action-output-to-Case-variable mapping, reviewer visibility for proof-critical fields, Case-bound Action app deployment/version, package/feed binding and version readback, external-evidence connector readiness, audit readiness, and agreement between Case validation, solution dry-run packaging, and Studio Web upload/import.

This could surface in Studio Web as `Run human-review readiness check` and in the CLI as `uip maestro case preflight`, returning specific pass/fail findings with fix links, for example:

* Actions is not enabled for this tenant.
* Action task `Title` is missing.
* `PolicyDecisionJson` has no rendered control in the generated reviewer page.
* This Case package will instantiate Action app version 1.0.0, not the repaired 1.0.1 deployment.
* External evidence connector selected, but no valid connection is configured — provide the exact setup link or block publish with a clear reason.
* Native Case history will not reconstruct the declared agent/policy/human audit contract without a custom event.

After runtime, the same primitive should produce a native Case audit timeline: linked Agent Interpretation Event, Policy Decision Event, evidence state, block reason, human action/comment, timestamps, package version, and policy versions — so this does not have to be assembled by hand.

This is not telecom-specific, and it is not a single-bug request. It comes from separate reproduced investigations across service enablement, Action field requirements, generated page binding, package version binding, validation/package/upload agreement, connector readiness, and audit-readiness proof. It also matches UiPath's own positioning for Maestro Case: long-running, exception-heavy work with people, agents, automations, visibility, and auditability needs a readiness and auditability contract up front, not only runtime recovery after something fails. Any serious Maestro Case workflow with agents, automations, humans, and policy decisions can hit the same wall we did.

## 12. What surprised you the most? What would you tell another developer?

The positive surprise was that the UiPath primitives were closer to our target architecture than expected. Maestro Case gave the long-running case shell, Action Center gave real human task lifecycle, and Orchestrator/Data Fabric gave package, process, job, and audit artifact operations.

The more interesting surprise was that the platform often preserved the right structure even when the generated UI did not show it cleanly. When the Action Center page showed `Unnamed String 1`, the task schema/readback still had the correct `PolicyDecisionJson`. That was the lesson: trust the platform's structured data more than the generated UI. Build proof on API readback and custom audit storage, not only on what the generated page shows.

Advice to another developer: validate hard gates early with API readback and committed proof artifacts, not only the designer or generated UI. Confirm tenant services, Action Center rendering, task return shape, package version readback, audit reconstruction, and any live LLM proof path before polishing the app. The best habit we found was a repeatable local submission check, confirmed against live API readback at the important boundaries.

## 13. What did you build with Maestro that would have been a mess to stitch together without it?

We used Maestro Case as the orchestration boundary for governed service-recovery exceptions. Without it, we would have had to stitch together case state, stage routing, agent interpretation, deterministic policy decisions, human task assignment, reviewer comments, process/package versioning, runtime timestamps, and audit artifacts across separate tools ourselves.

That matched Maestro's own positioning: coordination between agents, automations, and people in long-running exception-heavy work. In our validated proof beats, the raw agent event recommended `closure_candidate`, while policy overrode to `verify_telemetry` for missing telemetry or escalated to `human_review` for fresh contradiction. Action Center handled the human lifecycle, Orchestrator exposed package/process/job and audit operations, and explicit audit bundles reconstructed the domain event chain.

The strongest evidence was the end-to-end shape: the same workflow that would normally require custom glue across separate tools ran as one governed Case pattern with human review, policy audit, and artifact storage using UiPath primitives.

The product improvement request follows directly from that success: make the domain audit timeline native. A serious agent + policy + human Case should show linked agent interpretation, policy decision, evidence state, block reason, human action, timestamps, and policy/package versions in one Case view or query.

## 14. Can we share your story?

[Choose one before submission]

* Yes, you can use my name, title, and company in UiPath marketing materials.
* Yes, but please show me the final version before publishing.
* Use my story without my name.
* No. Please keep this private for the UiPath team's internal reference only.
