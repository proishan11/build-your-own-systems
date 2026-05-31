"""Learner implementation stub for Vulnerable Web App Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_vulnerable_web_app_lab_http_input_event`.
"""

def apply_vulnerable_web_app_lab_http_input_event(events: list[dict]) -> dict:
    """Apply ordered http input events to security policy while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
