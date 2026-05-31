import unittest

from lab_004 import recover_operator_for_postgresql_backups_missing_wal_archive


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_start_backup_failure(self):
        self.assertEqual(recover_operator_for_postgresql_backups_missing_wal_archive({'operation': 'start backup', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'backup schedule'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'backup schedule'})

    def test_fails_permanent_missing_wal_archive(self):
        self.assertEqual(recover_operator_for_postgresql_backups_missing_wal_archive({'operation': 'start backup', 'error': 'missing wal archive', 'attempt': 1, 'max_attempts': 3, 'resource': 'backup schedule'}), {'decision': 'fail', 'reason': 'missing wal archive', 'resource': 'backup schedule'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_operator_for_postgresql_backups_missing_wal_archive({'operation': 'start backup', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'backup schedule'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'backup schedule'})


if __name__ == "__main__":
    unittest.main()
