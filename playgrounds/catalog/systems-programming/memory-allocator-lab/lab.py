"""Learner implementation stub for Memory Allocator Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class OutOfMemory(Exception): pass
class InvalidFree(Exception): pass

class Allocator:
    def __init__(self, size: int):
        self.size = size
    def alloc(self, size: int) -> int:
        # TODO: First-fit allocation with block splitting.
        raise NotImplementedError
    def free(self, address: int) -> None:
        # TODO: Mark a block free and coalesce adjacent free blocks.
        raise NotImplementedError
    def free_bytes(self) -> int:
        # TODO: Return total free capacity.
        raise NotImplementedError
