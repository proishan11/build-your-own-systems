import unittest

from lab_004 import recover_cost_and_latency_dashboard_tail_spike


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_aggregate_sample_failure(self):
        self.assertEqual(recover_cost_and_latency_dashboard_tail_spike({'operation': 'aggregate sample', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'metric bucket'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'metric bucket'})

    def test_fails_permanent_tail_spike(self):
        self.assertEqual(recover_cost_and_latency_dashboard_tail_spike({'operation': 'aggregate sample', 'error': 'tail spike', 'attempt': 1, 'max_attempts': 3, 'resource': 'metric bucket'}), {'decision': 'fail', 'reason': 'tail spike', 'resource': 'metric bucket'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_cost_and_latency_dashboard_tail_spike({'operation': 'aggregate sample', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'metric bucket'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'metric bucket'})


if __name__ == "__main__":
    unittest.main()
