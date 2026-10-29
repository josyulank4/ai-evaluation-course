"""A calibrated LLM-judge model (Lesson 18 demo).

A real LLM judge is a model; here the judge is a deterministic rubric
scorer so students can watch the mechanics: three rubric dimensions
scored independently, a verbosity trap (the longer answer scores
WORSE because length is not evidence), and a calibration check that
compares judge verdicts against human labels before the judge is
trusted with a gate. Stdlib only.
"""
RUBRIC = ("grounded", "complete", "safe")

# Each answer: unsupported claims, required points covered (of 3),
# policy flags. The judge sees only these evidence fields — exactly
# like a real judge sees only the answer and the rubric.
ANSWERS = {
    "A (concise)": {"unsupported": 0, "covered": 2, "flags": 0},
    "B (verbose)": {"unsupported": 1, "covered": 3, "flags": 0},
}


def judge(evidence):
    grounded = 3 if evidence["unsupported"] == 0 else 1
    complete = evidence["covered"]  # 0..3, one point per required point
    safe = 3 if evidence["flags"] == 0 else 0
    return {"grounded": grounded, "complete": complete, "safe": safe}


def total(scores):
    return sum(scores.values())


# Calibration set: (item, human verdict, judge verdict) on pass/fail.
CALIBRATION = [
    ("case 1", "pass", "pass"),
    ("case 2", "pass", "pass"),
    ("case 3", "fail", "fail"),
    ("case 4", "pass", "fail"),  # the disagreement a calibration review must explain
]


def agreement(pairs=CALIBRATION):
    agree = sum(1 for _, h, j in pairs if h == j)
    return agree, len(pairs)


def main():
    print("rubric dimensions: grounded, complete, safe (0-3 each)")
    for name, ev in ANSWERS.items():
        s = judge(ev)
        print(f"  judge: answer {name} total {total(s)}/9 "
              f"(grounded {s['grounded']}, complete {s['complete']}, safe {s['safe']})")
    print("verbosity trap: answer B covers more points but loses on groundedness")
    a, n = agreement()
    print(f"calibration: judge agrees with humans on {a}/{n} cases")
    print("rule: a judge below the agreement bar annotates; it never gates alone")
    print("graders demo complete")


if __name__ == "__main__":
    main()
