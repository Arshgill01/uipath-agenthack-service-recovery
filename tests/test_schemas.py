import unittest
from datetime import datetime, timezone

from service_recovery_core.fixtures import load_scenarios
from service_recovery_core.schemas import ValidationError, validate_case, validate_evidence_signal


class SchemaTests(unittest.TestCase):
    def test_valid_fixture_cases_and_evidence_pass(self):
        for scenario in load_scenarios().values():
            validate_case(scenario["case"])
            for signal in scenario["evidence"]:
                validate_evidence_signal(signal)

    def test_invalid_authoritative_source_fails(self):
        signal = {
            "case_id": "CASE-X",
            "field": "service_live_status",
            "source": "support_note",
            "value": "live",
            "authoritative": True,
            "freshness_status": "fresh",
            "ttl_seconds": 300,
            "observed_at": "2026-06-18T10:00:00Z",
        }
        with self.assertRaises(ValidationError):
            validate_evidence_signal(signal)

    def test_fresh_signal_older_than_ttl_fails_when_now_supplied(self):
        signal = {
            "case_id": "CASE-X",
            "field": "service_live_status",
            "source": "network_telemetry",
            "value": "live",
            "authoritative": True,
            "freshness_status": "fresh",
            "ttl_seconds": 300,
            "observed_at": "2026-06-18T10:00:00Z",
        }
        with self.assertRaises(ValidationError):
            validate_evidence_signal(
                signal,
                now=datetime.fromisoformat("2026-06-18T10:06:00+00:00").astimezone(timezone.utc),
            )


if __name__ == "__main__":
    unittest.main()
