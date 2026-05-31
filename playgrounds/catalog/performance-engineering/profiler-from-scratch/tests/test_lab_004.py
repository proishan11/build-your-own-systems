import unittest

from lab_004 import recover_profiler_from_scratch_missing_frame


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_aggregate_sample_failure(self):
        self.assertEqual(recover_profiler_from_scratch_missing_frame({'operation': 'aggregate sample', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'profile tree'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'profile tree'})

    def test_fails_permanent_missing_frame(self):
        self.assertEqual(recover_profiler_from_scratch_missing_frame({'operation': 'aggregate sample', 'error': 'missing frame', 'attempt': 1, 'max_attempts': 3, 'resource': 'profile tree'}), {'decision': 'fail', 'reason': 'missing frame', 'resource': 'profile tree'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_profiler_from_scratch_missing_frame({'operation': 'aggregate sample', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'profile tree'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'profile tree'})


if __name__ == "__main__":
    unittest.main()
