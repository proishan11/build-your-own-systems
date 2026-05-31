"""Learner implementation stub for IP Router Lab First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class NoRoute(Exception): pass
class TTLExpired(Exception): pass
class Router:
    def __init__(self): pass
    def add_route(self, cidr: str, next_hop: str):
        # TODO: Store route.
        raise NotImplementedError
    def forward(self, dst: str, ttl: int) -> tuple[str,int]:
        # TODO: Return next_hop,new_ttl.
        raise NotImplementedError
