"""Learner implementation stub for Model Router First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class NoModel(Exception):
    pass


class ModelRouter:
    def __init__(self):
        pass

    def add(self, name: str, context: int, cost: float, latency: int):
        # TODO: Register model capabilities.
        raise NotImplementedError

    def route(self, tokens: int, max_cost: float) -> str:
        # TODO: Choose the lowest-latency model that can handle the request
        # within the caller's cost ceiling.
        raise NotImplementedError
