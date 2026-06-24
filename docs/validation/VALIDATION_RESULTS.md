# Validation Results

UiPath Labs hard gate validation has not been run yet.

Use [VALIDATION_GATES.md](VALIDATION_GATES.md) for pass/fail criteria.

Until hard gates G-001 through G-004 are answered, the data model and UiPath integration map remain provisional.

## 2026-06-18 - Local Provisional Core Baseline

Environment:

- Local Python 3.9.12.
- No UiPath Labs tenant or Maestro Case surface used.

Steps:

1. Installed local package with `python -m pip install .`.
2. Ran unit tests with `python -m unittest discover -s tests`.
3. Ran eval baseline with `python -m service_recovery_core.evals --output eval_results/local_baseline.json`.

Observed:

- Package build/install completed.
- Unit suite ran 16 tests.
- Eval suite ran E-001 through E-009 with 9/9 passing.
- E-009 persisted the raw agent recommendation and policy decision as separate linked events.

Result:

- PASS for local/provisional validation only.
- Not a UiPath Labs validation result.

Decision impact:

- Waves 07-14 are stable enough for local development.
- Wave 22 baseline is stable enough as a portable harness pending Test Cloud mapping.

Follow-up:

- Run G-001 through G-004 when Labs access is available.
- Map local eval scenarios to UiPath/Test Cloud only after platform assumptions are verified.

## 2026-06-24 - Wave 01 Platform Access And Inventory

Environment:

- Local macOS development machine.
- Safari opened to UiPath Automation Cloud for interactive Google login by the user.
- Controlled `agent-browser` Chromium session was available but did not inherit the user's Zen browser login.
- Node `v22.21.0`, npm `10.9.4`.
- UiPath CLI package `@uipath/cli` installed globally during this run.

Steps:

1. Confirmed repo status with `git status --short --branch`.
2. Confirmed recent commits with `git log --oneline -5`.
3. Re-ran local validation with `python -m unittest discover -s tests`.
4. Re-ran local eval baseline with `python -m service_recovery_core.evals --output eval_results/local_baseline.json`.
5. Checked for `uip` before install with `command -v uip && uip --version`.
6. Checked npm metadata with `npm view @uipath/cli version bin --json`.
7. Installed CLI with `npm install -g @uipath/cli@1.196.0`.
8. Verified CLI with `uip --version`.
9. Opened `https://cloud.uipath.com` in a controlled browser session and in Safari.
10. Started `uip login`; stopped it after it waited without producing a usable prompt in the terminal.

Observed:

- Repo was clean on `master...origin/master`.
- Latest commit remained `17a7017 Build local provisional service recovery core`.
- Unit suite ran 16 tests and passed.
- Eval suite ran E-001 through E-009 with 9/9 passing.
- `uip` was initially unavailable on PATH.
- `@uipath/cli` published version observed from npm was `1.196.0`; after install, `uip --version` returned `1.196.0`.
- Controlled browser reached the UiPath login page but was not authenticated.
- Safari reached `https://cloud.uipath.com/portal_/missingaccount` after the user attempted login, indicating authentication did not land in an accessible Automation Cloud account/tenant in that browser session.
- Access could not be confirmed for Maestro, Maestro Case, Studio Web, Action Center, Test Cloud/Test Manager, Integration Service, or Orchestrator.

Result:

- PARTIAL for Wave 01.
- PASS for local repo and local validation readiness.
- PASS for CLI installation/version verification.
- BLOCKED for UiPath tenant and product-surface inventory.
- NOT RUN for hard gates G-001 through G-004 because authenticated Labs tenant access was not available.

Decision impact:

- Do not start broad UiPath implementation.
- Keep Maestro Case, Action Center, Test Cloud, Integration Service, and Orchestrator mappings provisional.
- Hard validation gates remain blocked until the user account is associated with the correct UiPath Labs Automation Cloud organization/tenant or an inspectable authenticated browser session is available.

Follow-up:

- Resolve UiPath account/tenant access for `arshgill6120@gmail.com`.
- Re-run Wave 01 surface inventory after Automation Cloud lands in a tenant instead of `portal_/missingaccount`.
- Run `uip login` again only when the browser/device-code flow can be completed interactively.
- Run G-001 through G-004 only after Maestro Case access is confirmed.
