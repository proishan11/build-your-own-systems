"""Learner implementation stub for Rate-Limited API Gateway: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_rate_limited_api_gateway_api_request_event`.
"""

def apply_rate_limited_api_gateway_api_request_event(events: list[dict]) -> dict:
    """Apply ordered api request events to token bucket while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
