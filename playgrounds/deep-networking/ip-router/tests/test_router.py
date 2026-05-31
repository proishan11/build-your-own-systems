import unittest

from router import NoRoute, Packet, Router, TTLExpired


class RouterTest(unittest.TestCase):
    def test_longest_prefix_match(self):
        router = Router()
        router.add_route("10.0.0.0/8", "10.0.0.1", "eth0")
        router.add_route("10.1.0.0/16", "10.1.0.1", "eth1")

        decision = router.forward(Packet(dst="10.1.2.3", ttl=64))

        self.assertEqual(decision.next_hop, "10.1.0.1")
        self.assertEqual(decision.interface, "eth1")
        self.assertEqual(decision.ttl, 63)

    def test_no_route(self):
        router = Router()
        with self.assertRaises(NoRoute):
            router.forward(Packet(dst="192.0.2.1", ttl=64))

    def test_ttl_expired(self):
        router = Router()
        router.add_route("0.0.0.0/0", "203.0.113.1", "eth0")
        with self.assertRaises(TTLExpired):
            router.forward(Packet(dst="8.8.8.8", ttl=1))


if __name__ == "__main__":
    unittest.main()

