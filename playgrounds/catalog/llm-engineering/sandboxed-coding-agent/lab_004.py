"""Learner implementation stub for Sandboxed Coding Agent: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_sandboxed_coding_agent_filesystem_escape`.
"""

def recover_sandboxed_coding_agent_filesystem_escape(failure_report: dict) -> dict:
    """Classify recovery behavior for filesystem escape while protecting sandbox policy."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
