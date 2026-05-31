"""Learner implementation stub for Structured Output Validator: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_structured_output_validator_validate_outputs`.
"""

def plan_structured_output_validator_validate_outputs(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic validate output operations to converge observed json schema state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
