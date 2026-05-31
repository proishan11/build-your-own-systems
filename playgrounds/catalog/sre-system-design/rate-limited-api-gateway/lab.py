"""Learner implementation stub for Rate-Limited API Gateway First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class RateLimiter:
    def __init__(self, limit: int, window: int): pass
    def allow(self, tenant: str, timestamp: int) -> bool:
        # TODO
        raise NotImplementedError
