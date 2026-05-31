import unittest
from lab import p95, summarize
class ObsTest(unittest.TestCase):
    def test_p95(self): self.assertEqual(p95([1,2,3,100]), 100)
    def test_summary(self):
        s=summarize([{'route':'/','latency':10,'error':False},{'route':'/','latency':20,'error':True}], 'route')
        self.assertEqual(s['/']['requests'],2); self.assertEqual(s['/']['errors'],1)
if __name__ == '__main__': unittest.main()
