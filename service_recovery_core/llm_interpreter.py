from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from typing import Any, Protocol

from service_recovery_core.agent_validator import validate_agent_interpretation
from service_recovery_core.evals import _scenario_transition
from service_recovery_core.policy import decide_policy


DEFAULT_MODEL = "gemini-3-flash"
DEFAULT_LOCATION = "us-central1"
DISAGREEMENT_ESCALATION_THRESHOLD = 0.60


class LlmInterpreterError(RuntimeError):
    pass


class ContentClient(Protocol):
    def generate_content(self, *, model: str, contents: str, config: Any = None) -> Any:
        ...


class GoogleContentClient:
    def __init__(self, client: Any):
        self._client = client

    def generate_content(self, *, model: str, contents: str, config: Any = None) -> Any:
        return self._client.models.generate_content(model=model, contents=contents, config=config)


def interpret_notes_with_llm(
    *,
    notes: list[dict[str, str]],
    business_context: dict[str, str],
    event_id: str,
    input_refs: list[str],
    model: str = DEFAULT_MODEL,
    project: str | None = None,
    location: str | None = None,
    client: ContentClient | None = None,
    role_framing: str | None = None,
    repair_attempts: int = 1,
) -> dict[str, Any]:
    """Return a schema-validated Agent Interpretation Event from unstructured text."""

    active_client = client or _default_google_client(project=project, location=location)
    prompt = build_interpretation_prompt(notes=notes, business_context=business_context, role_framing=role_framing)
    try:
        raw_text = _response_text(
            active_client.generate_content(
                model=model,
                contents=prompt,
                config=_generation_config(),
            )
        )
    except Exception as exc:
        raise LlmInterpreterError(f"LLM provider call failed: {exc}") from exc
    payload = _json_object(raw_text)
    payload = _normalize_payload(payload)
    payload["event_id"] = event_id
    payload["input_refs"] = input_refs
    result = validate_agent_interpretation(payload)
    repairs_used = 0
    while not result["valid"] and repairs_used < repair_attempts:
        repairs_used += 1
        payload = _repair_payload_with_llm(
            client=active_client,
            model=model,
            invalid_payload=payload,
            validation_errors=result["errors"],
            notes=notes,
            business_context=business_context,
            role_framing=role_framing,
            event_id=event_id,
            input_refs=input_refs,
        )
        result = validate_agent_interpretation(payload)
    if not result["valid"]:
        raise LlmInterpreterError(f"LLM agent output failed validation: {result['errors']}")
    return payload


def build_interpretation_prompt(
    *,
    notes: list[dict[str, str]],
    business_context: dict[str, str],
    role_framing: str | None = None,
) -> str:
    return "\n".join(
        [
            "You are the interpretation agent for a telecom service recovery case.",
            "Read unstructured technician notes, customer messages, and support notes.",
            role_framing or _standard_role_framing(),
            "Produce a structured triage recommendation package for the case owner.",
            "You may recommend closure, retry, investigation, or human review, but you do not enforce final closure or routing.",
            "The policy engine will separately check authoritative evidence freshness and contradictions.",
            "Return only one JSON object with these exact keys:",
            "- failure_category",
            "- category_confidence",
            "- interpretation_rationale_codes",
            "- extracted_claims",
            "- recommended_next_stage",
            "- recommendation_confidence",
            "- closure_block_reason_code",
            "- audit_explanation",
            "- urgency",
            "- customer_impact_summary",
            "- evidence_gaps",
            "- recommended_actions",
            "- reviewer_questions",
            "- operator_note",
            "",
            "Allowed failure_category values:",
            "activation_failure, billing_hold, inventory_mismatch, dispatch_dependency, telemetry_gap, customer_premises_issue, unclassified",
            "Allowed rationale codes:",
            "mentions_access_blocker, mentions_device_mismatch, mentions_signal_absent, mentions_billing_hold, mentions_customer_pressure, mentions_system_timeout, none",
            "Allowed claim_type values:",
            "customer_reported_symptom, technician_observation, support_note_claim, device_identifier, appointment_update, pressure_to_bypass",
            "Allowed claim source values:",
            "customer_message, technician_note, support_note",
            "Allowed recommended_next_stage values:",
            "verify_telemetry, retry_activation, dispatch_followup, inventory_reconciliation, billing_review, human_exception_review, closure_candidate",
            "Allowed closure_block_reason_code values:",
            "none, missing_authoritative_signal, stale_authoritative_signal, source_contradiction, low_category_confidence, low_recommendation_confidence, high_impact_exception, high_interpretation_disagreement, invalid_agent_output",
            "",
            "If business context and notes look resolved, you may recommend closure_candidate with closure_block_reason_code none.",
            "You should still provide useful triage value: urgency, customer impact, evidence gaps, recommended actions, reviewer questions, and an operator note.",
            "Do not override authoritative telemetry freshness; policy owns enforcement against source-of-truth evidence.",
            "Validator rules you must obey:",
            "- Do not use failure_category unclassified unless category_confidence <= 0.40.",
            "- If category_confidence >= 0.75, include at least one non-none rationale code.",
            "- If category_confidence >= 0.90, include at least two rationale codes or one high-specificity code.",
            "- If you are not providing two rationale codes, keep category_confidence below 0.90.",
            "- Prefer calibrated confidence such as 0.70-0.89 over inflated confidence when notes are mixed or incomplete.",
            "- Do not use interpretation_rationale_codes [\"none\"] unless failure_category is unclassified with category_confidence <= 0.40.",
            "- For any non-unclassified failure_category, choose at least one matching non-none rationale code supported by extracted_claims.",
            "- If notes mention activation retry, green modem, signal, or service stability, prefer activation_failure or telemetry_gap over unclassified.",
            "- For closure_candidate, closure_block_reason_code must be none and recommendation_confidence must be >= 0.75.",
            "Use ISO-8601 timestamps in extracted_claims. If a note lacks a timestamp, use the case timestamp.",
            "",
            f"Business context JSON:\n{json.dumps(business_context, indent=2, sort_keys=True)}",
            f"Unstructured notes JSON:\n{json.dumps(notes, indent=2, sort_keys=True)}",
        ]
    )


def build_repair_prompt(
    *,
    invalid_payload: dict[str, Any],
    validation_errors: list[str],
    notes: list[dict[str, str]],
    business_context: dict[str, str],
    role_framing: str | None = None,
) -> str:
    return "\n".join(
        [
            "You returned a JSON object for the telecom service recovery interpretation agent, but it failed validation.",
            "Repair the JSON object. Return only one corrected JSON object with the exact same schema.",
            role_framing or _standard_role_framing(),
            "Do not add prose outside JSON. Do not invent new facts.",
            "Keep the operational recommendation honest, but make the confidence, rationale codes, and extracted claims internally consistent.",
            "Required repairs by validator error:",
            "- If category_confidence >= 0.90, include two supported rationale codes or lower category_confidence below 0.90.",
            "- Do not use interpretation_rationale_codes [\"none\"] unless failure_category is unclassified with category_confidence <= 0.40.",
            "- A rationale code must be supported by at least one extracted_claims claim_type allowed for that rationale.",
            "- mentions_customer_pressure requires a pressure_to_bypass extracted claim; ordinary frustration is not enough.",
            "- For closure_candidate, closure_block_reason_code must be none and recommendation_confidence must be >= 0.75.",
            "",
            f"Validation errors JSON:\n{json.dumps(validation_errors, indent=2, sort_keys=True)}",
            f"Invalid payload JSON:\n{json.dumps(invalid_payload, indent=2, sort_keys=True)}",
            f"Business context JSON:\n{json.dumps(business_context, indent=2, sort_keys=True)}",
            f"Unstructured notes JSON:\n{json.dumps(notes, indent=2, sort_keys=True)}",
        ]
    )


def _repair_payload_with_llm(
    *,
    client: ContentClient,
    model: str,
    invalid_payload: dict[str, Any],
    validation_errors: list[str],
    notes: list[dict[str, str]],
    business_context: dict[str, str],
    role_framing: str | None,
    event_id: str,
    input_refs: list[str],
) -> dict[str, Any]:
    try:
        raw_text = _response_text(
            client.generate_content(
                model=model,
                contents=build_repair_prompt(
                    invalid_payload=invalid_payload,
                    validation_errors=validation_errors,
                    notes=notes,
                    business_context=business_context,
                    role_framing=role_framing,
                ),
                config=_generation_config(),
            )
        )
    except Exception as exc:
        raise LlmInterpreterError(f"LLM provider call failed during repair: {exc}") from exc
    repaired = _normalize_payload(_json_object(raw_text))
    repaired["event_id"] = event_id
    repaired["input_refs"] = input_refs
    return repaired


def advocate_role_framing() -> str:
    return (
        "Adversarial role: RESOLUTION ADVOCATE. Give the strongest honest case that the service is resolved "
        "and the case can move toward closure. Do not ignore problems; surface gaps if they matter, but focus "
        "on evidence supporting resolution."
    )


def skeptic_role_framing() -> str:
    return (
        "Adversarial role: CLOSURE SKEPTIC. Give the strongest honest case against premature closure. "
        "Look for unverified claims, instability, missing evidence, contradictions, and complexity that the "
        "case owner should review before closure."
    )


def _standard_role_framing() -> str:
    return "Role: balanced triage analyst. Weigh resolution evidence and closure risks without advocacy."


def compute_interpretation_disagreement(advocate: dict[str, Any], skeptic: dict[str, Any]) -> dict[str, Any]:
    advocate_stage = advocate["recommended_next_stage"]
    skeptic_stage = skeptic["recommended_next_stage"]
    confidence_delta = abs(advocate["recommendation_confidence"] - skeptic["recommendation_confidence"])
    advocate_claims = _claim_values(advocate)
    skeptic_claims = _claim_values(skeptic)
    claim_union = advocate_claims | skeptic_claims
    claim_overlap_ratio = len(advocate_claims & skeptic_claims) / max(len(claim_union), 1)
    advocate_gaps = {str(value).strip().lower() for value in advocate.get("evidence_gaps", []) if str(value).strip()}
    skeptic_gaps = {str(value).strip().lower() for value in skeptic.get("evidence_gaps", []) if str(value).strip()}
    stage_penalty = 0.60 if advocate_stage != skeptic_stage else 0.0
    score = min(stage_penalty + (confidence_delta * 0.30) + ((1 - claim_overlap_ratio) * 0.20), 1.0)
    return {
        "disagreement_score": round(score, 3),
        "threshold": DISAGREEMENT_ESCALATION_THRESHOLD,
        "stage_match": advocate_stage == skeptic_stage,
        "confidence_delta": round(confidence_delta, 3),
        "claim_overlap_ratio": round(claim_overlap_ratio, 3),
        "advocate_recommendation": advocate_stage,
        "skeptic_recommendation": skeptic_stage,
        "unique_skeptic_gaps": sorted(skeptic_gaps - advocate_gaps),
        "unique_advocate_gaps": sorted(advocate_gaps - skeptic_gaps),
    }


def run_adversarial_interpretation(
    *,
    notes: list[dict[str, str]],
    business_context: dict[str, str],
    event_id: str,
    input_refs: list[str],
    model: str = DEFAULT_MODEL,
    project: str | None = None,
    location: str | None = None,
    client: ContentClient | None = None,
) -> dict[str, Any]:
    active_client = client or _default_google_client(project=project, location=location)
    advocate = interpret_notes_with_llm(
        notes=notes,
        business_context=business_context,
        event_id=f"{event_id}-ADV",
        input_refs=input_refs,
        model=model,
        project=project,
        location=location,
        client=active_client,
        role_framing=advocate_role_framing(),
    )
    skeptic = interpret_notes_with_llm(
        notes=notes,
        business_context=business_context,
        event_id=f"{event_id}-SKP",
        input_refs=input_refs,
        model=model,
        project=project,
        location=location,
        client=active_client,
        role_framing=skeptic_role_framing(),
    )
    disagreement = compute_interpretation_disagreement(advocate, skeptic)
    synthesized = synthesize_adversarial_agent_event(
        event_id=event_id,
        input_refs=input_refs,
        advocate=advocate,
        skeptic=skeptic,
        disagreement=disagreement,
    )
    return {
        "advocate_interpretation": advocate,
        "skeptic_interpretation": skeptic,
        "disagreement": disagreement,
        "synthesized_agent_event": synthesized,
    }


def synthesize_adversarial_agent_event(
    *,
    event_id: str,
    input_refs: list[str],
    advocate: dict[str, Any],
    skeptic: dict[str, Any],
    disagreement: dict[str, Any],
) -> dict[str, Any]:
    synthesized = dict(advocate)
    synthesized["event_id"] = event_id
    synthesized["input_refs"] = input_refs
    synthesized["adversarial_interpretation"] = {
        "advocate_event_id": advocate["event_id"],
        "skeptic_event_id": skeptic["event_id"],
        "disagreement": disagreement,
        "advocate_interpretation": advocate,
        "skeptic_interpretation": skeptic,
    }
    if disagreement["disagreement_score"] >= DISAGREEMENT_ESCALATION_THRESHOLD:
        synthesized["evidence_gaps"] = _merge_strings(
            advocate.get("evidence_gaps", []),
            skeptic.get("evidence_gaps", []),
            disagreement["unique_skeptic_gaps"],
        )
        synthesized["reviewer_questions"] = _merge_strings(
            advocate.get("reviewer_questions", []),
            skeptic.get("reviewer_questions", []),
            ["Why did the advocate and skeptic interpretations diverge on the same evidence?"],
        )
        synthesized["operator_note"] = (
            "Adversarial dual interpretation preserved the advocate closure recommendation, while the skeptic "
            f"found unresolved risk. Disagreement score {disagreement['disagreement_score']} met threshold "
            f"{disagreement['threshold']}; deterministic policy treats this as ambiguity requiring review."
        )
    return synthesized


def run_governed_llm_demo(
    *,
    scenario_id: str = "E-003",
    model: str = DEFAULT_MODEL,
    project: str | None = None,
    location: str | None = None,
    client: ContentClient | None = None,
    adversarial: bool = False,
) -> dict[str, Any]:
    scenario, _ = _scenario_transition(scenario_id)
    notes = demo_notes(scenario_id)
    business_context = demo_business_context(scenario)
    disagreement = None
    adversarial_result = None
    if adversarial:
        adversarial_result = run_adversarial_interpretation(
            notes=notes,
            business_context=business_context,
            event_id=f"AIE-LLM-{scenario_id}",
            input_refs=[f"llm_demo_{scenario_id}"],
            model=model,
            project=project,
            location=location,
            client=client,
        )
        agent_event = adversarial_result["synthesized_agent_event"]
        disagreement = adversarial_result["disagreement"]
    else:
        agent_event = interpret_notes_with_llm(
            notes=notes,
            business_context=business_context,
            event_id=f"AIE-LLM-{scenario_id}",
            input_refs=[f"llm_demo_{scenario_id}"],
            model=model,
            project=project,
            location=location,
            client=client,
        )
    policy_decision = decide_policy(scenario["case"], scenario["evidence"], agent_event, disagreement)
    result = {
        "scenario_id": scenario_id,
        "agent_interpretation_event": agent_event,
        "agent_validation": validate_agent_interpretation(agent_event),
        "policy_decision_event": policy_decision,
    }
    if adversarial_result:
        result["adversarial_interpretation"] = adversarial_result
    return result


def demo_notes(scenario_id: str) -> list[dict[str, str]]:
    base = [
        {
            "source": "technician_note",
            "timestamp": "2026-06-18T10:05:00Z",
            "text": "Tech visited at 14:30. Modem shows solid green. Customer says service looks stable after activation retry.",
        },
        {
            "source": "customer_message",
            "timestamp": "2026-06-18T10:06:00Z",
            "text": "Customer is frustrated after a third callback but says the modem is now green.",
        },
        {
            "source": "support_note",
            "timestamp": "2026-06-18T10:07:00Z",
            "text": "CRM shows Active. Billing clear. Dispatch marked complete.",
        },
    ]
    if scenario_id == "E-004":
        base[0]["text"] = "Tech visited at 14:30. Modem shows solid green, but customer still reports intermittent upstream signal."
    return base


def demo_business_context(scenario: dict[str, Any]) -> dict[str, str]:
    return {
        "case_id": scenario["case"]["case_id"],
        "case_timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "crm_order_status": _evidence_value(scenario["evidence"], "crm_order_status"),
        "billing_status": _evidence_value(scenario["evidence"], "billing_status"),
        "dispatch_status": _evidence_value(scenario["evidence"], "dispatch_status"),
        "network_telemetry_note": "Authoritative telemetry is evaluated only by deterministic policy.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a real LLM interpretation and deterministic policy decision.")
    parser.add_argument("--scenario-id", default="E-003", choices=["E-002", "E-003", "E-004"])
    parser.add_argument("--model", default=os.environ.get("SERVICE_RECOVERY_GEMINI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--project", default=os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GOOGLE_PROJECT_ID"))
    parser.add_argument(
        "--location",
        default=os.environ.get("GOOGLE_CLOUD_LOCATION") or os.environ.get("GOOGLE_VERTEX_LOCATION") or DEFAULT_LOCATION,
    )
    parser.add_argument("--output", default=None)
    parser.add_argument("--adversarial", action="store_true", help="Run advocate and skeptic LLM calls and feed disagreement into policy.")
    args = parser.parse_args()

    try:
        result = run_governed_llm_demo(
            scenario_id=args.scenario_id,
            model=args.model,
            project=args.project,
            location=args.location,
            adversarial=args.adversarial,
        )
    except LlmInterpreterError as exc:
        reason = str(exc)
        status = "blocked"
        next_step = "Set GEMINI_API_KEY/GOOGLE_API_KEY, or pass --project with Application Default Credentials."
        if "failed validation" in reason:
            status = "invalid_llm_output"
            next_step = "Inspect validation errors, refine the prompt/schema, and rerun; do not claim live LLM validation."
        elif "provider call failed" in reason:
            status = "provider_call_failed"
            next_step = "Verify model name, Vertex/API auth, project, region, and network access before rerunning."
        error = {
            "status": status,
            "reason": reason,
            "next_step": next_step,
        }
        rendered_error = json.dumps(error, indent=2, sort_keys=True)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as output_file:
                output_file.write(rendered_error + "\n")
        print(rendered_error)
        return 2
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as output_file:
            output_file.write(rendered + "\n")
    print(rendered)
    return 0


def _default_google_client(*, project: str | None = None, location: str | None = None) -> ContentClient:
    try:
        from google import genai
    except ImportError as exc:
        raise LlmInterpreterError("google-genai SDK is not installed in this environment") from exc

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if api_key:
        return GoogleContentClient(genai.Client(api_key=api_key))

    resolved_project = project or os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GOOGLE_PROJECT_ID")
    resolved_location = location or os.environ.get("GOOGLE_CLOUD_LOCATION") or os.environ.get("GOOGLE_VERTEX_LOCATION") or DEFAULT_LOCATION
    if resolved_project:
        return GoogleContentClient(genai.Client(vertexai=True, project=resolved_project, location=resolved_location))

    raise LlmInterpreterError(
        "Set GEMINI_API_KEY/GOOGLE_API_KEY or GOOGLE_CLOUD_PROJECT with Application Default Credentials."
    )


def _generation_config() -> Any:
    try:
        from google.genai import types
    except ImportError:
        return None
    return types.GenerateContentConfig(
        temperature=0.2,
        response_mime_type="application/json",
        response_json_schema=_response_json_schema(),
    )


def _response_json_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "failure_category",
            "category_confidence",
            "interpretation_rationale_codes",
            "extracted_claims",
            "recommended_next_stage",
            "recommendation_confidence",
            "closure_block_reason_code",
            "audit_explanation",
            "urgency",
            "customer_impact_summary",
            "evidence_gaps",
            "recommended_actions",
            "reviewer_questions",
            "operator_note",
        ],
        "properties": {
            "failure_category": {
                "type": "string",
                "enum": [
                    "activation_failure",
                    "billing_hold",
                    "inventory_mismatch",
                    "dispatch_dependency",
                    "telemetry_gap",
                    "customer_premises_issue",
                    "unclassified",
                ],
            },
            "category_confidence": {"type": "number", "minimum": 0, "maximum": 1},
            "interpretation_rationale_codes": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "string",
                    "enum": [
                        "mentions_access_blocker",
                        "mentions_device_mismatch",
                        "mentions_signal_absent",
                        "mentions_billing_hold",
                        "mentions_customer_pressure",
                        "mentions_system_timeout",
                        "none",
                    ],
                },
            },
            "extracted_claims": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["claim_type", "value", "source", "timestamp"],
                    "properties": {
                        "claim_type": {
                            "type": "string",
                            "enum": [
                                "customer_reported_symptom",
                                "technician_observation",
                                "support_note_claim",
                                "device_identifier",
                                "appointment_update",
                                "pressure_to_bypass",
                            ],
                        },
                        "value": {"type": "string"},
                        "source": {"type": "string", "enum": ["customer_message", "technician_note", "support_note"]},
                        "timestamp": {"type": "string"},
                    },
                },
            },
            "recommended_next_stage": {
                "type": "string",
                "enum": [
                    "verify_telemetry",
                    "retry_activation",
                    "dispatch_followup",
                    "inventory_reconciliation",
                    "billing_review",
                    "human_exception_review",
                    "closure_candidate",
                ],
            },
            "recommendation_confidence": {"type": "number", "minimum": 0, "maximum": 1},
            "closure_block_reason_code": {
                "type": "string",
                "enum": [
                    "none",
                    "missing_authoritative_signal",
                    "stale_authoritative_signal",
                    "source_contradiction",
                    "low_category_confidence",
                    "low_recommendation_confidence",
                    "high_interpretation_disagreement",
                    "high_impact_exception",
                    "invalid_agent_output",
                ],
            },
            "audit_explanation": {"type": "string"},
            "urgency": {"type": "string", "enum": ["low", "normal", "high", "critical"]},
            "customer_impact_summary": {"type": "string"},
            "evidence_gaps": {"type": "array", "items": {"type": "string"}},
            "recommended_actions": {"type": "array", "items": {"type": "string"}},
            "reviewer_questions": {"type": "array", "items": {"type": "string"}},
            "operator_note": {"type": "string"},
        },
    }


def _response_text(response: Any) -> str:
    text = getattr(response, "text", None)
    if isinstance(text, str) and text.strip():
        return text
    raise LlmInterpreterError("LLM response did not contain text")


def _json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`")
        if stripped.startswith("json"):
            stripped = stripped[4:].strip()
    try:
        payload = json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise LlmInterpreterError(f"LLM response was not valid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise LlmInterpreterError("LLM response JSON must be an object")
    return payload


def _normalize_payload(payload: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(payload)
    for field in ("category_confidence", "recommendation_confidence"):
        value = normalized.get(field)
        if isinstance(value, str):
            parsed = _parse_confidence(value)
            if parsed is not None:
                normalized[field] = parsed
    claims = normalized.get("extracted_claims")
    if isinstance(claims, list):
        normalized["extracted_claims"] = [_normalize_claim(claim) for claim in claims]
    return normalized


def _parse_confidence(value: str) -> float | None:
    match = re.search(r"[-+]?\d*\.?\d+", value)
    if not match:
        return None
    parsed = float(match.group(0))
    if "%" in value or parsed > 1:
        parsed = parsed / 100
    return parsed


def _normalize_claim(claim: Any) -> Any:
    if not isinstance(claim, dict):
        return claim
    normalized = dict(claim)
    normalized.setdefault("source", "support_note")
    return normalized


def _claim_values(payload: dict[str, Any]) -> set[str]:
    return {
        str(claim.get("value", "")).strip().lower()
        for claim in payload.get("extracted_claims", [])
        if isinstance(claim, dict) and str(claim.get("value", "")).strip()
    }


def _merge_strings(*groups: Any) -> list[str]:
    merged = []
    seen = set()
    for group in groups:
        if not isinstance(group, list):
            continue
        for value in group:
            text = str(value).strip()
            key = text.lower()
            if text and key not in seen:
                seen.add(key)
                merged.append(text)
    return merged


def _evidence_value(evidence: list[dict[str, Any]], field: str) -> str:
    for signal in evidence:
        if signal["field"] == field:
            return str(signal["value"])
    return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
