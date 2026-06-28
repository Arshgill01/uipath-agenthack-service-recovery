from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

from service_recovery_core.audit_bundle import build_case_audit_bundle
from service_recovery_core.evidence_packet_view import render_evidence_packet_html
from service_recovery_core.fixtures import scenario
from service_recovery_core.policy import decide_policy
from service_recovery_core.schemas import validate_evidence_signal
from service_recovery_core.state_machine import apply_policy_decision


DEFAULT_SAMPLE_PATH = Path(__file__).resolve().parent.parent / "fixtures" / "external_evidence_CASE_BG_CONTRA.csv"
DEFAULT_SCENARIO_ID = "E-004"
PROOF_JSON_NAME = "external_evidence_source_proof.json"
AUDIT_BUNDLE_NAME = "service_recovery_audit_bundle_external_E004.json"
PACKET_HTML_NAME = "evidence_packet_external_E004.html"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or verify optional external evidence-source proof artifacts.")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--source-url", default=None, help="Public read-only CSV or JSON evidence source URL.")
    source.add_argument("--source-file", default=None, help="Local CSV or JSON evidence source file.")
    parser.add_argument(
        "--source-ref",
        default=None,
        help="Optional display/source reference to record when reading from --source-file.",
    )
    parser.add_argument("--output-dir", default="docs/demo/artifacts", help="Output artifact directory.")
    parser.add_argument("--verify-only", action="store_true", help="Verify existing external evidence proof artifacts.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if not args.verify_only:
        if args.source_url:
            source_payload = load_external_source_url(args.source_url)
        else:
            source_path = Path(args.source_file) if args.source_file else DEFAULT_SAMPLE_PATH
            source_payload = load_external_source_file(source_path, source_ref=args.source_ref)
        build_external_evidence_artifacts(source_payload, output_dir)

    errors = verify_external_evidence_artifacts(output_dir)
    if errors:
        print(json.dumps({"status": "failed", "errors": errors}, indent=2, sort_keys=True))
        return 1
    print(json.dumps({"status": "passed", "artifact": str(output_dir / PROOF_JSON_NAME)}, indent=2))
    return 0


def load_external_source_url(url: str) -> dict[str, Any]:
    request = Request(url, headers={"User-Agent": "uipath-agenthack-service-recovery/1.0"})
    with urlopen(request, timeout=20) as response:
        content_type = response.headers.get("content-type", "")
        raw = response.read().decode("utf-8")
    return _source_payload(raw, source_ref=url, content_type=content_type)


def load_external_source_file(path: Path, *, source_ref: str | None = None) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    return _source_payload(raw, source_ref=source_ref or str(path), content_type=_content_type_for_path(path))


def build_external_evidence_artifacts(source_payload: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    fixture = scenario(DEFAULT_SCENARIO_ID)
    evidence = parse_external_evidence(source_payload, case_id=fixture["case"]["case_id"])
    fixture["evidence"] = evidence
    fixture["agent_interpretation"]["input_refs"] = sorted(
        set(fixture["agent_interpretation"].get("input_refs", []) + ["external_evidence_source_simulator"])
    )

    policy_decision = decide_policy(fixture["case"], fixture["evidence"], fixture["agent_interpretation"])
    transition = apply_policy_decision(
        fixture["case"],
        fixture["agent_interpretation"],
        policy_decision,
        event_id="PDE-EXT-E004",
    )
    audit_bundle = build_case_audit_bundle(fixture["case"], fixture["evidence"], transition)
    audit_bundle["external_evidence_source"] = _source_summary(source_payload, evidence)
    audit_bundle["claim_boundary"] = (
        "External source is a live-style systems-of-record simulator, not a production telecom OSS/BSS integration."
    )

    proof = {
        "artifact_type": "external-evidence-source-proof-v1",
        "scenario_id": DEFAULT_SCENARIO_ID,
        "case_id": fixture["case"]["case_id"],
        "source": audit_bundle["external_evidence_source"],
        "claim_boundary": audit_bundle["claim_boundary"],
        "policy_decision": policy_decision["decision"],
        "route": policy_decision["to_stage"],
        "reason_codes": policy_decision["reason_codes"],
        "audit_bundle_path": str(output_dir / AUDIT_BUNDLE_NAME),
        "evidence_packet_html_path": str(output_dir / PACKET_HTML_NAME),
    }

    _write_json(output_dir / PROOF_JSON_NAME, proof)
    _write_json(output_dir / AUDIT_BUNDLE_NAME, audit_bundle)
    (output_dir / PACKET_HTML_NAME).write_text(render_evidence_packet_html(audit_bundle), encoding="utf-8")
    return proof


def verify_external_evidence_artifacts(output_dir: Path) -> list[str]:
    errors: list[str] = []
    proof_path = output_dir / PROOF_JSON_NAME
    audit_path = output_dir / AUDIT_BUNDLE_NAME
    html_path = output_dir / PACKET_HTML_NAME

    for path in (proof_path, audit_path, html_path):
        if not path.exists():
            errors.append(f"missing external evidence artifact: {path}")
    if errors:
        return errors

    proof = _read_json(proof_path)
    audit = _read_json(audit_path)
    html = html_path.read_text(encoding="utf-8")
    checks = {
        "artifact_type": proof.get("artifact_type") == "external-evidence-source-proof-v1",
        "scenario_id": proof.get("scenario_id") == DEFAULT_SCENARIO_ID,
        "case_id": proof.get("case_id") == "CASE-BG-CONTRA",
        "policy_decision": proof.get("policy_decision") == "require_human_review",
        "route": proof.get("route") == "human_review",
        "reason_code": "source_contradiction" in proof.get("reason_codes", []),
        "claim_boundary": "not a production telecom OSS/BSS integration" in proof.get("claim_boundary", ""),
        "source_count": proof.get("source", {}).get("signal_count") == 5,
        "audit_external_source": audit.get("external_evidence_source", {}).get("signal_count") == 5,
        "html_mentions_external_source": "External evidence source" in html,
        "html_preserves_boundary": "not a production telecom OSS/BSS integration" in html,
        "html_shows_human_review": "human_review" in html,
    }
    return [f"external evidence proof failed check {name}" for name, passed in checks.items() if not passed]


def parse_external_evidence(source_payload: dict[str, Any], *, case_id: str | None = None) -> list[dict[str, Any]]:
    raw = source_payload["raw"]
    content_type = source_payload["content_type"]
    if "json" in content_type or raw.lstrip().startswith("[") or raw.lstrip().startswith("{"):
        rows = _json_rows(raw)
    else:
        rows = list(csv.DictReader(raw.splitlines()))
    selected_rows = [
        row
        for row in rows
        if not _is_blank_template_row(row) and (case_id is None or str(row.get("case_id", "")) == case_id)
    ]
    evidence = [_normalize_row(row) for row in selected_rows]
    for signal in evidence:
        validate_evidence_signal(signal)
    return evidence


def _source_payload(raw: str, *, source_ref: str, content_type: str) -> dict[str, Any]:
    return {
        "source_ref": source_ref,
        "content_type": content_type,
        "raw": raw,
        "sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "fetched_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }


def _source_summary(source_payload: dict[str, Any], evidence: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "source_ref": source_payload["source_ref"],
        "content_type": source_payload["content_type"],
        "sha256": source_payload["sha256"],
        "fetched_at": source_payload["fetched_at"],
        "signal_count": len(evidence),
        "sources": sorted({signal["source"] for signal in evidence}),
        "case_ids": sorted({signal["case_id"] for signal in evidence}),
        "proof_role": "live-style external systems-of-record simulator",
    }


def _json_rows(raw: str) -> list[dict[str, Any]]:
    payload = json.loads(raw)
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("evidence"), list):
        return payload["evidence"]
    if isinstance(payload, dict) and isinstance(payload.get("rows"), list):
        return payload["rows"]
    raise ValueError("JSON external evidence source must be a list or contain evidence/rows list")


def _normalize_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "case_id": str(row["case_id"]),
        "field": str(row["field"]),
        "source": str(row["source"]),
        "value": str(row["value"]),
        "authoritative": _parse_bool(row["authoritative"]),
        "freshness_status": str(row["freshness_status"]),
        "ttl_seconds": int(row["ttl_seconds"]),
        "observed_at": str(row["observed_at"]),
    }


def _is_blank_template_row(row: dict[str, Any]) -> bool:
    identifying_values = [row.get("source"), row.get("case_id"), row.get("field"), row.get("value")]
    return all(str(value or "").strip() == "" for value in identifying_values)


def _parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    raise ValueError(f"invalid boolean value: {value!r}")


def _content_type_for_path(path: Path) -> str:
    if path.suffix.lower() == ".json":
        return "application/json"
    return "text/csv"


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
