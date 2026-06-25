# Best Product Feedback Appendix

Status: curated evidence appendix for the UiPath AgentHack feedback survey. This is not final form prose; it is the high-signal source for writing the final answers.

## Submission Thesis

UiPath Maestro Case had the right core primitives for a governed telecom service-recovery workflow: case state, stages, human tasks, Action Center lifecycle, Orchestrator process/package/job readback, Test Manager representation, and CLI automation. The strongest product feedback is that first-time builders need a guided readiness and verification path for Maestro Case human-review workflows so they can trust tenant services, generated Action app bindings, required task fields, package/feed bindings, and audit reconstruction before spending hours in live runtime recovery.

The feedback should not read as a complaint list. It should read as:

> We built a real governed Maestro Case workflow, validated the hard gates, found the product primitives strong, and identified exact preflight/diagnostic improvements that would make adoption much faster for agent + policy + human casework.

## Best Final Answer Shape

### Overall Satisfaction

Recommended answer: `Somewhat satisfied`.

Reason:

- Satisfied because the platform supported real Maestro Case, Action Center, Orchestrator bucket, package/process readback, Test Manager mapping, and CLI lifecycle evidence.
- Not `Very satisfied` because setup, generated Action app binding, runtime validation, package/feed diagnostics, and native audit reconstruction required repeated workarounds.

Evidence:

- Positive: PF-013, PF-015, PF-017, PF-020.
- Friction: PF-003, PF-006, PF-007, PF-017, PF-019, PF-022.

### Ease Of Build

Recommended answer: `Somewhat difficult`.

Reason:

- The architecture mapped well to UiPath products.
- The time cost came from discovering platform readiness issues and proving runtime behavior: Actions enablement, generated Action app field rendering, required Action task title, package/feed binding, Data Fabric insert shape, and Case job/task readback.

Evidence:

- PF-003, PF-006, PF-007, PF-013, PF-017, PF-019, PF-022.

## Ranked Feedback Claims

| Rank | Claim | Why It Can Win | Evidence | Keep / Cut |
| --- | --- | --- | --- | --- |
| 1 | Add a Maestro Case readiness + human-review preflight. | It is high-impact, product-specific, actionable, and backed by several live blockers across setup, design, deploy, and runtime. | PF-003, PF-006, PF-007, PF-013. | Keep as the primary answer to "one thing to change." |
| 2 | Add native Case domain audit/event reconstruction for agent + policy + human workflows. | It ties directly to Maestro's value proposition and our hard gate G-001. It is strategic, not just a bug report. | PF-015, G-001 validation, audit bundle artifacts. | Keep as the strongest product-design insight. |
| 3 | Improve generated Action app field binding inspection/repair. | The platform persisted proof-critical data but the generated UI hid it, which is precise and fair. | PF-006, PF-013. | Keep as the concrete G-003 example. |
| 4 | Make package/feed/process binding diagnostics consistent. | It shows deep usage beyond UI clicks and supports the coding-agent/CLI story. | PF-017, PF-010, PF-011, PF-012. | Keep as integration/CLI feedback. |
| 5 | Add schema-aware Data Fabric record insert diagnostics. | Strong for regulated audit storage, but keep secondary because Orchestrator bucket gave a workaround. | PF-018, PF-019. | Keep as a secondary storage/audit point. |
| 6 | Support eval-suite import into Test Manager and clarify manual execution terminal status. | Good cross-platform feedback and useful for agent evals, but less central than Maestro Case. | PF-020, PF-021. | Keep if selecting Test Cloud/Test Manager category. |
| 7 | Clarify Case job/task lifecycle readback. | Practical CLI/operator feedback; helps repeatability and demo honesty. | PF-022. | Keep as supporting detail, not headline. |

## What Worked Well

Use these as positive counterweights:

- Maestro Case matched the orchestration shape for long-running exception work.
- Action Center worked for real task lifecycle after Actions was enabled: assignment, completion, reviewer comments, and structured return were observable.
- Task APIs preserved raw agent recommendation and final policy decision separately, supporting the governance boundary even when the generated UI was weak.
- Orchestrator buckets worked cleanly for durable JSON audit artifact storage.
- Orchestrator process readback and version history made package pinning visible.
- Test Manager could represent E-001 through E-009 as live manual test cases and a test set.

Evidence:

- PF-013, PF-015, PF-017, PF-020, PF-021.
- `docs/validation/TEST_MANAGER_MAPPING.md`.
- `docs/validation/artifacts/2026-06-25/orchestrator_bucket_audit_artifact_E004_manifest.json`.

## Strongest Critical Feedback

### Primary Recommendation

Add a Maestro Case readiness and human-review preflight path.

It should check:

- tenant services and roles: Actions, Orchestrator, Test Manager, Integration Service, Data Service/Data Fabric,
- Action task required fields such as Title,
- schema-to-generated-page binding for each input/output property,
- case variable to Action input mapping,
- Action output to Case variable mapping,
- package/feed binding and package version to be used by the next run,
- process `AutoUpdate` and package version readback,
- native audit coverage versus required custom audit events.

Why:

- It would have prevented or shortened PF-003, PF-006, PF-007, PF-008, PF-013, and PF-017.
- It aligns with Maestro Case's target use: end-to-end orchestration across agents, APIs, RPA, and people.

### Secondary Recommendations

- Add a native Case audit/event inspector for linked domain events.
- Add an Action app field-binding inspector and repair flow.
- Add feed-aware process creation and package lookup diagnostics.
- Add schema-aware Data Fabric insert/import diagnostics.
- Add Test Manager eval import from JSON/JUnit/agent-eval outputs.
- Add CaseManagement-aware job state explanations for human-task workflows.

## Final Survey Building Blocks

### Use Case

We built a telecom/broadband service activation and restoration exception workflow in Maestro Case. Business systems can look green while authoritative network evidence is missing, stale, or contradictory. An agent interprets ambiguous notes into structured signals, but deterministic policy makes the closure/routing decision. The demo proves that a raw `closure_candidate` recommendation is preserved, policy can override it to `verify_telemetry` when authoritative telemetry is missing, and policy can escalate to `human_review` when fresh authoritative telemetry contradicts the business state.

### Challenges

The hardest part was not the local policy model. It was turning a first-time Maestro Case build into a repeatable, observable runtime proof. We had to validate tenant service readiness, generated Action app bindings, required Action task fields, package/feed resolution, process version pinning, Action Center task return, Test Manager mapping, and audit storage. The strongest pattern is that UiPath exposed the needed primitives, but the product needs more preflight and diagnostic guidance for a new builder doing agent + policy + human orchestration.

### One Thing To Change

Add a Maestro Case human-review readiness/preflight wizard. It should verify services, roles, task required fields, Action app schema binding, input/output mappings, package/feed binding, package version pinning, and audit-readiness before the builder starts a live case. This would turn hours of runtime recovery into a short checklist.

### What Surprised Us

The positive surprise was that the platform persisted the governance boundary better than the generated UI showed. The raw agent recommendation and policy decision were available through task/API/audit data even when the generated reviewer page mislabeled or hid a proof-critical field. The adoption advice is to validate hard gates early with API readback, not only with the designer or generated UI.

### What Maestro Simplified

Without Maestro, we would have had to stitch together case state, task lifecycle, reviewer comments, policy outputs, package/process versioning, job history, and audit artifacts across unrelated tools. Maestro Case and Action Center gave the core orchestration shell; our feedback is that Maestro should make the domain audit timeline native so agent interpretation, policy decision, evidence state, human action, and versions appear in one place.

## Claims To Avoid

- Do not claim automated Test Cloud execution; current Test Manager validation is manual mapping plus passed manual logs.
- Do not claim Data Fabric audit record persistence; entity creation/readback worked, but record insert remains blocked.
- Do not claim generated Action Center UI is final-demo ready.
- Do not claim native Case history alone passes the domain audit gate.
- Do not pitch the project as a generic governance platform.
- Do not imply terminal Case job completion while E-002/E-004 jobs still read back as `Running`.

## Evidence Index

| Evidence | Use |
| --- | --- |
| `docs/product/PRODUCT_FEEDBACK_AWARD.md` | Source PF log and evidence matrix. |
| `docs/product/FEEDBACK_SURVEY_DRAFT.md` | Survey question scaffold and draft answer material. |
| `docs/validation/VALIDATION_RESULTS.md` | Chronological validation results and command evidence. |
| `docs/validation/VALIDATION_GATES.md` | Hard gate PASS/PARTIAL implications. |
| `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md` | Repeatable proof path and live readback commands. |
| `docs/demo/artifacts/demo_proof_manifest.json` | Local 2A/2B proof artifact manifest. |
| `docs/validation/TEST_MANAGER_MAPPING.md` | Test Manager eval mapping and manual execution evidence. |
