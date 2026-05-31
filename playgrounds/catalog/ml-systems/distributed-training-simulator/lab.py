"""Learner implementation stub for Distributed Training Simulator First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class Model:
    def __init__(self, params: dict[str,float]): self.params=params
    def step(self, grads: dict[str,float], lr: float):
        # TODO
        raise NotImplementedError
    def checkpoint(self, step: int) -> dict:
        # TODO
        raise NotImplementedError
    @classmethod
    def load(cls, checkpoint: dict) -> tuple['Model', int]:
        # TODO
        raise NotImplementedError
