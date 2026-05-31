"""Learner implementation stub for User-Level Thread Library First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class Scheduler:
    def __init__(self):
        pass
    def add(self, task_id: str) -> None:
        # TODO: Add a runnable task.
        raise NotImplementedError
    def block(self, task_id: str) -> None:
        # TODO: Mark task blocked.
        raise NotImplementedError
    def unblock(self, task_id: str) -> None:
        # TODO: Mark task runnable again.
        raise NotImplementedError
    def next(self) -> str:
        # TODO: Return next runnable task in round-robin order.
        raise NotImplementedError
