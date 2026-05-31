import unittest

from lab_004 import recover_kubernetes_controller_from_scratch_stale_observed_generation


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_reconcile_object_failure(self):
        self.assertEqual(recover_kubernetes_controller_from_scratch_stale_observed_generation({'operation': 'reconcile object', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'reconcile state'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'reconcile state'})

    def test_fails_permanent_stale_observed_generation(self):
        self.assertEqual(recover_kubernetes_controller_from_scratch_stale_observed_generation({'operation': 'reconcile object', 'error': 'stale observed generation', 'attempt': 1, 'max_attempts': 3, 'resource': 'reconcile state'}), {'decision': 'fail', 'reason': 'stale observed generation', 'resource': 'reconcile state'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_kubernetes_controller_from_scratch_stale_observed_generation({'operation': 'reconcile object', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'reconcile state'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'reconcile state'})


if __name__ == "__main__":
    unittest.main()
