"""Learner implementation stub for Feature Store: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_feature_store_materialize_features`.
"""

def plan_feature_store_materialize_features(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic materialize feature operations to converge observed feature registry state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
