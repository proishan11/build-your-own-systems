"""Learner implementation stub for Auth and Session System: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_auth_and_session_system_session_token_event`.
"""

def apply_auth_and_session_system_session_token_event(events: list[dict]) -> dict:
    """Apply ordered session token events to session store while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
