import unittest
from lab import LoadBalancer, NoHealthyBackends
class LBTest(unittest.TestCase):
    def test_least_connections(self):
        lb=LoadBalancer(); lb.add('a'); lb.add('b'); self.assertEqual(lb.acquire(),'a'); self.assertEqual(lb.acquire(),'b')
    def test_ignores_unhealthy(self):
        lb=LoadBalancer(); lb.add('a'); lb.add('b'); lb.set_health('a', False); self.assertEqual(lb.acquire(),'b')
    def test_no_healthy(self):
        lb=LoadBalancer(); lb.add('a'); lb.set_health('a', False)
        with self.assertRaises(NoHealthyBackends): lb.acquire()
if __name__ == '__main__': unittest.main()
