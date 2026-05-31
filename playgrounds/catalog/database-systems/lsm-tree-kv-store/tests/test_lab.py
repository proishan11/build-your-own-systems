import unittest

from lab import compact_run_memtable_write


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_memtable_write_request(self):
        self.assertEqual(compact_run_memtable_write({'id': 'memtable-write-001', 'kind': 'compact run', 'target': 'sstable level', 'priority': 2, 'metadata': {'source': 'LSM Tree KV Store', 'track': 'database-systems'}}), {'id': 'memtable-write-001', 'action': 'compact run', 'target': 'sstable level', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_memtable_write_request(self):
        self.assertEqual(compact_run_memtable_write({'id': 'bad', 'kind': '', 'target': 'sstable level', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'sstable level', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'memtable-write-001', 'kind': 'compact run', 'target': 'sstable level', 'priority': 2, 'metadata': {'source': 'LSM Tree KV Store', 'track': 'database-systems'}}
        original = dict(request)
        compact_run_memtable_write(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
