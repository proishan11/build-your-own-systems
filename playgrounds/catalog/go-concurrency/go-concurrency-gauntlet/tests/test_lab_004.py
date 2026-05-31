import unittest

from lab_004 import recover_go_concurrency_gauntlet_blocked_sender


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_fan_out_work_failure(self):
        self.assertEqual(recover_go_concurrency_gauntlet_blocked_sender({'operation': 'fan out work', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'worker group'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'worker group'})

    def test_fails_permanent_blocked_sender(self):
        self.assertEqual(recover_go_concurrency_gauntlet_blocked_sender({'operation': 'fan out work', 'error': 'blocked sender', 'attempt': 1, 'max_attempts': 3, 'resource': 'worker group'}), {'decision': 'fail', 'reason': 'blocked sender', 'resource': 'worker group'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_go_concurrency_gauntlet_blocked_sender({'operation': 'fan out work', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'worker group'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'worker group'})


if __name__ == "__main__":
    unittest.main()
