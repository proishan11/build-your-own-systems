"""Learner implementation stub for Virtual Memory Simulator: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_virtual_memory_simulator_map_pages`.
"""

def plan_virtual_memory_simulator_map_pages(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic map page operations to converge observed page table state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
