"""Learner implementation stub for Event Loop and Async Runtime: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_event_loop_and_async_runtime_async_task_event`.
"""

def apply_event_loop_and_async_runtime_async_task_event(events: list[dict]) -> dict:
    """Apply ordered async task events to ready queue while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
