"""Learner implementation stub for Query Optimizer Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

from dataclasses import dataclass
@dataclass(frozen=True)
class Plan: kind: str; estimated_rows: int
def choose_plan(table_rows: int, has_index: bool, selectivity: float) -> Plan:
    # TODO: Return Plan('index_scan' or 'table_scan', estimated_rows).
    raise NotImplementedError
