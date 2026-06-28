import tempfile
import unittest
from pathlib import Path

from service_recovery_core.external_evidence import (
    DEFAULT_SAMPLE_PATH,
    PROOF_JSON_NAME,
    build_external_evidence_artifacts,
    load_external_source_file,
    parse_external_evidence,
    verify_external_evidence_artifacts,
)


class ExternalEvidenceTests(unittest.TestCase):
    def test_sample_external_source_builds_human_review_proof(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_payload = load_external_source_file(DEFAULT_SAMPLE_PATH)
            proof = build_external_evidence_artifacts(source_payload, Path(temp_dir))
            errors = verify_external_evidence_artifacts(Path(temp_dir))

            self.assertEqual(errors, [])
            self.assertEqual(proof["artifact_type"], "external-evidence-source-proof-v1")
            self.assertEqual(proof["case_id"], "CASE-BG-CONTRA")
            self.assertEqual(proof["policy_decision"], "require_human_review")
            self.assertEqual(proof["route"], "human_review")
            self.assertIn("source_contradiction", proof["reason_codes"])
            self.assertIn("not a production telecom OSS/BSS integration", proof["claim_boundary"])
            self.assertTrue((Path(temp_dir) / PROOF_JSON_NAME).exists())

    def test_parser_normalizes_csv_rows_without_credentials(self):
        source_payload = load_external_source_file(DEFAULT_SAMPLE_PATH)

        evidence = parse_external_evidence(source_payload)

        self.assertEqual(len(evidence), 5)
        self.assertEqual(evidence[0]["source"], "crm")
        self.assertIs(evidence[0]["authoritative"], True)
        self.assertEqual(evidence[3]["field"], "service_live_status")
        self.assertEqual(evidence[3]["value"], "not_live")


if __name__ == "__main__":
    unittest.main()
