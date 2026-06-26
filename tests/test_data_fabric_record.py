import json
import unittest

from service_recovery_core.evals import build_audit_record


class DataFabricRecordTests(unittest.TestCase):
    def test_contradiction_record_matches_proposed_entity_shape(self):
        record = build_audit_record("E-004")

        self.assertEqual(record["case_id"], "CASE-BG-CONTRA")
        self.assertEqual(record["service_id"], "SVC-BG-1")
        self.assertEqual(record["scenario_id"], "E-004")
        self.assertEqual(record["audit_contract_version"], "service-recovery-audit-v1")
        self.assertEqual(record["business_state"], "green")
        self.assertEqual(record["derived_evidence_state"], "contradicting")
        self.assertEqual(record["closure_block_reason"], "source_contradiction")
        self.assertEqual(record["interpretation_policy_version"], "ip-v1")
        self.assertEqual(record["decision_policy_version"], "dp-v1")
        self.assertEqual(record["source_case_instance_key"], "9fc6fece-55ed-4fb2-b11a-6c96f7a3314e")
        self.assertEqual(record["source_task_id"], "4328396")
        self.assertEqual(record["package_version"], "1.0.6")

        policy = json.loads(record["policy_decision_event_json"])
        bundle = json.loads(record["audit_bundle_json"])
        self.assertEqual(policy["decision"], "require_human_review")
        self.assertEqual(policy["links_to"], "AIE-E004")
        self.assertEqual(bundle["reviewer_packet"]["block_reason"], "source_contradiction")

    def test_custom_serialize_formats_for_csv_properly(self):
        from service_recovery_core.data_fabric_record import serialize_for_data_fabric_csv

        test_obj = {
            "str_field": "hello 'world' \\ backslash",
            "bool_field": True,
            "null_field": None,
            "int_field": 42,
            "list_field": [1, "two", False],
            "dict_field": {"nested": "value"},
        }
        res = serialize_for_data_fabric_csv(test_obj)

        self.assertTrue(res.startswith("{'bool_field':true"))
        self.assertIn("'str_field':'hello \\'world\\' \\\\ backslash'", res)
        self.assertIn("'list_field':[1,'two',false]", res)
        self.assertNotIn('"', res)

    def test_data_fabric_record_with_for_csv_uses_single_quotes(self):
        from service_recovery_core.data_fabric_record import build_data_fabric_record
        from service_recovery_core.evals import build_audit_bundle

        bundle = build_audit_bundle("E-004")
        record = build_data_fabric_record(bundle, scenario_id="E-004", for_csv=True)

        for col in ["raw_agent_event_json", "policy_decision_event_json", "reviewer_packet_json", "audit_bundle_json"]:
            val = record[col]
            self.assertTrue(val.startswith("{"))
            self.assertTrue(val.endswith("}"))
            self.assertIn("'", val)
            self.assertNotIn('"', val)

    def test_default_record_keeps_parseable_json_payloads(self):
        record = build_audit_record("E-004")

        for col in ["raw_agent_event_json", "policy_decision_event_json", "reviewer_packet_json", "audit_bundle_json"]:
            self.assertIsInstance(json.loads(record[col]), dict)

    def test_pascal_record_matches_live_data_fabric_v2_shape(self):
        record = build_audit_record("E-004", field_style="pascal")

        self.assertEqual(record["CaseId"], "CASE-BG-CONTRA")
        self.assertEqual(record["ServiceId"], "SVC-BG-1")
        self.assertEqual(record["ScenarioId"], "E-004")
        self.assertEqual(record["InterpretationPolicyVersion"], "ip-v1")
        self.assertEqual(record["DecisionPolicyVersion"], "dp-v1")
        self.assertEqual(record["SourceCaseInstanceKey"], "9fc6fece-55ed-4fb2-b11a-6c96f7a3314e")
        self.assertEqual(record["SourceTaskId"], "4328396")
        self.assertEqual(record["PackageVersion"], "1.0.6")

        self.assertEqual(json.loads(record["PolicyDecisionEventJson"])["decision"], "require_human_review")
        self.assertEqual(json.loads(record["AuditBundleJson"])["policy_versions"]["decision_policy_version"], "dp-v1")

if __name__ == "__main__":
    unittest.main()
