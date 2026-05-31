import unittest

from lab_004 import recover_secrets_manager_plaintext_exposure


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_rotate_secret_failure(self):
        self.assertEqual(recover_secrets_manager_plaintext_exposure({'operation': 'rotate secret', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'secret store'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'secret store'})

    def test_fails_permanent_plaintext_exposure(self):
        self.assertEqual(recover_secrets_manager_plaintext_exposure({'operation': 'rotate secret', 'error': 'plaintext exposure', 'attempt': 1, 'max_attempts': 3, 'resource': 'secret store'}), {'decision': 'fail', 'reason': 'plaintext exposure', 'resource': 'secret store'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_secrets_manager_plaintext_exposure({'operation': 'rotate secret', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'secret store'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'secret store'})


if __name__ == "__main__":
    unittest.main()
