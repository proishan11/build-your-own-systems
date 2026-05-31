import unittest

from lab_004 import recover_layer_4_load_balancer_unhealthy_backend


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_choose_backend_failure(self):
        self.assertEqual(recover_layer_4_load_balancer_unhealthy_backend({'operation': 'choose backend', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'backend pool'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'backend pool'})

    def test_fails_permanent_unhealthy_backend(self):
        self.assertEqual(recover_layer_4_load_balancer_unhealthy_backend({'operation': 'choose backend', 'error': 'unhealthy backend', 'attempt': 1, 'max_attempts': 3, 'resource': 'backend pool'}), {'decision': 'fail', 'reason': 'unhealthy backend', 'resource': 'backend pool'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_layer_4_load_balancer_unhealthy_backend({'operation': 'choose backend', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'backend pool'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'backend pool'})


if __name__ == "__main__":
    unittest.main()
