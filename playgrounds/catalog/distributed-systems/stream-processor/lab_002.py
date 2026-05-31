"""Learner implementation stub for Stream Processor: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_stream_processor_stream_event`.
"""

def apply_stream_processor_stream_event(events: list[dict]) -> dict:
    """Apply ordered stream events to watermark state while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
