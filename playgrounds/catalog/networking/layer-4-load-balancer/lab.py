"""Learner implementation stub for Layer 4 Load Balancer First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class NoHealthyBackends(Exception): pass
class LoadBalancer:
    def __init__(self): pass
    def add(self, name: str):
        # TODO: Register backend.
        raise NotImplementedError
    def set_health(self, name: str, healthy: bool):
        # TODO: Update health.
        raise NotImplementedError
    def acquire(self) -> str:
        # TODO: Return healthy least-connections backend and increment active count.
        raise NotImplementedError
    def release(self, name: str):
        # TODO: Decrement active count.
        raise NotImplementedError
