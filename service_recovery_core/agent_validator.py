from __future__ import annotations

from typing import Any

from service_recovery_core.enums import (
    BLOCK_REASONS,
    CLAIM_SOURCES,
    CLAIM_TYPES,
    FAILURE_CATEGORIES,
    RATIONALE_CODES,
    RECOMMENDED_STAGES,
)
from service_recovery_core.schemas import ValidationError, parse_timestamp

CATEGORY_RATIONALE_CODES = {
    "activation_failure": {"mentions_signal_absent", "mentions_system_timeout"},
    "billing_hold": {"mentions_billing_hold"},
    "inventory_mismatch": {"mentions_device_mismatch"},
    "dispatch_dependency": {"mentions_access_blocker"},
    "telemetry_gap": {"mentions_signal_absent", "mentions_system_timeout"},
    "customer_premises_issue": {"mentions_signal_absent", "mentions_access_blocker"},
    "unclassified": {"none"},
}

HIGH_SPECIFICITY_CODES = {
    "mentions_access_blocker",
    "mentions_device_mismatch",
    "mentions_billing_hold",
    "mentions_customer_pressure",
}

RATIONALE_CLAIM_TYPES = {
    "mentions_access_blocker": {"technician_observation", "appointment_update"},
    "mentions_device_mismatch": {"device_identifier", "technician_observation"},
    "mentions_signal_absent": {"customer_reported_symptom", "technician_observation"},
    "mentions_billing_hold": {"support_note_claim"},
    "mentions_customer_pressure": {"pressure_to_bypass"},
    "mentions_system_timeout": {"support_note_claim", "technician_observation"},
}


def validate_agent_interpretation(payload: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    required = {
        "failure_category",
        "category_confidence",
        "interpretation_rationale_codes",
        "extracted_claims",
        "recommended_next_stage",
        "recommendation_confidence",
        "closure_block_reason_code",
        "audit_explanation",
    }
    missing = required - set(payload)
    if missing:
        errors.append(f"missing required keys: {sorted(missing)}")
        return {"valid": False, "errors": errors}

    _check_enum(payload["failure_category"], FAILURE_CATEGORIES, "failure_category", errors)
    _check_confidence(payload["category_confidence"], "category_confidence", errors)
    _check_enum(payload["recommended_next_stage"], RECOMMENDED_STAGES, "recommended_next_stage", errors)
    _check_confidence(payload["recommendation_confidence"], "recommendation_confidence", errors)
    _check_enum(payload["closure_block_reason_code"], BLOCK_REASONS, "closure_block_reason_code", errors)

    codes = payload["interpretation_rationale_codes"]
    if not isinstance(codes, list) or not codes:
        errors.append("interpretation_rationale_codes must be a non-empty list")
        codes = []
    else:
        for code in codes:
            _check_enum(code, RATIONALE_CODES, "interpretation_rationale_codes", errors)
        if "none" in codes and len(codes) > 1:
            errors.append("none rationale cannot be combined with other rationale codes")

    claims = payload["extracted_claims"]
    if not isinstance(claims, list):
        errors.append("extracted_claims must be a list")
        claims = []
    for index, claim in enumerate(claims):
        _validate_claim(claim, index, errors)

    if not isinstance(payload["audit_explanation"], str) or not payload["audit_explanation"].strip():
        errors.append("audit_explanation must be a non-empty string")

    _validate_optional_recommendation_package(payload, errors)

    category = payload["failure_category"]
    category_confidence = payload["category_confidence"]
    recommendation_confidence = payload["recommendation_confidence"]
    block_reason = payload["closure_block_reason_code"]
    recommended_stage = payload["recommended_next_stage"]

    if isinstance(category_confidence, (int, float)) and not isinstance(category_confidence, bool):
        if category == "unclassified" and category_confidence > 0.40:
            errors.append("unclassified requires category_confidence <= 0.40")
        if category_confidence >= 0.75 and (not codes or codes == ["none"]):
            errors.append("category_confidence >= 0.75 requires non-none rationale")
        if category_confidence >= 0.90:
            independent_codes = {code for code in codes if code != "none"}
            if len(independent_codes) < 2 and not independent_codes.intersection(HIGH_SPECIFICITY_CODES):
                errors.append("category_confidence >= 0.90 requires two rationale codes or one high-specificity code")
        if codes == ["none"] and category_confidence > 0.40 and category != "unclassified":
            errors.append("none rationale requires low confidence or unclassified category")

    if codes and category in CATEGORY_RATIONALE_CODES:
        allowed = CATEGORY_RATIONALE_CODES[category]
        meaningful_codes = {code for code in codes if code != "none"}
        if meaningful_codes and not meaningful_codes.intersection(allowed):
            errors.append(f"{category} conflicts with rationale codes {sorted(meaningful_codes)}")

    if isinstance(category_confidence, (int, float)) and not isinstance(category_confidence, bool) and category_confidence > 0.75:
        supported_codes = _supported_rationale_codes(claims)
        unsupported = {code for code in codes if code != "none"} - supported_codes
        if unsupported:
            errors.append(f"high confidence rationale lacks supporting extracted claims: {sorted(unsupported)}")

    if recommended_stage == "closure_candidate":
        if block_reason != "none":
            errors.append("closure_candidate recommendation requires closure_block_reason_code none")
        if isinstance(recommendation_confidence, (int, float)) and not isinstance(recommendation_confidence, bool) and recommendation_confidence < 0.75:
            errors.append("closure_candidate recommendation requires recommendation_confidence >= 0.75")

    return {"valid": not errors, "errors": errors}


def _validate_optional_recommendation_package(payload: dict[str, Any], errors: list[str]) -> None:
    urgency = payload.get("urgency")
    if urgency is not None:
        _check_enum(urgency, {"low", "normal", "high", "critical"}, "urgency", errors)

    for field in ("customer_impact_summary", "operator_note"):
        value = payload.get(field)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            errors.append(f"{field} must be a non-empty string when provided")

    for field in ("evidence_gaps", "recommended_actions", "reviewer_questions"):
        values = payload.get(field)
        if values is None:
            continue
        if not isinstance(values, list):
            errors.append(f"{field} must be a list when provided")
            continue
        for index, item in enumerate(values):
            if not isinstance(item, str) or not item.strip():
                errors.append(f"{field}[{index}] must be a non-empty string")


def _validate_claim(claim: Any, index: int, errors: list[str]) -> None:
    if not isinstance(claim, dict):
        errors.append(f"extracted_claims[{index}] must be an object")
        return
    required = {"claim_type", "value", "source", "timestamp"}
    missing = required - set(claim)
    if missing:
        errors.append(f"extracted_claims[{index}] missing required keys: {sorted(missing)}")
        return
    _check_enum(claim["claim_type"], CLAIM_TYPES, f"extracted_claims[{index}].claim_type", errors)
    _check_enum(claim["source"], CLAIM_SOURCES, f"extracted_claims[{index}].source", errors)
    if not isinstance(claim["value"], str) or not claim["value"].strip():
        errors.append(f"extracted_claims[{index}].value must be a non-empty string")
    try:
        parse_timestamp(claim["timestamp"])
    except ValidationError as exc:
        errors.append(f"extracted_claims[{index}].timestamp {exc}")


def _supported_rationale_codes(claims: list[Any]) -> set[str]:
    claim_types = {claim.get("claim_type") for claim in claims if isinstance(claim, dict)}
    return {
        code
        for code, supporting_claim_types in RATIONALE_CLAIM_TYPES.items()
        if claim_types.intersection(supporting_claim_types)
    }


def _check_enum(value: Any, allowed: set[str], field: str, errors: list[str]) -> None:
    if value not in allowed:
        errors.append(f"{field} has invalid value: {value}")


def _check_confidence(value: Any, field: str, errors: list[str]) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        errors.append(f"{field} must be a number")
        return
    if value < 0 or value > 1:
        errors.append(f"{field} must be between 0 and 1")
