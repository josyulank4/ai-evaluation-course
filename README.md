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

## Per-lesson checkpoints (hands-on format)

The course's hands-on lessons follow the founder's Hands-On Format Rule: the code is written on screen step by step, the real run — output, logs, and failures before fixes — is shown, the narration explains each step and why, and this repo is shared with per-lesson checkpoints. For every DEMO lesson there are two git tags:

- `lXX-start` — the repo state before the lesson's package is written: check this out to follow the lesson from the same starting point as the video.
- `lXX-finish` — the exact code as it runs at the end of the lesson video: check this out to compare against your own work. `python3 validate.py` passes at every `*-finish` tag.

| Lesson | Package | Start tag | Finish tag |
|---|---|---|---|
| L9 Build Your First Golden Set and Scoring Harness | evalkit | `l09-start` | `l09-finish` |
| L18 Build a Calibrated LLM Judge | graders | `l18-start` | `l18-finish` |
| L22 Agreement and Significance on Real Scores | stats4eval | `l22-start` | `l22-finish` |
| L26 Detect Drift Before Your Users Do | driftwatch | `l26-start` | `l26-finish` |
| L30 Calibrate Raters and Adjudicate Disagreements | humaneval | `l30-start` | `l30-finish` |
| L34 Build a Guardrail Pipeline That Logs Every Decision | guardrails | `l34-start` | `l34-finish` |
| L38 Run a Red-Team Session Against Your Own System | redteam | `l38-start` | `l38-finish` |
| L42 Sample Production Traffic and Evaluate It Live | onlineeval | `l42-start` | `l42-finish` |
| L46 Wire the Evaluation Gate Into Your Release Pipeline | gatekeeper | `l46-start` | `l46-finish` |
| L50 The Production Readiness Review, Run End to End | readiness | `l50-start` | `l50-finish` |

Tags are created as each DEMO lesson is produced (build first, make it pass, then record the replay — nothing is narrated that was not executed). The design state of the repo carries the full package set; the tags mark the per-lesson journey through it.

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
