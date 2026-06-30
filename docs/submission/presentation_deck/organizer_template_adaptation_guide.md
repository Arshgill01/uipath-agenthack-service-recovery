# Organizer Template Adaptation Guide

Official template link supplied by Devpost: https://bit.ly/3R0MsHU

Use `governed_service_recovery_uipath_agenthack.pptx` as the finished editable deck. If the official Google Slides template must be used exactly, paste this content into the organizer slides while preserving the organizer title/body placeholders.

A compact 5-slide companion deck matching the organizer template structure is generated as `clearpath_recovery_official_template_version.pptx`.

## Slide Mapping

### 1. ClearPath Recovery
- Layout: cover
- Subtitle: No service case closes until authoritative evidence proves the customer is actually restored

### 2. The riskiest case is the one that looks resolved everywhere except the customer’s service.
- Layout: problem
- Eyebrow: 01 · BUSINESS PROBLEM
- Lead: CRM, orders, billing, and support notes can all look green while authoritative service evidence is missing, stale, or contradictory.
- Bottom callout: The project is not a generic governance platform. It is a concrete telecom exception workflow.

### 3. Agents interpret. Policy decides. Maestro routes. Humans own exceptions.
- Layout: architecture
- Eyebrow: 02 · ARCHITECTURE THESIS
- Bottom callout: The LLM never closes cases, overrides policy, or mutates production rules.

### 4. This is Case work because the route emerges as evidence changes.
- Layout: casefit
- Eyebrow: 03 · WHY MAESTRO CASE
- Lead: The workflow is not a fixed BPMN-style happy path. It is long-running exception handling with changing evidence, SLA pressure, human accountability, and audit requirements.
- Bottom callout: ClearPath Recovery fits Track 1: dynamic exception-heavy casework with agents, automation, and humans in charge at key decision points.

### 5. UiPath is the orchestration and governance boundary.
- Layout: map
- Eyebrow: 04 · UIPATH PLATFORM MAP
- Bottom callout: Custom evidence packets make the proof readable; they do not replace UiPath orchestration.

### 6. Same green business systems. Missing signal means verify, not close.
- Layout: evidence
- Eyebrow: 05 · SCENARIO 2A
- Image: `docs/demo/artifacts/evidence_packet_E002_desktop.png`

### 7. Same green business systems. Contradiction means human review.
- Layout: evidence
- Eyebrow: 06 · SCENARIO 2B
- Image: `docs/demo/artifacts/evidence_packet_E004_desktop.png`

### 8. Missing evidence and contradicting evidence are different operational problems.
- Layout: comparison
- Eyebrow: 07 · ONE VARIABLE, DIFFERENT ROUTE
- Bottom callout: This is the central proof: same business-green fixture, different authoritative signal, different route.

### 9. The LLM contributes structured interpretation, not final authority.
- Layout: evidence
- Eyebrow: 08 · AGENT USEFULNESS BOUNDARY
- Image: `docs/demo/artifacts/evidence_packet_E003_adversarial_desktop.png`

### 10. The eval suite keeps the agent useful without weakening closure policy.
- Layout: evals
- Eyebrow: 09 · EVAL AND LEARNING LOOP
- Bottom callout: Validated path: local tests plus Test Manager manual representation, not claimed automated Test Cloud execution.

### 11. The strongest product ask is a Maestro Case Human-Review Readiness Check.
- Layout: feedback
- Eyebrow: 10 · PRODUCT FEEDBACK AWARD
- Lead: The pieces exist across Maestro, Actions, packages, Data Fabric, and Test Manager. Builders need one preflight and auditability contract that proves the human-review path will work before runtime.
- Bottom callout: This is framed as actionable product feedback, not a complaint list.

### 12. Codex helped build and verify the submission pack.
- Layout: coding
- Eyebrow: 11 · CODING AGENT CONTRIBUTION
- Bottom callout: Runtime authority remains: deterministic policy, UiPath orchestration, and human review.

### 13. ClearPath Recovery makes agentic service recovery safer without making it toothless.
- Layout: close
- Eyebrow: 12 · IMPACT
- Bottom callout: Agents interpret. Policy decides. Maestro routes. Humans own exceptions.

## Video Use

Use slides 1, 3, 4, and 12 as quick framing in the video. Spend most of the video on the live/proof screens: E-002, E-004, E-003 adversarial, Test Manager, product feedback, Codex proof, and `scripts/run_submission_check.sh` output.

## Claim Boundaries

- Do not claim real telecom integration.
- Do not claim automated Test Cloud execution.
- Do not claim generated Action Center UI is the judge-facing proof surface.
- Do not claim LLMs or Codex can close cases or override policy.