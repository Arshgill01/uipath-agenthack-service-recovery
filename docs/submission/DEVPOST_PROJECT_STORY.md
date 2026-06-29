# ClearPath Recovery - Devpost Project Story

Status: paste-ready Devpost story source.

Use this as the polished long-form project story. It keeps the standard Devpost headings while adding concise sections for UiPath platform depth, validation, product feedback, and coding-agent proof. Claim boundaries are part of the story because the project is strongest when it is precise about what is real.

## Inspiration

Telecom service recovery often fails at the moment the workflow looks clean on paper.

A broadband activation case can show complete in CRM. The order system can say activation finished. Billing can show the account as active. A support note can say the customer is ready for closure.

But the customer may still have no working service because the evidence that matters at closure time is different: fresh network telemetry, correct device inventory, authoritative activation state, and contradiction-free service evidence.

ClearPath Recovery was built around that gap. We did not want a demo where an agent reads a few notes and confidently closes a case. That is the failure mode. The harder question is: how should an enterprise workflow use agents when the agent is useful, but not trustworthy enough to own the final decision?

Our answer is deliberately governed:

> Agents interpret ambiguous evidence into structured signals. Deterministic policy decides allowed actions. UiPath Maestro Case routes the work. Humans own high-impact exceptions. Explanations are generated once and logged.

ClearPath is a focused Maestro Case submission for broadband activation and restoration exceptions. It proves that agentic recovery can be fast, explainable, and safe without turning the LLM into the decision authority.

## What it does

ClearPath Recovery runs a telecom service-recovery case through a governed exception workflow when source systems disagree.

The demo proves two closely related paths using the same green business fixture. Only the authoritative evidence changes.

**Path 1: Missing or stale authoritative evidence**

- **Business state:** CRM, order, billing, and support note look resolved.
- **Authoritative evidence:** Network telemetry is missing or stale.
- **Raw agent recommendation:** `closure_candidate`
- **Policy outcome:** Closure is blocked because required authoritative evidence is not fresh.
- **Case route:** `verify_telemetry`

**Path 2: Fresh contradiction**

- **Business state:** Same green business fixture.
- **Authoritative evidence:** Fresh telemetry or inventory contradicts the business state.
- **Raw agent recommendation:** `closure_candidate`
- **Policy outcome:** Human review is required because authoritative evidence disagrees.
- **Case route:** `human_review`

The core behavior is the separation between recommendation and authority. ClearPath stores the raw Agent Interpretation Event separately from the final Policy Decision Event. A reviewer can see exactly what the agent wanted to do, why policy overrode or escalated it, which evidence source caused the block, and what must be true before closure is safe.

ClearPath includes:

- schema-validated interpretation of technician, customer, and support notes,
- deterministic policy checks for source authority, freshness, contradiction, confidence, and policy version,
- Maestro Case routing for dynamic exception-heavy work,
- Action Center human review lifecycle and structured reviewer return,
- judge-readable evidence packets generated from the same policy/evidence contract,
- Data Fabric V2 and Orchestrator bucket audit proof for full-payload reconstruction,
- Test Manager representation of eval scenarios E-001 through E-009,
- optional live Gemini/Vertex interpretation, including an adversarial advocate/skeptic run,
- a governed learning-loop artifact where policy changes remain proposal-only until human approval and eval pass.

## How we built it

We built ClearPath as a small deterministic recovery core wrapped by UiPath orchestration and proof surfaces.

The runtime flow is:

1. CRM, order, billing, support notes, telemetry, and inventory evidence are collected.
2. The agent interprets messy text into a closed-schema Agent Interpretation Event.
3. Deterministic policy checks authority, freshness, contradiction, confidence, and policy version.
4. Maestro Case routes the work to telemetry verification, human review, or policy-safe closure.
5. Action Center captures human review when the exception is high impact.
6. Audit data and evidence packets preserve the agent recommendation, policy decision, evidence state, and reviewer action.

The local core handles evidence modeling, structured agent-output validation, deterministic policy reconciliation, Action Center payload generation, audit-bundle generation, evidence-packet rendering, and eval scenarios.

UiPath Maestro Case is the orchestration boundary because this is dynamic casework, not a predictable straight-line process. The correct route depends on evidence freshness, contradiction state, reviewer action, retry outcome, and audit requirements.

The platform surfaces used are:

- Maestro Case for case lifecycle, routing, stages, and runtime case validation.
- Action Center for reviewer task lifecycle, assignment, completion, reviewer action, and structured return.
- Orchestrator for package/process/job readback, version pinning, and bucket-backed audit artifacts.
- Data Fabric V2 for queryable full-payload audit readback.
- Test Manager for manual eval-suite representation of E-001 through E-009.
- UiPath CLI for repeatable readback, diagnostics, and validation.

The proof strategy has three layers:

| Layer | Role |
| --- | --- |
| Native UiPath proof | Shows live or CLI-readback evidence from Maestro Case, Action Center, Orchestrator, Data Fabric, Test Manager, and UiPath CLI. |
| Judge-readable proof | Gives reviewers evidence-packet HTML, screenshots, proof indexes, and JSON audit bundles generated from the same contract. |
| Local deterministic proof | Keeps behavior repeatable through unit tests, evals, fixture validation, submission proof checks, and non-mutating wrappers. |

That three-layer shape was necessary because one surface was not enough to tell the story honestly. Native UiPath proof shows platform connection. Evidence packets make the agent-policy-human boundary readable. Local deterministic proof keeps the behavior regression-checked without mutating a live tenant.

## UiPath platform integration

ClearPath is anchored in UiPath rather than using UiPath as a label on top of a local script.

Maestro Case owns the case orchestration boundary. Action Center proves human task lifecycle and structured reviewer return. Orchestrator proves package/process versioning and provides bucket-backed audit artifact storage. Data Fabric V2 proves queryable full-payload audit readback. Test Manager represents the E-001 through E-009 eval suite with 9/9 manual execution evidence. UiPath CLI makes the proof repeatable through readback commands instead of relying only on screenshots.

We are careful about what we do not claim:

- Native Maestro Case history alone is not presented as the complete domain audit.
- Generated Action Center UI was validated for lifecycle, but not used as the final judge-readable evidence surface.
- Test Manager proof is manual representation/execution, not automated Test Cloud execution.
- The telecom systems are simulated, not production OSS/BSS integrations.
- Gemini, Codex, and any other LLM do not close cases or override policy.

## Agentic behavior and governance

The agentic part of ClearPath is interpretation, not final authority.

The agent reads messy service context and emits a closed-schema Agent Interpretation Event. That event can include a recommendation such as `closure_candidate`, extracted evidence gaps, customer-impact notes, urgency, suggested reviewer questions, and a one-time explanation.

Policy then evaluates the structured event against authoritative evidence. It checks whether required signals are present, fresh, authoritative, and non-contradictory. It records the active policy version and produces a separate Policy Decision Event linked back to the raw agent event.

This is the central safety pattern:

- The agent can be helpful and still wrong.
- Policy can preserve the agent's recommendation without obeying it.
- Maestro Case can route the exception based on the policy decision.
- Humans can review high-impact contradictions with a packet that shows the evidence, recommendation, override, and closure checklist.

The optional live Gemini/Vertex path deepens this pattern. In the adversarial run, an advocate interpretation pressed toward closure while a skeptic interpretation found unresolved risk. The disagreement became structured policy input, and policy routed to human review. The LLM did not close the case, override policy, or mutate rules.

## Validation and evidence

ClearPath was built with validation as part of the product, not as final polish.

Current validation includes:

- unit tests passing in the maintained baseline,
- E-001 through E-009 passing 9/9,
- non-mutating `scripts/run_submission_check.sh` proof verification,
- live UiPath Labs validation in org `keepingitlowkey`, tenant `DefaultTenant`,
- Action Center lifecycle and structured reviewer return proof,
- Data Fabric V2 full-payload audit readback for E-004,
- Orchestrator bucket audit artifact proof,
- Test Manager project `SREV`, test set `SREV:9`, and terminal manual execution with 9/9 passed logs,
- optional live Gemini/Vertex proof artifacts for the E-003 adversarial interpretation path.

Eval coverage includes aligned closure, missing telemetry, stale telemetry, contradicting telemetry, technician-note route change, adversarial pressure, invalid agent output, override persistence, and governed policy-improvement proposal.

The GitHub repository carries the full evidence set: proof packets, screenshots, audit bundles, CLI readbacks, validation logs, product-feedback notes, and coding-agent proof.

## Challenges we ran into

The hardest challenge was not writing a local policy engine. The hard part was making every important claim observable, repeatable, and honest across UiPath surfaces.

We ran into concrete platform and proof challenges:

- Native Case history was useful operationally, but not sufficient by itself for full domain audit reconstruction.
- Generated Action Center UI preserved lifecycle, but hid or mislabeled proof-critical fields during runtime validation.
- Data Fabric legacy snake_case custom fields did not reliably populate/read back, so the validated audit path moved to a PascalCase V2 schema.
- Test Manager could represent the eval suite through manual test cases and terminal manual execution, but automated Test Cloud execution was not proven and is not claimed.
- Package/feed/process versioning needed careful CLI readback to avoid assuming the runtime was using the intended artifact.
- The optional external evidence-source path had to remain honest: it is a systems-of-record simulator, not a real telecom integration.

Those constraints improved the submission. They forced the proof architecture to separate UiPath runtime evidence, judge-readable packets, and deterministic local validation instead of relying on a single polished screen.

## Accomplishments that we're proud of

We are proud that ClearPath demonstrates a real enterprise pattern in hackathon form: an agent can be useful without being trusted blindly.

The strongest accomplishments are:

- clear separation of raw agent recommendation and final policy decision,
- two same-fixture proof beats where only authoritative evidence changes,
- a Maestro Case-centered architecture with Action Center human lifecycle proof,
- durable audit reconstruction through Data Fabric V2 and Orchestrator bucket artifacts,
- repeatable local validation through tests, evals, demo wrappers, and submission proof checks,
- optional live Gemini/Vertex interpretation that stays inside the same schema and policy boundary,
- a governed learning-loop artifact where policy improvement remains pending human approval,
- specific UiPath product feedback backed by reproduced evidence,
- auditable Codex coding-agent proof that satisfies the bonus requirement without weakening runtime governance.

The part we care about most is that the demo does not reward reckless automation. It shows a closure recommendation being blocked, and it makes the block explainable.

## What we learned

We learned that the hardest enterprise AI workflows are not always the ones where the model is uncertain. The harder case is when the model sounds certain because part of the enterprise record looks clean.

For service recovery, we learned:

- "CRM says active" is not the same as "the customer has working service."
- Source hierarchy matters.
- Freshness rules matter.
- Contradictions are different from missing evidence.
- High-impact exceptions need human escalation.

We also learned that agent usefulness and agent authority should be designed separately. A good agent can extract notes, identify evidence gaps, ask reviewer questions, summarize customer impact, and propose the next stage. That does not mean it should close the case.

On the UiPath side, Maestro Case is a strong fit for dynamic exception-heavy work. The product primitives are there; the builder experience would improve if readiness checks made runtime binding, reviewer visibility, package version, and audit coverage explicit before the first live run.

On the coding-agent side, Codex was most valuable for disciplined build loops: implementation, validation, evidence capture, claim-boundary checks, and documentation. The useful pattern was not "let the agent invent the product." It was using the coding agent to keep the repo coherent, testable, and evidence-backed while humans owned product direction and safety decisions.

## Product feedback and what we learned about UiPath

We treated product feedback as a first-class workstream because the project pushed on the real edge of agent + policy + human casework.

The strongest recommendation is a Maestro Case Human-Review Readiness Check: a preflight and auditability contract for cases with human review.

That readiness check should validate:

- tenant services and roles,
- Action task required fields,
- schema-to-generated-page bindings,
- case-to-action input mappings,
- action-to-case output mappings,
- reviewer visibility,
- Case-bound Action app deployment/version,
- package/feed binding,
- process version pinning,
- optional Integration Service connector readiness,
- audit coverage before a live run starts.

After runtime, the same contract should support a native Case audit timeline linking the Agent Interpretation Event, Policy Decision Event, evidence state, block reason, human action/comment, timestamps, package version, and policy version.

The positive lesson is that UiPath has the right primitives for serious governed casework. Maestro Case, Action Center, Orchestrator, Data Fabric, Test Manager, and the CLI gave us enough to build a credible proof chain. The hard lesson is that first-time builders need stronger readiness diagnostics when those primitives meet at runtime.

## Coding-agent proof for the bonus

We used Codex as the coding agent throughout the build, and the proof is auditable from the repository rather than asserted in one sentence.

Codex helped build and harden the local service-recovery core, deterministic policy tests, eval harness, evidence-packet renderer, audit-bundle generation, UiPath CLI validation loops, Data Fabric and Orchestrator readback diagnostics, Test Manager mapping, product-feedback evidence collection, and final submission documentation.

The repository contains a dedicated proof package:

- README coding-agent disclosure,
- coding-agent proof log,
- compact evidence manifest,
- build logs,
- Codex-prefixed branches and workstreams,
- non-mutating submission check.

The boundary is important: Codex was build-time assistance only. Codex is not part of runtime case closure, does not mutate production policy, and does not replace UiPath Maestro Case orchestration, deterministic policy, Action Center accountability, or human review.

In one sentence:

> Codex helped build, test, validate, and document ClearPath; UiPath remains the runtime orchestration and governance layer, and deterministic policy owns closure decisions.

## What's next for ClearPath

The next step is to turn ClearPath from a hackathon proof into a stronger reusable pattern for governed service operations.

Near-term improvements:

- Add more telecom exception scenarios: partial activation, wrong device assignment, intermittent telemetry, missed dispatch, and repeat-contact escalation.
- Expand the evidence-source simulator and optionally wire a real approved Integration Service connection for a non-production system.
- Improve reviewer evidence packets with role-specific views for NOC, field operations, customer care, and compliance.
- Add richer metrics for wrongful closure prevention, repeat-contact reduction, SLA breach risk, and audit completeness.
- Extend the eval suite with more adversarial and low-confidence cases.
- Build a fuller policy-improvement review flow where proposed rule changes are compared against historical evals before human approval.

The broader goal is ClearPath as a pattern: governed agentic recovery for operations teams where evidence can be missing, stale, contradictory, or adversarial, and where the cost of a confident wrong closure is higher than the cost of a careful escalation.

## Short Devpost summary option

ClearPath Recovery is a UiPath Maestro Case workflow for telecom service activation and restoration exceptions. It prevents unsafe closure when CRM/order/billing/support data looks resolved but authoritative network telemetry is missing, stale, or contradictory. Agents interpret messy notes into structured signals; deterministic policy decides allowed routing; Maestro Case orchestrates the case; Action Center handles human review; Data Fabric and Orchestrator preserve audit proof; Test Manager represents the eval suite. The demo proves two high-risk paths: missing/stale evidence routes to verification, while fresh contradiction escalates to human review. Codex was used as the coding agent to build, validate, and document the repo, with proof in the README, coding-agent proof log, evidence manifest, build log, and validation wrappers.

## GitHub audit trail

The Devpost story intentionally avoids listing every internal artifact path. The GitHub README is the front door for:

- setup and validation commands,
- UiPath component proof,
- evidence packets and screenshots,
- audit bundles,
- product-feedback evidence,
- Codex coding-agent proof.

## Claims to avoid in Devpost

- Do not claim real production telecom integrations.
- Do not claim automated Test Cloud execution.
- Do not claim generated Action Center UI was the final judge-readable proof surface.
- Do not claim native Maestro Case history alone reconstructs the full domain audit.
- Do not claim Gemini, Codex, or any LLM closes cases or overrides policy.
- Do not pitch ClearPath as a generic AI governance platform.
