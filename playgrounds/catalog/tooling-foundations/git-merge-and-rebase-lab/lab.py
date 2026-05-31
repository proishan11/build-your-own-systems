"""Learner implementation stub for Git Merge and Rebase Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class CommitGraph:
    def __init__(self): pass
    def add(self, commit: str, parents: list[str]):
        # TODO
        raise NotImplementedError
    def is_ancestor(self, ancestor: str, commit: str) -> bool:
        # TODO
        raise NotImplementedError
    def merge_base(self, a: str, b: str) -> str | None:
        # TODO
        raise NotImplementedError
