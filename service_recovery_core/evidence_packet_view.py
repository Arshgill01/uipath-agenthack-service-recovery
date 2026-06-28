from __future__ import annotations

from html import escape
from typing import Any


def render_evidence_packet_html(audit_bundle: dict[str, Any]) -> str:
    packet = audit_bundle["reviewer_packet"]
    agent = audit_bundle["agent_interpretation_event"]
    policy = audit_bundle["policy_decision_event"]
    state = audit_bundle["evidence_state"]
    versions = audit_bundle["policy_versions"]

    return "\n".join(
        [
            "<!doctype html>",
            '<html lang="en">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f"<title>Evidence Packet - {escape(audit_bundle['case_id'])}</title>",
            "<style>",
            _CSS,
            "</style>",
            "</head>",
            "<body>",
            '<main class="page">',
            _header(audit_bundle, state),
            _proof_strip(agent, policy, state, versions),
            _decision_compare(agent, policy, state),
            '<section class="layout">',
            '<div class="primary">',
            _platform_note(),
            _external_evidence_source(audit_bundle),
            _policy_boundary(agent, policy),
            _adversarial_interpretation(agent),
            _llm_recommendation_package(agent),
            _evidence_table(packet["evidence_table"]),
            "</div>",
            '<aside class="side">',
            _reviewer_actions(packet),
            _timeline(audit_bundle["events"]),
            "</aside>",
            "</section>",
            "</main>",
            "</body>",
            "</html>",
            "",
        ]
    )


def _header(audit_bundle: dict[str, Any], state: dict[str, Any]) -> str:
    mode = _case_mode(state)
    return f"""
<header class="topbar {escape(mode)}">
  <div>
    <h1>Review service recovery evidence</h1>
    <p>{escape(audit_bundle["case_id"])} / {escape(audit_bundle["service_id"])}</p>
  </div>
  <dl class="summary">
    <div><dt>Business state</dt><dd>{escape(state["business_state"])}</dd></div>
    <div><dt>Evidence state</dt><dd>{escape(state["derived_evidence_state"])}</dd></div>
    <div><dt>Block reason</dt><dd>{escape(state["closure_block_reason"])}</dd></div>
    </dl>
</header>""".strip()


def _proof_strip(
    agent: dict[str, Any],
    policy: dict[str, Any],
    state: dict[str, Any],
    versions: dict[str, Any],
) -> str:
    return f"""
<section class="proof-strip" aria-label="Demo proof summary">
  <div>
    <span>Raw agent recommendation</span>
    <strong>{escape(agent["recommended_next_stage"])}</strong>
  </div>
  <div>
    <span>Policy decision</span>
    <strong>{escape(policy["decision"])}</strong>
  </div>
  <div>
    <span>Final route</span>
    <strong>{escape(policy["to_stage"])}</strong>
  </div>
  <div>
    <span>Closure guard</span>
    <strong>{escape(state["closure_block_reason"])}</strong>
  </div>
  <div>
    <span>Policy versions</span>
    <strong>{escape(versions["interpretation_policy_version"])} / {escape(versions["decision_policy_version"])}</strong>
  </div>
</section>""".strip()


def _decision_compare(agent: dict[str, Any], policy: dict[str, Any], state: dict[str, Any]) -> str:
    mode = _case_mode(state)
    return f"""
<section class="decision-compare {escape(mode)}" aria-label="Agent recommendation and final policy decision">
  <article>
    <span class="eyebrow">Raw Agent Interpretation Event</span>
    <h2>{escape(agent["recommended_next_stage"])}</h2>
    <dl>
      <div><dt>AIE ID</dt><dd>{escape(agent["event_id"])}</dd></div>
      <div><dt>Confidence</dt><dd>{escape(str(agent["confidence"]))}</dd></div>
      <div><dt>Failure category</dt><dd>{escape(agent["failure_category"])}</dd></div>
    </dl>
  </article>
  <div class="override-arrow" aria-hidden="true">-></div>
  <article>
    <span class="eyebrow">Linked Policy Decision Event</span>
    <h2>{escape(policy["decision"])}</h2>
    <dl>
      <div><dt>PDE ID</dt><dd>{escape(policy["event_id"])}</dd></div>
      <div><dt>Links to</dt><dd>{escape(policy["links_to"])}</dd></div>
      <div><dt>Route</dt><dd>{escape(policy["to_stage"])}</dd></div>
    </dl>
  </article>
  <div class="route-banner">
    <span>{escape(_route_label(state, policy))}</span>
    <strong>{escape(policy["from_recommended_stage"])} -> {escape(policy["to_stage"])}</strong>
    <em>{escape(policy["block_reason"])}</em>
  </div>
</section>""".strip()


def _platform_note() -> str:
    return """
<section class="panel platform-note">
  <h2>UiPath platform role</h2>
  <p>Maestro Case and Action Center own lifecycle, assignment, completion, and reviewer return. This custom packet is the legible audit/evidence surface because the generated Action Center page hid or mislabeled proof-critical fields during validation.</p>
</section>""".strip()


def _external_evidence_source(audit_bundle: dict[str, Any]) -> str:
    source = audit_bundle.get("external_evidence_source")
    if not isinstance(source, dict):
        return ""
    sources = ", ".join(source.get("sources", []))
    return f"""
<section class="panel external-source">
  <h2>External evidence source</h2>
  <p>This packet was generated from a live-style external systems-of-record simulator, not a production telecom OSS/BSS integration.</p>
  <dl>
    <div><dt>Source ref</dt><dd>{escape(str(source.get("source_ref", "")))}</dd></div>
    <div><dt>Signals</dt><dd>{escape(str(source.get("signal_count", "")))}</dd></div>
    <div><dt>Systems represented</dt><dd>{escape(sources)}</dd></div>
    <div><dt>Fetched at</dt><dd>{escape(str(source.get("fetched_at", "")))}</dd></div>
    <div><dt>SHA-256</dt><dd>{escape(str(source.get("sha256", "")))}</dd></div>
  </dl>
</section>""".strip()


def _policy_boundary(agent: dict[str, Any], policy: dict[str, Any]) -> str:
    return f"""
<section class="panel boundary">
  <h2>Agent and policy boundary</h2>
  <div class="boundary-grid">
    <article>
      <h3>Raw agent interpretation</h3>
      <dl>
        <div><dt>Event</dt><dd>{escape(agent["event_id"])}</dd></div>
        <div><dt>Recommendation</dt><dd>{escape(agent["recommended_next_stage"])}</dd></div>
        <div><dt>Failure category</dt><dd>{escape(agent["failure_category"])}</dd></div>
        <div><dt>Confidence</dt><dd>{escape(str(agent["confidence"]))}</dd></div>
        <div><dt>Policy version</dt><dd>{escape(agent["interpretation_policy_version"])}</dd></div>
      </dl>
      <p>{escape(agent["rationale"])}</p>
    </article>
    <article>
      <h3>Final policy decision</h3>
      <dl>
        <div><dt>Event</dt><dd>{escape(policy["event_id"])}</dd></div>
        <div><dt>Links to</dt><dd>{escape(policy["links_to"])}</dd></div>
        <div><dt>Decision</dt><dd>{escape(policy["decision"])}</dd></div>
        <div><dt>Block reason</dt><dd>{escape(policy["block_reason"])}</dd></div>
        <div><dt>Reason codes</dt><dd>{escape(", ".join(policy.get("reason_codes", [])))}</dd></div>
        <div><dt>From</dt><dd>{escape(policy["from_recommended_stage"])}</dd></div>
        <div><dt>To</dt><dd>{escape(policy["to_stage"])}</dd></div>
        <div><dt>Policy version</dt><dd>{escape(policy["decision_policy_version"])}</dd></div>
      </dl>
    </article>
  </div>
</section>""".strip()


def _llm_recommendation_package(agent: dict[str, Any]) -> str:
    if not any(
        agent.get(field)
        for field in (
            "urgency",
            "customer_impact_summary",
            "evidence_gaps",
            "recommended_actions",
            "reviewer_questions",
            "operator_note",
        )
    ):
        return ""
    return f"""
<section class="panel">
  <h2>LLM triage package</h2>
  <dl>
    <div><dt>Urgency</dt><dd>{escape(str(agent.get("urgency") or "not_provided"))}</dd></div>
    <div><dt>Customer impact</dt><dd>{escape(str(agent.get("customer_impact_summary") or "not_provided"))}</dd></div>
    <div><dt>Operator note</dt><dd>{escape(str(agent.get("operator_note") or "not_provided"))}</dd></div>
  </dl>
  <div class="triage-grid">
    {_list_block("Evidence gaps", agent.get("evidence_gaps", []))}
    {_list_block("Recommended actions", agent.get("recommended_actions", []))}
    {_list_block("Reviewer questions", agent.get("reviewer_questions", []))}
  </div>
</section>""".strip()


def _adversarial_interpretation(agent: dict[str, Any]) -> str:
    adversarial = agent.get("adversarial_interpretation")
    if not isinstance(adversarial, dict):
        return ""
    disagreement = adversarial.get("disagreement", {})
    advocate = adversarial.get("advocate_interpretation", {})
    skeptic = adversarial.get("skeptic_interpretation", {})
    return f"""
<section class="panel adversarial">
  <h2>Adversarial dual interpretation</h2>
  <div class="disagreement-score">
    <span>Disagreement score</span>
    <strong>{escape(str(disagreement.get("disagreement_score", "not_provided")))}</strong>
    <em>threshold {escape(str(disagreement.get("threshold", "not_provided")))}</em>
  </div>
  <div class="adversarial-grid">
    {_interpretation_column("Resolution advocate", advocate)}
    {_interpretation_column("Closure skeptic", skeptic)}
  </div>
  <dl>
    <div><dt>Stage match</dt><dd>{escape(str(disagreement.get("stage_match", "not_provided")))}</dd></div>
    <div><dt>Confidence delta</dt><dd>{escape(str(disagreement.get("confidence_delta", "not_provided")))}</dd></div>
    <div><dt>Claim overlap</dt><dd>{escape(str(disagreement.get("claim_overlap_ratio", "not_provided")))}</dd></div>
  </dl>
  {_list_block("Skeptic-only gaps", disagreement.get("unique_skeptic_gaps", []))}
</section>""".strip()


def _interpretation_column(title: str, interpretation: dict[str, Any]) -> str:
    return f"""
<article>
  <h3>{escape(title)}</h3>
  <dl>
    <div><dt>Event</dt><dd>{escape(str(interpretation.get("event_id", "not_provided")))}</dd></div>
    <div><dt>Recommendation</dt><dd>{escape(str(interpretation.get("recommended_next_stage", "not_provided")))}</dd></div>
    <div><dt>Confidence</dt><dd>{escape(str(interpretation.get("recommendation_confidence", "not_provided")))}</dd></div>
    <div><dt>Failure category</dt><dd>{escape(str(interpretation.get("failure_category", "not_provided")))}</dd></div>
  </dl>
  <p>{escape(str(interpretation.get("audit_explanation", "No explanation provided.")))}</p>
</article>""".strip()


def _list_block(title: str, values: list[Any]) -> str:
    if not values:
        return f"<article><h3>{escape(title)}</h3><p>None provided.</p></article>"
    items = "\n".join(f"<li>{escape(str(value))}</li>" for value in values)
    return f"<article><h3>{escape(title)}</h3><ul class=\"actions\">{items}</ul></article>"


def _evidence_table(evidence: list[dict[str, Any]]) -> str:
    rows = "\n".join(
        f"""
        <tr>
          <td>{escape(signal["field"])}</td>
          <td>{escape(signal["source"])}</td>
          <td>{escape(str(signal["value"]))}</td>
          <td><span class="status">{escape(signal["freshness_status"])}</span></td>
          <td><span class="authority">{escape("authoritative" if signal["authoritative"] else "supporting")}</span></td>
          <td>{escape(str(signal["ttl_seconds"]))}</td>
        </tr>""".rstrip()
        for signal in evidence
    )
    return f"""
<section class="panel">
  <h2>Evidence table</h2>
  <div class="table-scroll">
  <table>
    <thead>
      <tr>
        <th>Field</th>
        <th>Source</th>
        <th>Value</th>
        <th>Freshness</th>
        <th>Authoritative</th>
        <th>TTL seconds</th>
      </tr>
    </thead>
    <tbody>
{rows}
    </tbody>
  </table>
  </div>
</section>""".strip()


def _reviewer_actions(packet: dict[str, Any]) -> str:
    options = "\n".join(f"<li>{escape(option)}</li>" for option in packet["recommended_options"])
    return f"""
<section class="panel">
  <h2>Reviewer packet</h2>
  <p>{escape(packet["content"])}</p>
  <dl>
    <div><dt>Block reason</dt><dd>{escape(packet["block_reason"])}</dd></div>
    <div><dt>Rendering status</dt><dd>{escape(packet["rendering_status"])}</dd></div>
  </dl>
  <h3>Recommended options</h3>
  <ul class="actions">{options}</ul>
{_closure_readiness(packet.get("closure_readiness_checklist", []))}
  {_list_block("Reviewer questions", packet.get("reviewer_questions", []))}
  <p class="guardrail">Closure is not available until fresh authoritative service evidence confirms recovery.</p>
</section>""".strip()


def _closure_readiness(checklist: list[dict[str, Any]]) -> str:
    if not checklist:
        return ""
    items = "\n".join(
        f"""
        <li class="{escape(str(item["status"]))}">
          <strong>{escape(str(item["criterion"]))}</strong>
          <span>{escape(str(item["status"]))}</span>
          <p>{escape(str(item["evidence"]))}</p>
        </li>""".rstrip()
        for item in checklist
    )
    return f"""  <h3>Closure readiness checklist</h3>
  <ol class="closure-checklist">
{items}
  </ol>""".rstrip()


def _timeline(events: list[dict[str, Any]]) -> str:
    items = "\n".join(
        f"""
        <li>
          <span>{escape(str(event["sort_order"]))}</span>
          <strong>{escape(event["event_type"])}</strong>
          <code>{escape(event["event_id"])}</code>
        </li>""".rstrip()
        for event in events
    )
    return f"""
<section class="panel">
  <h2>Audit order</h2>
  <ol class="timeline">
{items}
  </ol>
</section>""".strip()


def _case_mode(state: dict[str, Any]) -> str:
    if state["closure_block_reason"] == "source_contradiction":
        return "escalated"
    return "controlled"


def _route_label(state: dict[str, Any], policy: dict[str, Any]) -> str:
    if policy["to_stage"] == "human_review" or state["closure_block_reason"] == "source_contradiction":
        return "Escalated exception review"
    return "Controlled verification retry"


_CSS = """
:root {
  color-scheme: light;
  --bg: #fbfaf5;
  --surface: #ffffff;
  --ink: #252826;
  --muted: #62675f;
  --line: #d5c8b8;
  --line-soft: #e8e0d6;
  --strong: #17385f;
  --warn: #aa522f;
  --danger: #b42318;
  --blue: #2556a3;
  --controlled: #227268;
  --escalated: #b42318;
  --shadow: 0 1px 2px rgba(35, 38, 34, 0.06), 0 12px 36px rgba(35, 38, 34, 0.05);
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background-color: var(--bg);
  background-image:
    linear-gradient(rgba(213, 200, 184, 0.16) 1px, transparent 1px),
    linear-gradient(90deg, rgba(213, 200, 184, 0.12) 1px, transparent 1px);
  background-size: 44px 44px;
  color: var(--ink);
  font: 14.5px/1.58 ui-sans-serif, -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", sans-serif;
  -webkit-font-smoothing: antialiased;
}

.page {
  max-width: 1280px;
  margin: 0 auto;
  padding: 24px;
}

.topbar {
  display: grid;
  grid-template-columns: minmax(250px, 0.75fr) minmax(660px, 1.65fr);
  align-items: center;
  gap: 24px;
  border-bottom: 2px double var(--line);
  padding-bottom: 20px;
  margin-bottom: 24px;
}

.topbar.controlled {
  border-top: 4px solid var(--controlled);
  padding-top: 16px;
}

.topbar.escalated {
  border-top: 4px solid var(--escalated);
  padding-top: 16px;
}

.proof-strip {
  display: grid;
  grid-template-columns: repeat(5, minmax(140px, 1fr));
  gap: 12px;
  margin-bottom: 24px;
}

.proof-strip div {
  background: var(--strong);
  color: var(--bg);
  border: 1px solid rgba(23, 56, 95, 0.12);
  border-radius: 6px;
  padding: 14px;
  min-height: 84px;
  box-shadow: var(--shadow);
}

.proof-strip span {
  display: block;
  color: rgba(251, 250, 245, 0.74);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.04em;
  margin-bottom: 6px;
  text-transform: uppercase;
}

.proof-strip strong {
  display: block;
  font-size: 15px;
  line-height: 1.25;
  overflow-wrap: anywhere;
}

.decision-compare {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 48px minmax(0, 1fr);
  gap: 16px;
  align-items: stretch;
  margin-bottom: 24px;
}

.decision-compare article,
.route-banner {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 20px;
  box-shadow: var(--shadow);
}

.decision-compare.controlled article:first-child {
  border-left: 4px solid var(--warn);
}

.decision-compare.controlled article:nth-of-type(2),
.decision-compare.controlled .route-banner {
  border-left: 4px solid var(--controlled);
}

.decision-compare.escalated article:first-child {
  border-left: 4px solid var(--warn);
}

.decision-compare.escalated article:nth-of-type(2),
.decision-compare.escalated .route-banner {
  border-left: 4px solid var(--escalated);
}

.decision-compare h2 {
  font-size: 24px;
  line-height: 1.15;
  margin-bottom: 16px;
  overflow-wrap: break-word;
}

.eyebrow {
  display: block;
  color: var(--muted);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  margin-bottom: 8px;
  text-transform: uppercase;
}

.override-arrow {
  align-self: center;
  color: var(--muted);
  font-size: 24px;
  font-weight: 700;
  text-align: center;
}

.route-banner {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 240px minmax(0, 1fr) minmax(240px, auto);
  gap: 16px;
  align-items: center;
}

.route-banner span {
  color: var(--muted);
  font-weight: 700;
}

.route-banner strong,
.route-banner em {
  overflow-wrap: break-word;
}

.route-banner em {
  color: var(--danger);
  font-style: normal;
  font-weight: 700;
  background: rgba(180, 35, 24, 0.08);
  border: 1px solid rgba(180, 35, 24, 0.16);
  border-radius: 6px;
  padding: 4px 10px;
}

h1, h2, h3, p { margin-top: 0; }
h1 { color: var(--strong); font-size: 28px; line-height: 1.16; margin-bottom: 6px; }
h2 { color: var(--strong); font-size: 17px; margin-bottom: 14px; }
h3 { color: var(--strong); font-size: 14px; margin-bottom: 10px; }
p { color: var(--muted); }

.summary {
  display: grid;
  grid-template-columns: repeat(3, minmax(190px, 1fr));
  gap: 12px;
  margin: 0;
}

.summary div {
  display: block;
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid var(--line);
  border-radius: 6px;
  box-shadow: var(--shadow);
  padding: 12px 14px;
}

.summary dt {
  margin-bottom: 6px;
}

.summary dd {
  line-height: 1.35;
}

.layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 360px;
  gap: 16px;
  min-width: 0;
}

.primary, .side {
  display: grid;
  gap: 16px;
  align-content: start;
  min-width: 0;
}

.panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 20px;
  box-shadow: var(--shadow);
  min-width: 0;
}

.platform-note {
  border-left: 4px solid var(--blue);
  background: linear-gradient(90deg, rgba(37, 86, 163, 0.04), var(--surface) 40%);
}

.boundary-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.boundary article {
  border: 1px solid var(--line-soft);
  background: rgba(251, 250, 245, 0.54);
  border-radius: 6px;
  padding: 14px;
}

.triage-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  margin-top: 16px;
}

.triage-grid article {
  border: 1px solid var(--line-soft);
  background: rgba(251, 250, 245, 0.54);
  border-radius: 6px;
  padding: 14px;
}

.adversarial {
  border-left: 4px solid var(--danger);
  background: linear-gradient(90deg, rgba(180, 35, 24, 0.035), var(--surface) 34%);
}

.adversarial-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin: 14px 0;
}

.adversarial-grid article {
  border: 1px solid var(--line-soft);
  background: rgba(251, 250, 245, 0.54);
  border-radius: 6px;
  padding: 14px;
}

.disagreement-score {
  display: grid;
  grid-template-columns: 180px minmax(0, 1fr) minmax(140px, auto);
  gap: 12px;
  align-items: center;
  background: #fff7ed;
  border: 1px solid #f7c9a7;
  border-radius: 6px;
  padding: 12px;
}

.disagreement-score span,
.disagreement-score em {
  color: var(--muted);
  font-style: normal;
}

.disagreement-score strong {
  color: var(--danger);
  font-size: 22px;
}

dl {
  display: grid;
  gap: 8px;
  margin: 0;
}

dl div {
  display: grid;
  grid-template-columns: 140px minmax(0, 1fr);
  gap: 12px;
  border-bottom: 1px dotted var(--line-soft);
  padding-bottom: 4px;
}

dl div:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

dt {
  color: var(--muted);
  font-size: 13px;
}

dd {
  margin: 0;
  color: var(--ink);
  font-weight: 600;
  overflow-wrap: anywhere;
}

.table-scroll {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  max-width: 100%;
  width: 100%;
}

table {
  width: 100%;
  border-collapse: collapse;
  min-width: 760px;
  margin-top: 8px;
}

th, td {
  border-bottom: 1px solid var(--line-soft);
  padding: 11px 9px;
  text-align: left;
  vertical-align: top;
}

th {
  color: var(--strong);
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.actions {
  margin: 0;
  padding-left: 18px;
}

.closure-checklist {
  display: grid;
  gap: 10px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.closure-checklist li {
  border: 1px solid var(--line-soft);
  border-radius: 6px;
  padding: 10px;
}

.closure-checklist li.blocked {
  border-color: rgba(180, 35, 24, 0.22);
  background: rgba(180, 35, 24, 0.05);
}

.closure-checklist li.satisfied {
  border-color: rgba(34, 114, 104, 0.22);
  background: rgba(34, 114, 104, 0.05);
}

.closure-checklist strong,
.closure-checklist span {
  display: block;
}

.closure-checklist span {
  color: var(--muted);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.04em;
  margin-top: 4px;
  text-transform: uppercase;
}

.closure-checklist p {
  margin: 6px 0 0;
}

.guardrail {
  margin: 16px 0 0;
  color: var(--danger);
  font-weight: 700;
  background: rgba(180, 35, 24, 0.08);
  border: 1px solid rgba(180, 35, 24, 0.16);
  border-radius: 6px;
  padding: 10px 12px;
}

.status,
.authority {
  display: inline-block;
  border-radius: 6px;
  border: 1px solid var(--line);
  padding: 2px 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.status {
  background: rgba(34, 114, 104, 0.10);
  color: var(--strong);
}

.authority {
  background: rgba(37, 86, 163, 0.08);
  color: var(--blue);
}

.timeline {
  display: grid;
  gap: 10px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.timeline li {
  display: grid;
  grid-template-columns: 32px minmax(0, 1fr);
  gap: 8px 12px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 10px;
}

.timeline span {
  grid-row: span 2;
  color: var(--strong);
  font-weight: 700;
}

code {
  color: var(--muted);
  white-space: normal;
  overflow-wrap: anywhere;
}

@media (max-width: 900px) {
  .topbar, .layout, .boundary-grid, .summary, .proof-strip, .decision-compare, .route-banner, .triage-grid, .adversarial-grid, .disagreement-score {
    display: block;
  }

  .summary, .side, .proof-strip div + div, .decision-compare article + article, .route-banner strong, .route-banner em {
    margin-top: 16px;
  }

  .override-arrow {
    margin: 10px 0;
  }

  .panel + .panel,
  .primary + .side,
  .triage-grid article + article,
  .adversarial-grid article + article {
    margin-top: 16px;
  }
}
""".strip()
