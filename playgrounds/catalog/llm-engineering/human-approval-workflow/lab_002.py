"""Learner implementation stub for Human Approval Workflow: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_human_approval_workflow_approval_request_event`.
"""

def apply_human_approval_workflow_approval_request_event(events: list[dict]) -> dict:
    """Apply ordered approval request events to approval queue while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
