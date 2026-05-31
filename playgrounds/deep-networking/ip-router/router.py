from dataclasses import dataclass


class NoRoute(Exception):
    pass


class TTLExpired(Exception):
    pass


@dataclass(frozen=True)
class Packet:
    dst: str
    ttl: int


@dataclass(frozen=True)
class ForwardDecision:
    next_hop: str
    interface: str
    ttl: int


class Router:
    def __init__(self):
        self._routes = []

    def add_route(self, cidr: str, next_hop: str, interface: str) -> None:
        # TODO: Store enough parsed route information to do longest-prefix
        # matching. The standard library ipaddress module is fair game.
        raise NotImplementedError

    def forward(self, packet: Packet) -> ForwardDecision:
        # TODO: Reject expired TTL, find the longest matching route, decrement
        # TTL, and return the forwarding decision.
        raise NotImplementedError

