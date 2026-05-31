import unittest

from lab_004 import recover_benchmark_harness_warmup_bias


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_compare_runs_failure(self):
        self.assertEqual(recover_benchmark_harness_warmup_bias({'operation': 'compare runs', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'run config'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'run config'})

    def test_fails_permanent_warmup_bias(self):
        self.assertEqual(recover_benchmark_harness_warmup_bias({'operation': 'compare runs', 'error': 'warmup bias', 'attempt': 1, 'max_attempts': 3, 'resource': 'run config'}), {'decision': 'fail', 'reason': 'warmup bias', 'resource': 'run config'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_benchmark_harness_warmup_bias({'operation': 'compare runs', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'run config'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'run config'})


if __name__ == "__main__":
    unittest.main()
