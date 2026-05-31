import unittest
from lab import regressed, summarize
class PerfTest(unittest.TestCase):
    def test_summary(self): self.assertEqual(summarize([1,2,100])['p95'], 100)
    def test_regression(self): self.assertTrue(regressed([10,10,30], [10,10,10], 0.5))
if __name__ == '__main__': unittest.main()
