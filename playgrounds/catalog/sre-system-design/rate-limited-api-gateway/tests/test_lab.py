import unittest
from lab import RateLimiter
class RateTest(unittest.TestCase):
    def test_limit(self):
        r=RateLimiter(2,10); self.assertTrue(r.allow('a',0)); self.assertTrue(r.allow('a',1)); self.assertFalse(r.allow('a',2)); self.assertTrue(r.allow('a',11))
if __name__ == '__main__': unittest.main()
