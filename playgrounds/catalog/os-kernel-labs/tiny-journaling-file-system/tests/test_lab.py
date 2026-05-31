import unittest
from lab import FileSystem
class FSTest(unittest.TestCase):
    def test_create_logs_and_applies(self):
        fs=FileSystem(); fs.create('/a'); self.assertTrue(fs.exists('/a')); self.assertEqual(fs.journal(), [('create','/a')])
    def test_replay_is_idempotent(self):
        fs=FileSystem(); fs.replay([('create','/a'),('create','/a')]); self.assertTrue(fs.exists('/a'))
if __name__ == '__main__': unittest.main()
