"""Learner implementation stub for Autograd Engine: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_autograd_engine_backpropagate_gradients`.
"""

def plan_autograd_engine_backpropagate_gradients(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic backpropagate gradient operations to converge observed computation graph state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
