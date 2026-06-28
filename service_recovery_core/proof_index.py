from __future__ import annotations

import argparse
import json
from html import escape
from pathlib import Path
from typing import Any


PROOF_INDEX_NAME = "proof_index.html"


def build_proof_index(artifact_dir: Path, *, output_path: Path | None = None) -> dict[str, Any]:
    artifact_dir = artifact_dir.resolve()
    output_path = output_path or artifact_dir / PROOF_INDEX_NAME
    index = _build_index_payload(artifact_dir)
    output_path.write_text(render_proof_index_html(index), encoding="utf-8")
    return index


def verify_proof_index(artifact_dir: Path, *, output_path: Path | None = None) -> list[str]:
    artifact_dir = artifact_dir.resolve()
    output_path = output_path or artifact_dir / PROOF_INDEX_NAME
    errors: list[str] = []

    required_artifacts = (
        "demo_proof_manifest.json",
        "service_recovery_audit_bundle_E002.json",
        "service_recovery_audit_bundle_E004.json",
        "evidence_packet_E002.html",
        "evidence_packet_E004.html",
        "llm_interpreter_E003_adversarial_live.json",
        "evidence_packet_E003_adversarial_live.html",
        "policy_improvement_E008.json",
    )
    for name in required_artifacts:
        if not (artifact_dir / name).exists():
            errors.append(f"missing source artifact: {artifact_dir / name}")

    if not output_path.exists():
        errors.append(f"missing proof index: {output_path}")
        return errors

    html = output_path.read_text(encoding="utf-8")
    required_strings = (
        "Judge-facing proof index",
        "Claim boundaries",
        "judge-readable support surface",
        "not a replacement for UiPath Maestro Case",
        "E-002",
        "E-004",
        "E-003",
        "E-008",
        "closure_candidate",
        "verify_telemetry",
        "human_review",
        "missing_authoritative_signal",
        "source_contradiction",
        "high_interpretation_disagreement",
        "pending_human_approval",
        "not_promoted",
        "Action Center lifecycle",
        "Data Fabric V2",
        "Test Manager manual execution",
    )
    for value in required_strings:
        if value not in html:
            errors.append(f"{output_path.name}: missing required index string {value!r}")

    if not errors:
        index = _build_index_payload(artifact_dir)
        scenario_ids = [beat["scenario_id"] for beat in index["beats"]]
        if scenario_ids != ["E-002", "E-004", "E-003", "E-008"]:
            errors.append(f"{output_path.name}: unexpected beat order {scenario_ids}")
    return errors


def render_proof_index_html(index: dict[str, Any]) -> str:
    beat_cards = "\n".join(_beat_card(beat) for beat in index["beats"])
    return "\n".join(
        [
            "<!doctype html>",
            '<html lang="en">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            "<title>Judge-facing proof index</title>",
            "<style>",
            _CSS,
            "</style>",
            "</head>",
            "<body>",
            '<main class="page">',
            "<header>",
            "<p>UiPath AgentHack service recovery</p>",
            "<h1>Judge-facing proof index</h1>",
            "<p>This generated page links the demo proof artifacts and makes the claim boundary inspectable before recording.</p>",
            "</header>",
            '<section class="claim-boundary">',
            "<h2>Claim boundaries</h2>",
            "<p>This is a judge-readable support surface generated from existing proof artifacts. It is not a replacement for UiPath Maestro Case, Action Center, Data Fabric V2, Orchestrator, or Test Manager manual execution proof.</p>",
            "<ul>",
            "<li>Agents produce structured recommendations; deterministic policy decides the route.</li>",
            "<li>Action Center lifecycle proves human task handling; custom packets make proof-critical fields readable.</li>",
            "<li>No automated Test Cloud execution, generated Action Center UI readiness, real telecom integration, or LLM/Codex final-closure authority is claimed.</li>",
            "</ul>",
            "</section>",
            '<section class="proof-chain">',
            "<h2>Demo proof chain</h2>",
            beat_cards,
            "</section>",
            '<section class="platform-map">',
            "<h2>Platform proof anchors</h2>",
            "<dl>",
            "<div><dt>Maestro Case / Action Center lifecycle</dt><dd>Validated case and task IDs are documented in the runbook and proof map; this page links the generated local payloads that fed those proof beats.</dd></div>",
            "<div><dt>Data Fabric V2 / Orchestrator audit</dt><dd>The E-004 audit bundle is the full-payload proof shape used for UiPath-hosted audit readback.</dd></div>",
            "<div><dt>Test Manager manual execution</dt><dd>E-001 through E-009 are represented by the SREV:9 manual execution, not automated Test Cloud execution.</dd></div>",
            "</dl>",
            "</section>",
            "</main>",
            "</body>",
            "</html>",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate and verify the judge-facing proof index.")
    parser.add_argument(
        "--artifact-dir",
        default="docs/demo/artifacts",
        help="Directory containing generated proof artifacts.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Proof index output path. Defaults to <artifact-dir>/proof_index.html.",
    )
    parser.add_argument("--verify-only", action="store_true", help="Verify an existing proof index.")
    args = parser.parse_args()

    artifact_dir = Path(args.artifact_dir)
    output_path = Path(args.output) if args.output else None

    if not args.verify_only:
        index = build_proof_index(artifact_dir, output_path=output_path)
        print(json.dumps(index, indent=2, sort_keys=True))

    errors = verify_proof_index(artifact_dir, output_path=output_path)
    if errors:
        print(json.dumps({"status": "failed", "errors": errors}, indent=2, sort_keys=True))
        return 1

    print(json.dumps({"status": "passed", "artifact": str(output_path or artifact_dir / PROOF_INDEX_NAME)}, indent=2))
    return 0


def _build_index_payload(artifact_dir: Path) -> dict[str, Any]:
    manifest = _read_json(artifact_dir / "demo_proof_manifest.json")
    beats = [_core_beat(artifact_dir, scenario) for scenario in manifest["scenarios"]]
    beats.append(_llm_beat(artifact_dir))
    beats.append(_learning_loop_beat(artifact_dir))
    return {
        "artifact_type": "service-recovery-proof-index",
        "source_artifact_dir": str(artifact_dir),
        "beats": beats,
    }


def _core_beat(artifact_dir: Path, manifest_scenario: dict[str, Any]) -> dict[str, Any]:
    scenario_id = manifest_scenario["scenario_id"]
    audit_path = _manifest_path(artifact_dir, manifest_scenario["audit_bundle_path"])
    audit = _read_json(audit_path)
    agent = audit["agent_interpretation_event"]
    policy = audit["policy_decision_event"]
    state = audit["evidence_state"]
    return {
        "scenario_id": scenario_id,
        "title": "2A missing or stale authoritative evidence" if scenario_id == "E-002" else "2B fresh authoritative contradiction",
        "claim": _core_claim(scenario_id),
        "agent_recommendation": agent["recommended_next_stage"],
        "policy_decision": policy["decision"],
        "route": policy["to_stage"],
        "reason": state["closure_block_reason"],
        "boundary": "Custom packet supports UiPath runtime proof; policy, not the agent, controls routing.",
        "links": [
            ("Evidence packet", _relative_name(manifest_scenario["evidence_packet_html_path"])),
            ("Audit bundle", _relative_name(manifest_scenario["audit_bundle_path"])),
            ("Action Center payload", _relative_name(manifest_scenario["payload_path"])),
        ],
    }


def _llm_beat(artifact_dir: Path) -> dict[str, Any]:
    artifact_name = "llm_interpreter_E003_adversarial_live.json"
    result = _read_json(artifact_dir / artifact_name)
    agent = result["agent_interpretation_event"]
    policy = result["policy_decision_event"]
    disagreement = agent.get("adversarial_interpretation", {}).get("disagreement", {})
    return {
        "scenario_id": "E-003",
        "title": "Live adversarial LLM interpretation",
        "claim": "LLM output remains advisory and schema-validated; disagreement becomes structured policy input.",
        "agent_recommendation": agent["recommended_next_stage"],
        "policy_decision": policy["decision"],
        "route": policy["to_stage"],
        "reason": ", ".join(policy.get("reason_codes", [])),
        "boundary": f"Disagreement score {disagreement.get('disagreement_score')} crosses threshold {disagreement.get('threshold')}; the LLM still does not close the case.",
        "links": [
            ("Adversarial packet", "evidence_packet_E003_adversarial_live.html"),
            ("LLM JSON", artifact_name),
            ("Desktop screenshot", "evidence_packet_E003_adversarial_desktop.png"),
            ("Mobile screenshot", "evidence_packet_E003_adversarial_mobile.png"),
        ],
    }


def _learning_loop_beat(artifact_dir: Path) -> dict[str, Any]:
    artifact_name = "policy_improvement_E008.json"
    artifact = _read_json(artifact_dir / artifact_name)
    return {
        "scenario_id": "E-008",
        "title": "Governed learning-loop artifact",
        "claim": "Usefulness degradation creates a proposal-only policy improvement case.",
        "agent_recommendation": artifact["trigger"],
        "policy_decision": artifact["approval_status"],
        "route": artifact["promotion_status"],
        "reason": artifact["active_case_policy_version_action"],
        "boundary": "Policy stays pending human approval and is not_promoted; active cases remain pinned until explicit migration.",
        "links": [("Policy improvement JSON", artifact_name)],
    }


def _beat_card(beat: dict[str, Any]) -> str:
    links = "\n".join(
        f'<li><a href="{escape(href)}">{escape(label)}</a></li>' for label, href in beat["links"]
    )
    return f"""
<article class="beat">
  <div class="beat-head">
    <span>{escape(beat["scenario_id"])}</span>
    <h3>{escape(beat["title"])}</h3>
  </div>
  <p>{escape(beat["claim"])}</p>
  <dl>
    <div><dt>Raw agent / trigger</dt><dd>{escape(str(beat["agent_recommendation"]))}</dd></div>
    <div><dt>Policy decision</dt><dd>{escape(str(beat["policy_decision"]))}</dd></div>
    <div><dt>Route / status</dt><dd>{escape(str(beat["route"]))}</dd></div>
    <div><dt>Reason</dt><dd>{escape(str(beat["reason"]))}</dd></div>
  </dl>
  <p class="boundary">{escape(beat["boundary"])}</p>
  <ul class="links">{links}</ul>
</article>""".strip()


def _core_claim(scenario_id: str) -> str:
    if scenario_id == "E-002":
        return "Same green business fixture; missing authoritative telemetry overrides closure to verification."
    if scenario_id == "E-004":
        return "Same green business fixture; fresh authoritative contradiction escalates to human review."
    return "Core service-recovery proof beat."


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _manifest_path(artifact_dir: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    if path.exists():
        return path
    return artifact_dir / path.name


def _relative_name(value: str) -> str:
    return Path(value).name


_CSS = """
:root {
  color-scheme: light;
  --bg: #f7f8f3;
  --surface: #ffffff;
  --ink: #202522;
  --muted: #5f6861;
  --line: #cfd7ce;
  --accent: #245a4f;
  --warn: #9b3f2f;
  --blue: #284f93;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 14.5px/1.55 ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.page {
  max-width: 1180px;
  margin: 0 auto;
  padding: 28px;
}

header {
  border-bottom: 2px solid var(--line);
  padding-bottom: 18px;
  margin-bottom: 18px;
}

header p {
  max-width: 780px;
}

h1, h2, h3, p {
  margin-top: 0;
}

h1 {
  color: var(--accent);
  font-size: 30px;
  line-height: 1.12;
  margin-bottom: 8px;
}

h2 {
  color: var(--accent);
  font-size: 18px;
  margin-bottom: 12px;
}

h3 {
  font-size: 18px;
  margin-bottom: 10px;
}

p, li, dt {
  color: var(--muted);
}

.claim-boundary,
.platform-map,
.beat {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 18px;
}

.claim-boundary {
  border-left: 4px solid var(--warn);
  margin-bottom: 18px;
}

.proof-chain {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin-bottom: 18px;
}

.proof-chain h2 {
  grid-column: 1 / -1;
  margin-bottom: 0;
}

.beat {
  display: grid;
  gap: 12px;
  align-content: start;
}

.beat-head {
  display: flex;
  align-items: center;
  gap: 10px;
}

.beat-head span {
  background: var(--accent);
  border-radius: 6px;
  color: #fff;
  display: inline-block;
  font-weight: 700;
  padding: 3px 8px;
}

dl {
  display: grid;
  gap: 8px;
  margin: 0;
}

dl div {
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: 12px;
  border-bottom: 1px dotted var(--line);
  padding-bottom: 5px;
}

dd {
  margin: 0;
  font-weight: 700;
  overflow-wrap: anywhere;
}

.boundary {
  background: #fff8ed;
  border: 1px solid #f0d0a9;
  border-radius: 6px;
  color: var(--warn);
  font-weight: 700;
  padding: 10px 12px;
}

.links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.links a {
  border: 1px solid var(--line);
  border-radius: 6px;
  color: var(--blue);
  display: inline-block;
  font-weight: 700;
  padding: 5px 9px;
  text-decoration: none;
}

@media (max-width: 780px) {
  .page {
    padding: 16px;
  }

  .proof-chain {
    grid-template-columns: 1fr;
  }

  dl div {
    grid-template-columns: 1fr;
    gap: 2px;
  }
}
"""


if __name__ == "__main__":
    raise SystemExit(main())
