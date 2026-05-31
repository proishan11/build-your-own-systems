"""Learner implementation stub for Reliable Transport From Scratch First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class StreamReassembler:
    def __init__(self): pass
    def push(self, offset: int, data: bytes) -> bytes:
        # TODO: Buffer frame and return newly contiguous bytes.
        raise NotImplementedError
    def next_offset(self) -> int:
        # TODO: Return next expected offset.
        raise NotImplementedError
