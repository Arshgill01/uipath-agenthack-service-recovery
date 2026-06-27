# AgentHack Forum Research

Date: 2026-06-27.

Primary source:

- UiPath Forum topic: `https://forum.uipath.com/t/uipath-agenthack-is-live-50-000-in-prizes-three-tracks-and-7-weeks-to-build/5746132`
- Official Devpost page: `https://uipath-agenthack.devpost.com/`
- 2025 winners forum topic: `https://forum.uipath.com/t/here-are-the-uipath-agenthack-2025-winners/3586396`
- 2025 UiPath Community blog: `https://www.uipath.com/community-blog/community-news/uipath-community-annual-global-hackathon-2025`

Local scrape artifacts:

- `docs/research/artifacts/2026-06-27/uipath_agenthack_forum_topic_5746132.json`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_forum_topic_5746132_all_posts.json`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_forum_topic_5746132_all_posts.txt`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_forum_topic_5746132_high_signal_posts.txt`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_devpost.html`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_devpost.html.txt`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_2025_winners_topic_3586396.json`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_2025_winners_topic_3586396_posts.txt`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_2025_blog.html`
- `docs/research/artifacts/2026-06-27/uipath_agenthack_2025_blog.html.txt`

## High-Signal Findings

### Track Positioning

The official Devpost distinction strongly favors Track 1 for this project:

- Track 1, UiPath Maestro Case, is for dynamic, exception-heavy casework moving through stages with handoffs between agents, robots, and people while humans stay in charge at key decision points.
- Track 2, UiPath Maestro BPMN, is for a predictable end-to-end sequence modeled in BPMN 2.0.
- Devpost gives the explicit tip: unpredictable paths that emerge as work unfolds belong in Maestro Case; predictable sequences map to Maestro BPMN.

Decision impact:

- Keep the primary track as UiPath Maestro Case.
- Do not pivot to Maestro BPMN. This repo does not have a validated BPMN 2.0 runtime artifact, and the value proposition is exception routing rather than a fixed linear process.
- Do not pivot to Test Cloud. Test Manager/Test Cloud is supporting evidence for eval discipline, not the main product surface.

### Submission Requirements We Need To Satisfy

Devpost requires all of the following:

- a Devpost project page with track, written description, business problem, screenshots/images,
- a demo video of five minutes maximum that shows the solution running, walks through architecture, explains which agents are involved and how they are orchestrated, and shows where humans fit in,
- a public GitHub repository with README, setup instructions, prerequisites, UiPath components used, and clear indication of coding-agent / low-code-agent use,
- a solution built on UiPath Automation Cloud, with orchestration and agent logic running through UiPath Platform,
- a completed presentation deck,
- optional product feedback survey for Best Product Feedback.

Decision impact:

- README needed a coding-agent section and a pointer to proof logs.
- Demo must visibly show UiPath running surfaces, not just local HTML or slides.
- The submission should list Maestro Case as the selected track and mention Test Manager only as supporting eval representation.

### Coding-Agent Bonus

The forum Q&A and Devpost both make coding-agent proof explicit.

Minimum evidence expected:

- which coding agent tool was used,
- how it contributed,
- at least one verifiable proof form such as prompt log, screenshots, or a dedicated README section,
- Devpost says the demo video should show use of UiPath for Coding Agents / coding agents to build part of the solution.

Decision impact:

- Add `docs/submission/CODING_AGENT_PROOF_LOG.md`.
- Keep thread IDs, branch names, commits, and concrete outputs visible.
- Add a short README section that names Codex and points to the proof log.
- Add one 10 to 20 second demo beat showing Codex + repo logs + validation command output.

### Platform/Product Feedback Evidence From Forum

The forum independently reinforces our product-feedback thesis:

- Multiple participants hit Action Center / Actions enablement or license confusion.
- UiPath/community replies pointed builders to Admin > Tenant > Services > Add Service and role/license assignment.
- Participants reported Maestro Case / Maestro Flow publish and package blockers near the deadline.
- Participants reported runtime or authoring confusion around serverless, entry points, Action Center, and Labs access.
- UiPath staff explicitly asked a participant to file detailed product feedback for a Maestro bug.

Decision impact:

- Our product feedback is not isolated. PF-003, PF-026, PF-027, and PF-028 are consistent with broader builder pain visible in the public forum.
- Keep the primary feedback recommendation: a Maestro Case human-review readiness/preflight path.
- Add forum research as supporting context, but do not convert other participants' reports into our PF entries unless we reproduce them ourselves.

### 2025 Winner Patterns

The 2025 winner sources emphasize:

- real-world production-grade problems,
- business impact,
- live demos and clear presentation,
- multi-agent solutions across healthcare, safety, insurance, testing, welfare, and support,
- cross-platform integration and product feedback as special award opportunities.

Decision impact:

- Our telecom service-recovery scenario is appropriately enterprise and high-impact.
- The strongest levelling-up opportunity is not adding generic features. It is making business impact, UiPath platform depth, human control, and evidence-backed product feedback obvious in the demo and README.

## Gaps Found

| Gap | Why it matters | Action |
| --- | --- | --- |
| README did not clearly disclose coding-agent use. | Devpost requires a clear indication of coding-agent / low-code-agent use. | Added README section and coding-agent proof log. |
| Track selection was spread across docs, not locked as a decision. | User needs confidence that the submission is advertised under the right track. | Added `docs/submission/TRACK_SELECTION_DECISION.md`. |
| Forum scrape was not preserved. | Research would be hard to audit later. | Saved full JSON/text artifacts under `docs/research/artifacts/2026-06-27/`. |
| Demo storyboard did not explicitly include a coding-agent proof beat. | Bonus points depend on showing coding-agent use. | Add/update demo runbook/storyboard with Codex proof beat. |

## Recommendations

1. Submit under UiPath Maestro Case.
2. Mention Test Manager/Test Cloud as supporting eval evidence, not the selected track, unless the final form allows multiple category tags without track conflict.
3. Use the demo opening and README to make the claim: UiPath is the orchestration/governance layer; Codex accelerated implementation, tests, runbooks, and product-feedback evidence.
4. Add one slide or README table mapping judging criteria to proof artifacts.
5. Keep Best Product Feedback as a serious special-award target, now supported by public-forum context plus our own PF-001 through PF-028 evidence.
