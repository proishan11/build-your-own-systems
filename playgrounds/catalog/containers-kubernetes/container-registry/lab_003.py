"""Learner implementation stub for Container Registry: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_container_registry_serve_manifests`.
"""

def plan_container_registry_serve_manifests(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic serve manifest operations to converge observed blob store state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
