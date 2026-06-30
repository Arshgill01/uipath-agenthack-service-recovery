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
        self.assertIn("Raw Agent Interpretation Event", html)
        self.assertIn("Linked Policy Decision Event", html)
        self.assertIn("Controlled verification retry", html)
        self.assertIn("closure_candidate", html)
        self.assertIn("override_recommendation", html)
        self.assertIn("verify_telemetry", html)
        self.assertIn("missing_authoritative_signal", html)
        self.assertIn("Policy versions", html)
        self.assertIn("ip-v1 / dp-v1", html)
        self.assertIn("UiPath platform role", html)
        self.assertIn("generated Action Center page hid or mislabeled proof-critical fields", html)
        self.assertIn("Closure readiness checklist", html)
        self.assertIn("Fresh authoritative telemetry confirms service is live", html)
        self.assertIn("Which authoritative telemetry retry or source will produce service_live_status before closure?", html)
        self.assertIn("Closure is not available until fresh authoritative service evidence confirms recovery", html)
        self.assertIn("retry_telemetry", html)
        self.assertIn('class="table-scroll"', html)
        self.assertNotIn("@import url(", html)

    def test_contradiction_html_shows_human_review_route(self):
        html = build_evidence_packet_html("E-004")

        self.assertIn("CASE-BG-CONTRA", html)
        self.assertIn("source_contradiction", html)
        self.assertIn("require_human_review", html)
        self.assertIn("human_review", html)
        self.assertIn("Escalated exception review", html)
        self.assertIn("closure_candidate -> human_review", html)
        self.assertIn("Final route", html)
        self.assertIn("Closure guard", html)
        self.assertIn("authoritative", html)
        self.assertIn("open_investigation", html)
        self.assertIn("fresh authoritative telemetry contradicts", html)
        self.assertIn("Why do business systems show active while fresh authoritative service evidence disagrees?", html)
        self.assertIn("Required human review has resolved the exception", html)
        self.assertIn("--parchment: #f5f4ed", html)


if __name__ == "__main__":
    unittest.main()
