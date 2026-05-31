"""Learner implementation stub for Auth and Session System First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class SessionStore:
    def __init__(self): pass
    def create(self, user: str) -> str:
        # TODO
        raise NotImplementedError
    def get(self, session_id: str) -> str | None:
        # TODO
        raise NotImplementedError
    def rotate(self, session_id: str) -> str:
        # TODO
        raise NotImplementedError
