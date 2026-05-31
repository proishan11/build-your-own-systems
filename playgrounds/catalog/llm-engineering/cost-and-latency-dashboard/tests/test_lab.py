import unittest
from lab import summarize
class CostTest(unittest.TestCase):
    def test_summary(self):
        s=summarize([{'route':'a','cost':0.1,'kind':'model','latency_ms':10},{'route':'a','cost':0.2,'kind':'tool','latency_ms':50}])
        self.assertEqual(s['route_costs'], {'a':0.3}); self.assertEqual(s['request_count'],2); self.assertEqual(s['tool_p95_ms'],50)
if __name__ == '__main__': unittest.main()
