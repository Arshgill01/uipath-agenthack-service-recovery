# Policy Improvement Loop

## Principle

The system learns through governance.

Agents may propose policy/schema/prompt improvements. They may not apply production policy changes directly.

## Flow

1. Case failures, eval failures, repeated policy overrides, invalid outputs, or usefulness incidents are logged.
2. System creates a policy improvement case.
3. Agent summarizes pattern and proposes a structured diff.
4. Eval/Test Cloud validates proposed change against baseline and regression scenarios.
5. Human owner approves or rejects.
6. Approved change creates a new policy version.
7. New cases use latest approved version.
8. Active cases remain pinned unless explicitly migrated.

## Proposal Types

Lower-risk:

- new eval scenario,
- new rationale code,
- prompt/schema clarification,
- synonym/pattern hint,
- human-review checklist item,
- closure-block reason code.

Higher-risk:

- source-of-truth hierarchy change,
- TTL/freshness threshold change,
- closure eligibility change,
- SLA escalation change,
- automatic remediation permission.

Forbidden:

- auto-promoting rules,
- weakening closure requirements without approval,
- overriding authoritative evidence with free text,
- disabling audit logging,
- bypassing eval/regression checks.

## Demo Artifact

The demo should show a real produced artifact, not necessarily execute this entire loop live:

- improvement case,
- trigger,
- proposed diff,
- eval result,
- approval status,
- new policy version.

Current artifact:

- `docs/demo/artifacts/policy_improvement_E008.json`

It is generated from E-008 by:

```sh
python -m service_recovery_core.evals \
  --policy-improvement-artifact-scenario E-008 \
  --output docs/demo/artifacts/policy_improvement_E008.json
```

The artifact is proposal-only. It records `approval_status: pending_human_approval`, `promotion_status: not_promoted`, the current `ip-v1` / `dp-v1` policy versions, proposed next `ip-v2-proposed` interpretation policy, and `active_cases_remain_pinned_until_explicit_migration_event`.
