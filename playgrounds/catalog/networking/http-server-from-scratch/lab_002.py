"""Learner implementation stub for HTTP Server From Scratch: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_http_server_from_scratch_http_request_event`.
"""

def apply_http_server_from_scratch_http_request_event(events: list[dict]) -> dict:
    """Apply ordered http request events to route table while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
