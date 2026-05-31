import unittest

from lab_004 import recover_mini_git_hash_mismatch


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_write_object_failure(self):
        self.assertEqual(recover_mini_git_hash_mismatch({'operation': 'write object', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'object database'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'object database'})

    def test_fails_permanent_hash_mismatch(self):
        self.assertEqual(recover_mini_git_hash_mismatch({'operation': 'write object', 'error': 'hash mismatch', 'attempt': 1, 'max_attempts': 3, 'resource': 'object database'}), {'decision': 'fail', 'reason': 'hash mismatch', 'resource': 'object database'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_mini_git_hash_mismatch({'operation': 'write object', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'object database'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'object database'})


if __name__ == "__main__":
    unittest.main()
