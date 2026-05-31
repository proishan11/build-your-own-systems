import unittest
from lab import NoRoute, Router, TTLExpired
class RouterTest(unittest.TestCase):
    def test_lpm(self):
        r=Router(); r.add_route('10.0.0.0/8','a'); r.add_route('10.1.0.0/16','b'); self.assertEqual(r.forward('10.1.2.3',64), ('b',63))
    def test_no_route(self):
        with self.assertRaises(NoRoute): Router().forward('8.8.8.8',64)
    def test_ttl(self):
        r=Router(); r.add_route('0.0.0.0/0','gw')
        with self.assertRaises(TTLExpired): r.forward('8.8.8.8',1)
if __name__ == '__main__': unittest.main()
