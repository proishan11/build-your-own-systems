"""Learner implementation stub for Profiler From Scratch: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_profiler_from_scratch_stack_sample_event`.
"""

def apply_profiler_from_scratch_stack_sample_event(events: list[dict]) -> dict:
    """Apply ordered stack sample events to profile tree while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
