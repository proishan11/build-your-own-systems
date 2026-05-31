import unittest
from lab import TraceStore
class TraceTest(unittest.TestCase):
    def test_children_and_cost(self):
        t=TraceStore(); t.add_span('root',None,10,0.1); t.add_span('tool','root',20,0.2)
        self.assertEqual(t.children('root'), ['tool']); self.assertAlmostEqual(t.total_cost(),0.3)
if __name__ == '__main__': unittest.main()
