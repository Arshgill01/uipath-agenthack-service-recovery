import copy
import unittest

from service_recovery_core.agent_validator import validate_agent_interpretation
from service_recovery_core.fixtures import scenario


class AgentValidatorTests(unittest.TestCase):
    def setUp(self):
        self.valid = scenario("E-001")["agent_interpretation"]

    def test_valid_fixture_agent_output_passes(self):
        result = validate_agent_interpretation(self.valid)
        self.assertTrue(result["valid"], result["errors"])

    def test_unclassified_high_confidence_fails(self):
        payload = copy.deepcopy(self.valid)
        payload["failure_category"] = "unclassified"
        payload["category_confidence"] = 0.95
        payload["interpretation_rationale_codes"] = ["none"]
        result = validate_agent_interpretation(payload)
        self.assertFalse(result["valid"])

    def test_closure_candidate_with_block_reason_fails(self):
        payload = copy.deepcopy(self.valid)
        payload["closure_block_reason_code"] = "missing_authoritative_signal"
        result = validate_agent_interpretation(payload)
        self.assertFalse(result["valid"])

    def test_closure_candidate_with_low_recommendation_confidence_fails(self):
        payload = copy.deepcopy(self.valid)
        payload["recommendation_confidence"] = 0.40
        result = validate_agent_interpretation(payload)
        self.assertFalse(result["valid"])

    def test_category_rationale_conflict_fails(self):
        payload = copy.deepcopy(self.valid)
        payload["failure_category"] = "billing_hold"
        payload["interpretation_rationale_codes"] = ["mentions_device_mismatch"]
        payload["extracted_claims"] = [
            {
                "claim_type": "device_identifier",
                "value": "Device serial mismatch.",
                "source": "technician_note",
                "timestamp": "2026-06-18T10:05:00Z",
            }
        ]
        result = validate_agent_interpretation(payload)
        self.assertFalse(result["valid"])

    def test_bad_enum_fails(self):
        payload = copy.deepcopy(self.valid)
        payload["recommended_next_stage"] = "close_now"
        result = validate_agent_interpretation(payload)
        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()
