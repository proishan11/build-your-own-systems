"""Learner implementation stub for LSM Tree KV Store First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

TOMBSTONE = object()
class SSTable:
    def __init__(self, entries): pass
    def get(self, key: str):
        # TODO: Return value, None for missing or tombstone.
        raise NotImplementedError
def get_from_levels(tables: list[SSTable], key: str):
    # TODO: Search tables newest to oldest.
    raise NotImplementedError
