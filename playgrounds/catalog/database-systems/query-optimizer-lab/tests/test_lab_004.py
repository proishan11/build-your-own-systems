import unittest

from lab_004 import recover_query_optimizer_lab_bad_cardinality_estimate


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_choose_plan_failure(self):
        self.assertEqual(recover_query_optimizer_lab_bad_cardinality_estimate({'operation': 'choose plan', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'plan space'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'plan space'})

    def test_fails_permanent_bad_cardinality_estimate(self):
        self.assertEqual(recover_query_optimizer_lab_bad_cardinality_estimate({'operation': 'choose plan', 'error': 'bad cardinality estimate', 'attempt': 1, 'max_attempts': 3, 'resource': 'plan space'}), {'decision': 'fail', 'reason': 'bad cardinality estimate', 'resource': 'plan space'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_query_optimizer_lab_bad_cardinality_estimate({'operation': 'choose plan', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'plan space'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'plan space'})


if __name__ == "__main__":
    unittest.main()
