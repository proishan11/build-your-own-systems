import unittest
from lab import Router
class DVTest(unittest.TestCase):
    def test_direct_route(self):
        r=Router('a'); r.add_link('b',2); self.assertEqual(r.route('b'), ('b',2))
    def test_relaxes_advertised_route(self):
        r=Router('a'); r.add_link('b',2); r.receive('b', {'c': 5}); self.assertEqual(r.route('c'), ('b',7))
    def test_keeps_better_route(self):
        r=Router('a'); r.add_link('b',2); r.add_link('c',10); r.receive('b', {'c': 20}); self.assertEqual(r.route('c'), ('c',10))
if __name__ == '__main__': unittest.main()
