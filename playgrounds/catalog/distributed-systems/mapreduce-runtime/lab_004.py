"""Learner implementation stub for MapReduce Runtime: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_mapreduce_runtime_worker_crash`.
"""

def recover_mapreduce_runtime_worker_crash(failure_report: dict) -> dict:
    """Classify recovery behavior for worker crash while protecting task tracker."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
