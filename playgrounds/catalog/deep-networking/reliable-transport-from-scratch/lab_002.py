"""Learner implementation stub for Reliable Transport From Scratch: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_reliable_transport_from_scratch_transport_segment_event`.
"""

def apply_reliable_transport_from_scratch_transport_segment_event(events: list[dict]) -> dict:
    """Apply ordered transport segment events to receive window while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
