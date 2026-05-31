"""Learner implementation stub for Replicated WAL With Raft First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class LogMismatch(Exception): pass
class RaftLog:
    def __init__(self, entries=None): pass
    def append_entries(self, prev_index: int, prev_term: int, entries: list[tuple[int,str]]) -> None:
        # TODO: Apply AppendEntries log-matching behavior.
        raise NotImplementedError
    def entries(self) -> list[tuple[int,str]]:
        # TODO: Return entries as [(term,command)].
        raise NotImplementedError
