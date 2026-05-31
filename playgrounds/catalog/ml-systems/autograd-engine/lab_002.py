"""Learner implementation stub for Autograd Engine: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_autograd_engine_tensor_operation_event`.
"""

def apply_autograd_engine_tensor_operation_event(events: list[dict]) -> dict:
    """Apply ordered tensor operation events to computation graph while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
