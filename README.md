# AI Evaluation & Guardrails — Course Code

Companion code for **AI Evaluation & Guardrails: Production-Grade
Evaluation Systems** (Udemy Course 6) by Naveen Kumar Josyula.

Every demo is small, self-contained, and runs **offline with no API
keys**: Python standard library only. The demos implement the
evaluation machinery transparently — a golden-set harness, a rubric
judge, agreement statistics, drift detection, a human review round, a
guardrail pipeline, a red-team suite, an online sampler, a release
gate and a readiness review — so students see exactly what evaluation
tools do, then map each piece to the real platforms.

## Requirements

- Python 3.11+
- No third-party packages (`requirements.txt` is intentionally empty)

## How to run each demo

Run from the repo root:

| Area | Command | What it shows |
|---|---|---|
| Golden sets | `python -m evalkit.goldenset` | A 6-case golden set scoring two triage systems on success and tool correctness |
| LLM judges | `python -m graders.judge` | A rubric judge, the verbosity trap, and a calibration check against human labels |
| Statistics | `python -m stats4eval.agreement` | Cohen's kappa and a Wilson interval, computed by hand |
| Drift | `python -m driftwatch.drift` | Label-mix and length drift between two dataset versions, with an alert verdict |
| Human evaluation | `python -m humaneval.review` | A review round with hidden gold items, annotator accuracy and adjudication |
| Guardrails | `python -m guardrails.pipeline` | Input/output guardrail checks with a full audit log |
| Red team | `python -m redteam.suite` | An adversarial suite against a naive stub — including the breach it finds |
| Online evaluation | `python -m onlineeval.sampler` | Production sampling that catches a silent quality drift and raises an alert |
| Release gates | `python -m gatekeeper.gate` | A CI regression gate that blocks a release on a faithfulness drop |
| Readiness | `python -m readiness.review` | The capstone evaluation readiness review: GO / NO-GO with named blockers |

## Validation

`python validate.py` runs every demo end to end as a subprocess, checks
the expected output markers, and adds direct assertions per module.
It exits non-zero if anything fails.
