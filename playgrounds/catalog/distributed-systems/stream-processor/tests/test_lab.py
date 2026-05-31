import unittest
from lab import aggregate
class StreamTest(unittest.TestCase):
    def test_tumbling_sum(self):
        events=[(0,'a',1),(3,'a',2),(5,'a',10),(6,'b',4)]
        self.assertEqual(aggregate(events,5), {(0,'a'):3,(5,'a'):10,(5,'b'):4})
if __name__ == '__main__': unittest.main()
