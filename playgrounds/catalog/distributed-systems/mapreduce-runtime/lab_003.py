"""Learner implementation stub for MapReduce Runtime: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_mapreduce_runtime_schedule_tasks`.
"""

def plan_mapreduce_runtime_schedule_tasks(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic schedule task operations to converge observed task tracker state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
