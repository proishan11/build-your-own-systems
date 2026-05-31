"""Learner implementation stub for Dynamo-Style KV Store: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_dynamo_style_kv_store_write_quorums`.
"""

def plan_dynamo_style_kv_store_write_quorums(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic write quorum operations to converge observed replica set state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
