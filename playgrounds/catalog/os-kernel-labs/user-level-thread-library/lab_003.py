"""Learner implementation stub for User-Level Thread Library: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_user_level_thread_library_yield_threads`.
"""

def plan_user_level_thread_library_yield_threads(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic yield thread operations to converge observed run queue state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
