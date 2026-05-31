import unittest
from lab import CommitGraph
class GitGraphTest(unittest.TestCase):
    def test_ancestor(self):
        g=CommitGraph(); g.add('a',[]); g.add('b',['a']); self.assertTrue(g.is_ancestor('a','b'))
    def test_merge_base(self):
        g=CommitGraph(); g.add('a',[]); g.add('b',['a']); g.add('c',['a']); self.assertEqual(g.merge_base('b','c'),'a')
if __name__ == '__main__': unittest.main()
