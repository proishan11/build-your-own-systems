"""Learner implementation stub for MapReduce Runtime First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

def partition(records, mapper, reducers: int) -> list[list[tuple[str, int]]]:
    # TODO: Run mapper(record)->iterable[(key,value)] and bucket by hash(key)%reducers.
    raise NotImplementedError
