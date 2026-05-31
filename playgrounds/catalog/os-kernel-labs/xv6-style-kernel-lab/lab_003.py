"""Learner implementation stub for xv6-Style Kernel Lab: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_xv6_style_kernel_lab_enter_kernels`.
"""

def plan_xv6_style_kernel_lab_enter_kernels(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic enter kernel operations to converge observed process table state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
