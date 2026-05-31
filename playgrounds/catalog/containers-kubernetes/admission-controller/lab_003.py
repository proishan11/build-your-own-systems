"""Learner implementation stub for Admission Controller: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_admission_controller_admit_objects`.
"""

def plan_admission_controller_admit_objects(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic admit object operations to converge observed policy set state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
