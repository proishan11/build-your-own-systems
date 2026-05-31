from dataclasses import dataclass


class KernelError(Exception):
    pass


class BadAddress(KernelError):
    pass


class BadFileDescriptor(KernelError):
    pass


@dataclass
class OpenFile:
    data: bytes
    offset: int = 0


class UserMemory:
    def __init__(self, size: int):
        self._data = bytearray(size)

    def validate(self, ptr: int, length: int) -> None:
        # TODO: Reject negative pointers, negative lengths, and ranges that
        # extend beyond the memory buffer.
        raise NotImplementedError

    def write(self, ptr: int, data: bytes) -> None:
        # TODO: Validate then copy data into user memory.
        raise NotImplementedError

    def read(self, ptr: int, length: int) -> bytes:
        # TODO: Validate then return bytes from user memory.
        raise NotImplementedError


class Kernel:
    def __init__(self, memory: UserMemory):
        self.memory = memory
        self.files = {}

    def open_bytes(self, fd: int, data: bytes) -> None:
        self.files[fd] = OpenFile(data=data)

    def sys_read(self, fd: int, ptr: int, length: int) -> int:
        # TODO: Validate fd and user memory before copying. Advance file offset
        # only for bytes actually copied.
        raise NotImplementedError

