"""Learner implementation stub for Secrets Manager First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class AccessDenied(Exception): pass
class SecretStore:
    def __init__(self): pass
    def put(self, name: str, value: str, readers: set[str]):
        # TODO
        raise NotImplementedError
    def get(self, actor: str, name: str) -> str:
        # TODO
        raise NotImplementedError
    def audit(self) -> list[dict]:
        # TODO
        raise NotImplementedError
