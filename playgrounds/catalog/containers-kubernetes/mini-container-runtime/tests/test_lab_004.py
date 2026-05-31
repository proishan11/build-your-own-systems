import unittest

from lab_004 import recover_mini_container_runtime_missing_isolation


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_start_container_failure(self):
        self.assertEqual(recover_mini_container_runtime_missing_isolation({'operation': 'start container', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'namespace plan'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'namespace plan'})

    def test_fails_permanent_missing_isolation(self):
        self.assertEqual(recover_mini_container_runtime_missing_isolation({'operation': 'start container', 'error': 'missing isolation', 'attempt': 1, 'max_attempts': 3, 'resource': 'namespace plan'}), {'decision': 'fail', 'reason': 'missing isolation', 'resource': 'namespace plan'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_mini_container_runtime_missing_isolation({'operation': 'start container', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'namespace plan'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'namespace plan'})


if __name__ == "__main__":
    unittest.main()
