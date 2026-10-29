"""A regression gate for a release pipeline (Lesson 46 demo).

The gate compares a candidate build against the standing baseline
on the metrics the team agreed matter, each with a tolerance set
BEFORE the run: quality metrics may not drop beyond tolerance,
safety may not drop at all, and cost per success may not rise
beyond its budget. One failed check blocks the release and names
itself — a gate that fails silently is worse than no gate.
Stdlib only.
"""
BASELINE = {"task_success": 0.88, "faithfulness": 0.91, "safety": 1.00, "cost_per_success": 0.042}
CANDIDATE = {"task_success": 0.90, "faithfulness": 0.86, "safety": 1.00, "cost_per_success": 0.044}
TOLERANCE = {"task_success": 0.02, "faithfulness": 0.02, "safety": 0.0}
COST_BUDGET = 0.050


def evaluate_gate(base=BASELINE, cand=CANDIDATE):
    failures = []
    for metric, tol in TOLERANCE.items():
        drop = base[metric] - cand[metric]
        if drop > tol:
            failures.append(f"{metric} regressed {base[metric]:.2f} -> {cand[metric]:.2f} (max drop {tol:.2f})")
    if cand["cost_per_success"] > COST_BUDGET:
        failures.append(f"cost_per_success {cand['cost_per_success']:.3f} over budget {COST_BUDGET:.3f}")
    return failures


def main():
    failures = evaluate_gate()
    for metric in ("task_success", "faithfulness", "safety"):
        print(f"  {metric}: {BASELINE[metric]:.2f} -> {CANDIDATE[metric]:.2f}")
    if failures:
        for f in failures:
            print(f"gate: FAIL — {f}")
        print("release: BLOCKED")
    else:
        print("gate: PASS")
        print("release: APPROVED")
    print("gatekeeper demo complete")


if __name__ == "__main__":
    main()
