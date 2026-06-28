import json
import unittest
from pathlib import Path

from service_recovery_core.evals import build_llm_result_evidence_packet_html
from service_recovery_core.llm_interpreter import (
    LlmInterpreterError,
    compute_interpretation_disagreement,
    interpret_notes_with_llm,
    run_adversarial_interpretation,
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


class SequenceFakeModels:
    def __init__(self, payloads):
        self.payloads = list(payloads)
        self.prompts = []

    def generate_content(self, *, model, contents, config=None):
        self.prompts.append(contents)
        return FakeResponse(json.dumps(self.payloads.pop(0)))


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

    def test_repairs_live_observed_none_rationale_drift(self):
        invalid = _valid_llm_payload()
        invalid["interpretation_rationale_codes"] = ["none"]
        repaired = _valid_llm_payload()
        client = SequenceFakeModels([invalid, repaired])

        event = interpret_notes_with_llm(
            notes=[],
            business_context={"case_id": "CASE-BG-STALE"},
            event_id="AIE-REPAIRED",
            input_refs=["repair_demo"],
            client=client,
        )

        self.assertEqual(len(client.prompts), 2)
        self.assertIn("failed validation", client.prompts[1])
        self.assertIn("none rationale requires low confidence", client.prompts[1])
        self.assertEqual(event["interpretation_rationale_codes"], ["mentions_signal_absent"])

    def test_repairs_live_observed_unsupported_customer_pressure_drift(self):
        invalid = _valid_llm_payload()
        invalid["category_confidence"] = 0.91
        invalid["interpretation_rationale_codes"] = ["mentions_customer_pressure"]
        repaired = _valid_llm_payload()
        repaired["category_confidence"] = 0.82
        client = SequenceFakeModels([invalid, repaired])

        event = interpret_notes_with_llm(
            notes=[],
            business_context={"case_id": "CASE-BG-STALE"},
            event_id="AIE-REPAIRED-PRESSURE",
            input_refs=["repair_demo"],
            client=client,
        )

        self.assertEqual(len(client.prompts), 2)
        self.assertIn("mentions_customer_pressure requires a pressure_to_bypass extracted claim", client.prompts[1])
        self.assertEqual(event["category_confidence"], 0.82)

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

    def test_computes_interpretation_disagreement(self):
        advocate = _valid_llm_payload()
        skeptic = _skeptic_payload()

        disagreement = compute_interpretation_disagreement(advocate, skeptic)

        self.assertGreaterEqual(disagreement["disagreement_score"], 0.60)
        self.assertFalse(disagreement["stage_match"])
        self.assertEqual(disagreement["advocate_recommendation"], "closure_candidate")
        self.assertEqual(disagreement["skeptic_recommendation"], "human_exception_review")
        self.assertIn("confirm upstream signal stability", disagreement["unique_skeptic_gaps"])

    def test_adversarial_disagreement_escalates_policy_to_human_review(self):
        client = SequenceFakeModels([_valid_llm_payload(), _skeptic_payload()])

        result = run_governed_llm_demo(scenario_id="E-001", client=client, adversarial=True)

        self.assertEqual(len(client.prompts), 2)
        self.assertIn("RESOLUTION ADVOCATE", client.prompts[0])
        self.assertIn("CLOSURE SKEPTIC", client.prompts[1])
        self.assertTrue(result["agent_validation"]["valid"], result["agent_validation"]["errors"])
        self.assertGreaterEqual(result["adversarial_interpretation"]["disagreement"]["disagreement_score"], 0.60)
        self.assertEqual(result["policy_decision_event"]["decision"], "require_human_review")
        self.assertEqual(result["policy_decision_event"]["to_stage"], "human_review")
        self.assertIn("high_interpretation_disagreement", result["policy_decision_event"]["reason_codes"])

    def test_adversarial_mode_repairs_each_role_before_disagreement(self):
        invalid_advocate = _valid_llm_payload()
        invalid_advocate["interpretation_rationale_codes"] = ["none"]
        client = SequenceFakeModels([invalid_advocate, _valid_llm_payload(), _skeptic_payload()])

        result = run_governed_llm_demo(scenario_id="E-001", client=client, adversarial=True)

        self.assertEqual(len(client.prompts), 3)
        self.assertIn("failed validation", client.prompts[1])
        self.assertTrue(result["agent_validation"]["valid"], result["agent_validation"]["errors"])
        self.assertEqual(result["policy_decision_event"]["to_stage"], "human_review")

    def test_adversarial_trace_reaches_audit_and_packet(self):
        fixture = scenario("E-001")
        result = run_adversarial_interpretation(
            notes=[],
            business_context={"case_id": "CASE-E001"},
            event_id="AIE-ADV",
            input_refs=["adversarial_demo"],
            client=SequenceFakeModels([_valid_llm_payload(), _skeptic_payload()]),
        )
        policy_decision = decide_policy(
            fixture["case"],
            fixture["evidence"],
            result["synthesized_agent_event"],
            result["disagreement"],
        )
        transition = apply_policy_decision(
            fixture["case"],
            result["synthesized_agent_event"],
            policy_decision,
            event_id="PDE-ADV",
        )
        audit_bundle = build_case_audit_bundle(fixture["case"], fixture["evidence"], transition)
        html = render_evidence_packet_html(audit_bundle)

        self.assertIn("adversarial_interpretation", audit_bundle["agent_interpretation_event"])
        self.assertIn("Adversarial dual interpretation", html)
        self.assertIn("Resolution advocate", html)
        self.assertIn("Closure skeptic", html)
        self.assertIn("high_interpretation_disagreement", html)
        self.assertIn("Closure readiness checklist", html)
        self.assertIn("Advocate/skeptic interpretation disagreement is resolved", html)
        self.assertIn("Resolve skeptic-only gap before closure", html)

    def test_live_adversarial_artifact_renders_packet(self):
        artifact_path = Path("docs/demo/artifacts/llm_interpreter_E003_adversarial_live.json")

        html = build_llm_result_evidence_packet_html(artifact_path)

        self.assertIn("Adversarial dual interpretation", html)
        self.assertIn("Resolution advocate", html)
        self.assertIn("Closure skeptic", html)
        self.assertIn("Disagreement score", html)
        self.assertIn("closure_candidate -> human_review", html)
        self.assertIn("high_interpretation_disagreement", html)
        self.assertIn("Closure readiness checklist", html)
        self.assertIn("Which interpretation is supported by authoritative evidence", html)


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


def _skeptic_payload():
    payload = _valid_llm_payload()
    payload.update(
        {
            "failure_category": "telemetry_gap",
            "category_confidence": 0.82,
            "interpretation_rationale_codes": ["mentions_signal_absent", "mentions_system_timeout"],
            "recommended_next_stage": "human_exception_review",
            "recommendation_confidence": 0.41,
            "closure_block_reason_code": "stale_authoritative_signal",
            "audit_explanation": "The green modem note is not enough because the customer had repeated callbacks and upstream stability is unverified.",
            "urgency": "high",
            "evidence_gaps": ["Confirm upstream signal stability", "Verify fresh authoritative telemetry"],
            "recommended_actions": ["Escalate for human review before closure."],
            "reviewer_questions": ["Did the upstream signal remain stable after the technician left?"],
            "operator_note": "Skeptic interpretation found unresolved signal-risk language in the same evidence.",
        }
    )
    payload["extracted_claims"] = [
        {
            "claim_type": "customer_reported_symptom",
            "value": "Customer is frustrated after a third callback.",
            "source": "customer_message",
            "timestamp": "2026-06-18T10:06:00Z",
        },
        {
            "claim_type": "technician_observation",
            "value": "Upstream signal stability is not confirmed.",
            "source": "technician_note",
            "timestamp": "2026-06-18T10:05:00Z",
        },
    ]
    return payload


if __name__ == "__main__":
    unittest.main()
