"""Learner implementation stub for Kubernetes Controller From Scratch: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_kubernetes_controller_from_scratch_reconcile_objects`.
"""

def plan_kubernetes_controller_from_scratch_reconcile_objects(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic reconcile object operations to converge observed reconcile state state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
