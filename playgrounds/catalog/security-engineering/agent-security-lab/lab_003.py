"""Learner implementation stub for Agent Security Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_agent_security_lab_classify_tools`.
"""

def plan_agent_security_lab_classify_tools(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic classify tool operations to converge observed tool policy state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
