# Build Log

Append one entry per substantial agent run.

## Template

### YYYY-MM-DD HH:MM - Agent / Wave

What changed:

- ...

Commands run:

- `...`

Validation:

- PASS / FAIL / PARTIAL

Open risks:

- ...

Next:

- ...

## 2026-06-18 - Scaffolding Setup

What changed:

- Created initial repository scaffolding documents.
- Added operating rules, project brief, high-level plan, research log, decision log, architecture/validation/doc directories, local skills directory, and wave plan skeleton.

Commands run:

- See final report for this run.

Validation:

- Pending final structure scan.

Open risks:

- UiPath Labs platform assumptions remain unvalidated.

### 2026-06-18 20:10 IST - Agent / Waves 07-14, 22

What changed:

- Selected dependency-free Python local core stack.
- Added package foundation, `.env.example`, JSON eval fixtures, schema validators, agent output validator, deterministic reconciliation/closure policy, local case state machine, and eval runner.
- Added unit tests for evidence/case schemas, invalid agent outputs, canonical business-green fixture discipline, closure blocking, distinct missing/stale vs contradiction routes, event persistence, and eval baseline.
- Represented E-008 usefulness degradation as an eval incident and E-009 override persistence as linked agent/policy events.

Commands run:

- `python -m unittest`
- `python -m unittest discover -s tests`
- `python -m service_recovery_core.evals --output eval_results/local_baseline.json`
- `python -m pip install -e .`
- `python -m pip install .`
- `python -m compileall service_recovery_core tests`

Validation:

- PASS: `python -m pip install .`
- PASS: `python -m compileall service_recovery_core tests`
- PASS: `python -m unittest discover -s tests` ran 16 tests.
- PASS: `python -m service_recovery_core.evals --output eval_results/local_baseline.json` passed 9/9 eval scenarios.
- PARTIAL: `python -m unittest` ran 0 tests because explicit discovery is required.
- FAIL: `python -m pip install -e .` failed in this Python 3.9/older pip environment because editable install invoked a Python environment without `pip`; non-editable local install passed.

Open risks:

- UiPath Labs hard gates G-001 through G-004 remain unvalidated.
- Local case state machine and audit events are provisional and not yet mapped to Maestro Case native state/history.
- Test Cloud integration is not implemented; the eval harness is local and portable.

Next:

- Do not start UiPath implementation waves until Labs access is granted and hard gates are run or explicitly waived.
