# Agent Loop Protocol

Future agents should work in short, evidence-backed loops.

## Loop

1. **Goal**: identify the active wave and exact outcome.
2. **Context**: read relevant docs and current files.
3. **Plan**: state scoped steps and validation.
4. **Act**: make minimal changes.
5. **Observe**: run checks and inspect outputs.
6. **Reflect**: update logs, risks, decisions.
7. **Gate**: decide continue, stop, or escalate.

## Stop Conditions

Stop and ask or log a blocker when:

- a hard platform assumption is unverified,
- a change would weaken closure policy,
- a UiPath feature is unavailable,
- validation cannot run,
- scope drifts into generic platform territory,
- a decision affects architecture beyond the active wave.

## Eval Mindset

Convert failures into evals:

- What failed?
- Was it an agent schema failure, policy failure, evidence fixture issue, UI issue, or platform limitation?
- Can this be added as a labeled scenario?
- Does it require interpretation-policy or decision-policy change?

## Trace / Log Requirements

Every meaningful transition should produce or document:

- input evidence,
- agent interpretation event,
- policy decision event,
- stage transition,
- human action if any,
- audit explanation,
- validation result.

## Quality Loop

Do not "fix prompt and hope." The preferred loop is:

1. capture failure,
2. label failure,
3. add/adjust eval,
4. propose change,
5. run regression,
6. review,
7. promote version.
