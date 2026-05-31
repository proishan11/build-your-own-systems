"""Learner implementation stub for Agent Runtime: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_agent_runtime_choose_tools`.
"""

def plan_agent_runtime_choose_tools(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic choose tool operations to converge observed execution trace state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
