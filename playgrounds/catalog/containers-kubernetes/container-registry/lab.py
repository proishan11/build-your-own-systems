"""Learner implementation stub for Container Registry First Implementation Lab.

Read exercises/001-project-kickoff.md before coding. Keep the solution
small, deterministic, and focused on the contract tested by tests/test_lab.py.
The placeholder raises NotImplementedError so validation fails for the intended
learning reason until you implement the behavior.
"""

class BlobInUse(Exception): pass
class Registry:
    def __init__(self): pass
    def put_blob(self, data: bytes) -> str:
        # TODO: Return sha256 digest.
        raise NotImplementedError
    def put_manifest(self, name: str, digests: list[str]):
        # TODO
        raise NotImplementedError
    def delete_blob(self, digest: str):
        # TODO
        raise NotImplementedError
    def has_blob(self, digest: str) -> bool:
        # TODO
        raise NotImplementedError
