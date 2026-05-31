"""Learner implementation stub for Model Router: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_model_router_llm_request_event`.
"""

def apply_model_router_llm_request_event(events: list[dict]) -> dict:
    """Apply ordered llm request events to model catalog while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
