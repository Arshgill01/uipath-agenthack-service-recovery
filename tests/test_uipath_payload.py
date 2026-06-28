import json
import unittest

from service_recovery_core.fixtures import scenario
from service_recovery_core.evals import build_uipath_payload
from service_recovery_core.policy import decide_policy
from service_recovery_core.state_machine import apply_policy_decision
from service_recovery_core.uipath_payload import build_action_center_payload


class UiPathPayloadTests(unittest.TestCase):
    def test_missing_telemetry_payload_preserves_raw_agent_and_policy_override(self):
        fixture = scenario("E-002")
        decision = decide_policy(fixture["case"], fixture["evidence"], fixture["agent_interpretation"])
        transition = apply_policy_decision(
            fixture["case"],
            fixture["agent_interpretation"],
            decision,
            event_id="PDE-E002",
        )

        payload = build_action_center_payload(fixture["case"], fixture["evidence"], transition)

        raw_agent = json.loads(payload["RawAgentRecommendation"])
        policy_decision = json.loads(payload["PolicyDecisionJson"])
        evidence_packet = json.loads(payload["EvidencePacketJson"])

        self.assertEqual(raw_agent["event_type"], "AgentInterpretationEvent")
        self.assertEqual(raw_agent["recommended_next_stage"], "closure_candidate")
        self.assertEqual(raw_agent["interpretation_policy_version"], "ip-v1")
        self.assertEqual(policy_decision["event_type"], "PolicyDecisionEvent")
        self.assertEqual(policy_decision["links_to"], raw_agent["event_id"])
        self.assertEqual(policy_decision["decision"], "override_recommendation")
        self.assertEqual(policy_decision["from_recommended_stage"], "closure_candidate")
        self.assertEqual(policy_decision["to_stage"], "verify_telemetry")
        self.assertEqual(policy_decision["block_reason"], "missing_authoritative_signal")
        self.assertEqual(policy_decision["decision_policy_version"], "dp-v1")
        self.assertEqual(evidence_packet["business_state"], "green")
        self.assertEqual(evidence_packet["closure_block_reason"], "missing_authoritative_signal")
        self.assertIn("retry_telemetry", evidence_packet["recommended_options"])
        self.assertIn("closure_readiness_checklist", evidence_packet)
        self.assertIn("reviewer_questions", evidence_packet)
        self.assertIn(
            "Which authoritative telemetry retry or source will produce service_live_status before closure?",
            evidence_packet["reviewer_questions"],
        )
        network_check = evidence_packet["closure_readiness_checklist"][0]
        self.assertEqual(network_check["criterion"], "Fresh authoritative telemetry confirms service is live")
        self.assertEqual(network_check["status"], "blocked")
        self.assertIn("No authoritative network telemetry signal", network_check["evidence"])
        self.assertIn("closure is blocked by missing_authoritative_signal", payload["Content"])

    def test_contradiction_payload_routes_to_human_review(self):
        fixture = scenario("E-004")
        decision = decide_policy(fixture["case"], fixture["evidence"], fixture["agent_interpretation"])
        transition = apply_policy_decision(
            fixture["case"],
            fixture["agent_interpretation"],
            decision,
            event_id="PDE-E004",
        )

        payload = build_action_center_payload(fixture["case"], fixture["evidence"], transition)
        policy_decision = json.loads(payload["PolicyDecisionJson"])

        self.assertEqual(policy_decision["decision"], "require_human_review")
        self.assertEqual(policy_decision["to_stage"], "human_review")
        self.assertEqual(policy_decision["block_reason"], "source_contradiction")
        self.assertIn("open_investigation", policy_decision["allowed_actions"])
        self.assertIn(
            "Why do business systems show active while fresh authoritative service evidence disagrees?",
            policy_decision["reviewer_questions"],
        )
        self.assertIn("Required human review has resolved the exception", [
            item["criterion"] for item in policy_decision["closure_readiness_checklist"]
        ])
        self.assertIn("fresh authoritative telemetry contradicts", payload["Content"])

    def test_eval_helper_exports_named_scenario_payload(self):
        payload = build_uipath_payload("E-002")
        self.assertEqual(set(payload), {"Content", "EvidencePacketJson", "RawAgentRecommendation", "PolicyDecisionJson", "Comment"})
        self.assertEqual(json.loads(payload["PolicyDecisionJson"])["to_stage"], "verify_telemetry")


if __name__ == "__main__":
    unittest.main()
