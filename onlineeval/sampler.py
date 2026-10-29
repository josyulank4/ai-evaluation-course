"""Online evaluation: sample, score, alert (Lesson 42 demo).

Offline scores describe the system you tested; online evaluation
describes the system your users have. This sampler takes a
deterministic stream of 200 production events, samples every 10th
(the way a cost-bounded production sampler does), scores the sample
with the same rubric as the offline suite, and raises an alert when
the sampled failure rate crosses the threshold the team agreed
before seeing the data. Stdlib only; the stream is formula-built so
every run is identical.
"""
EVENTS = 200
SAMPLE_EVERY = 10
FAIL_SCORE = 0.60
ALERT_RATE = 0.15


def event_score(i):
    # Deterministic pseudo-traffic: quality drifts down late in the
    # stream (a silent model change at event ~150), which the sampler
    # must catch even though it only sees 1 event in 10.
    base = 0.55 + ((i * 37) % 45) / 100.0
    if i >= 150:
        base -= 0.35
    return round(max(0.0, base), 2)


def sampled_indices(n=EVENTS, every=SAMPLE_EVERY):
    return list(range(0, n, every))


def evaluate_stream():
    idx = sampled_indices()
    fails = [i for i in idx if event_score(i) < FAIL_SCORE]
    return idx, fails


def main():
    idx, fails = evaluate_stream()
    rate = len(fails) / len(idx)
    print(f"production events: {EVENTS}, sampled every {SAMPLE_EVERY}: {len(idx)} scored")
    print(f"sampled failures: {len(fails)}/{len(idx)} ({rate:.0%})")
    if rate > ALERT_RATE:
        print(f"ALERT: sampled failure rate {rate:.0%} exceeds the {ALERT_RATE:.0%} threshold — page the owner")
    else:
        print("no alert: sampled failure rate within threshold")
    print("onlineeval demo complete")


if __name__ == "__main__":
    main()
