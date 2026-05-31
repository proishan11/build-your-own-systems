"""Learner implementation stub for MiniDB Storage Engine First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

def recover(records: list[tuple[int, str, str, str | None]]) -> dict[str, str]:
    # TODO: Records are (lsn, op, key, value). Apply idempotently by LSN.
    raise NotImplementedError
