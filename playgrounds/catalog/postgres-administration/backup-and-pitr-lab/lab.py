"""Learner implementation stub for Backup and PITR Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class RestoreError(Exception): pass
def plan_restore(backups: list[int], wal_segments: list[tuple[int,int]], target: int) -> dict:
    # TODO
    raise NotImplementedError
