"""Learner implementation stub for NAT Gateway First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class NoMapping(Exception): pass
class NAT:
    def __init__(self, public_ip: str, start_port: int = 40000):
        self.public_ip = public_ip
    def outbound(self, internal_ip: str, internal_port: int, remote_ip: str, remote_port: int) -> tuple[str,int]:
        # TODO: Return public_ip, allocated_port.
        raise NotImplementedError
    def inbound(self, public_port: int, remote_ip: str, remote_port: int) -> tuple[str,int]:
        # TODO: Return internal_ip, internal_port for existing mapping.
        raise NotImplementedError
