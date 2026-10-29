"""Statistics an evaluator can defend (Lesson 22 demo).

Three computations, all by hand so nothing is a black box:
- Cohen's kappa: do two graders agree beyond chance?
- A Wilson score interval: a success rate with honest uncertainty.
- A plain-language read of both, the way you would defend them in a
  release review. Stdlib only.
"""
import math

# 12 shared items, two graders, pass/fail labels.
GRADER_A = ["pass", "pass", "fail", "pass", "fail", "pass",
            "pass", "fail", "pass", "pass", "fail", "pass"]
GRADER_B = ["pass", "pass", "fail", "pass", "pass", "pass",
            "pass", "fail", "fail", "pass", "fail", "pass"]


def cohens_kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = 0.0
    for label in set(a) | set(b):
        pe += (a.count(label) / n) * (b.count(label) / n)
    return po, pe, (po - pe) / (1 - pe)


def wilson(successes, n, z=1.96):
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return centre - half, centre + half


def main():
    po, pe, k = cohens_kappa(GRADER_A, GRADER_B)
    print(f"observed agreement: {po:.3f}, chance agreement: {pe:.3f}")
    print(f"cohen kappa: {k:.3f} (0.61-0.80 reads as substantial agreement)")
    lo, hi = wilson(46, 60)
    print(f"success rate 46/60 = {46 / 60:.3f}, wilson 95% interval: [{lo:.3f}, {hi:.3f}]")
    print("defence: report the interval, not the point estimate — the interval is the claim")
    print("stats demo complete")


if __name__ == "__main__":
    main()
