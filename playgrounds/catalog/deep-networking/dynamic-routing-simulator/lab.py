"""Learner implementation stub for Dynamic Routing Simulator First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class Router:
    def __init__(self, name: str): self.name=name
    def add_link(self, neighbor: str, cost: int):
        # TODO: Store directly connected neighbor route.
        raise NotImplementedError
    def receive(self, neighbor: str, advertised: dict[str,int]):
        # TODO: Relax routes through neighbor.
        raise NotImplementedError
    def route(self, dest: str) -> tuple[str,int]:
        # TODO: Return next_hop,total_cost.
        raise NotImplementedError
