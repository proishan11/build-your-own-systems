from dataclasses import dataclass


class PageFault(Exception):
    pass


@dataclass(frozen=True)
class PageTableEntry:
    frame: int
    readable: bool
    writable: bool


class AddressSpace:
    def __init__(self, page_size: int):
        self.page_size = page_size
        self._entries = {}

    def map_page(self, vpn: int, frame: int, *, readable: bool = True, writable: bool = False) -> None:
        # TODO: Store a page-table entry for vpn.
        raise NotImplementedError

    def translate(self, virtual_address: int, *, write: bool = False) -> int:
        # TODO: Split virtual_address into VPN and offset. Look up the page,
        # enforce permissions, and return physical frame address + offset.
        raise NotImplementedError

