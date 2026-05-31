"""Learner implementation stub for Inference Server: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_inference_server_inference_request_event`.
"""

def apply_inference_server_inference_request_event(events: list[dict]) -> dict:
    """Apply ordered inference request events to batch queue while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
