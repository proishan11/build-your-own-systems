import unittest

from lab import write_record_database_record


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_database_record_request(self):
        self.assertEqual(write_record_database_record({'id': 'database-record-001', 'kind': 'write record', 'target': 'page cache', 'priority': 2, 'metadata': {'source': 'MiniDB Storage Engine', 'track': 'database-systems'}}), {'id': 'database-record-001', 'action': 'write record', 'target': 'page cache', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_database_record_request(self):
        self.assertEqual(write_record_database_record({'id': 'bad', 'kind': '', 'target': 'page cache', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'page cache', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'database-record-001', 'kind': 'write record', 'target': 'page cache', 'priority': 2, 'metadata': {'source': 'MiniDB Storage Engine', 'track': 'database-systems'}}
        original = dict(request)
        write_record_database_record(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
