# Validation Gates

Do not scaffold major application code until hard gates are answered or explicitly waived.

## Hard Gates

These can force architecture changes.

### G-001: Native Case State / Audit Reconstruction

Question: Can a single case run be reconstructed through one case view or one query?

Pass condition:

- evidence state at each stage,
- policy version active,
- raw agent recommendation,
- policy decision,
- closure block reason,
- human action,
- timestamp/order of events.

Strict rule: manual log archaeology across many sources is not a pass. If one-view or one-query reconstruction is not possible, use Data Fabric/Data Service or explicit custom audit events.

### G-002: Policy Version Pinning

Question: Can each case persist interpretation and decision policy versions?

Pass condition:

- active case has `interpretation_policy_version`,
- active case has `decision_policy_version`,
- versions do not silently change,
- migration can be represented as explicit audited event.

Native support is optional. Metadata + audit event is acceptable.

### G-003: Human Evidence Packet

Question: Can human review show structured evidence clearly?

Pass condition:

- evidence table,
- agent output,
- policy decision,
- block reason,
- recommended options,
- approve/reject/request-evidence/comment result returned as structured data.

If Action Center works but renders this generically, prefer custom evidence-packet UI for demo legibility.

### G-004: Agent Recommendation Visible Before Override

Question: Can the demo show raw recommendation separately from final policy decision?

Pass condition:

- same test run as G-001,
- raw `recommended_next_stage` persists,
- final policy decision persists,
- visible before/after override is available in UI, event view, or controlled screen.

This is central to the demo. Do not fake it if it can be logged.

## Soft Gates

These affect effort, not core architecture.

### G-005: Case Stage / Routing Control

Question: Can structured policy output drive distinct 2A and 2B routes?

Desired:

- `missing_pending` routes to retry/verification with SLA.
- `contradicting` routes to elevated human review/investigation.

### G-006: Case App / Instance Visibility

Question: Can demo surfaces show severity, SLA, stage, history, and blocked closure reason clearly?

### G-007: Test Cloud / Eval Crossover

Question: Can labeled eval scenarios run or be represented in UiPath-native way and attach result to policy improvement?

### G-008: Coding-Agent Bonus

Question: Can `uip skills install --agent codex` and CLI/skills-assisted workflow be shown?

Desired visible proof:

- install/list skills,
- package/deploy/test/troubleshoot step,
- agent-authored or agent-guided UiPath lifecycle artifact.

## Validation Run Template

Add results to [VALIDATION_RESULTS.md](VALIDATION_RESULTS.md).

```md
## YYYY-MM-DD - Gate G-XXX

Environment:
- UiPath tenant:
- Product surface:
- User/role:

Steps:
1. ...

Observed:
- ...

Result:
- PASS / FAIL / PARTIAL

Decision impact:
- ...

Follow-up:
- ...
```
