#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

ARTIFACT_DIR="${ARTIFACT_DIR:-docs/demo/artifacts}"
PYTHON="${PYTHON_BIN:-${PYTHON:-}}"

if [[ -z "${PYTHON:-}" ]]; then
  if command -v python >/dev/null 2>&1; then
    PYTHON="$(command -v python)"
  elif command -v python3 >/dev/null 2>&1; then
    PYTHON="$(command -v python3)"
  else
    echo "Python executable not found. Set PYTHON=/path/to/python3 and retry." >&2
    exit 127
  fi
fi

usage() {
  cat <<'EOF'
Usage: scripts/run_submission_check.sh

Runs the non-mutating local submission sanity check:
  - unit tests
  - local eval suite
  - policy-boundary hardening report
  - Test Manager manual-evidence bridge verifier
  - existing E-002/E-004 demo proof artifact verification
  - generated proof index verification
  - final-form claim-boundary overclaim scanning
  - parsed final proof index for track, coding-agent, feedback, LLM, and learning-loop artifacts
  - LLM/adversarial proof artifact presence and key-string checks
  - governed learning-loop artifact presence and key-string checks
  - platform integration proof-map presence and key-string checks
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

"$PYTHON" -m unittest discover -s tests
"$PYTHON" -m service_recovery_core.evals --output /tmp/service_recovery_local_baseline.json >/dev/null
"$PYTHON" -m service_recovery_core.evals --policy-boundary-report --output /tmp/service_recovery_policy_boundary_report.json >/dev/null
"$PYTHON" -m service_recovery_core.test_manager_bridge \
  --eval-results /tmp/service_recovery_local_baseline.json \
  --junit docs/validation/artifacts/test-manager-results/Service_Recovery_E_001_through_E_009_Baseline___20260626_1017.xml \
  --execution-stats docs/validation/artifacts/2026-06-28/test-manager-feasibility-spike/04-tm-terminal-execution-stats.json \
  --output /tmp/service_recovery_test_manager_bridge.json >/dev/null
"$PYTHON" -m service_recovery_core.demo_proof --output-dir "$ARTIFACT_DIR" --verify-only >/dev/null
"$PYTHON" -m service_recovery_core.proof_index --artifact-dir "$ARTIFACT_DIR" --verify-only >/dev/null
"$PYTHON" -m service_recovery_core.submission_proof --artifact-dir "$ARTIFACT_DIR" >/dev/null

bash -n scripts/run_demo.sh
bash -n scripts/run_llm_demo.sh
bash -n scripts/run_test_manager_manual_eval.sh

test -f "$ARTIFACT_DIR/evidence_packet_E002.html"
test -f "$ARTIFACT_DIR/evidence_packet_E004.html"
test -f "$ARTIFACT_DIR/demo_proof_manifest.json"
test -f "$ARTIFACT_DIR/proof_index.html"
test -f "$ARTIFACT_DIR/llm_interpreter_E003_live.json"
test -f "$ARTIFACT_DIR/llm_interpreter_E003_adversarial_live.json"
test -f "$ARTIFACT_DIR/evidence_packet_E003_adversarial_live.html"
test -f "$ARTIFACT_DIR/evidence_packet_E003_adversarial_desktop.png"
test -f "$ARTIFACT_DIR/evidence_packet_E003_adversarial_mobile.png"
test -f "$ARTIFACT_DIR/policy_improvement_E008.json"
test -f docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md

rg "closure_candidate -> verify_telemetry|missing_authoritative_signal|Raw agent interpretation|Final policy decision" \
  "$ARTIFACT_DIR/evidence_packet_E002.html" >/dev/null
rg "closure_candidate -> human_review|source_contradiction|Raw agent interpretation|Final policy decision" \
  "$ARTIFACT_DIR/evidence_packet_E004.html" >/dev/null
rg "Adversarial dual interpretation|Resolution advocate|Closure skeptic|closure_candidate -> human_review|high_interpretation_disagreement" \
  "$ARTIFACT_DIR/evidence_packet_E003_adversarial_live.html" >/dev/null
rg "Judge-facing proof index|Claim boundaries|not a replacement for UiPath Maestro Case|E-002|E-004|E-003|E-008|pending_human_approval" \
  "$ARTIFACT_DIR/proof_index.html" >/dev/null
rg "policy_improvement_case|pending_human_approval|not_promoted|active_cases_remain_pinned_until_explicit_migration_event|ip-v2-proposed" \
  "$ARTIFACT_DIR/policy_improvement_E008.json" >/dev/null

required_proof_map_strings=(
  "Native UiPath proof"
  "Custom judge-readable proof"
  "Local deterministic policy proof"
  "ServiceRecoveryAuditBundleV2"
  "SREV:9"
  "4300080"
  "4300219"
  "automated Test Cloud execution"
)

for required in "${required_proof_map_strings[@]}"; do
  rg "$required" docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md >/dev/null
done

cat <<EOF
Submission check passed.
Artifacts verified in: $ARTIFACT_DIR
EOF
