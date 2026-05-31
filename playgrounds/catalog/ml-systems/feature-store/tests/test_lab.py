import unittest
from lab import FeatureStore
class FeatureTest(unittest.TestCase):
    def test_as_of(self):
        s=FeatureStore(); s.put('u1','age',10,30); s.put('u1','age',20,31); self.assertEqual(s.get_as_of('u1','age',15),30)
    def test_no_future_leakage(self):
        s=FeatureStore(); s.put('u1','age',20,31); self.assertIsNone(s.get_as_of('u1','age',10))
if __name__ == '__main__': unittest.main()
