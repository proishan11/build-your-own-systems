import unittest
from lab import make_batches
class BatchTest(unittest.TestCase):
    def test_max_size(self): self.assertEqual(make_batches([(0,'a'),(0,'b'),(0,'c')],2,10), [['a','b'],['c']])
    def test_timeout_flush(self): self.assertEqual(make_batches([(0,'a'),(9,'b')],4,5), [['a'],['b']])
if __name__ == '__main__': unittest.main()
