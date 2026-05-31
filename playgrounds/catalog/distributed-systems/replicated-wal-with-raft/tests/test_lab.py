import unittest

from lab import append_entries_raft_log_entry


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_raft_log_entry_request(self):
        self.assertEqual(append_entries_raft_log_entry({'id': 'raft-log-entry-001', 'kind': 'append entries', 'target': 'replica log', 'priority': 2, 'metadata': {'source': 'Replicated WAL With Raft', 'track': 'distributed-systems'}}), {'id': 'raft-log-entry-001', 'action': 'append entries', 'target': 'replica log', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_raft_log_entry_request(self):
        self.assertEqual(append_entries_raft_log_entry({'id': 'bad', 'kind': '', 'target': 'replica log', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'replica log', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'raft-log-entry-001', 'kind': 'append entries', 'target': 'replica log', 'priority': 2, 'metadata': {'source': 'Replicated WAL With Raft', 'track': 'distributed-systems'}}
        original = dict(request)
        append_entries_raft_log_entry(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
