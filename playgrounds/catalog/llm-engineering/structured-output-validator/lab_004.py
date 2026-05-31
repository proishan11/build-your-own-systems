"""Learner implementation stub for Structured Output Validator: Failure, Retry, and Recovery Boundary.

Read exercises/004-failure-recovery.md before coding. This file is
intentionally incomplete: implement the contract and use tests/test_lab_004.py
to validate behavior.
"""

class RetryPolicy:
    def __init__(self, max_attempts: int, retryable_errors: set[str]):
        # TODO: Store retry budget, retryable error names, attempts by operation, and completed IDs.
        pass

    def record_failure(self, operation_id: str, error: str) -> dict:
        """Return a retry/fail/give_up decision for a failed operation."""
        # TODO: Make retry decisions idempotent and budget-aware.
        raise NotImplementedError

    def record_success(self, operation_id: str) -> dict:
        """Mark an operation complete and return a success decision."""
        # TODO: Mark success so later duplicate failures cannot reopen the operation.
        raise NotImplementedError

