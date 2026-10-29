"""The evaluation readiness review (Lesson 50 capstone demo).

The capstone's final act: a checklist review that ends in GO or
NO-GO, with every blocker named out loud. A system is ready to ship
when its evaluation system is ready — golden set current, judges
calibrated, guardrails audited, red team fresh, online sampling
live, and a named owner for every alert. One standing blocker makes
the honest verdict NO-GO, and writing it down is the deliverable.
Stdlib only.
"""
CHECKS = [
    ("golden set refreshed this quarter", True),
    ("judge calibration at or above the agreement bar", True),
    ("guardrail audit log reviewed weekly", True),
    ("red-team suite run within 30 days", False),  # last run: 74 days ago
    ("online sampling live with alert owner named", True),
    ("regression gate wired into the release pipeline", True),
    ("incident-to-test loop rehearsed", True),
    ("evaluation owner named for the first 90 days", True),
]


def review(checks=CHECKS):
    blockers = [name for name, ok in checks if not ok]
    return ("GO" if not blockers else "NO-GO"), blockers


def main():
    verdict, blockers = review()
    print(f"evaluation readiness review: {len(CHECKS)} checks")
    for name, ok in CHECKS:
        print(f"  [{'x' if ok else ' '}] {name}")
    print(f"verdict: {verdict}")
    for b in blockers:
        print(f"blocker: {b}")
    print("readiness demo complete")


if __name__ == "__main__":
    main()
