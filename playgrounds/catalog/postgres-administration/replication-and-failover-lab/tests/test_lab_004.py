import unittest

from lab_004 import recover_replication_and_failover_lab_split_brain


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_promote_replica_failure(self):
        self.assertEqual(recover_replication_and_failover_lab_split_brain({'operation': 'promote replica', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'failover plan'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'failover plan'})

    def test_fails_permanent_split_brain(self):
        self.assertEqual(recover_replication_and_failover_lab_split_brain({'operation': 'promote replica', 'error': 'split brain', 'attempt': 1, 'max_attempts': 3, 'resource': 'failover plan'}), {'decision': 'fail', 'reason': 'split brain', 'resource': 'failover plan'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_replication_and_failover_lab_split_brain({'operation': 'promote replica', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'failover plan'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'failover plan'})


if __name__ == "__main__":
    unittest.main()
