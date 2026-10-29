"""A golden dataset + scoring harness (Lesson 9 / Lesson 14 demo).

A golden set is a small, labelled set of real cases with one defensible
expected outcome each. The harness scores any system on two separate
axes — did it reach the right outcome (task success), and did it use
the right tool to get there (tool correctness) — because a system can
be right for the wrong reason, and that luck does not survive scale.
Stdlib only, deterministic, offline.
"""
GOLDEN = [
    # (case, expected action, expected tool)
    ("refund within window", "approve", "lookup_order"),
    ("refund outside window", "deny", "lookup_order"),
    ("account locked", "escalate", "draft_reply"),
    ("billing question", "answer", "lookup_order"),
    ("angry customer demands a manager", "escalate", "draft_reply"),
    ("password reset loop", "answer", "reset_password"),
]


def system_v1(case):
    # v1 answers two cases a human would escalate: it is polite, fast,
    # and wrong exactly where the risk lives.
    return {
        "refund within window": ("approve", "lookup_order"),
        "refund outside window": ("deny", "lookup_order"),
        "account locked": ("answer", "draft_reply"),
        "billing question": ("answer", "lookup_order"),
        "angry customer demands a manager": ("answer", "draft_reply"),
        "password reset loop": ("answer", "reset_password"),
    }[case]


def system_v2(case):
    return {
        "refund within window": ("approve", "lookup_order"),
        "refund outside window": ("deny", "lookup_order"),
        "account locked": ("escalate", "draft_reply"),
        "billing question": ("answer", "lookup_order"),
        "angry customer demands a manager": ("escalate", "draft_reply"),
        "password reset loop": ("answer", "reset_password"),
    }[case]


def score(fn):
    success = 0
    tools = 0
    misses = []
    for case, expected, tool in GOLDEN:
        action, used = fn(case)
        if action == expected:
            success += 1
        else:
            misses.append(case)
        if used == tool:
            tools += 1
    return success, tools, misses


def main():
    print(f"golden set: {len(GOLDEN)} cases, each with an expected action and tool")
    for name, fn in [("v1", system_v1), ("v2", system_v2)]:
        s, t, misses = score(fn)
        print(f"  {name}: task success {s}/{len(GOLDEN)}, tool correctness {t}/{len(GOLDEN)}")
        for m in misses:
            print(f"    miss: {m}")
    print("lesson: v1 and v2 differ only on escalation — the harness names the cases")
    print("evalkit demo complete")


if __name__ == "__main__":
    main()
