"""Learner implementation stub for LLM Trace Store First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class TraceStore:
    def __init__(self): pass
    def add_span(self, span_id: str, parent_id: str | None, latency_ms: int, cost: float):
        # TODO
        raise NotImplementedError
    def children(self, span_id: str) -> list[str]:
        # TODO
        raise NotImplementedError
    def total_cost(self) -> float:
        # TODO
        raise NotImplementedError
