# Demo Storyboard

Recording target: June 29, 2026. Devpost maximum: five minutes. Aim for 4:45 to 4:55 so upload trimming does not create a rule violation.

## Screen Setup

Open these before recording, in this order:

1. UiPath Automation Cloud tabs: Maestro Case process/case surface, Action Center task list or completed task details for tasks `4300080` and `4300219`, Orchestrator bucket or process readback surface, and Test Manager project `SREV`.
2. `docs/demo/artifacts/evidence_packet_E002.html`.
3. `docs/demo/artifacts/evidence_packet_E004.html`.
4. `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html`.
5. `docs/demo/artifacts/policy_improvement_E008.json`.
6. `README.md` at the coding-agent section and `docs/submission/CODING_AGENT_PROOF_LOG.md`.
7. Terminal at repo root with the final `scripts/run_submission_check.sh` output still visible.

If a browser login expires during recording, switch to the terminal readback output from `docs/demo/DEMO_SAFE_PROOF_RUNBOOK.md`. Do not start a fresh live case during the recording unless new IDs are intentionally needed and logged.

## Recording Run-Of-Show

| Time box | Screen | Say | Do not say |
| --- | --- | --- | --- |
| 0:00-0:20 | UiPath Maestro Case or E-002 packet title/header | "This is a telecom service-recovery exception workflow. The business systems can look resolved while the customer still lacks service, so the risk is wrongful closure, repeat contact, SLA breach, and audit gaps." | Do not pitch this as a generic AI governance platform. |
| 0:20-0:50 | UiPath Automation Cloud surfaces: Maestro Case, Action Center, Orchestrator, Test Manager | "UiPath is the orchestration boundary: Maestro Case owns case routing, Action Center owns the human task lifecycle, Orchestrator/Data Fabric own audit/version proof, and Test Manager represents the eval suite." | Do not imply the custom HTML packet replaces UiPath orchestration. It is the judge-readable proof surface for the same case data. |
| 0:50-1:45 | `docs/demo/artifacts/evidence_packet_E002.html` | "In 2A, CRM, order, billing, and support note all look green. The agent emits a raw `closure_candidate` recommendation, but authoritative telemetry is missing or stale. Policy overrides closure to `verify_telemetry` and keeps the SLA clock alive." | Do not rely on narration only. Point at `Agent Interpretation Event`, `Policy Decision Event`, `from_recommended_stage`, `to_stage`, and `missing_authoritative_signal` or `stale_authoritative_signal`. |
| 1:45-2:35 | `docs/demo/artifacts/evidence_packet_E004.html` | "In 2B, the business fixture is intentionally the same. The only meaningful change is fresh authoritative telemetry or inventory contradiction. That routes to `human_review`, not a retry, because this is a higher-risk exception." | Do not make 2A and 2B sound like unrelated scenarios. Do not claim old E-002/E-004 jobs reached terminal case completion. |
| 2:35-3:10 | `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` | "The LLM is useful as an interpreter, not as the final authority. In the adversarial run, one interpretation pressed for closure, another found unresolved risk, and structured disagreement became policy input for escalation." | Do not say Gemini, Codex, or any LLM closes the case or overrides policy. |
| 3:10-3:45 | `docs/demo/artifacts/policy_improvement_E008.json` and Test Manager `SREV` | "The eval layer guards usefulness and safety. E-001 through E-009 cover aligned closure, missing/stale evidence, contradiction, adversarial pressure, invalid output, override persistence, and a learning-loop artifact. Proposed policy changes remain pending human approval and are not auto-promoted." | Do not claim automated Test Cloud execution. Say Test Manager manual representation/execution. |
| 3:45-4:15 | Product feedback doc or appendix section on Maestro Case preflight | "We also produced concrete product feedback: the strongest request is a Maestro Case human-review readiness preflight that checks services, roles, Action task fields, binding, package/feed versioning, and audit readiness before live runtime." | Do not turn forum reports into our own reproduced defects. Our PF entries are based on observed evidence. |
| 4:15-4:35 | `README.md` coding-agent section and `docs/submission/CODING_AGENT_PROOF_LOG.md` | "Codex was the coding agent used to build the core, evals, UiPath validation runbooks, product-feedback evidence, and submission pack. UiPath remains the runtime orchestration and governance layer." | Do not imply Codex is part of runtime case authority. |
| 4:35-4:55 | Terminal with `scripts/run_submission_check.sh` passed output, then E-004 packet | "The business impact is fewer wrongful closures, lower repeat contact, better SLA control, and a complete decision trail when evidence is missing, stale, or contradictory. The core pattern is simple: agents interpret, policy decides, Maestro routes, humans own exceptions." | Do not keep talking past 4:55. |

## Must Show

- Raw `Agent Interpretation Event` with `recommended_next_stage: closure_candidate`.
- Linked `Policy Decision Event` overriding or escalating that recommendation.
- E-002 route `verify_telemetry`.
- E-004 route `human_review`.
- At least one UiPath platform surface, not only local files.
- Coding-agent proof in README/proof log plus validation output.

## Demo Constraints

- Spend less than 20 seconds explaining telecom.
- Do not demo every failure type.
- Do not rely on generated Action Center UI for proof-critical field readability.
- Do not hide behind dashboards; show case movement and evidence.
- Do not author 2A and 2B as unrelated examples. They must be fixture variants.
- Do not hide coding-agent usage; the submission needs visible proof for the bonus.
