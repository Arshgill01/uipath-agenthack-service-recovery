# Project Brief

## One-Line Concept

A UiPath Maestro Case workflow for telecom service recovery that prevents unsafe case closure when systems disagree, while using agents to interpret messy evidence and Test Cloud-style evals to keep the agent useful over time.

This is a concrete telecom service-recovery solution. Its architecture is reusable, but the submission should not be pitched as a generic governance platform.

## Why This Exists

Telecom service recovery breaks down when business systems say a service is active while the customer still lacks working service. A naive agent can make this worse by trusting the cleanest text field or closing a case based on CRM/order status. The project proves a safer pattern:

- agents interpret ambiguous evidence,
- deterministic policy decides allowed actions,
- Maestro Case enforces routing and auditability,
- humans own high-impact exceptions,
- evals catch regressions and usefulness drift.

## Hackathon Fit

Primary track: **Maestro Case**.

The submission should satisfy Track 1 by showing:

- dynamic, exception-heavy casework,
- long-running service restoration lifecycle,
- stages, milestones, and state,
- humans, agents, APIs, and simulated system-of-record calls,
- missing/stale evidence vs contradicting evidence,
- human-in-loop exception review,
- retry/recovery paths,
- auditability and decision trace.

Supporting award posture:

- Grand Prize first.
- Secondary special award targets: Best Demo/Presentation, Best Cross-Platform Integration, Best Product Feedback.
- Coding-agent bonus must be visible.

## Core Demo Scenario

The core scenario has two related failure paths:

1. **Missing/stale authoritative evidence**
   - CRM/order/billing/support note look green.
   - Agent recommends closure.
   - Network telemetry is missing or stale.
   - Policy blocks closure and routes to telemetry verification/retry with SLA clock.

2. **Contradicting authoritative evidence**
   - CRM says active.
   - Fresh network telemetry says not live, or inventory/device assignment conflicts.
   - Severity escalates.
   - Case routes to human exception review with structured evidence packet.

The demo must visibly show:

- raw agent recommendation before policy acts,
- policy rejecting or downgrading the recommendation,
- logged closure block reason,
- distinct treatment for missing/stale vs contradicting evidence,
- unstructured technician note changing route,
- a real policy-improvement artifact or eval result.

## Architecture Thesis

> Agents interpret ambiguous evidence into structured signals. Policy decides allowed actions. Maestro Case enforces routing. Humans own high-impact exceptions. Explanations are generated once and logged.

## Business Metrics

Primary:

- MTTR reduction.
- SLA breach reduction.
- wrongful closure reduction.
- repeat-contact reduction.
- audit completeness.

Secondary:

- lower human handoff count for non-exception cases.
- faster time to correct remediation path.
- lower service-credit exposure.
- measurable agent usefulness and calibration.

## Non-Goals

- Real telecom system integration.
- Generic governance platform.
- LLM-driven final decisions.
- Live production policy mutation.
- Full monitoring dashboard.
- Full Test Cloud product.
- Every telecom failure type.

## Current Validation Status

This repository contains a local/provisional recovery core plus UiPath Labs validation logs. Wave 01 access and Maestro Case design-surface validation have run against org `keepingitlowkey`, tenant `DefaultTenant`; hard gates G-001 through G-004 remain PARTIAL until a live case proves runtime audit reconstruction, policy version pinning, evidence-packet review/return, and raw recommendation visibility before policy override.

Before major application scaffolding, complete or explicitly waive:

- Maestro Case state/audit reconstruction.
- Policy version pinning.
- Human evidence packet rendering.
- Raw agent recommendation visibility before policy override.

See [docs/validation/VALIDATION_GATES.md](docs/validation/VALIDATION_GATES.md).
