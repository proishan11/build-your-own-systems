"""Learner implementation stub for Distributed Training Simulator: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_distributed_training_simulator_allreduce_shards`.
"""

def plan_distributed_training_simulator_allreduce_shards(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic allreduce shard operations to converge observed worker ring state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
