# ClearPath Recovery Final Video Main Script

Status: recording-ready main script. Target runtime: 4:50 to 4:55. Hard stop: 4:58.

Use the main script word for word. The delivery should sound calm and confident, not dramatic. Keep your cursor movement deliberate: point at the exact field named in the script, pause for half a second, then move on.

## Recording Setup

Open these screens before recording, in this order:

1. Main deck: `docs/submission/presentation_deck/rendered/governed_service_recovery_uipath_agenthack.pdf`
2. UiPath Automation Cloud tab showing Maestro Case / Action Center / Orchestrator / Test Manager surfaces
3. `docs/demo/artifacts/proof_index.html`
4. `docs/demo/artifacts/evidence_packet_E002.html`
5. `docs/demo/artifacts/evidence_packet_E004.html`
6. `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html`
7. `docs/demo/artifacts/policy_improvement_E008.json`
8. `docs/product/FEEDBACK_AWARD_APPENDIX.md`
9. `README.md`
10. `docs/submission/CODING_AGENT_PROOF_LOG.md`
11. `docs/submission/coding_agent_evidence_manifest.json`
12. Terminal at repo root with the latest `scripts/run_submission_check.sh` output visible

If a UiPath login expires, do not burn recording time. Show the deck platform map, then the proof index and local artifacts. Say: "The live UiPath references are captured in the proof map and runbook; for the recording, I am using the non-mutating proof surfaces."

## Main Script

| Time | Screen | Action | Say exactly |
| --- | --- | --- | --- |
| 0:00-0:06 | Deck slide 1, `ClearPath Recovery` | Start on the title. Do not move the cursor yet. | "This is ClearPath Recovery: a UiPath Maestro Case workflow for telecom service recovery." |
| 0:06-0:14 | Deck slide 1 | Point at the subtitle. | "The rule is simple: no service case closes until authoritative evidence proves the customer is actually restored." |
| 0:14-0:24 | Deck slide 2, business problem | Advance. Point at `Wrongful closure`, then `Repeat contact`, then `Audit gap`. | "The risky moment is when CRM, orders, billing, and support notes all look green, but the customer still has no working service. That creates wrongful closure, repeat contact, and an audit gap." |
| 0:24-0:34 | Deck slide 3, architecture thesis | Advance. Move across the five steps from left to right. | "The architecture keeps the agent useful without giving it final authority: agents interpret, policy decides, Maestro routes, and humans own exceptions." |
| 0:34-0:43 | Deck slide 4, why Maestro Case | Advance. Point at the title and the three cards. | "This belongs in Maestro Case because the route is not a fixed happy path. It changes when evidence is missing, stale, contradictory, or high-impact enough for a reviewer." |
| 0:43-0:57 | Deck slide 5, UiPath platform map | Advance. Point down the rows: Maestro Case, Action Center, Data Fabric / Orchestrator, Test Manager, UiPath CLI. | "UiPath is the orchestration boundary. Maestro Case carries the case lifecycle, Action Center handles human review, Data Fabric and Orchestrator preserve audit and version proof, Test Manager represents the eval suite, and the UiPath CLI gives repeatable readback." |
| 0:57-1:06 | UiPath platform tab | Switch to the prepared UiPath tab. Slowly sweep across visible platform surfaces. | "This is not just a local script with a UiPath logo. The live validation used Maestro Case, Action Center, Orchestrator, Data Fabric, Test Manager, and CLI readback." |
| 1:06-1:13 | Proof index or deck slide 6 | Switch to `proof_index.html`, then open E-002 if needed. | "Now I will show the core proof: two cases with the same green business fixture, and only the authoritative service evidence changes." |
| 1:13-1:22 | `evidence_packet_E002.html` | Point at the case header and business/evidence summary. | "Scenario 2A is missing or stale authoritative evidence. CRM, order, billing, and the support note look resolved." |
| 1:22-1:34 | `evidence_packet_E002.html` | Point at `Agent Interpretation Event` and `recommended_next_stage`. | "The agent sees that green business state and emits the raw recommendation `closure_candidate`. I keep that recommendation visible; it is not overwritten." |
| 1:34-1:51 | `evidence_packet_E002.html` | Point at `Policy Decision Event`, `from_recommended_stage`, `to_stage`, and block reason. | "Then deterministic policy checks source authority and freshness. Because telemetry is missing or stale, policy overrides closure from `closure_candidate` to `verify_telemetry`, with the block reason `missing_authoritative_signal` or `stale_authoritative_signal`." |
| 1:51-2:00 | `evidence_packet_E002.html` | Point at SLA / verification route if visible. | "Operationally, that means: do not close, do not escalate as a contradiction yet, keep the SLA clock alive, and verify telemetry." |
| 2:00-2:08 | Deck slide 7 or `evidence_packet_E004.html` | Switch to E-004. Point at the title/header. | "Scenario 2B starts from the same green business fixture. That matters. I am not comparing unrelated examples." |
| 2:08-2:21 | `evidence_packet_E004.html` | Point at evidence rows showing fresh contradiction. | "The only meaningful change is authoritative evidence: fresh telemetry or inventory now contradicts the business-system state. The service is not actually proven live." |
| 2:21-2:34 | `evidence_packet_E004.html` | Point at the raw agent recommendation, then the policy decision. | "The agent can still recommend `closure_candidate`, but policy does not obey it. This decision becomes `require_human_review`, linked back to the raw agent event." |
| 2:34-2:47 | `evidence_packet_E004.html` | Point at `source_contradiction`, `human_review`, and reviewer packet / closure guard. | "The reason is `source_contradiction`, and the route is `human_review`. Missing evidence is a controlled verification problem. Fresh contradiction is a higher-risk exception." |
| 2:47-2:55 | Deck slide 8, one variable different route | Advance or switch. Point left then right. | "This is the central product behavior: same business-green fixture, different authoritative signal, different route." |
| 2:55-3:08 | `evidence_packet_E003_adversarial_live.html` or deck slide 9 | Switch to the adversarial packet. Point at advocate/skeptic sections. | "The optional live Gemini path uses the LLM as an interpreter, not a decision maker. In the adversarial run, one interpretation pushed toward closure while another found unresolved risk." |
| 3:08-3:20 | `evidence_packet_E003_adversarial_live.html` | Point at disagreement / policy route. | "That disagreement is turned into structured policy input. Policy can escalate on `high_interpretation_disagreement`, but the LLM never closes the case, overrides policy, or mutates rules." |
| 3:20-3:32 | Deck slide 10 or `policy_improvement_E008.json` | Switch to eval / learning loop. Point at E-001 through E-009 or JSON fields. | "The eval layer keeps both safety and usefulness honest. E-001 through E-009 cover aligned closure, missing and stale evidence, contradiction, note-driven routing, adversarial pressure, invalid output, override persistence, and usefulness degradation." |
| 3:32-3:44 | `policy_improvement_E008.json` | Point at `pending_human_approval`, `not_promoted`, policy versions if visible. | "When the agent gets less useful, the system produces a proposal-only policy improvement artifact. It stays `pending_human_approval` and `not_promoted`; active cases remain pinned until an explicit migration event." |
| 3:44-3:58 | Test Manager surface or deck slide 10 | If UiPath tab is available, show Test Manager `SREV`; otherwise stay on slide 10. | "The Test Manager proof is intentionally described as manual representation and execution: project `SREV`, test set `SREV:9`, and nine passed eval scenarios. I am not claiming automated Test Cloud execution." |
| 3:58-4:12 | Deck slide 11 or `docs/product/FEEDBACK_AWARD_APPENDIX.md` | Switch to product feedback. Point at Human-Review Readiness Check. | "The strongest product feedback is a Maestro Case Human-Review Readiness Check: one preflight that verifies services, roles, Action task fields, generated bindings, package and feed versioning, reviewer visibility, and audit readiness before runtime." |
| 4:12-4:22 | Product feedback doc | Point at before / during / after runtime areas if visible. | "The positive finding is that UiPath has the right primitives. The improvement is to give builders one readiness and auditability contract when agents, policy, and human review meet in a live case." |
| 4:22-4:34 | Deck slide 12, README, proof log, or manifest | Switch to coding-agent proof. Point at README, then proof log or manifest. | "Codex helped build, test, validate, and document the solution: the core, evals, UiPath runbooks, evidence packets, product-feedback logs, and submission pack." |
| 4:34-4:44 | Coding-agent proof / terminal | Point at the boundary line or manifest runtime-authority flags. | "But Codex is build-time assistance only. UiPath remains the runtime orchestration layer, deterministic policy owns closure decisions, and humans own high-impact exceptions." |
| 4:44-4:51 | Terminal with `scripts/run_submission_check.sh` output | Point at final passed output. | "The submission check is non-mutating, and it verifies the proof set without starting fresh live UiPath work." |
| 4:51-4:58 | Deck slide 13, impact | Switch to final slide. Stop moving by the last sentence. | "The business impact is fewer wrongful closures, lower repeat contact, better SLA control, and a complete decision trail. Agents interpret. Policy decides. Maestro routes. Humans own exceptions." |

## Emergency Cut

Use this tighter version only if you stumble during the main script and need to recover time.

| Time | Screen | Say exactly |
| --- | --- | --- |
| 0:00-0:20 | Slides 1-2 | "This is ClearPath Recovery, a UiPath Maestro Case workflow for telecom service recovery. The risk is that CRM, order, billing, and support notes can all look resolved while the customer still has no working service. That creates wrongful closure, repeat contact, and audit gaps." |
| 0:20-0:45 | Slides 3-5 | "The architecture keeps the agent useful without giving it final authority: agents interpret, deterministic policy decides, Maestro routes, and humans own exceptions. UiPath is the orchestration boundary: Maestro Case, Action Center, Data Fabric and Orchestrator, Test Manager, and CLI readback." |
| 0:45-1:45 | E-002 packet | "In 2A, the business fixture is green, so the agent emits a raw `closure_candidate` recommendation. But authoritative telemetry is missing or stale. Policy keeps the raw agent event visible, links it to a separate policy decision, blocks closure, and routes to `verify_telemetry` with `missing_authoritative_signal` or `stale_authoritative_signal`." |
| 1:45-2:35 | E-004 packet | "In 2B, the business fixture is intentionally the same. Only authoritative evidence changes: fresh telemetry or inventory contradicts the green business state. The agent may still recommend closure, but policy requires `human_review` with `source_contradiction`. Missing evidence is verification. Contradiction is an exception." |
| 2:35-3:10 | E-003 adversarial packet | "The LLM is an interpreter, not final authority. In the live adversarial proof, one interpretation pushed for closure while another found unresolved risk. That disagreement became structured policy input, and deterministic policy controlled the route." |
| 3:10-3:45 | E-008 JSON / Test Manager | "The eval layer covers E-001 through E-009: aligned closure, missing and stale evidence, contradiction, note-driven routing, adversarial pressure, invalid output, override persistence, and usefulness degradation. Policy improvements stay proposal-only: `pending_human_approval`, `not_promoted`, and active cases pinned until explicit migration." |
| 3:45-4:15 | Product feedback | "The strongest product feedback is a Maestro Case Human-Review Readiness Check: one preflight for services, roles, Action task fields, generated bindings, package and feed versioning, reviewer visibility, and audit readiness. UiPath has the right primitives; builders need one readiness and auditability contract." |
| 4:15-4:38 | Coding-agent proof | "Codex helped build, test, validate, and document the core, evals, UiPath runbooks, evidence packets, product-feedback logs, and submission pack. Codex is build-time assistance only. UiPath remains runtime orchestration, and deterministic policy owns closure decisions." |
| 4:38-4:55 | Terminal and slide 13 | "The non-mutating submission check verifies the proof set without starting fresh live UiPath work. The impact is fewer wrongful closures, lower repeat contact, better SLA control, and a complete decision trail. Agents interpret. Policy decides. Maestro routes. Humans own exceptions." |

## Screen Direction Details

### Deck

- Use the 13-page deck as the spine.
- Do not read every slide. Use slides 1 through 5 for framing, slides 6 through 10 for proof, slide 11 for feedback, slide 12 for coding-agent proof, and slide 13 for close.
- If you are running behind at 2:30, skip slide 8 and say the comparison line while staying on E-004.

### E-002 Packet

Point at these fields in order:

1. Business systems green
2. `Agent Interpretation Event`
3. `recommended_next_stage: closure_candidate`
4. `Policy Decision Event`
5. `from_recommended_stage: closure_candidate`
6. `to_stage: verify_telemetry`
7. `missing_authoritative_signal` or `stale_authoritative_signal`

Do not say "the agent was wrong." Say "the agent recommendation was useful but not sufficient for closure."

### E-004 Packet

Point at these fields in order:

1. Same business-green fixture
2. Fresh authoritative contradiction
3. Raw `closure_candidate`
4. `require_human_review`
5. `source_contradiction`
6. `human_review`
7. Reviewer packet / closure guard

Do not describe 2A and 2B as separate examples. The proof is the controlled change in authoritative evidence.

### E-003 Adversarial Packet

Point at:

1. Advocate interpretation
2. Skeptic interpretation
3. Disagreement score / structured disagreement
4. Policy route

Do not say Gemini or any LLM closes the case.

### Product Feedback

Say "Human-Review Readiness Check" exactly. The phrasing is stronger than "better docs" or "more validation" because it describes a product-shaped fix.

### Coding-Agent Proof

Show at least two of:

- README coding-agent section
- `docs/submission/CODING_AGENT_PROOF_LOG.md`
- `docs/submission/coding_agent_evidence_manifest.json`
- terminal output from `scripts/run_submission_check.sh`

Say the boundary plainly: "Codex is build-time assistance only."

## Claim Boundaries To Keep

- Say: "Test Manager manual representation and execution." Do not say: "automated Test Cloud execution."
- Say: "simulated telecom systems" or "systems-of-record simulator." Do not say: "real production telecom integration."
- Say: "custom evidence packet is the judge-readable proof surface." Do not say: "generated Action Center UI is final-demo ready."
- Say: "Data Fabric V2 and Orchestrator bucket provide full-payload audit proof." Do not say: "native Case history alone is the full audit."
- Say: "LLM and Codex are not runtime closure authority." Do not imply either one can close cases, override policy, or mutate production rules.

## Verification Passes

- Pass 1, structural coverage: main script covers deck slides 1-13, UiPath platform surfaces, E-002, E-004, E-003 adversarial proof, E-008 learning loop, product feedback, coding-agent proof, terminal validation, and final impact.
- Pass 2, claim-boundary audit: script explicitly says Test Manager is manual representation/execution, telecom systems are simulated, custom packets are the judge-readable surface, Data Fabric V2/Orchestrator carry full-payload audit proof, and LLM/Codex are not runtime closure authority.
- Pass 3, timing and delivery: main narration is about 680 spoken words, which leaves screen-transition margin inside the 4:58 hard stop at normal presentation pace.
- Pass 4, artifact/path audit: the setup list points to the current deck, proof index, E-002/E-004 packets, E-003 adversarial packet, E-008 artifact, product-feedback source, coding-agent proof, and submission check output.

## Delivery Notes

- Speak at about 150 words per minute.
- Keep the cursor still while saying field names.
- If a field is not visible, say the line while pointing at the nearest section header, not while searching.
- Do not apologize for the custom packet. Say it is the judge-readable proof surface for the same case data.
- Stop at the closing sentence. Do not add "and that's it" or a second summary.
