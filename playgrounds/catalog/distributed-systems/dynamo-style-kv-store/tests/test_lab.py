import unittest
from lab import VectorClock
class VCTest(unittest.TestCase):
    def test_before_after(self):
        a=VectorClock(); b=a.tick('n1'); self.assertEqual(a.compare(b),'before'); self.assertEqual(b.compare(a),'after')
    def test_concurrent(self):
        self.assertEqual(VectorClock().tick('a').compare(VectorClock().tick('b')), 'concurrent')
    def test_merge(self):
        m=VectorClock().tick('a').merge(VectorClock().tick('b')); self.assertEqual(m.compare(VectorClock({'a':1,'b':1})), 'equal')
if __name__ == '__main__': unittest.main()
