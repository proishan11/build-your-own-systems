"""Learner implementation stub for Mini Container Runtime: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_mini_container_runtime_container_spec_event`.
"""

def apply_mini_container_runtime_container_spec_event(events: list[dict]) -> dict:
    """Apply ordered container spec events to namespace plan while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
