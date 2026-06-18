# UiPath AgentHack Service Recovery

Scaffolding repository for a UiPath AgentHack Maestro Case submission.

Start here:

1. [AGENTS.md](AGENTS.md)
2. [PROJECT_BRIEF.md](PROJECT_BRIEF.md)
3. [PLAN.md](PLAN.md)
4. [waves/00_WAVES_INDEX.md](waves/00_WAVES_INDEX.md)
5. [docs/validation/VALIDATION_GATES.md](docs/validation/VALIDATION_GATES.md)

Current project direction:

> Telecom/broadband service activation and restoration exception workflow, proving that UiPath Maestro Case can govern agentic service recovery when evidence is missing, stale, contradicting, or adversarial.

Local provisional core status:

- Python package: `service_recovery_core`
- Fixtures: `fixtures/eval_scenarios.json`
- Tests: `python -m unittest discover -s tests`
- Evals: `python -m service_recovery_core.evals --output eval_results/local_baseline.json`

Setup:

```sh
python -m pip install .
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
```

The local core is intentionally portable and has no runtime dependencies outside the Python standard library. It implements provisional fixtures, schema validation, deterministic policy reconciliation, closure blocking, local case state transitions, and baseline eval scenarios E-001 through E-009.

Validation status:

- UiPath Labs hard gates have not been run.
- The data model is provisional until validation gates 1-4 are answered or explicitly waived.
- The local core does not implement Maestro-specific behavior; it is ready to map once Labs access is granted.
