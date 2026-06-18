# Metrics

## Primary Metrics

| Metric | Meaning | Demo / artifact proof |
| --- | --- | --- |
| MTTR | Time from case open to safe remediation/closure candidate. | Runbook timestamps or scenario comparison. |
| SLA breach rate | Cases that exceed deadline due to stalled handoffs. | SLA clock and route escalation. |
| Wrongful closure rate | Cases closed without fresh authoritative confirmation. | Eval scenarios prove blocked closure. |
| Repeat contact rate | Customer contacts after premature closure. | Business-case estimate or fixture narrative. |
| Audit completeness | Ability to reconstruct recommendation, policy decision, reason, human action. | One-view/one-query audit reconstruction. |

## Agent Usefulness Metrics

- schema validity rate,
- category accuracy,
- recommendation accepted rate,
- policy override rate,
- low-confidence/unclassified rate vs baseline,
- invalid output rate,
- usefulness incident count.

## Demo Guidance

Use honest labels:

- measured in prototype,
- estimated based on scenario,
- target production metric,
- not yet measured.
