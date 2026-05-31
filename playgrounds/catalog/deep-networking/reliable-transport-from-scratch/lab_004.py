"""Learner implementation stub for Reliable Transport From Scratch: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_reliable_transport_from_scratch_out_of_order_segment`.
"""

def recover_reliable_transport_from_scratch_out_of_order_segment(failure_report: dict) -> dict:
    """Classify recovery behavior for out-of-order segment while protecting receive window."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
