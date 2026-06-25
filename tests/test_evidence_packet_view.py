import unittest

from service_recovery_core.evals import build_evidence_packet_html


class EvidencePacketViewTests(unittest.TestCase):
    def test_missing_telemetry_html_shows_agent_policy_boundary(self):
        html = build_evidence_packet_html("E-002")

        self.assertIn("<!doctype html>", html)
        self.assertIn("Review service recovery evidence", html)
        self.assertIn("CASE-BG-MISSING", html)
        self.assertIn("Raw agent interpretation", html)
        self.assertIn("Final policy decision", html)
        self.assertIn("closure_candidate", html)
        self.assertIn("override_recommendation", html)
        self.assertIn("verify_telemetry", html)
        self.assertIn("missing_authoritative_signal", html)
        self.assertIn("retry_telemetry", html)

    def test_contradiction_html_shows_human_review_route(self):
        html = build_evidence_packet_html("E-004")

        self.assertIn("CASE-BG-CONTRA", html)
        self.assertIn("source_contradiction", html)
        self.assertIn("require_human_review", html)
        self.assertIn("human_review", html)
        self.assertIn("open_investigation", html)
        self.assertIn("fresh authoritative telemetry contradicts", html)


if __name__ == "__main__":
    unittest.main()
