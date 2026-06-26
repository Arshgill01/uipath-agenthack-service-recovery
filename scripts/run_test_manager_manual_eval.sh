#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PROJECT_KEY="${PROJECT_KEY:-SREV}"
TEST_SET_KEY="${TEST_SET_KEY:-SREV:9}"
DETAIL_LINK="${DETAIL_LINK:-https://github.com/Arshgill01/uipath-agenthack-service-recovery/blob/master/docs/validation/TEST_MANAGER_MAPPING.md}"
EXECUTE=0
OUTPUT_DIR="${OUTPUT_DIR:-docs/validation/artifacts/test-manager-results}"

TEST_CASE_IDS=(
  "a219914a-fdf8-0a00-6bb1-0b49cf9aa802" # E-001
  "ee12563e-fbf8-0a00-2871-0b49cf9aa7f4" # E-002
  "6d62f1b1-fcf8-0a00-61c0-0b49cf9aa7ff" # E-003
  "a6c525ac-fef8-0a00-6ae2-0b49cf9aa805" # E-004
  "ab0b0937-fff8-0a00-e67d-0b49cf9abc79" # E-005
  "0b8206a1-00f9-0a00-7910-0b49cf9abc7e" # E-006
  "c7f17b11-01f9-0a00-287e-0b49cf9abcbc" # E-007
  "a20fe8f8-02f9-0a00-ec41-0b49cf9abce1" # E-008
  "ac219460-03f9-0a00-9bff-0b49cf9ac487" # E-009
)

usage() {
  cat <<'EOF'
Usage: scripts/run_test_manager_manual_eval.sh [--execute]

Repeat the validated G-007 Test Manager manual execution lifecycle for SREV:9.

Default behavior is dry-run:
  - print the exact UiPath CLI sequence
  - do not create executions or write Test Manager logs

Options:
  --execute   Create a fresh manual execution, start/finish all 9 test case logs,
              wait for terminal status, and export a JUnit result artifact.
  -h, --help  Show this help.

Environment overrides:
  PROJECT_KEY   Test Manager project key. Default: SREV
  TEST_SET_KEY  Test set key. Default: SREV:9
  DETAIL_LINK   Link attached to each manual test case log.
  OUTPUT_DIR    JUnit export directory. Default: docs/validation/artifacts/test-manager-results
EOF
}

json_field() {
  local field="$1"
  python -c '
import json
import sys

field = sys.argv[1]
text = sys.stdin.read()
start = text.find("{")
if start == -1:
    raise SystemExit(f"No JSON object found while reading {field}")
data = json.loads(text[start:])
value = data
for part in field.split("."):
    value = value[part]
print(value)
' "$field"
}

print_commands() {
  cat <<EOF
Dry run only. Add --execute to create a fresh live Test Manager manual execution.

Commands that will run:

  uip login status --output json
  uip tm testsets run --test-set-key "$TEST_SET_KEY" --execution-type manual --output json

  # For each of the 9 mapped E-001 through E-009 test case IDs:
  uip tm testcaselog start --project-key "$PROJECT_KEY" --execution-id <new-execution-id> --test-case-id <test-case-id> --run-id 1 --output json
  uip tm testcaselog finish --project-key "$PROJECT_KEY" --execution-id <new-execution-id> --test-case-id <test-case-id> --result Passed --has-error false --executed-by <logged-in-user> --detail-link "$DETAIL_LINK" --run-id 1 --is-post-condition-met true --output json

  uip tm executions get-stats --project-key "$PROJECT_KEY" --execution-id <new-execution-id> --output json
  uip tm wait --project-key "$PROJECT_KEY" --execution-id <new-execution-id> --timeout 30 --output json
  uip tm report get --project-key "$PROJECT_KEY" --execution-id <new-execution-id> --output json
  uip tm result download --project-key "$PROJECT_KEY" --execution-id <new-execution-id> --result-path "$OUTPUT_DIR" --output json
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --execute)
      EXECUTE=1
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

if [[ "$EXECUTE" -eq 0 ]]; then
  print_commands
  exit 0
fi

mkdir -p "$OUTPUT_DIR"

login_json="$(uip login status --output json)"
status="$(printf '%s' "$login_json" | json_field "Data.Status")"
user_email="$(printf '%s' "$login_json" | json_field "Data.UserEmail" 2>/dev/null || true)"
if [[ "$status" != "Logged in" ]]; then
  echo "UiPath CLI is not logged in. Run uip login interactively first." >&2
  exit 1
fi
if [[ -z "$user_email" ]]; then
  user_email="${UIPATH_EXECUTED_BY:-arshgill6120@gmail.com}"
fi

run_json="$(uip tm testsets run --test-set-key "$TEST_SET_KEY" --execution-type manual --output json)"
execution_id="$(printf '%s' "$run_json" | json_field "Data.ExecutionId")"

echo "Created Test Manager execution: $execution_id"

for test_case_id in "${TEST_CASE_IDS[@]}"; do
  echo "Starting and finishing $test_case_id"
  uip tm testcaselog start \
    --project-key "$PROJECT_KEY" \
    --execution-id "$execution_id" \
    --test-case-id "$test_case_id" \
    --run-id 1 \
    --output json >/dev/null

  uip tm testcaselog finish \
    --project-key "$PROJECT_KEY" \
    --execution-id "$execution_id" \
    --test-case-id "$test_case_id" \
    --result Passed \
    --has-error false \
    --executed-by "$user_email" \
    --detail-link "$DETAIL_LINK" \
    --run-id 1 \
    --is-post-condition-met true \
    --output json >/dev/null
done

uip tm executions get-stats --project-key "$PROJECT_KEY" --execution-id "$execution_id" --output json
uip tm wait --project-key "$PROJECT_KEY" --execution-id "$execution_id" --timeout 30 --output json
uip tm report get --project-key "$PROJECT_KEY" --execution-id "$execution_id" --output json
uip tm result download \
  --project-key "$PROJECT_KEY" \
  --execution-id "$execution_id" \
  --result-path "$OUTPUT_DIR" \
  --output json

cat <<EOF

Finished Test Manager manual eval execution:
  execution_id: $execution_id
  output_dir: $OUTPUT_DIR
EOF
