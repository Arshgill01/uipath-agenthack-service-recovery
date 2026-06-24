# UiPath Integration Map

This map is provisional until validation gates are run.

| Capability | Planned use | Validation dependency |
| --- | --- | --- |
| Maestro Case | Primary case lifecycle, stages, routing, incident/recovery, human accountability. | G-001, G-002, G-005, G-006 |
| Agent Builder / Coded Agent | Interpret unstructured notes/messages into structured schema. | Stack choice and UiPath access |
| API Workflows | Query simulated CRM/billing/telemetry/inventory/dispatch APIs. | G-005 and Wave 28 |
| Action Center | Human review/approval if evidence packet renders well. | G-003 |
| Case App / custom UI | Fallback or primary evidence packet/demo surface. | G-003, G-004, G-006 |
| Data Fabric/Data Service | Store case/audit/policy/eval objects if native Case state is insufficient. | G-001, G-002 |
| Test Cloud | Eval/regression validation for agent usefulness and policy changes. | G-007 |
| UiPath CLI + skills | Coding-agent bonus proof and lifecycle automation. | G-008; CLI version `1.196.0` installed locally on 2026-06-24, login not completed |
| Orchestrator | Assets, packages, jobs, logs, deployment, secrets if needed. | Wave 01 and stack selection |

## Rule

Do not use a UiPath component for checkbox breadth. Use it when it has visible responsibility in the demo or build lifecycle.

## Wave 01 Observed Access Status

Observed on 2026-06-24:

- Local `uip` CLI is installed and reports version `1.196.0`.
- Automation Cloud browser access did not reach a tenant; Safari landed at `portal_/missingaccount`.
- Product access for Maestro, Maestro Case, Studio Web, Action Center, Test Cloud/Test Manager, Integration Service, and Orchestrator is unconfirmed.
- Hard gate validation must not start until Automation Cloud tenant access and Maestro Case availability are confirmed.
