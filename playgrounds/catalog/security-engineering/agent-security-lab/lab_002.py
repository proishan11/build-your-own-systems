"""Learner implementation stub for Agent Security Lab: State and Invariants.

Read exercises/002-state-model.md before coding. The tests in
tests/test_lab_002.py define the project-specific behavior for `apply_agent_security_lab_agent_tool_call_event`.
"""

def apply_agent_security_lab_agent_tool_call_event(events: list[dict]) -> dict:
    """Apply ordered agent tool call events to tool policy while preserving version and idempotency invariants."""
    # TODO: Track accepted event ids, ignore duplicates, reject stale versions,
    # and return the final state plus accepted/rejected event ids.
    raise NotImplementedError
