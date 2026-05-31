import unittest
from lab import citations_supported, precision_at_k
class EvalTest(unittest.TestCase):
    def test_precision(self): self.assertEqual(precision_at_k(['a','b','c'], {'a','c'}, 2), 0.5)
    def test_citations(self): self.assertTrue(citations_supported(['d1'], {'d1','d2'})); self.assertFalse(citations_supported(['d3'], {'d1'}))
if __name__ == '__main__': unittest.main()
