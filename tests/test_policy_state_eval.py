import unittest

from service_recovery_core.evals import build_policy_improvement_artifact_for_scenario, run_eval_suite
from service_recovery_core.fixtures import scenario
from service_recovery_core.policy import decide_policy, reconcile_evidence
from service_recovery_core.state_machine import apply_policy_decision


class PolicyStateEvalTests(unittest.TestCase):
    def test_reconciles_all_evidence_states(self):
        expected_states = {
            "E-001": "confirmed_aligned",
            "E-002": "missing_pending",
            "E-003": "authoritative_unavailable_or_stale",
            "E-004": "contradicting",
        }
        for scenario_id, expected in expected_states.items():
            with self.subTest(scenario_id=scenario_id):
                result = reconcile_evidence(scenario(scenario_id)["evidence"])
                self.assertEqual(result["derived_evidence_state"], expected)

    def test_business_green_variants_only_change_telemetry(self):
        baseline = _evidence_by_field(scenario("E-002")["evidence"])
        for scenario_id in ("E-003", "E-004", "E-009"):
            variant = _evidence_by_field(scenario(scenario_id)["evidence"])
            with self.subTest(scenario_id=scenario_id):
                for field in ("crm_order_status", "billing_status", "inventory_assignment", "dispatch_status"):
                    self.assertEqual(variant[field], baseline[field])
                if scenario_id == "E-009":
                    self.assertEqual(variant["service_live_status"], baseline["service_live_status"])
                else:
                    self.assertNotEqual(variant["service_live_status"], baseline["service_live_status"])

    def test_closure_requires_fresh_authoritative_telemetry(self):
        missing = scenario("E-002")
        decision = decide_policy(missing["case"], missing["evidence"], missing["agent_interpretation"])
        self.assertFalse(decision["closure_allowed"])
        self.assertEqual(decision["decision"], "override_recommendation")
        self.assertIn("missing_authoritative_signal", decision["reason_codes"])
        self.assertEqual(decision["to_stage"], "verify_telemetry")

    def test_missing_and_contradiction_route_differently(self):
        missing = scenario("E-002")
        contradiction = scenario("E-004")
        missing_decision = decide_policy(missing["case"], missing["evidence"], missing["agent_interpretation"])
        contradiction_decision = decide_policy(
            contradiction["case"],
            contradiction["evidence"],
            contradiction["agent_interpretation"],
        )
        self.assertEqual(missing_decision["to_stage"], "verify_telemetry")
        self.assertEqual(contradiction_decision["to_stage"], "human_review")
        self.assertEqual(contradiction_decision["severity"], "elevated")

    def test_non_closure_agent_route_does_not_allow_closure(self):
        fixture = scenario("E-005")
        decision = decide_policy(fixture["case"], fixture["evidence"], fixture["agent_interpretation"])
        self.assertFalse(decision["closure_allowed"])
        self.assertEqual(decision["to_stage"], "dispatch_followup")
        self.assertIn("high_impact_exception", decision["reason_codes"])

    def test_agent_and_policy_events_persist_separately(self):
        fixture = scenario("E-009")
        policy_decision = decide_policy(
            fixture["case"],
            fixture["evidence"],
            fixture["agent_interpretation"],
        )
        transition = apply_policy_decision(
            fixture["case"],
            fixture["agent_interpretation"],
            policy_decision,
            event_id="PDE-E009",
        )
        self.assertEqual(transition["agent_event"]["recommended_next_stage"], "closure_candidate")
        self.assertEqual(transition["policy_event"]["agent_event_id"], "AIE-E009")
        self.assertEqual(transition["policy_event"]["decision"], "override_recommendation")
        self.assertEqual(transition["policy_event"]["from_recommended_stage"], "closure_candidate")
        self.assertEqual(transition["policy_event"]["to_stage"], "verify_telemetry")

    def test_eval_suite_passes(self):
        result = run_eval_suite()
        self.assertEqual(result["summary"]["failed"], 0, result)
        e008 = next(item for item in result["results"] if item["scenario_id"] == "E-008")
        self.assertEqual(e008["usefulness_incident"]["incident_type"], "agent_usefulness_degradation")
        artifact = e008["policy_improvement_artifact"]
        self.assertEqual(artifact["artifact_type"], "policy_improvement_case")
        self.assertEqual(artifact["trigger"], "low_confidence_despite_sufficient_signal")
        self.assertTrue(artifact["eval_result"]["passed"])
        self.assertEqual(artifact["approval_status"], "pending_human_approval")
        self.assertEqual(artifact["promotion_status"], "not_promoted")
        self.assertEqual(
            artifact["active_case_policy_version_action"],
            "active_cases_remain_pinned_until_explicit_migration_event",
        )

    def test_policy_improvement_artifact_is_proposal_only(self):
        artifact = build_policy_improvement_artifact_for_scenario("E-008")
        self.assertEqual(artifact["current_policy_version"]["decision_policy_version"], "dp-v1")
        self.assertEqual(artifact["proposed_next_version"]["decision_policy_version"], "dp-v1")
        self.assertEqual(artifact["proposed_next_version"]["interpretation_policy_version"], "ip-v2-proposed")
        self.assertIn("auto_promote_policy", artifact["forbidden_actions"])

def _evidence_by_field(evidence):
    return {
        signal["field"]: {
            "source": signal["source"],
            "value": signal["value"],
            "authoritative": signal["authoritative"],
            "freshness_status": signal["freshness_status"],
        }
        for signal in evidence
    }


if __name__ == "__main__":
    unittest.main()
