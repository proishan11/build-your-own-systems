import unittest

from lab_004 import recover_replicated_wal_with_raft_term_mismatch


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_append_entries_failure(self):
        self.assertEqual(recover_replicated_wal_with_raft_term_mismatch({'operation': 'append entries', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'replica log'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'replica log'})

    def test_fails_permanent_term_mismatch(self):
        self.assertEqual(recover_replicated_wal_with_raft_term_mismatch({'operation': 'append entries', 'error': 'term mismatch', 'attempt': 1, 'max_attempts': 3, 'resource': 'replica log'}), {'decision': 'fail', 'reason': 'term mismatch', 'resource': 'replica log'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_replicated_wal_with_raft_term_mismatch({'operation': 'append entries', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'replica log'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'replica log'})


if __name__ == "__main__":
    unittest.main()
