import json
import unittest

from service_recovery_core.llm_interpreter import (
    LlmInterpreterError,
    interpret_notes_with_llm,
    run_governed_llm_demo,
)
from service_recovery_core.audit_bundle import build_case_audit_bundle
from service_recovery_core.evidence_packet_view import render_evidence_packet_html
from service_recovery_core.fixtures import scenario
from service_recovery_core.policy import decide_policy
from service_recovery_core.state_machine import apply_policy_decision


class FakeResponse:
    def __init__(self, text):
        self.text = text


class FakeModels:
    def __init__(self, payload):
        self.payload = payload
        self.last_prompt = None

    def generate_content(self, *, model, contents, config=None):
        self.last_prompt = contents
        return FakeResponse(json.dumps(self.payload))


class LlmInterpreterTests(unittest.TestCase):
    def test_llm_output_can_include_rich_triage_package(self):
        client = FakeModels(_valid_llm_payload())

        event = interpret_notes_with_llm(
            notes=[
                {
                    "source": "technician_note",
                    "timestamp": "2026-06-18T10:05:00Z",
                    "text": "Modem green after activation retry.",
                }
            ],
            business_context={"case_id": "CASE-BG-STALE", "crm_order_status": "active"},
            event_id="AIE-LLM-E003",
            input_refs=["llm_demo_E003"],
            client=client,
        )

        self.assertEqual(event["recommended_next_stage"], "closure_candidate")
        self.assertEqual(event["urgency"], "high")
        self.assertIn("network telemetry", event["evidence_gaps"][0])
        self.assertIn("Return only one JSON object", client.last_prompt)

    def test_policy_can_override_rich_llm_closure_recommendation(self):
        result = run_governed_llm_demo(scenario_id="E-003", client=FakeModels(_valid_llm_payload()))

        self.assertTrue(result["agent_validation"]["valid"], result["agent_validation"]["errors"])
        self.assertEqual(result["agent_interpretation_event"]["recommended_next_stage"], "closure_candidate")
        self.assertEqual(result["policy_decision_event"]["decision"], "override_recommendation")
        self.assertEqual(result["policy_decision_event"]["to_stage"], "verify_telemetry")
        self.assertIn("stale_authoritative_signal", result["policy_decision_event"]["reason_codes"])

    def test_invalid_llm_output_fails_before_policy(self):
        payload = _valid_llm_payload()
        payload["recommended_next_stage"] = "close_now"

        with self.assertRaises(LlmInterpreterError):
            interpret_notes_with_llm(
                notes=[],
                business_context={"case_id": "CASE-BG-STALE"},
                event_id="AIE-BAD",
                input_refs=[],
                client=FakeModels(payload),
            )

    def test_normalizes_common_llm_schema_drift(self):
        payload = _valid_llm_payload()
        payload["category_confidence"] = "78%"
        payload["recommendation_confidence"] = "0.83 confidence"
        del payload["extracted_claims"][0]["source"]

        event = interpret_notes_with_llm(
            notes=[],
            business_context={"case_id": "CASE-BG-STALE"},
            event_id="AIE-DRIFT",
            input_refs=[],
            client=FakeModels(payload),
        )

        self.assertEqual(event["category_confidence"], 0.78)
        self.assertEqual(event["recommendation_confidence"], 0.83)
        self.assertEqual(event["extracted_claims"][0]["source"], "support_note")

    def test_rich_llm_package_reaches_audit_and_packet(self):
        fixture = scenario("E-003")
        agent_event = dict(_valid_llm_payload(), event_id="AIE-LLM-E003", input_refs=["llm_demo_E003"])
        policy_decision = decide_policy(fixture["case"], fixture["evidence"], agent_event)
        transition = apply_policy_decision(fixture["case"], agent_event, policy_decision, event_id="PDE-LLM-E003")
        audit_bundle = build_case_audit_bundle(fixture["case"], fixture["evidence"], transition)
        html = render_evidence_packet_html(audit_bundle)

        self.assertEqual(audit_bundle["agent_interpretation_event"]["urgency"], "high")
        self.assertIn("Confirm fresh authoritative network telemetry", html)
        self.assertIn("LLM triage package", html)
        self.assertIn("override_recommendation", html)


def _valid_llm_payload():
    return {
        "failure_category": "activation_failure",
        "category_confidence": 0.78,
        "interpretation_rationale_codes": ["mentions_signal_absent"],
        "extracted_claims": [
            {
                "claim_type": "technician_observation",
                "value": "Technician reports modem is green after activation retry.",
                "source": "technician_note",
                "timestamp": "2026-06-18T10:05:00Z",
            }
        ],
        "recommended_next_stage": "closure_candidate",
        "recommendation_confidence": 0.83,
        "closure_block_reason_code": "none",
        "audit_explanation": "The notes and business systems look resolved, so the LLM recommends closure pending policy review.",
        "urgency": "high",
        "customer_impact_summary": "Third callback and frustrated customer increase service-credit and churn risk.",
        "evidence_gaps": ["Confirm fresh authoritative network telemetry before closure."],
        "recommended_actions": ["Prepare closure only if policy confirms fresh telemetry.", "Keep SLA clock active until telemetry is fresh."],
        "reviewer_questions": ["Is the latest network telemetry fresh enough for closure?"],
        "operator_note": "LLM sees a likely resolved activation, but policy must verify source-of-truth freshness.",
    }


if __name__ == "__main__":
    unittest.main()
