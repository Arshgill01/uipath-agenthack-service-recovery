#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

ARTIFACT_DIR="${ARTIFACT_DIR:-docs/demo/artifacts}"

usage() {
  cat <<'EOF'
Usage: scripts/run_submission_check.sh

Runs the non-mutating local submission sanity check:
  - unit tests
  - local eval suite
  - existing E-002/E-004 demo proof artifact verification
  - LLM/adversarial proof artifact presence and key-string checks
  - governed learning-loop artifact presence and key-string checks
  - shell syntax checks for demo wrappers

This command does not start live UiPath cases, complete Action Center tasks, or
call Gemini/Vertex. Use run_demo.sh or run_llm_demo.sh intentionally for those.
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -gt 0 ]]; then
  echo "Unknown option: $1" >&2
  usage >&2
  exit 2
fi

python -m unittest discover -s tests
python -m service_recovery_core.evals --output /tmp/service_recovery_local_baseline.json >/dev/null
python -m service_recovery_core.demo_proof --output-dir "$ARTIFACT_DIR" --verify-only >/dev/null

bash -n scripts/run_demo.sh
bash -n scripts/run_llm_demo.sh
bash -n scripts/run_test_manager_manual_eval.sh

test -f "$ARTIFACT_DIR/evidence_packet_E002.html"
test -f "$ARTIFACT_DIR/evidence_packet_E004.html"
test -f "$ARTIFACT_DIR/demo_proof_manifest.json"
test -f "$ARTIFACT_DIR/llm_interpreter_E003_live.json"
test -f "$ARTIFACT_DIR/llm_interpreter_E003_adversarial_live.json"
test -f "$ARTIFACT_DIR/evidence_packet_E003_adversarial_live.html"
test -f "$ARTIFACT_DIR/evidence_packet_E003_adversarial_desktop.png"
test -f "$ARTIFACT_DIR/evidence_packet_E003_adversarial_mobile.png"
test -f "$ARTIFACT_DIR/policy_improvement_E008.json"

rg "closure_candidate -> verify_telemetry|missing_authoritative_signal|Raw agent interpretation|Final policy decision" \
  "$ARTIFACT_DIR/evidence_packet_E002.html" >/dev/null
rg "closure_candidate -> human_review|source_contradiction|Raw agent interpretation|Final policy decision" \
  "$ARTIFACT_DIR/evidence_packet_E004.html" >/dev/null
rg "Adversarial dual interpretation|Resolution advocate|Closure skeptic|closure_candidate -> human_review|high_interpretation_disagreement" \
  "$ARTIFACT_DIR/evidence_packet_E003_adversarial_live.html" >/dev/null
rg "policy_improvement_case|pending_human_approval|not_promoted|active_cases_remain_pinned_until_explicit_migration_event|ip-v2-proposed" \
  "$ARTIFACT_DIR/policy_improvement_E008.json" >/dev/null

cat <<EOF
Submission check passed.
Artifacts verified in: $ARTIFACT_DIR
EOF
