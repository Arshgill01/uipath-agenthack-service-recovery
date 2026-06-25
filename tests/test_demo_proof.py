import tempfile
import unittest
from pathlib import Path

from service_recovery_core.demo_proof import build_demo_proof_artifacts, verify_demo_proof_artifacts


class DemoProofTests(unittest.TestCase):
    def test_builds_and_verifies_core_demo_artifacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)

            manifest = build_demo_proof_artifacts(output_dir)
            errors = verify_demo_proof_artifacts(output_dir)

            self.assertEqual(errors, [])
            self.assertEqual([scenario["scenario_id"] for scenario in manifest["scenarios"]], ["E-002", "E-004"])
            self.assertEqual(manifest["scenarios"][0]["decision"], "override_recommendation")
            self.assertEqual(manifest["scenarios"][0]["to_stage"], "verify_telemetry")
            self.assertEqual(manifest["scenarios"][1]["decision"], "require_human_review")
            self.assertEqual(manifest["scenarios"][1]["to_stage"], "human_review")
            self.assertTrue((output_dir / "action_payload_E002.json").exists())
            self.assertTrue((output_dir / "service_recovery_audit_bundle_E004.json").exists())
            self.assertTrue((output_dir / "evidence_packet_E004.html").exists())
            self.assertTrue((output_dir / "demo_proof_manifest.json").exists())

    def test_verifier_reports_missing_artifacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            errors = verify_demo_proof_artifacts(Path(temp_dir))

            self.assertIn("E-002: missing audit bundle", errors[0])
            self.assertIn("E-004: missing audit bundle", errors[1])


if __name__ == "__main__":
    unittest.main()
