"""Dataset drift detection (Lesson 26 demo).

A golden set frozen last quarter quietly stops representing this
quarter's users. This watcher compares two dataset versions on the
two signals that move first: the label mix (what users ask for) and
the input length (how they ask). Any label share moving more than
0.10, or mean length moving more than 20%, raises a drift alert —
the set must be reviewed before its scores are quoted again.
Stdlib only; counts are exact, nothing is sampled.
"""
V1 = {"answer": 50, "approve": 20, "deny": 15, "escalate": 15}
V2 = {"answer": 34, "approve": 18, "deny": 14, "escalate": 34}
MEAN_TOKENS_V1 = 42
MEAN_TOKENS_V2 = 61
LABEL_THRESHOLD = 0.10
LENGTH_THRESHOLD = 0.20


def shares(counts):
    total = sum(counts.values())
    return {k: v / total for k, v in counts.items()}


def detect(v1=V1, v2=V2, len1=MEAN_TOKENS_V1, len2=MEAN_TOKENS_V2):
    s1, s2 = shares(v1), shares(v2)
    alerts = []
    for label in sorted(set(s1) | set(s2)):
        d = s2.get(label, 0.0) - s1.get(label, 0.0)
        if abs(d) > LABEL_THRESHOLD:
            alerts.append(f"{label} share {s1.get(label, 0.0):.2f} -> {s2.get(label, 0.0):.2f}")
    change = (len2 - len1) / len1
    if abs(change) > LENGTH_THRESHOLD:
        alerts.append(f"mean input length {len1} -> {len2} tokens ({change:+.0%})")
    return alerts


def main():
    print("comparing golden set v1 (last quarter) with v2 (this quarter)")
    alerts = detect()
    for a in alerts:
        print(f"  drift: {a}")
    if alerts:
        print(f"verdict: DRIFT DETECTED ({len(alerts)} signals) — review the set before quoting its scores")
    else:
        print("verdict: no drift beyond thresholds")
    print("driftwatch demo complete")


if __name__ == "__main__":
    main()
