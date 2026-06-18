from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from service_recovery_core.enums import (
    CASE_STAGES,
    EVIDENCE_FIELDS,
    EVIDENCE_STATES,
    FRESHNESS_STATUSES,
    SEVERITIES,
    SOURCES,
)

AUTHORITATIVE_SOURCE_BY_FIELD = {
    "service_live_status": "network_telemetry",
    "crm_order_status": "crm",
    "billing_status": "billing",
    "inventory_assignment": "inventory",
    "dispatch_status": "dispatch",
}


class ValidationError(ValueError):
    pass


def parse_timestamp(value: str) -> datetime:
    if not isinstance(value, str):
        raise ValidationError("timestamp must be a string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"invalid timestamp: {value}") from exc
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def validate_case(case: dict[str, Any]) -> None:
    required = {
        "case_id",
        "customer_id",
        "service_id",
        "case_stage",
        "severity",
        "sla_deadline",
        "interpretation_policy_version",
        "decision_policy_version",
        "derived_evidence_state",
    }
    _require_keys(case, required, "case")
    _require_enum(case["case_stage"], CASE_STAGES, "case_stage")
    _require_enum(case["severity"], SEVERITIES, "severity")
    _require_enum(case["derived_evidence_state"], EVIDENCE_STATES, "derived_evidence_state")
    parse_timestamp(case["sla_deadline"])


def validate_evidence_signal(signal: dict[str, Any], *, now: datetime | None = None) -> None:
    required = {
        "case_id",
        "field",
        "source",
        "value",
        "authoritative",
        "freshness_status",
        "ttl_seconds",
        "observed_at",
    }
    _require_keys(signal, required, "evidence signal")
    _require_enum(signal["field"], EVIDENCE_FIELDS, "field")
    _require_enum(signal["source"], SOURCES, "source")
    _require_enum(signal["freshness_status"], FRESHNESS_STATUSES, "freshness_status")
    if not isinstance(signal["authoritative"], bool):
        raise ValidationError("authoritative must be boolean")
    if not isinstance(signal["ttl_seconds"], int) or signal["ttl_seconds"] <= 0:
        raise ValidationError("ttl_seconds must be a positive integer")
    observed_at = parse_timestamp(signal["observed_at"])
    if signal["authoritative"]:
        expected_source = AUTHORITATIVE_SOURCE_BY_FIELD[signal["field"]]
        if signal["source"] != expected_source:
            raise ValidationError(f"{signal['field']} authoritative source must be {expected_source}")
    if now and signal["freshness_status"] == "fresh":
        age = (now - observed_at).total_seconds()
        if age > signal["ttl_seconds"]:
            raise ValidationError("fresh evidence is older than ttl_seconds")


def _require_keys(payload: dict[str, Any], required: set[str], label: str) -> None:
    missing = required - set(payload)
    if missing:
        raise ValidationError(f"{label} missing required keys: {sorted(missing)}")


def _require_enum(value: Any, allowed: set[str], field: str) -> None:
    if value not in allowed:
        raise ValidationError(f"{field} has invalid value: {value}")
