from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


EXPECTED_TEST_MANAGER_CASES = {
    "E-001": {
        "test_case_key": "SREV:3",
        "test_case_id": "a219914a-fdf8-0a00-6bb1-0b49cf9aa802",
        "name": "E-001 Closure allowed with fresh aligned telemetry",
    },
    "E-002": {
        "test_case_key": "SREV:1",
        "test_case_id": "ee12563e-fbf8-0a00-2871-0b49cf9aa7f4",
        "name": "E-002 Missing authoritative telemetry blocks closure",
    },
    "E-003": {
        "test_case_key": "SREV:2",
        "test_case_id": "6d62f1b1-fcf8-0a00-61c0-0b49cf9aa7ff",
        "name": "E-003 Stale authoritative telemetry blocks closure",
    },
    "E-004": {
        "test_case_key": "SREV:4",
        "test_case_id": "a6c525ac-fef8-0a00-6ae2-0b49cf9aa805",
        "name": "E-004 Contradicting authoritative signal escalates",
    },
    "E-005": {
        "test_case_key": "SREV:5",
        "test_case_id": "ab0b0937-fff8-0a00-e67d-0b49cf9abc79",
        "name": "E-005 High-impact exception stays out of closure",
    },
    "E-006": {
        "test_case_key": "SREV:6",
        "test_case_id": "0b8206a1-00f9-0a00-7910-0b49cf9abc7e",
        "name": "E-006 Verify telemetry cannot close on missing signal",
    },
    "E-007": {
        "test_case_key": "SREV:7",
        "test_case_id": "c7f17b11-01f9-0a00-287e-0b49cf9abcbc",
        "name": "E-007 Invalid agent output is overridden",
    },
    "E-008": {
        "test_case_key": "SREV:8",
        "test_case_id": "a20fe8f8-02f9-0a00-ec41-0b49cf9abce1",
        "name": "E-008 Low confidence creates usefulness incident",
    },
    "E-009": {
        "test_case_key": "SREV:10",
        "test_case_id": "ac219460-03f9-0a00-9bff-0b49cf9ac487",
        "name": "E-009 Override persistence links raw and policy events",
    },
}

EXPECTED_EXECUTION_ID = "40a1b334-5df8-1100-0a4b-0b49d0564f11"
EXPECTED_TEST_SET_KEY = "SREV:9"


def verify_test_manager_bridge(
    eval_results_path: Path,
    junit_path: Path,
    execution_stats_path: Path | None = None,
) -> dict[str, Any]:
    errors: list[str] = []
    eval_results = _read_json(eval_results_path)
    junit_root = ET.parse(junit_path).getroot()

    errors.extend(_verify_eval_results(eval_results))
    errors.extend(_verify_junit(junit_root))
    if execution_stats_path is not None:
        errors.extend(_verify_execution_stats(_read_json(execution_stats_path)))

    return {
        "status": "passed" if not errors else "failed",
        "errors": errors,
        "eval_results_path": str(eval_results_path),
        "junit_path": str(junit_path),
        "execution_stats_path": str(execution_stats_path) if execution_stats_path else None,
        "expected_execution_id": EXPECTED_EXECUTION_ID,
        "expected_test_set_key": EXPECTED_TEST_SET_KEY,
        "mapped_scenarios": sorted(EXPECTED_TEST_MANAGER_CASES),
        "claim_boundary": "manual_test_manager_execution_only; automated_test_cloud_execution_unclaimed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify local eval results against exported Test Manager JUnit evidence.")
    parser.add_argument("--eval-results", required=True, help="Path to local eval JSON output.")
    parser.add_argument("--junit", required=True, help="Path to exported Test Manager JUnit XML.")
    parser.add_argument("--execution-stats", default=None, help="Optional Test Manager execution stats JSON.")
    parser.add_argument("--output", default=None, help="Optional machine-readable bridge report path.")
    args = parser.parse_args()

    report = verify_test_manager_bridge(
        Path(args.eval_results),
        Path(args.junit),
        Path(args.execution_stats) if args.execution_stats else None,
    )
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["status"] == "passed" else 1


def _verify_eval_results(eval_results: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    summary = eval_results.get("summary", {})
    if summary.get("total") != 9 or summary.get("passed") != 9 or summary.get("failed") != 0:
        errors.append("eval summary must show 9 total, 9 passed, 0 failed")

    results = eval_results.get("results")
    if not isinstance(results, list):
        return errors + ["eval results must contain a results list"]

    observed_ids = {result.get("scenario_id") for result in results}
    expected_ids = set(EXPECTED_TEST_MANAGER_CASES)
    if observed_ids != expected_ids:
        errors.append(f"eval scenario IDs mismatch: expected {sorted(expected_ids)}, observed {sorted(observed_ids)}")

    for result in results:
        scenario_id = result.get("scenario_id")
        if scenario_id not in EXPECTED_TEST_MANAGER_CASES:
            continue
        if result.get("passed") is not True:
            errors.append(f"{scenario_id}: local eval did not pass")
        policy_decision = result.get("policy_decision", {})
        policy_event = result.get("policy_event", {})
        if policy_event.get("agent_event_id") != policy_decision.get("agent_event_id"):
            errors.append(f"{scenario_id}: policy event is not linked to policy decision agent_event_id")

    return errors


def _verify_junit(root: ET.Element) -> list[str]:
    errors: list[str] = []
    suite = root.find("testsuite") if root.tag == "testsuites" else root
    if suite is None:
        return ["JUnit XML does not contain a testsuite"]

    expected_counts = {"tests": "9", "failures": "0", "errors": "0", "cancelled": "0"}
    for key, expected in expected_counts.items():
        if suite.attrib.get(key) != expected:
            errors.append(f"JUnit testsuite expected {key}={expected}, observed {suite.attrib.get(key)}")
    if suite.attrib.get("id") != EXPECTED_EXECUTION_ID:
        errors.append(f"JUnit testsuite execution id mismatch: {suite.attrib.get('id')}")

    testcases = list(suite.findall("testcase"))
    by_scenario = {_scenario_id_from_name(testcase.attrib.get("name", "")): testcase for testcase in testcases}
    observed_ids = set(by_scenario)
    expected_ids = set(EXPECTED_TEST_MANAGER_CASES)
    if observed_ids != expected_ids:
        errors.append(f"JUnit scenario IDs mismatch: expected {sorted(expected_ids)}, observed {sorted(observed_ids)}")

    for scenario_id, expected in EXPECTED_TEST_MANAGER_CASES.items():
        testcase = by_scenario.get(scenario_id)
        if testcase is None:
            continue
        name = testcase.attrib.get("name", "")
        if name != expected["name"]:
            errors.append(f"{scenario_id}: JUnit name mismatch: {name}")
        if testcase.attrib.get("status") != "Passed":
            errors.append(f"{scenario_id}: JUnit status is {testcase.attrib.get('status')}")
        system_out = testcase.findtext("system-out", default="")
        expected_url_bits = (
            f"/testexecution-results/{EXPECTED_EXECUTION_ID}/{expected['test_case_id']}",
            "Input arguments {}",
            "Output arguments {}",
        )
        for expected_bit in expected_url_bits:
            if expected_bit not in system_out:
                errors.append(f"{scenario_id}: JUnit system-out missing {expected_bit!r}")

    return errors


def _verify_execution_stats(stats: dict[str, Any]) -> list[str]:
    data = stats.get("Data", {})
    checks = {
        "Passed": data.get("Passed") == 9,
        "Failed": data.get("Failed") == 0,
        "None": data.get("None") == 0,
        "IsRunningAutomated": data.get("IsRunningAutomated") is False,
        "Status": data.get("Status") == "Finished",
        "ExecutionType": data.get("ExecutionType") == "Manual",
        "TestSetObjKey": data.get("TestSetObjKey") == EXPECTED_TEST_SET_KEY,
        "Id": data.get("Id") == EXPECTED_EXECUTION_ID,
    }
    return [f"execution stats failed check {name}" for name, passed in checks.items() if not passed]


def _scenario_id_from_name(name: str) -> str | None:
    match = re.match(r"^(E-\d{3})\b", name)
    return match.group(1) if match else None


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
