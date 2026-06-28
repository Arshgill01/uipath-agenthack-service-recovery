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
8. [docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md](docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md)

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

Coding-agent proof:

This project used Codex as the coding agent for build-time implementation, validation, UiPath CLI investigation, product-feedback evidence gathering, and submission documentation. The auditable proof package is [docs/submission/CODING_AGENT_PROOF_LOG.md](docs/submission/CODING_AGENT_PROOF_LOG.md). It maps what Codex did, what humans decided, which commits/branches/docs prove the work, and the safety boundary: Codex is not runtime closure authority; deterministic policy, UiPath Maestro Case routing, and human review remain the governance path.

Fast audit commands:

```sh
git log --oneline --decorate --max-count=40
git branch --all --verbose --no-abbrev
scripts/run_submission_check.sh
```

UiPath component summary:

- Maestro Case: primary track and orchestration boundary for dynamic exception-heavy casework.
- Action Center: human task lifecycle, reviewer action/comment, and structured return.
- Orchestrator: package/process/job readback and bucket-backed audit artifact storage.
- Data Fabric: validated full-payload audit readback path for E-004.
- Test Manager: manual representation and terminal execution evidence for E-001 through E-009.
- UiPath CLI: repeatable packaging, readback, validation, task, Test Manager, and Data Fabric evidence collection.

The connected platform-depth proof map is maintained in [docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md](docs/submission/PLATFORM_INTEGRATION_PROOF_MAP.md). It separates native UiPath proof, custom judge-readable evidence packets, and local deterministic policy proof.

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
