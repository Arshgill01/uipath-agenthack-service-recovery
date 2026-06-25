# UiPath AgentHack Service Recovery

Scaffolding repository for a UiPath AgentHack Maestro Case submission.

Start here:

1. [AGENTS.md](AGENTS.md)
2. [PROJECT_BRIEF.md](PROJECT_BRIEF.md)
3. [PLAN.md](PLAN.md)
4. [waves/00_WAVES_INDEX.md](waves/00_WAVES_INDEX.md)
5. [docs/validation/VALIDATION_GATES.md](docs/validation/VALIDATION_GATES.md)
6. [docs/product/PRODUCT_FEEDBACK_AWARD.md](docs/product/PRODUCT_FEEDBACK_AWARD.md)
7. [docs/submission/SUBMISSION_BRIEF.md](docs/submission/SUBMISSION_BRIEF.md)

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

- UiPath Labs access and Maestro Case validation have run against org `keepingitlowkey`, tenant `DefaultTenant`.
- G-001 is PARTIAL natively and PASS with the custom UiPath-hosted audit artifact fallback.
- G-002 is PASS for explicit package/process/artifact policy-version pinning.
- G-003 is PASS for Action Center lifecycle/structured reviewer return and PARTIAL for generated Action Center UI legibility.
- G-004 is PASS for persisted raw agent recommendation and linked policy decision in task/API/audit data.
- The demo-safe proof path is: Action Center for human-task lifecycle, custom evidence packet for judge-readable proof, and Orchestrator bucket audit bundle for durable UiPath-hosted domain audit evidence.

Repeatable demo proof:

```sh
scripts/run_demo.sh --with-local-checks
```

This refreshes and verifies the E-002/E-004 proof artifacts without mutating the live tenant.
