"""Learner implementation stub for Mini Deep Learning Framework: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_mini_deep_learning_framework_run_forward_passs`.
"""

def plan_mini_deep_learning_framework_run_forward_passs(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic run forward pass operations to converge observed module graph state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
