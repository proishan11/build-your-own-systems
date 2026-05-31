"""Learner implementation stub for Go Concurrency Gauntlet First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class DuplicateResource(Exception): pass
class ResourceStore:
    def __init__(self): pass
    def create(self, resource_id: str, state: str):
        # TODO
        raise NotImplementedError
    def transition(self, resource_id: str, state: str):
        # TODO
        raise NotImplementedError
    def get(self, resource_id: str) -> str:
        # TODO
        raise NotImplementedError
    def audit(self) -> list[tuple[str,str]]:
        # TODO
        raise NotImplementedError
