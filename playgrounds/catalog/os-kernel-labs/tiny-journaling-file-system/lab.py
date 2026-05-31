"""Learner implementation stub for Tiny Journaling File System First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class FileSystem:
    def __init__(self):
        pass
    def create(self, path: str) -> None:
        # TODO: Log intent then apply metadata.
        raise NotImplementedError
    def exists(self, path: str) -> bool:
        # TODO: Return whether path exists.
        raise NotImplementedError
    def replay(self, journal: list[tuple[str, str]]) -> None:
        # TODO: Reapply journal entries idempotently.
        raise NotImplementedError
    def journal(self) -> list[tuple[str, str]]:
        # TODO: Return journal entries.
        raise NotImplementedError
