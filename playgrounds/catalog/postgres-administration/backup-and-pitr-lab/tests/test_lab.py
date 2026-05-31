import unittest

from lab import restore_target_wal_segment


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_wal_segment_request(self):
        self.assertEqual(restore_target_wal_segment({'id': 'wal-segment-001', 'kind': 'restore target', 'target': 'backup catalog', 'priority': 2, 'metadata': {'source': 'Backup and PITR Lab', 'track': 'postgres-administration'}}), {'id': 'wal-segment-001', 'action': 'restore target', 'target': 'backup catalog', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_wal_segment_request(self):
        self.assertEqual(restore_target_wal_segment({'id': 'bad', 'kind': '', 'target': 'backup catalog', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'backup catalog', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'wal-segment-001', 'kind': 'restore target', 'target': 'backup catalog', 'priority': 2, 'metadata': {'source': 'Backup and PITR Lab', 'track': 'postgres-administration'}}
        original = dict(request)
        restore_target_wal_segment(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
