# Feedback Survey Prep

This file preserves the exact evidence fields requested for product-feedback preparation. It is not final survey prose.

## Exact Evidence Fields

- product surface
- workflow
- worked
- failed/confused
- expected vs observed
- workaround
- severity/impact
- suggested improvement
- evidence path/link
- classification
- confidence
- follow-up validation needed

## Exact Survey Questions Captured From Prompt

These are the fields to answer near submission time. Do not fill final prose until each claim maps back to `PRODUCT_FEEDBACK_AWARD.md`.

1. What's your first name?
2. What's your last (family) name?
3. What's the name of your team? If you participated solo, write the name you chose or your name again.
4. Add here your email address.
5. Please rate your overall satisfaction with UiPath AgentHack.
6. Which of the following categories did you compete in AgentHack?
   - UiPath Maestro Case
   - UiPath Maestro BPMN
   - UiPath Test Cloud
7. Please briefly describe your use case.
8. Please indicate your overall satisfaction with the UiPath Platform:
   - Very satisfied
   - Somewhat satisfied
   - Neither satisfied nor dissatisfied
   - Somewhat dissatisfied
   - Very dissatisfied
9. How easy was it to build your solution?
   - Very easy
   - Somewhat easy
   - Neither easy, nor difficult
   - Somewhat difficult
   - Very difficult
10. What challenges (if any) did you encounter while building the solution?
11. If you had to change one thing about the UiPath Platform experience, what would it be and why?
12. What surprised you the most about building with UiPath during AgentHack? What would you tell another developer who's about to try automating and/or orchestrating with UiPath for the first time?
13. UiPath Maestro orchestrates AI agents, RPA, APIs, and people across one end-to-end process. What did you build with Maestro that would have been a mess to stitch together without it?
14. Can we share your story?
   - Yes, you can use my name, title, and company in UiPath marketing materials
   - Yes, but please show me the final version before publishing
   - Use my story without my name (anonymous attribution)
   - No. Please keep this private for the UiPath team's internal reference only

## Use Rule

Do not invent final answers here. Draft survey responses only after the matching `PF-XXX` entries in `PRODUCT_FEEDBACK_AWARD.md` have evidence paths, confidence, and follow-up validation status.

## Current Evidence-Backed Draft - 2026-06-25

This is not final submission prose. It is the current best draft assembled from observed PF entries so the final form can be completed without one-shot memory reconstruction.

### 1. What's your first name?

Placeholder: `Arshdeep`

### 2. What's your last (family) name?

Placeholder: `Singh`

### 3. What's the name of your team?

Placeholder: team name still needs user confirmation before submission.

### 4. Add here your email address.

Placeholder: `arshgill6120@gmail.com`

### 5. Please rate your overall satisfaction with UiPath AgentHack.

Draft choice: likely `Somewhat satisfied` or `Very satisfied`, depending on final build outcome.

Rationale to preserve: the platform enabled a real Maestro Case + Action Center + Orchestrator proof, but the build hit multiple setup, generated app, package, and diagnostics issues that materially slowed validation.

Evidence:
- PF-003, PF-006, PF-007, PF-013, PF-015, PF-017.

### 6. Which categories did you compete in AgentHack?

Draft selections:
- UiPath Maestro Case
- UiPath Test Cloud, only if a Test Cloud mapping or run is actually validated before final submission.

Do not select Maestro BPMN unless we actually build/validate that track.

### 7. Please briefly describe your use case.

Draft:

We built a telecom/broadband service activation and restoration exception workflow in Maestro Case. The case starts with business systems that appear green, while an agent interprets ambiguous support evidence into structured signals. A deterministic policy layer then decides whether closure is allowed. If authoritative network telemetry is missing or stale, policy overrides a raw `closure_candidate` recommendation and routes to telemetry verification instead of closure. If fresh authoritative telemetry contradicts the green business state, severity escalates and the case routes to human exception review with an evidence packet. The point is to prevent unsafe service-closure decisions while preserving an auditable boundary between agent recommendation, policy decision, and human action.

Evidence:
- `docs/demo/DEMO_STORYBOARD.md`
- `docs/validation/VALIDATION_RESULTS.md`
- PF-015.

### 8. Please indicate your overall satisfaction with the UiPath Platform.

Draft choice: `Somewhat satisfied`.

Rationale:
- Strong primitives: Maestro Case, Action Center, Studio Web, Orchestrator processes/jobs, task APIs, and package/version readback gave enough platform surface to validate the core architecture.
- Friction: first-time tenant readiness, generated Action app field reliability, required-field validation, package/feed diagnostics, and native audit reconstruction are still rough for a time-boxed builder.

Evidence:
- PF-003, PF-006, PF-007, PF-013, PF-015, PF-017.

### 9. How easy was it to build your solution?

Draft choice: `Somewhat difficult`.

Rationale:
- Conceptually, the products map well to the architecture.
- Practically, reaching a live evidence-packet task required working through Actions enablement, generated page issues, missing required Action task title at runtime, publish/versioning friction, package repair, solution-feed package lookup, and process version update workarounds.

Evidence:
- PF-003 through PF-017.

### 10. What challenges did you encounter while building the solution?

Draft:

The hardest part was not the core idea; it was turning a first-time Maestro Case build into a repeatable, observable runtime proof. We hit several distinct categories of friction:

- Tenant/service readiness: Action Center was required for the human review path, but Actions was not enabled for the tenant at first and the disabled-service page did not give the exact admin enablement path we eventually used.
- Human review authoring: Studio Web exposed the right primitives, but the Human action picker and generated Action app flow did not clearly guide input/output mapping, evidence-packet layout, or structured return.
- Generated app reliability: our Action schema included `EvidencePacketJson`, `RawAgentRecommendation`, and `PolicyDecisionJson`. The task APIs persisted the fields correctly, but the generated reviewer page rendered the proof-critical policy field as `Unnamed String 1`, so the platform preserved the data while the runtime UI made the governance boundary hard to demo.
- Runtime validation: deployment succeeded even when a required Action task Title was missing, and the first clear failure appeared only after starting a live case as an AppTasks runtime incident.
- Package and CLI recovery: a package uploaded successfully to the solution feed and could be read with `--feed-id`, but the default package lookup and direct process-create path could not bind the same version. Updating an existing process version worked, but this took extra readback and version-history checks to trust.
- Audit reconstruction: case/task APIs can reconstruct package version, stage/task order, timestamps, raw agent recommendation, policy decision, reviewer action, and structured return when we explicitly carry the payloads. A clean native domain audit view still appears to require custom audit events or a separate audit/event store.

Evidence:
- PF-003, PF-004, PF-006, PF-007, PF-013, PF-015, PF-017.

### 11. If you had to change one thing about the UiPath Platform experience, what would it be and why?

Draft:

I would add a Maestro Case readiness and human-review preflight path. Before a builder publishes or runs a Case with a human review step, UiPath should check tenant services and roles, confirm Actions/Action Center availability, validate required Action task fields such as Title, verify schema-to-page bindings for every Action input/output property, and show exactly how each case variable maps into the reviewer page and back into the case. This would have prevented most of our slowest iteration loops: enabling Actions, discovering Action task configuration, fixing runtime-only required-field failures, and diagnosing why `PolicyDecisionJson` existed in task data but rendered as `Unnamed String 1`.

The reason this matters is that Maestro Case is most valuable when it coordinates agents, systems, and humans across a governed process. That kind of workflow needs stronger design-time verification than a normal demo form because the reviewer must trust what they are seeing before approving or rejecting a policy-sensitive action.

Evidence:
- PF-003, PF-006, PF-007, PF-013.

### 12. What surprised you most? What would you tell another developer?

Draft:

The positive surprise was that the platform primitives are closer to the architecture than expected. Maestro Case gave us a real case runtime, Orchestrator gave package/process/job controls, Action Center gave a real human task lifecycle, and task APIs preserved structured payloads well enough to prove the separation between raw agent recommendation and final policy decision.

The practical warning for another developer is: validate the hard gates before building the polished app. Confirm tenant services, publish/deploy/version behavior, Action Center rendering, task return shape, and package readback early. Do not assume a generated human review page is demo-ready just because the schema fields exist. Also, read back the runtime state from APIs; the UI and the persisted task data can tell different stories during development.

Evidence:
- PF-013, PF-015, PF-016, PF-017.

### 13. What did you build with Maestro that would have been a mess to stitch together without it?

Draft:

We used Maestro Case as the orchestration boundary for a governed service-recovery exception. The messy part without Maestro would have been stitching together case state, agent interpretation, policy enforcement, human review, task assignment, reviewer comments, routing, runtime timestamps, and process/package version evidence across separate tools. In our proof runs, the raw agent event recommended `closure_candidate`, while the policy event overrode it to `verify_telemetry` for missing authoritative telemetry or escalated it to `human_review` for contradiction. Action Center handled the human task lifecycle, Orchestrator exposed the package/process/job layer, and Case APIs gave enough runtime state to reconstruct the flow when combined with explicit domain payloads.

That said, our feedback is that Maestro should make the domain audit trail more native. Regulated workflows need one place to see linked agent interpretation, policy decision, evidence state, block reason, human action, timestamps, and policy/package versions.

Evidence:
- Live E-002 task `4300080`, case `3af41e1d-8b04-4eba-aa5e-a95c5c673730`.
- Live E-004 task `4300219`, case `60e52ca5-6891-45b4-9e98-e1b08a984f06`.
- PF-015, PF-017.

### 14. Can we share your story?

Placeholder: requires user choice before final submission.

Options:
- Yes, you can use my name, title, and company in UiPath marketing materials.
- Yes, but please show me the final version before publishing.
- Use my story without my name.
- No. Please keep this private for the UiPath team's internal reference only.

## Current Highest-Value Feedback Claims

Use these as the backbone for the final answer. Do not submit unsupported claims that are not tied to PF evidence.

| Rank | Claim | Why it is strong | Evidence |
| --- | --- | --- | --- |
| 1 | Add a Maestro Case readiness + human-review preflight. | High-impact, concrete, spans setup, authoring, validation, and runtime. | PF-003, PF-006, PF-007, PF-013. |
| 2 | Generated Action app pages need field-binding inspection and repair. | Proof-critical field persisted in APIs but rendered as `Unnamed String 1`. | PF-006, PF-013. |
| 3 | Native domain audit/event inspector would make Maestro stronger for governed agentic workflows. | Directly tied to the central architecture and hard gate G-001. | PF-015. |
| 4 | Feed-aware CLI/process diagnostics should be consistent across upload/get/create/update. | Reproducible CLI/package workflow with clear workaround. | PF-017. |
| 5 | Runtime task state should sync or warn when completed outside the browser session. | Smaller but precise UI/runtime consistency issue. | PF-016. |

## Final Submission Ingredients

Use this section as the concise answer source when filling the form. Keep the final tone fair: the strongest submission is not "everything was broken"; it is "the platform primitives worked, and here are the exact preflight/diagnostic improvements that would make adoption much faster."

### Best Positive Findings To Include

| Finding | Why it matters | Evidence |
| --- | --- | --- |
| Maestro Case matches the orchestration shape. | It gave a real place to coordinate case state, stages, human tasks, package/process state, and incidents for a governed service-recovery workflow. | PF-015; `docs/validation/VALIDATION_RESULTS.md`. |
| Action Center mechanics worked after enablement. | Assignment, completion, reviewer comment, and structured return could be validated; the issue is legibility/binding, not total task failure. | PF-013, PF-016. |
| Orchestrator CLI lifecycle was strong once the right path was found. | Package/process readback and bucket create/upload/list/download gave real build-lifecycle evidence and a durable audit-artifact fallback. | PF-017; `docs/validation/artifacts/2026-06-25/orchestrator_bucket_audit_artifact_E004_manifest.json`. |
| Task APIs preserved the governance boundary. | Raw agent recommendation and final policy decision were both available in persisted payloads, which supports the architecture thesis. | PF-013, PF-015. |

### Best Critical Feedback To Include

| Claim | Expected | Observed | Workaround | Product improvement |
| --- | --- | --- | --- | --- |
| Maestro Case human-review readiness needs a preflight. | A Case with human review should verify tenant services, required fields, schema bindings, and return mapping before runtime. | Actions was initially disabled; required Action task Title failed only at runtime; generated page binding hid proof-critical fields. | Manually enabled Actions, repaired package/version path, used task APIs and custom evidence surface for legibility. | Add a readiness/preflight wizard for Maestro Case human-review dependencies. |
| Generated Action app field binding needs inspection and repair. | Every schema field should render with a readable label/value or produce a precise repair action. | `PolicyDecisionJson` persisted in APIs but rendered as `Unnamed String 1`; E-004 completed task repeated blank/unreadable proof fields. | Keep Action Center for lifecycle; use custom evidence/audit surface for final demo. | Add schema-to-control binding inspector, failed-property report, and evidence-packet template. |
| Native case audit needs domain-event reconstruction. | One view/query should reconstruct evidence state, policy versions, raw recommendation, policy decision, block reason, human action, and timestamps. | Native runtime history plus task APIs reconstruct operational flow, but domain audit requires explicit custom payloads/artifacts. | Use `service-recovery-audit-v1` bundle and Orchestrator bucket artifact fallback. | Add native Case audit/event inspector for linked agent/policy/human/domain events. |
| CLI/package diagnostics need feed awareness. | Upload/get/create/update process commands should resolve the same package feed or explain mismatch. | Feed-scoped package lookup worked, while default lookup/process create could not bind the same version. | Verified with `--feed-id`; used process version update and readback. | Add feed selector/diagnostics to process creation and package binding paths. |
| Data Fabric record insert needs schema-aware diagnostics. | A record body keyed by schema field names should insert or explain exact expected shape. | Entity create/readback succeeded, but multiple insert/import shapes failed with required `case_id` reported missing. | Use Orchestrator bucket artifact while Data Fabric insert remains blocked. | Echo recognized/unrecognized fields and provide insert examples for custom required fields. |

### Do Not Claim Yet

- Do not claim a Test Cloud implementation unless a Test Manager/Test Cloud project/run is actually validated.
- Do not claim Data Fabric audit storage is complete; only entity schema create/readback is validated, while record insert is blocked.
- Do not claim native Maestro Case history alone passes G-001; current result is native PARTIAL plus custom audit artifact PASS.
- Do not claim the generated Action Center page is demo-ready; task mechanics are validated, but field legibility is not.
- Do not describe the project as a generic agent governance platform. Keep it as telecom/broadband service recovery with an architecture that generalizes.
