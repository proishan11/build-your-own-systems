"""Learner implementation stub for LLM Evals Harness: Planning and Ordering.

Read exercises/003-operation-planner.md before coding. The tests in
tests/test_lab_003.py define the project-specific behavior for `plan_llm_evals_harness_score_answers`.
"""

def plan_llm_evals_harness_score_answers(desired: dict, observed: dict) -> list[dict]:
    """Plan deterministic score answer operations to converge observed score rubric state to desired state."""
    # TODO: Emit minimal create/update/delete actions in stable operation order.
    # Sort by operation type priority and name so reviews and retries are deterministic.
    raise NotImplementedError
