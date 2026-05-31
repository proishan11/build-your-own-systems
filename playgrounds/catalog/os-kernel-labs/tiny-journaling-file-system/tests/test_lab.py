import unittest

from lab import commit_record_journal_transaction


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_journal_transaction_request(self):
        self.assertEqual(commit_record_journal_transaction({'id': 'journal-transaction-001', 'kind': 'commit record', 'target': 'inode block', 'priority': 2, 'metadata': {'source': 'Tiny Journaling File System', 'track': 'os-kernel-labs'}}), {'id': 'journal-transaction-001', 'action': 'commit record', 'target': 'inode block', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_journal_transaction_request(self):
        self.assertEqual(commit_record_journal_transaction({'id': 'bad', 'kind': '', 'target': 'inode block', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'inode block', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'journal-transaction-001', 'kind': 'commit record', 'target': 'inode block', 'priority': 2, 'metadata': {'source': 'Tiny Journaling File System', 'track': 'os-kernel-labs'}}
        original = dict(request)
        commit_record_journal_transaction(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
