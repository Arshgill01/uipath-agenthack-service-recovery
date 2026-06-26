from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any


def build_data_fabric_record(
    audit_bundle: dict[str, Any],
    *,
    scenario_id: str,
    source_case_instance_key: str | None = None,
    source_task_id: str | None = None,
    package_version: str | None = None,
    for_csv: bool = False,
) -> dict[str, Any]:
    """Flatten a case audit bundle into the proposed Data Fabric audit entity shape."""
    state = audit_bundle["evidence_state"]
    versions = audit_bundle["policy_versions"]

    def _serialize(payload: dict[str, Any]) -> str:
        if for_csv:
            return serialize_for_data_fabric_csv(payload)
        return _dumps(payload)

    return {
        "case_id": audit_bundle["case_id"],
        "service_id": audit_bundle["service_id"],
        "scenario_id": scenario_id,
        "audit_contract_version": audit_bundle["audit_contract_version"],
        "business_state": state["business_state"],
        "derived_evidence_state": state["derived_evidence_state"],
        "closure_block_reason": state["closure_block_reason"],
        "interpretation_policy_version": versions["interpretation_policy_version"],
        "decision_policy_version": versions["decision_policy_version"],
        "source_case_instance_key": source_case_instance_key or "",
        "source_task_id": source_task_id or "",
        "package_version": package_version or "",
        "raw_agent_event_json": _serialize(audit_bundle["agent_interpretation_event"]),
        "policy_decision_event_json": _serialize(audit_bundle["policy_decision_event"]),
        "reviewer_packet_json": _serialize(audit_bundle["reviewer_packet"]),
        "audit_bundle_json": _serialize(audit_bundle),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


def _dumps(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def serialize_for_data_fabric_csv(obj: Any) -> str:
    """Render nested payloads in the CSV shape accepted by Data Fabric import.

    Data Fabric rejected standard JSON strings in CSV import for these text
    columns. This is a storage/import wire format only; use the default record
    output when downstream code needs JSON that can be parsed with json.loads.
    """
    if isinstance(obj, dict):
        items = []
        for k, v in sorted(obj.items()):
            items.append(f"'{k}':{serialize_for_data_fabric_csv(v)}")
        return "{" + ",".join(items) + "}"
    if isinstance(obj, list):
        return "[" + ",".join(serialize_for_data_fabric_csv(x) for x in obj) + "]"
    if isinstance(obj, str):
        escaped = obj.replace("\\", "\\\\").replace("'", "\\'")
        return f"'{escaped}'"
    if isinstance(obj, bool):
        return "true" if obj else "false"
    if obj is None:
        return "null"
    return str(obj)


custom_serialize = serialize_for_data_fabric_csv
