#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

OUTPUT_DIR="${OUTPUT_DIR:-docs/demo/artifacts}"
RUN_LOCAL_CHECKS=0
SHOW_UIPATH_COMMANDS=1

usage() {
  cat <<'EOF'
Usage: scripts/run_demo.sh [--with-local-checks] [--no-uipath-next-steps]

Build and verify the demo-safe E-002/E-004 proof artifacts.

Default behavior is tenant-safe:
  - regenerate Action Center payloads, audit bundles, and evidence-packet HTML
  - verify raw AIE -> linked PDE proof fields
  - print the UiPath CLI readback/upload commands to run manually

Options:
  --with-local-checks       Also run unit tests and the full local eval suite.
  --no-uipath-next-steps    Suppress the printed UiPath CLI next-step commands.
  -h, --help                Show this help.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-local-checks)
      RUN_LOCAL_CHECKS=1
      ;;
    --no-uipath-next-steps)
      SHOW_UIPATH_COMMANDS=0
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

if [[ "$RUN_LOCAL_CHECKS" -eq 1 ]]; then
  python -m unittest discover -s tests
  python -m service_recovery_core.evals --output eval_results/local_baseline.json >/dev/null
fi

python -m service_recovery_core.demo_proof --output-dir "$OUTPUT_DIR" >/dev/null
python -m service_recovery_core.demo_proof --output-dir "$OUTPUT_DIR" --verify-only
python -m service_recovery_core.proof_index --artifact-dir "$OUTPUT_DIR" >/dev/null

cat <<EOF

Demo proof artifacts refreshed in $OUTPUT_DIR:
  - action_payload_E002.json
  - action_payload_E004.json
  - service_recovery_audit_bundle_E002.json
  - service_recovery_audit_bundle_E004.json
  - evidence_packet_E002.html
  - evidence_packet_E004.html
  - demo_proof_manifest.json
  - proof_index.html

Open the judge-facing packets:
  open "$ROOT_DIR/$OUTPUT_DIR/proof_index.html"
  open "$ROOT_DIR/$OUTPUT_DIR/evidence_packet_E002.html"
  open "$ROOT_DIR/$OUTPUT_DIR/evidence_packet_E004.html"
EOF

if [[ "$SHOW_UIPATH_COMMANDS" -eq 1 ]]; then
  cat <<'EOF'

Tenant-safe UiPath readback/upload commands to run when validating live evidence:

  uip login status --output json

  uip or processes get 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 --output json

  uip or processes version-history 9a7eb300-7b16-4856-b14f-d6f2da3dbe61 \
    --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de \
    --output json

  uip tasks get 4300080 --output json
  uip tasks get 4300219 --output json

  uip or bucket-files upload \
    dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb \
    audit/service_recovery_audit_bundle_E004.json \
    --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de \
    --file docs/demo/artifacts/service_recovery_audit_bundle_E004.json \
    --content-type application/json \
    --output json

  uip or bucket-files download \
    dc4c3bc3-fd8c-4143-93f0-57346f2b1ecb \
    audit/service_recovery_audit_bundle_E004.json \
    --folder-key 9d7ae568-d60e-4395-94d7-db115bfb25de \
    --destination eval_results/downloaded_audit_bundle_E004.json \
    --output json

  cmp -s docs/demo/artifacts/service_recovery_audit_bundle_E004.json \
    eval_results/downloaded_audit_bundle_E004.json \
    && echo bucket-download-matches

This script does not start fresh live cases or complete live tasks. Use it as the
repeatable local proof and operator checklist unless you intentionally run live
UiPath commands from the runbook.
EOF
fi
