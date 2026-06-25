import unittest

from service_recovery_core.evals import build_audit_bundle


class AuditBundleTests(unittest.TestCase):
    def test_missing_telemetry_bundle_reconstructs_override_in_one_object(self):
        bundle = build_audit_bundle("E-002")

        self.assertEqual(bundle["audit_contract_version"], "service-recovery-audit-v1")
        self.assertEqual(bundle["evidence_state"]["business_state"], "green")
        self.assertEqual(bundle["evidence_state"]["derived_evidence_state"], "missing_pending")
        self.assertEqual(bundle["evidence_state"]["closure_block_reason"], "missing_authoritative_signal")
        self.assertEqual(bundle["policy_versions"]["interpretation_policy_version"], "ip-v1")
        self.assertEqual(bundle["policy_versions"]["decision_policy_version"], "dp-v1")
        self.assertEqual(bundle["agent_interpretation_event"]["recommended_next_stage"], "closure_candidate")
        self.assertEqual(bundle["policy_decision_event"]["decision"], "override_recommendation")
        self.assertEqual(bundle["policy_decision_event"]["links_to"], bundle["agent_interpretation_event"]["event_id"])
        self.assertEqual(bundle["policy_decision_event"]["from_recommended_stage"], "closure_candidate")
        self.assertEqual(bundle["policy_decision_event"]["to_stage"], "verify_telemetry")
        self.assertEqual(bundle["reviewer_packet"]["block_reason"], "missing_authoritative_signal")
        self.assertIn("retry_telemetry", bundle["reviewer_packet"]["recommended_options"])
        self.assertEqual(bundle["human_review_event"]["decision"], "pending")
        self.assertEqual(
            [event["event_type"] for event in bundle["events"]],
            ["EvidenceStateEvent", "AgentInterpretationEvent", "PolicyDecisionEvent", "HumanReviewEvent"],
        )

    def test_contradiction_bundle_routes_to_human_review(self):
        bundle = build_audit_bundle("E-004")

        self.assertEqual(bundle["evidence_state"]["business_state"], "green")
        self.assertEqual(bundle["evidence_state"]["derived_evidence_state"], "contradicting")
        self.assertEqual(bundle["evidence_state"]["closure_block_reason"], "source_contradiction")
        self.assertEqual(bundle["policy_decision_event"]["decision"], "require_human_review")
        self.assertEqual(bundle["policy_decision_event"]["to_stage"], "human_review")
        self.assertIn("open_investigation", bundle["reviewer_packet"]["recommended_options"])


if __name__ == "__main__":
    unittest.main()
