import unittest

from lab_004 import recover_scheduler_simulator_resource_overcommit


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_bind_pod_failure(self):
        self.assertEqual(recover_scheduler_simulator_resource_overcommit({'operation': 'bind pod', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'node inventory'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'node inventory'})

    def test_fails_permanent_resource_overcommit(self):
        self.assertEqual(recover_scheduler_simulator_resource_overcommit({'operation': 'bind pod', 'error': 'resource overcommit', 'attempt': 1, 'max_attempts': 3, 'resource': 'node inventory'}), {'decision': 'fail', 'reason': 'resource overcommit', 'resource': 'node inventory'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_scheduler_simulator_resource_overcommit({'operation': 'bind pod', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'node inventory'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'node inventory'})


if __name__ == "__main__":
    unittest.main()
