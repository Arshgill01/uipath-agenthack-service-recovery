# Architecture

## Thesis

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

## System Shape

```text
Customer/support/tech text ─┐
CRM/order API ──────────────┤
Billing API ────────────────┤
Network telemetry API ──────┼─> Evidence collector ─> Reconciliation policy ─> Maestro Case stage route
Inventory/activation API ───┤                         ↑                         │
Dispatch notes ─────────────┘                         │                         │
                                                       │                         v
Agent interpretation ─ structured signals ─────────────┘                  Human review / retry / remediation / closure candidate

Eval/Test Cloud loop ─> usefulness + regression results ─> policy improvement case ─> human approval ─> new policy version
```

## Core Components

| Component | Responsibility | Must not do |
| --- | --- | --- |
| Agent interpretation | Parse unstructured messages/notes into closed-schema signals, classify failure category, recommend next stage, explain once. | Decide closure, override policy, mutate production rules. |
| Reconciliation policy | Evaluate authoritative sources, freshness, contradictions, closure eligibility, route safety. | Parse free-form prose or trust unsupported claims. |
| Maestro Case | Carry case lifecycle, stages, routing, human tasks, audit timeline, incident/retry paths. | Hide the agent/policy boundary. |
| Human review | Approve risky remediation, request evidence, reject unsafe closure, handle contradictions. | Rubber-stamp opaque agent output. |
| Eval/Test Cloud | Validate scenarios, schema, calibration, policy regressions, usefulness drift. | Become a second full product. |
| Policy improvement loop | Convert repeated failures into proposed policy/schema/prompt diffs. | Auto-promote production policy changes. |

## Required Visible Demo Behaviors

1. Raw agent recommendation appears before policy action.
2. Policy visibly rejects or downgrades at least one agent recommendation.
3. Missing/stale evidence routes differently from contradicting evidence.
4. Human reviewer sees a structured evidence packet.
5. Audit event contains the generated-once explanation.
6. Eval/policy-improvement artifact proves learning is governed.

## Evidence-State Semantics

| State | Meaning | Route |
| --- | --- | --- |
| `confirmed_aligned` | Authoritative sources are fresh and satisfy closure policy. | Closure candidate or safe remediation completion. |
| `missing_pending` | Required signal has not arrived but source is expected/reachable. | Verification/retry with SLA clock. |
| `contradicting` | Fresh authoritative or material sources disagree. | Elevated severity and human exception review/investigation. |
| `authoritative_unavailable_or_stale` | Source of truth is down, unavailable, or older than TTL. | Block closure, verify source, escalate if SLA/risk threshold reached. |

## Design Principle

False caution is not automatically acceptable. A single case may route conservatively, but repeated low-confidence or unclassified behavior is an **agent usefulness failure** and must generate eval/product feedback or a policy improvement case.
