# UI Requirements

UI should serve demo clarity, not decorative polish.

## Required Views

### Case Stage View

- case id,
- customer/service id,
- current stage,
- severity,
- SLA deadline/clock,
- derived evidence state,
- policy versions.

### Evidence Packet

- evidence source table,
- authoritative marker,
- freshness/TTL,
- current value,
- observed timestamp,
- contradictions highlighted.

### Agent / Policy Boundary

- raw agent recommendation,
- confidence values,
- rationale codes,
- policy decision,
- override/block reason,
- resulting stage.

### Human Review

- evidence packet,
- recommended options,
- approve/reject/request evidence,
- reviewer comment,
- structured result.

## Visual Requirements

- 2A missing/stale evidence should feel pending/controlled.
- 2B contradiction should feel escalated/serious.
- Policy override should get a visible before/after beat.
