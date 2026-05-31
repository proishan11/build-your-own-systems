from dataclasses import dataclass


@dataclass(frozen=True)
class Segment:
    seq: int
    data: bytes


class Receiver:
    def __init__(self):
        self._next = 0
        self._delivered = bytearray()
        self._buffer = {}

    def receive(self, segment: Segment) -> int:
        """Receive one segment and return the next expected byte offset."""
        # TODO: Buffer out-of-order data, append newly contiguous data to
        # _delivered, ignore duplicate data, and return the ACK number.
        raise NotImplementedError

    def read(self) -> bytes:
        return bytes(self._delivered)

