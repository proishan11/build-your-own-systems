"""Learner implementation stub for Stream Processor: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_stream_processor_late_event`.
"""

def recover_stream_processor_late_event(failure_report: dict) -> dict:
    """Classify recovery behavior for late event while protecting watermark state."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
