import unittest
from lab import SSTable, TOMBSTONE, get_from_levels
class LSMTest(unittest.TestCase):
    def test_lookup(self): self.assertEqual(SSTable([('a','1'),('b','2')]).get('b'), '2')
    def test_tombstone(self): self.assertIsNone(SSTable([('a',TOMBSTONE)]).get('a'))
    def test_newer_wins(self): self.assertEqual(get_from_levels([SSTable([('a','new')]), SSTable([('a','old')])], 'a'), 'new')
if __name__ == '__main__': unittest.main()
