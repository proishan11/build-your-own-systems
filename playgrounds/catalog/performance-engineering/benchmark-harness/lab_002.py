"""Learner implementation stub for Benchmark Harness: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_benchmark_harness_benchmark_sample_event`.
"""

def apply_benchmark_harness_benchmark_sample_event(events: list[dict]) -> dict:
    """Apply ordered benchmark sample events to run config while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
