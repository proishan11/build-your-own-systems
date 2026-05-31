import unittest
from lab import delete_lines, insert_line, substitute
class VimTest(unittest.TestCase):
    def test_delete(self): self.assertEqual(delete_lines(['a','b','c'],2,2), ['a','c'])
    def test_insert(self): self.assertEqual(insert_line(['a','c'],2,'b'), ['a','b','c'])
    def test_substitute(self): self.assertEqual(substitute(['foo','bar foo'],'foo','x',1,2), ['x','bar x'])
if __name__ == '__main__': unittest.main()
