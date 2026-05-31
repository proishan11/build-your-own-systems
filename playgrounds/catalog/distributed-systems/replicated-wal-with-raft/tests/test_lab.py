import unittest
from lab import LogMismatch, RaftLog
class RaftLogTest(unittest.TestCase):
    def test_append_after_match(self):
        l=RaftLog([(1,'a')]); l.append_entries(1,1,[(1,'b')]); self.assertEqual(l.entries(), [(1,'a'),(1,'b')])
    def test_reject_mismatch(self):
        with self.assertRaises(LogMismatch): RaftLog([(2,'a')]).append_entries(1,1,[])
    def test_truncate_conflict(self):
        l=RaftLog([(1,'a'),(2,'old')]); l.append_entries(1,1,[(3,'new')]); self.assertEqual(l.entries(), [(1,'a'),(3,'new')])
if __name__ == '__main__': unittest.main()
