"""Learner implementation stub for Prompt and Model Registry: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_prompt_and_model_registry_publish_prompts`.
"""

def plan_prompt_and_model_registry_publish_prompts(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic publish prompt operations to converge observed model binding state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
