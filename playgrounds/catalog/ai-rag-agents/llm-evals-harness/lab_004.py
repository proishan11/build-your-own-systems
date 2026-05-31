"""Learner implementation stub for LLM Evals Harness: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_llm_evals_harness_flaky_evaluator`.
"""

def recover_llm_evals_harness_flaky_evaluator(failure_report: dict) -> dict:
    """Classify recovery behavior for flaky evaluator while protecting score rubric."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
