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
- Submission sanity check: `scripts/run_submission_check.sh`

Setup:

```sh
python -m pip install .
python -m unittest discover -s tests
python -m service_recovery_core.evals --output eval_results/local_baseline.json
```

The local core is intentionally portable and keeps deterministic policy independent from LLM output. It implements fixtures, schema validation, deterministic policy reconciliation, closure blocking, local case state transitions, and baseline eval scenarios E-001 through E-009. Optional Gemini/Vertex paths can produce live Agent Interpretation Events, including an adversarial advocate/skeptic interpretation, but policy remains the final routing authority.

Coding-agent use:

This project was built primarily with Codex as the coding agent, alongside UiPath CLI and repo-local validation scripts. Codex helped design and implement the local recovery core, evals, evidence-packet renderer, UiPath validation runbooks, product-feedback evidence logs, and submission readiness checks. The detailed coding-agent proof log is maintained in [docs/submission/CODING_AGENT_PROOF_LOG.md](docs/submission/CODING_AGENT_PROOF_LOG.md).

UiPath component summary:

- Maestro Case: primary track and orchestration boundary for dynamic exception-heavy casework.
- Action Center: human task lifecycle, reviewer action/comment, and structured return.
- Orchestrator: package/process/job readback and bucket-backed audit artifact storage.
- Data Fabric: validated full-payload audit readback path for E-004.
- Test Manager: manual representation and terminal execution evidence for E-001 through E-009.
- UiPath CLI: repeatable packaging, readback, validation, task, Test Manager, and Data Fabric evidence collection.

Validation status:

- UiPath Labs access and Maestro Case validation have run against org `keepingitlowkey`, tenant `DefaultTenant`.
- G-001 is PARTIAL natively and PASS with the custom UiPath-hosted audit artifact fallback.
- G-002 is PASS for explicit package/process/artifact policy-version pinning.
- G-003 is PASS for Action Center lifecycle/structured reviewer return and PARTIAL for generated Action Center UI legibility.
- G-004 is PASS for persisted raw agent recommendation and linked policy decision in task/API/audit data.
- The demo-safe proof path is: Action Center for human-task lifecycle, custom evidence packet for judge-readable proof, and Orchestrator bucket audit bundle for durable UiPath-hosted domain audit evidence.
- Live Gemini/Vertex proof artifacts exist for E-003, including `docs/demo/artifacts/evidence_packet_E003_adversarial_live.html` and desktop/mobile screenshots.

Repeatable local proof:

```sh
scripts/run_submission_check.sh
scripts/run_demo.sh --with-local-checks
```

`scripts/run_submission_check.sh` is non-mutating and verifies tests, evals, proof artifacts, proof strings, screenshots, and wrapper syntax. `scripts/run_demo.sh --with-local-checks` refreshes and verifies the E-002/E-004 proof artifacts without mutating the live tenant.
