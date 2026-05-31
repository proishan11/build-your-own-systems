"""Learner implementation stub for Tail Latency Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_tail_latency_lab_latency_sample_event`.
"""

def apply_tail_latency_lab_latency_sample_event(events: list[dict]) -> dict:
    """Apply ordered latency sample events to histogram bucket while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
