import unittest

from lab_004 import recover_model_router_context_overflow


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_route_model_failure(self):
        self.assertEqual(recover_model_router_context_overflow({'operation': 'route model', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'model catalog'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'model catalog'})

    def test_fails_permanent_context_overflow(self):
        self.assertEqual(recover_model_router_context_overflow({'operation': 'route model', 'error': 'context overflow', 'attempt': 1, 'max_attempts': 3, 'resource': 'model catalog'}), {'decision': 'fail', 'reason': 'context overflow', 'resource': 'model catalog'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_model_router_context_overflow({'operation': 'route model', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'model catalog'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'model catalog'})


if __name__ == "__main__":
    unittest.main()
