import unittest

from lab_004 import recover_tiny_journaling_file_system_torn_journal_write


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_commit_record_failure(self):
        self.assertEqual(recover_tiny_journaling_file_system_torn_journal_write({'operation': 'commit record', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'inode block'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'inode block'})

    def test_fails_permanent_torn_journal_write(self):
        self.assertEqual(recover_tiny_journaling_file_system_torn_journal_write({'operation': 'commit record', 'error': 'torn journal write', 'attempt': 1, 'max_attempts': 3, 'resource': 'inode block'}), {'decision': 'fail', 'reason': 'torn journal write', 'resource': 'inode block'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_tiny_journaling_file_system_torn_journal_write({'operation': 'commit record', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'inode block'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'inode block'})


if __name__ == "__main__":
    unittest.main()
