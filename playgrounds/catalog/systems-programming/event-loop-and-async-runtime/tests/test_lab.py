import unittest
from lab import EventLoop
class EventLoopTest(unittest.TestCase):
    def test_runs_in_time_order(self):
        loop=EventLoop(); seen=[]
        loop.call_at(5, lambda: seen.append(('late', loop.now)))
        loop.call_at(1, lambda: seen.append(('early', loop.now)))
        loop.run(); self.assertEqual(seen, [('early',1), ('late',5)])
    def test_preserves_insertion_order_for_same_time(self):
        loop=EventLoop(); seen=[]
        loop.call_at(2, lambda: seen.append('a')); loop.call_at(2, lambda: seen.append('b'))
        loop.run(); self.assertEqual(seen, ['a','b'])
if __name__ == '__main__': unittest.main()
