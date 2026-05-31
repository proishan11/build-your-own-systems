import unittest
from lab import recover
class RecoveryTest(unittest.TestCase):
    def test_put_delete(self): self.assertEqual(recover([(1,'put','a','1'),(2,'delete','a',None)]), {})
    def test_lsn_order(self): self.assertEqual(recover([(2,'put','a','2'),(1,'put','a','1')]), {'a':'2'})
    def test_duplicate_lsn(self): self.assertEqual(recover([(1,'put','a','1'),(1,'put','a','1')]), {'a':'1'})
if __name__ == '__main__': unittest.main()
