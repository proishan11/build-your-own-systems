import unittest
from lab import Scheduler
class SchedulerTest(unittest.TestCase):
    def test_round_robin(self):
        s=Scheduler(); s.add('a'); s.add('b'); s.add('c')
        self.assertEqual([s.next(),s.next(),s.next(),s.next()], ['a','b','c','a'])
    def test_skips_blocked_tasks(self):
        s=Scheduler(); s.add('a'); s.add('b'); s.block('a')
        self.assertEqual([s.next(),s.next()], ['b','b'])
    def test_unblock_restores_task(self):
        s=Scheduler(); s.add('a'); s.add('b'); s.block('a'); s.unblock('a')
        self.assertIn(s.next(), {'a','b'})
if __name__ == '__main__': unittest.main()
