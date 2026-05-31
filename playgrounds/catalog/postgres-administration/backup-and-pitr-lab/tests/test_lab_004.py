import unittest

from lab_004 import recover_backup_and_pitr_lab_missing_base_backup


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_restore_target_failure(self):
        self.assertEqual(recover_backup_and_pitr_lab_missing_base_backup({'operation': 'restore target', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'backup catalog'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'backup catalog'})

    def test_fails_permanent_missing_base_backup(self):
        self.assertEqual(recover_backup_and_pitr_lab_missing_base_backup({'operation': 'restore target', 'error': 'missing base backup', 'attempt': 1, 'max_attempts': 3, 'resource': 'backup catalog'}), {'decision': 'fail', 'reason': 'missing base backup', 'resource': 'backup catalog'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_backup_and_pitr_lab_missing_base_backup({'operation': 'restore target', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'backup catalog'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'backup catalog'})


if __name__ == "__main__":
    unittest.main()
