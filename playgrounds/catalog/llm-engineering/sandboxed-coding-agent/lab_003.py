"""Learner implementation stub for Sandboxed Coding Agent: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_sandboxed_coding_agent_authorize_tools`.
"""

def plan_sandboxed_coding_agent_authorize_tools(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic authorize tool operations to converge observed sandbox policy state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
