"""Learner implementation stub for Replication and Failover Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_replication_and_failover_lab_promote_replicas`.
"""

def plan_replication_and_failover_lab_promote_replicas(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic promote replica operations to converge observed failover plan state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
