"""Learner implementation stub for Distributed Training Simulator: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_distributed_training_simulator_straggler_worker`.
"""

def recover_distributed_training_simulator_straggler_worker(failure_report: dict) -> dict:
    """Classify recovery behavior for straggler worker while protecting worker ring."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
