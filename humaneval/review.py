"""A human review round, measured (Lesson 30 demo).

Human evaluation is an instrument, and instruments get calibrated.
This round interleaves hidden gold-standard items (known labels)
among real queue items, so each annotator's accuracy is measured,
not assumed. Disagreements go to adjudication — they are data about
the guidelines, not noise to average away. Stdlib only.
"""
# (item, gold label or None, annotator 1, annotator 2)
ROUND = [
    ("q1", "pass", "pass", "pass"),
    ("q2", None, "fail", "fail"),
    ("q3", "fail", "fail", "pass"),   # ann2 misses a gold item
    ("q4", None, "pass", "fail"),     # genuine disagreement -> adjudicate
    ("q5", "pass", "pass", "pass"),
    ("q6", None, "pass", "pass"),
    ("q7", "fail", "fail", "fail"),
    ("q8", None, "fail", "pass"),     # genuine disagreement -> adjudicate
]


def annotator_scores(rounds):
    gold_items = [r for r in rounds if r[1] is not None]
    ann1 = sum(1 for r in gold_items if r[2] == r[1])
    ann2 = sum(1 for r in gold_items if r[3] == r[1])
    return ann1, ann2, len(gold_items)


def disagreements(rounds):
    return [r[0] for r in rounds if r[2] != r[3]]


def main():
    a1, a2, n = annotator_scores(ROUND)
    print(f"gold-standard items hidden in queue: {n}")
    print(f"  annotator 1 accuracy on gold: {a1}/{n}")
    print(f"  annotator 2 accuracy on gold: {a2}/{n}")
    d = disagreements(ROUND)
    print(f"  disagreements sent to adjudication: {len(d)} ({', '.join(d)})")
    print("rule: an annotator below the gold bar is retrained, not averaged in")
    print("humaneval demo complete")


if __name__ == "__main__":
    main()
