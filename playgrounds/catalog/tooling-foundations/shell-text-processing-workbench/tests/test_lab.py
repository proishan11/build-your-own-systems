import unittest
from lab import wc
class WCTest(unittest.TestCase):
    def test_counts(self): self.assertEqual(wc(b'hello world\nbye\n'), (2,3,16))
    def test_empty(self): self.assertEqual(wc(b''), (0,0,0))
if __name__ == '__main__': unittest.main()
