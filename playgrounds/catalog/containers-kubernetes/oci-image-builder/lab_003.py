"""Learner implementation stub for OCI Image Builder: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_oci_image_builder_assemble_images`.
"""

def plan_oci_image_builder_assemble_images(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic assemble image operations to converge observed image manifest state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
