import hashlib
import zlib
from dataclasses import dataclass


class GitObjectError(Exception):
    pass


@dataclass(frozen=True)
class GitObject:
    kind: str
    payload: bytes


def encode_blob(payload: bytes) -> bytes:
    """Return Git's canonical byte representation for a blob."""
    # TODO: Git hashes "blob <len>\0<payload>", not the payload alone.
    raise NotImplementedError


def object_id(encoded: bytes) -> str:
    """Return the SHA-1 object id for encoded object bytes."""
    # TODO: Return the lowercase hexadecimal SHA-1 digest.
    raise NotImplementedError


def decode_loose_object(compressed: bytes) -> GitObject:
    """Decode zlib-compressed loose object bytes into type and payload."""
    # TODO: Decompress, parse the "<type> <size>\0" header, validate size, and
    # return GitObject(kind, payload).
    raise NotImplementedError


def compress_loose_object(encoded: bytes) -> bytes:
    return zlib.compress(encoded)

