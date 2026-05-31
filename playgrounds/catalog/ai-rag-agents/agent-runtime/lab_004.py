"""Learner implementation stub for Agent Runtime: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_agent_runtime_infinite_loop`.
"""

def recover_agent_runtime_infinite_loop(failure_report: dict) -> dict:
    """Classify recovery behavior for infinite loop while protecting execution trace."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
