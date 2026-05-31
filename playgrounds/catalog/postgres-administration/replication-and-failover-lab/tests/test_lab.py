import unittest
from lab import NoCandidate, choose_replica
class FailoverTest(unittest.TestCase):
    def test_choose_lowest_lag(self): self.assertEqual(choose_replica([{'name':'a','lag':5,'healthy':True},{'name':'b','lag':1,'healthy':True}], 10)['name'], 'b')
    def test_no_candidate(self):
        with self.assertRaises(NoCandidate): choose_replica([{'name':'a','lag':50,'healthy':True}], 10)
if __name__ == '__main__': unittest.main()
