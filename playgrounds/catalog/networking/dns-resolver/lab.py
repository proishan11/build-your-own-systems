"""Learner implementation stub for DNS Resolver First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class DNSError(Exception): pass
def encode_name(name: str) -> bytes:
    # TODO: Encode www.example.com as length-prefixed labels.
    raise NotImplementedError
def decode_name(data: bytes, offset: int = 0) -> tuple[str, int]:
    # TODO: Decode one uncompressed DNS name and return name,next_offset.
    raise NotImplementedError
