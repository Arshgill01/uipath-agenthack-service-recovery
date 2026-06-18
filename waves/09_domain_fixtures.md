# Wave 09: Domain Fixtures

## Goal

Create telecom restoration fixtures for all core scenarios.

## Tasks

- Define customer, service, order, billing, telemetry, inventory, dispatch, message fixtures.
- Include happy path, missing telemetry, stale telemetry, contradiction, dispatch dependency, adversarial pressure.
- Keep fixtures realistic but small.
- Create one canonical "business systems green" fixture reused by missing/stale and contradiction variants.
- Ensure E-002, E-003, and E-004 differ only in authoritative telemetry/inventory conditions unless the wave explicitly documents why.

## Exit Criteria

- Fixtures support all minimum eval scenarios.
- 2A and 2B demo beats are variants of the same setup, not unrelated cases.
