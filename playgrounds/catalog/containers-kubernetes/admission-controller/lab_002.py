"""Learner implementation stub for Admission Controller: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_admission_controller_admission_request_event`.
"""

def apply_admission_controller_admission_request_event(events: list[dict]) -> dict:
    """Apply ordered admission request events to policy set while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
