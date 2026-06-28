# Feedback Survey Copy-Ready Bank

Status: copy-ready answer bank for the final UiPath product feedback form. Fill owner/team/share fields manually at submission time.

Use this file as the form-facing source. Do not paste internal PF IDs into the Microsoft Form unless UiPath explicitly asks for evidence references. The answers below should stand alone for a reviewer who never opens the repo.

Paste only the answer prose for each Microsoft Form field. Do not paste section labels such as "Recommended Choices", "Internal Traceability", or "Do Not Claim" into the form unless there is a matching field. Resolve team name, story-sharing preference, and whether to select the Test Cloud category at submission time.

Source files:

- `docs/product/PRODUCT_FEEDBACK_AWARD.md`
- `docs/product/FEEDBACK_AWARD_APPENDIX.md`
- `docs/product/FEEDBACK_SURVEY_DRAFT.md`
- `docs/product/FEEDBACK_SURVEY_FINAL_DRAFT.md`
- `docs/validation/VALIDATION_RESULTS.md`
- `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`
- `docs/research/RESEARCH_LOG.md`

Evidence handling:

- The Microsoft Form answers should lead with the experience, impact, expected behavior, observed behavior, and requested product improvement.
- Internal evidence labels such as `PF-003` are for our traceability only.
- Repo paths and artifact names can be mentioned sparingly when they clarify that the feedback came from a real reproduced build, but they should not be used as the main explanation.
- Public forum anecdotes and official docs are context only. The form should make clear which observations came from our own reproduced build.

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

If the form provides an optional proof/details field, mention this in plain language instead of internal IDs: the demo produced evidence packets for the missing-telemetry and contradiction paths, live Action Center tasks for both review flows, and a manifest tying those artifacts to the submitted project.

## Q10 - Challenges Encountered

The hardest part was turning a first-time Maestro Case build into a repeatable, observable runtime proof. The policy engine and evals were straightforward; the slower work was validating platform readiness and runtime behavior across Maestro Case, Action Center, Orchestrator, Data Fabric, Test Manager, and the UiPath CLI.

The main gap was not one isolated bug. It was that readiness checks were split across product surfaces at exactly the point where a builder needs confidence before starting a live case.

Observed workflow and impact, grouped by product gap:

**1. Readiness gaps before runtime**

- Actions/Action Center was required for human review but was not enabled for the tenant at first. The disabled-service page did not show the exact admin enablement path we later used.
- Human-review authoring exposed the right primitives, but the generated Action app flow did not make schema-to-page binding, required task fields, or structured return mapping obvious. A required Action task `Title` field passed deployment and failed only at live runtime.
- A scratch Case probe showed inconsistent readiness signals: Case validation caught missing rules and a required field, while solution dry-run packaging reported valid and upload accepted the same invalid scratch solution with no errors.

**2. Runtime binding, rendering, and version gaps**

- The generated reviewer page hid or mislabeled a proof-critical field. The policy decision persisted correctly in task/API data, but the Action Center page rendered it as `Unnamed String 1`, so the UI did not reliably show the governing policy decision next to the raw agent recommendation.
- Runtime diagnostics were too late and too generic for the failure family. Deployment succeeded despite the missing required task `Title`, then process diagnosis failed with an internal `summaries.find is not a function` error instead of repair guidance.
- Package/feed/process diagnostics required extra readbacks. A package could be read when the solution feed was specified, while default lookup and direct process creation could not bind the same version.

**3. Audit and eval reconstruction gaps**

- Native Case history and task APIs reconstructed operational flow, but the full domain audit for evidence state, raw recommendation, policy decision, policy versions, block reason, human action, and timestamps still required explicit custom audit artifacts.
- Data Fabric became useful after a PascalCase V2 schema, but the first snake_case entity accepted schema creation and then failed or hid custom-field write/readback in confusing ways.
- Test Manager represented our E-001 through E-009 eval suite as manual cases and a terminal manual execution with 9/9 passed logs, but it was not a one-step import from a local eval result. Automated Test Cloud execution remained unclaimed because a concrete Orchestrator package probe did not become Test Manager-discoverable/linkable automation.

Expected behavior: before publishing or running a human-review Case, the platform should tell the builder whether required services, task fields, app bindings, package/feed versions, reviewer visibility, and audit paths are ready.

Workaround used: we manually enabled Actions, ran Case validation separately from solution packaging, used CLI/API readbacks for task and package state, used custom evidence packets for readable policy proof, stored audit payloads through validated Data Fabric V2 and Orchestrator artifact paths, and kept Test Manager claims manual-only.

Reviewer-facing evidence summary: these observations came from repeated live build attempts and read-only probes, not from hypothetical review or forum anecdotes.

## Q11 - One Thing To Change

Add a Maestro Case Human-Review Readiness Check: a preflight and auditability contract for Cases that route work to a human reviewer.

This is not a request for generic validation. Maestro already has validation, simulation, debug, testing, Actions, retry, and migration primitives. The gap we hit is that the proof of "will this human-review Case actually work at runtime?" is split across too many surfaces. Before a builder publishes or starts a Case with a human review step, UiPath should produce one readiness report that verifies:

- tenant services and roles: Actions, Action Center, Orchestrator, Test Manager, Integration Service, Data Service/Data Fabric,
- required Action task fields such as `Title`,
- schema-to-generated-page binding for every input/output property,
- Case variable to Action input mapping and Action output to Case variable mapping,
- whether the reviewer will see proof-critical fields with stable labels, not generated placeholders such as `Unnamed String 1`,
- package/feed binding and the package version the next process run will use,
- process `AutoUpdate` and package-version readback,
- agreement between Case validation, solution dry-run packaging, and Studio Web upload/import,
- native Case audit coverage versus required custom audit events.

The report could live in Studio Web as `Run human-review readiness check` and in CLI as a command such as `uip maestro case preflight`. It should return pass/fail findings with fix links, not just a generic runtime incident: for example, "Actions is not enabled for this tenant," "Action task Title is missing," "PolicyDecisionJson has no rendered control in the generated reviewer page," "this Case package will instantiate Action app version 1.0.0, not the repaired 1.0.1 deployment," or "native Case history will not reconstruct the declared agent/policy/human audit contract without a custom event."

The same product primitive should also produce a native Case audit timeline after runtime: linked Agent Interpretation Event, Policy Decision Event, evidence state, block reason, human action/comment, timestamps, package version, and policy versions. That makes this one coherent request: prove the human-review Case is ready before runtime, then prove what happened after runtime.

This would have shortened our slowest loops: enabling Actions, diagnosing generated Action page binding, fixing runtime-only task field failures, proving package version pinning, reconciling Case validation versus solution dry-run/upload, and deciding where to store audit evidence. This is not telecom-specific. Any serious Maestro Case workflow with agents, automations, humans, policy decisions, and audit obligations can fail in the same way if designer validity does not prove runtime reviewer readiness.

Reviewer-facing evidence summary: this recommendation is based on the same readiness problems appearing in several places: tenant service enablement, Action task required fields, generated reviewer-page binding, package/feed version binding, Case validation versus solution packaging, and audit-readiness proof. Public docs show related validation/simulation/testing primitives, but our build needed one cross-surface readiness and auditability contract for human-review Cases.

## Q12 - What Surprised You / Advice To Another Developer

The positive surprise was that the UiPath primitives were closer to our architecture than expected. Maestro Case gave the long-running case shell, Action Center gave real human task lifecycle, Orchestrator gave process/package/job controls and bucket storage, and task APIs preserved structured payloads well enough to prove the boundary between raw agent recommendation and final policy decision.

The advice to another developer is to validate hard gates early with API readback and committed proof artifacts, not only with the designer or generated UI. Confirm tenant services, Action Center rendering, package version readback, task return shape, audit reconstruction, and any live LLM proof path before polishing the app. In our build, the backend task data preserved the policy payload correctly even when the generated reviewer UI hid it, so API readback and repeatable local checks were essential.

If the form asks how we validated this advice, say that we used repeatable local checks plus live platform readbacks: demo proof scripts, submission checks, task API readback, package/process inspection, and audit artifact verification.

## Q13 - What Maestro Simplified

We used Maestro Case as the orchestration boundary for governed service-recovery exceptions. Without Maestro, we would have had to stitch together case state, stage routing, agent interpretation, deterministic policy decisions, human task assignment, reviewer comments, process/package versioning, runtime timestamps, and audit artifacts across separate tools. The official Maestro positioning matched what we needed: coordination between agents, automations, and people in long-running exception-heavy work.

In the validated proof beats, the raw agent event recommended `closure_candidate`, while policy either overrode to `verify_telemetry` for missing authoritative telemetry or escalated to `human_review` for fresh contradiction. Action Center handled the human lifecycle, Orchestrator exposed package/process/job and audit artifact operations, and explicit audit bundles reconstructed the domain event chain. The product improvement request is to make that domain audit timeline native: linked agent interpretation, policy decision, evidence state, block reason, human action, timestamps, and policy/package versions in one Case view or query.

If the form provides room for proof details, mention only the concrete examples: two live Action Center human-review tasks were created for the missing-telemetry and contradiction paths, and the E-004 audit bundle was stored as an Orchestrator artifact to preserve the raw agent event, policy decision, evidence state, and human action.

## Internal Traceability - Do Not Paste Into The Form

These labels map the copy-ready answers back to the detailed evidence log in `docs/product/FEEDBACK_AWARD_APPENDIX.md`.

| Survey answer | Internal evidence labels |
| --- | --- |
| Q7 use case | PF-015 plus demo evidence packets and live E-002/E-004 tasks |
| Q10 challenges | PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-019, PF-020, PF-021, PF-022, PF-023, PF-024, PF-025, PF-026, PF-027, PF-028 |
| Q11 one change | PF-003, PF-006, PF-007, PF-013, PF-015, PF-017, PF-026, PF-027, PF-028; secondary support from PF-019 and PF-023 |
| Q12 surprise/advice | PF-013, PF-015, PF-017, PF-022 plus `scripts/run_demo.sh` and `scripts/run_submission_check.sh` |
| Q13 Maestro value | PF-015, PF-022 plus live E-002/E-004 task and audit-bundle artifacts |

## Do Not Claim

- Automated Test Cloud execution. We only validated manual Test Manager execution; package probe `ServiceRecoveryEvalProcessProbe:0.0.2/0.0.3` did not become Test Manager-discoverable/linkable automation.
- Legacy snake_case Data Fabric audit persistence. Use the validated PascalCase `ServiceRecoveryAuditBundleV2` path for queryable E-004 audit readback.
- Generated Action Center UI is final-demo ready.
- Native Case history alone passes the domain audit gate.
- Terminal Case job completion for E-002/E-004 while jobs still read `Running`.
- A generic agent governance platform; the product is telecom/broadband service recovery.
