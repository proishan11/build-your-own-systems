"""Learner implementation stub for Prompt and Model Registry: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_prompt_and_model_registry_unsafe_prompt_change`.
"""

def recover_prompt_and_model_registry_unsafe_prompt_change(failure_report: dict) -> dict:
    """Classify recovery behavior for unsafe prompt change while protecting model binding."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
