import unittest
from lab import partition
class MRTest(unittest.TestCase):
    def test_partitions_all_pairs(self):
        out=partition(['a b','a'], lambda s: [(w,1) for w in s.split()], 2)
        self.assertEqual(sorted(pair for bucket in out for pair in bucket), [('a',1),('a',1),('b',1)])
        self.assertEqual(len(out),2)
if __name__ == '__main__': unittest.main()
