# Product Feedback Award Log

The team wants to seriously compete for the Best Product Feedback award. This file is the working evidence log.

## Feedback Principles

Good feedback is:

- specific,
- reproducible,
- tied to a real workflow,
- fair about uncertainty,
- clear about builder impact,
- paired with a concrete improvement suggestion.

Bad feedback is:

- vague frustration,
- unsupported claims,
- duplicate notes with no reproduction detail,
- complaints about user/account setup mixed with product bugs,
- feedback written only at the end from memory.

## Entry Template

```md
## YYYY-MM-DD - Product Surface / Workflow

Context:
- Goal:
- Product surface:
- Account/tenant:
- Wave/gate:

What worked:
- ...

What failed or confused us:
- ...

Expected:
- ...

Observed:
- ...

Impact:
- Build impact:
- Demo/submission impact:
- Severity: low / medium / high

Workaround:
- ...

Suggested improvement:
- ...

Evidence:
- Screenshot/path/link:
- Commands/logs:

Classification:
- access / docs / UX / missing feature / product defect / performance / integration / other
```

## Feedback Entries

### 2026-06-24 - Automation Cloud Login / Labs Tenant Access

Context:

- Goal: complete Wave 01 platform access inventory.
- Product surface: Automation Cloud login / portal routing.
- Account/tenant: Google login attempted for the hackathon account.
- Wave/gate: Wave 01.

What worked:

- UiPath CLI package could be installed locally.
- Browser reached UiPath login.

What failed or confused us:

- After login attempt, browser landed at `portal_/missingaccount` rather than an accessible Automation Cloud tenant.
- It was not clear from that page/session what action was required to attach the account to the AgentHack Labs tenant.

Expected:

- After accepting a Labs invite and logging in, the account should land in a usable Automation Cloud organization/tenant or provide a clear next action.

Observed:

- Prior agent recorded `https://cloud.uipath.com/portal_/missingaccount`.
- Product surfaces such as Maestro, Maestro Case, Action Center, Test Cloud, Integration Service, and Orchestrator could not be inventoried in that session.

Impact:

- Build impact: blocked hard validation gates G-001 through G-004.
- Demo/submission impact: delayed confirmation of the primary Maestro Case track.
- Severity: high during access setup.

Workaround:

- User later reported receiving Labs access and logging in through Zen browser. Wave 01 must be rerun against the working session before closing this feedback item.

Suggested improvement:

- Provide clearer Labs invite/account-linking status on `missingaccount`, including whether invite acceptance is pending, wrong account is logged in, tenant provisioning is incomplete, or the user needs to switch organizations.

Evidence:

- See `docs/validation/VALIDATION_RESULTS.md`, Wave 01 entry.

Classification:

- access / UX / docs
