"""Learner implementation stub for Memory Allocator Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_memory_allocator_lab_split_allocations`.
"""

def plan_memory_allocator_lab_split_allocations(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic split allocation operations to converge observed free block state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
