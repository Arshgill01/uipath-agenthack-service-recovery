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
            _policy_boundary(agent, policy),
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
    <span>{escape(_route_label(state))}</span>
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
  <p class="guardrail">Closure is not available until fresh authoritative service evidence confirms recovery.</p>
</section>""".strip()


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


def _route_label(state: dict[str, Any]) -> str:
    if state["closure_block_reason"] == "source_contradiction":
        return "Escalated exception review"
    return "Controlled verification retry"


_CSS = """
:root {
  color-scheme: light;
  --bg: #f6f7f4;
  --surface: #ffffff;
  --ink: #171a16;
  --muted: #60675e;
  --line: #d8ddd4;
  --strong: #0f766e;
  --warn: #b45309;
  --danger: #b42318;
  --blue: #1d4ed8;
  --controlled: #0f766e;
  --escalated: #b42318;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 14px/1.5 ui-sans-serif, -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
}

.page {
  max-width: 1280px;
  margin: 0 auto;
  padding: 24px;
}

.topbar {
  display: grid;
  grid-template-columns: minmax(260px, 1fr) auto;
  align-items: flex-start;
  gap: 24px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 18px;
  margin-bottom: 18px;
}

.topbar.controlled {
  border-top: 6px solid var(--controlled);
  padding-top: 14px;
}

.topbar.escalated {
  border-top: 6px solid var(--escalated);
  padding-top: 14px;
}

.proof-strip {
  display: grid;
  grid-template-columns: repeat(5, minmax(140px, 1fr));
  gap: 10px;
  margin-bottom: 16px;
}

.proof-strip div {
  background: var(--ink);
  color: #ffffff;
  border-radius: 8px;
  padding: 12px;
  min-height: 76px;
}

.proof-strip span {
  display: block;
  color: #cfd6cc;
  font-size: 12px;
  margin-bottom: 6px;
}

.proof-strip strong {
  display: block;
  font-size: 14px;
  overflow-wrap: break-word;
}

.decision-compare {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 44px minmax(0, 1fr);
  gap: 12px;
  align-items: stretch;
  margin-bottom: 16px;
}

.decision-compare article,
.route-banner {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px;
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
  margin-bottom: 14px;
  overflow-wrap: break-word;
}

.eyebrow {
  display: block;
  color: var(--muted);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0;
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
  grid-template-columns: 220px minmax(0, 1fr) minmax(220px, auto);
  gap: 14px;
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
}

h1, h2, h3, p { margin-top: 0; }
h1 { font-size: 24px; line-height: 1.2; margin-bottom: 6px; }
h2 { font-size: 16px; margin-bottom: 14px; }
h3 { font-size: 14px; margin-bottom: 10px; }
p { color: var(--muted); }

.summary {
  display: grid;
  grid-template-columns: repeat(3, minmax(180px, 1fr));
  gap: 12px;
  margin: 0;
}

.layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 360px;
  gap: 16px;
}

.primary, .side {
  display: grid;
  gap: 16px;
  align-content: start;
}

.panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px;
}

.platform-note {
  border-left: 4px solid var(--blue);
}

.boundary-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.boundary article {
  border: 1px solid var(--line);
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
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 14px;
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
}

dt {
  color: var(--muted);
}

dd {
  margin: 0;
  overflow-wrap: break-word;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border-bottom: 1px solid var(--line);
  padding: 10px 8px;
  text-align: left;
  vertical-align: top;
}

th {
  color: var(--muted);
  font-weight: 600;
}

.actions {
  margin: 0;
  padding-left: 18px;
}

.guardrail {
  margin: 14px 0 0;
  color: var(--danger);
  font-weight: 700;
}

.status,
.authority {
  display: inline-block;
  border-radius: 999px;
  border: 1px solid var(--line);
  padding: 2px 8px;
  font-size: 12px;
}

.status {
  color: var(--strong);
}

.authority {
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
}

@media (max-width: 900px) {
  .topbar, .layout, .boundary-grid, .summary, .proof-strip, .decision-compare, .route-banner, .triage-grid {
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
  .triage-grid article + article {
    margin-top: 16px;
  }
}
""".strip()
