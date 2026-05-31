"""Learner implementation stub for Agent Runtime: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_agent_runtime_agent_step_event`.
"""

def apply_agent_runtime_agent_step_event(events: list[dict]) -> dict:
    """Apply ordered agent step events to execution trace while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
