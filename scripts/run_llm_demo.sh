#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

SCENARIO_ID="${SCENARIO_ID:-E-003}"
MODEL="${MODEL:-gemini-3-flash}"
LOCATION="${LOCATION:-us-central1}"
OUTPUT="${OUTPUT:-eval_results/llm_interpreter_${SCENARIO_ID}.json}"
PROJECT="${PROJECT:-${GOOGLE_CLOUD_PROJECT:-${GOOGLE_PROJECT_ID:-}}}"

usage() {
  cat <<'EOF'
Usage: scripts/run_llm_demo.sh [--scenario-id E-003] [--model gemini-3-flash] [--project PROJECT_ID] [--location us-central1] [--output PATH] [--adversarial]

Runs the optional Gemini-backed LLM interpretation proof.

Auth options:
  - GEMINI_API_KEY or GOOGLE_API_KEY for Gemini API
  - --project PROJECT_ID with Application Default Credentials for Vertex AI

The command writes JSON to the output path. If auth is unavailable, the JSON
contains status=blocked and the next required action.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scenario-id)
      SCENARIO_ID="$2"
      shift
      ;;
    --model)
      MODEL="$2"
      shift
      ;;
    --project)
      PROJECT="$2"
      shift
      ;;
    --location)
      LOCATION="$2"
      shift
      ;;
    --output)
      OUTPUT="$2"
      shift
      ;;
    --adversarial)
      ADVERSARIAL=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

mkdir -p "$(dirname "$OUTPUT")"

cmd=(python -m service_recovery_core.llm_interpreter --scenario-id "$SCENARIO_ID" --model "$MODEL" --location "$LOCATION" --output "$OUTPUT")
if [[ -n "$PROJECT" ]]; then
  cmd+=(--project "$PROJECT")
fi
if [[ "${ADVERSARIAL:-0}" == "1" ]]; then
  cmd+=(--adversarial)
fi

set +e
"${cmd[@]}"
exit_code=$?
set -e

cat <<EOF

LLM demo output: $OUTPUT
LLM demo exit code: $exit_code
EOF

if [[ "$exit_code" -eq 0 ]]; then
  cat <<'EOF'
Status: live LLM interpretation succeeded. Inspect agent_interpretation_event and policy_decision_event in the output JSON.
EOF
elif [[ "$exit_code" -eq 2 ]]; then
  cat <<'EOF'
Status: LLM run did not produce a usable governed event. Inspect the output JSON; common causes are missing auth or schema validation failure.
EOF
else
  cat <<'EOF'
Status: failed unexpectedly. Inspect the output above and do not claim live LLM validation.
EOF
fi

exit "$exit_code"
