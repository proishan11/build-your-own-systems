"""Learner implementation stub for Prompt and Model Registry First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class NotApproved(Exception): pass
class Registry:
    def __init__(self): pass
    def register(self, name: str, artifact: str, metrics: dict) -> int:
        # TODO
        raise NotImplementedError
    def approve(self, version: int):
        # TODO
        raise NotImplementedError
    def promote(self, version: int):
        # TODO
        raise NotImplementedError
    def active(self) -> int | None:
        # TODO
        raise NotImplementedError
