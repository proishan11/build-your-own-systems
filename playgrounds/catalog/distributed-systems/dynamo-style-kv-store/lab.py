"""Learner implementation stub for Dynamo-Style KV Store First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class VectorClock:
    def __init__(self, values=None): pass
    def tick(self, node: str):
        # TODO: Increment node counter.
        raise NotImplementedError
    def merge(self, other: 'VectorClock') -> 'VectorClock':
        # TODO: Return elementwise max clock.
        raise NotImplementedError
    def compare(self, other: 'VectorClock') -> str:
        # TODO: Return 'before', 'after', 'equal', or 'concurrent'.
        raise NotImplementedError
