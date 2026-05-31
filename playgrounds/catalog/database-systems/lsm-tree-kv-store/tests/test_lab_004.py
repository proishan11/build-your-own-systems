import unittest

from lab_004 import recover_lsm_tree_kv_store_tombstone_resurrection


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_compact_run_failure(self):
        self.assertEqual(recover_lsm_tree_kv_store_tombstone_resurrection({'operation': 'compact run', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'sstable level'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'sstable level'})

    def test_fails_permanent_tombstone_resurrection(self):
        self.assertEqual(recover_lsm_tree_kv_store_tombstone_resurrection({'operation': 'compact run', 'error': 'tombstone resurrection', 'attempt': 1, 'max_attempts': 3, 'resource': 'sstable level'}), {'decision': 'fail', 'reason': 'tombstone resurrection', 'resource': 'sstable level'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_lsm_tree_kv_store_tombstone_resurrection({'operation': 'compact run', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'sstable level'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'sstable level'})


if __name__ == "__main__":
    unittest.main()
