import copy
import json
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from service_recovery_core.evals import run_eval_suite
from service_recovery_core.test_manager_bridge import verify_test_manager_bridge


REPO_ROOT = Path(__file__).resolve().parents[1]
JUNIT_PATH = (
    REPO_ROOT
    / "docs/validation/artifacts/test-manager-results/Service_Recovery_E_001_through_E_009_Baseline___20260626_1017.xml"
)
EXECUTION_STATS_PATH = (
    REPO_ROOT
    / "docs/validation/artifacts/2026-06-28/test-manager-feasibility-spike/04-tm-terminal-execution-stats.json"
)


class TestManagerBridgeTests(unittest.TestCase):
    def test_current_eval_and_test_manager_export_bridge_passes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            eval_path = Path(temp_dir) / "local_baseline.json"
            eval_path.write_text(json.dumps(run_eval_suite(), indent=2, sort_keys=True) + "\n", encoding="utf-8")

            report = verify_test_manager_bridge(eval_path, JUNIT_PATH, EXECUTION_STATS_PATH)

            self.assertEqual(report["status"], "passed", report)
            self.assertEqual(report["claim_boundary"], "manual_test_manager_execution_only; automated_test_cloud_execution_unclaimed")

    def test_reports_failed_local_eval(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            eval_results = run_eval_suite()
            mutated = copy.deepcopy(eval_results)
            mutated["summary"]["passed"] = 8
            mutated["summary"]["failed"] = 1
            mutated["results"][0]["passed"] = False
            eval_path = Path(temp_dir) / "local_baseline.json"
            eval_path.write_text(json.dumps(mutated, indent=2, sort_keys=True) + "\n", encoding="utf-8")

            report = verify_test_manager_bridge(eval_path, JUNIT_PATH)

            self.assertEqual(report["status"], "failed")
            self.assertIn("eval summary must show 9 total, 9 passed, 0 failed", report["errors"])
            self.assertIn("E-001: local eval did not pass", report["errors"])

    def test_reports_wrong_test_manager_case_id(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            eval_path = Path(temp_dir) / "local_baseline.json"
            eval_path.write_text(json.dumps(run_eval_suite(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
            junit_path = Path(temp_dir) / "results.xml"
            tree = ET.parse(JUNIT_PATH)
            first_system_out = tree.getroot().find(".//testcase/system-out")
            self.assertIsNotNone(first_system_out)
            first_system_out.text = first_system_out.text.replace(
                "ac219460-03f9-0a00-9bff-0b49cf9ac487",
                "00000000-0000-0000-0000-000000000000",
            )
            tree.write(junit_path, encoding="utf-8", xml_declaration=True)

            report = verify_test_manager_bridge(eval_path, junit_path)

            self.assertEqual(report["status"], "failed")
            self.assertIn(
                "E-009: JUnit system-out missing '/testexecution-results/40a1b334-5df8-1100-0a4b-0b49d0564f11/ac219460-03f9-0a00-9bff-0b49cf9ac487'",
                report["errors"],
            )


if __name__ == "__main__":
    unittest.main()
