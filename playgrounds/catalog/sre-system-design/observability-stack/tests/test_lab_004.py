import unittest

from lab_004 import recover_observability_stack_cardinality_explosion


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_ingest_telemetry_failure(self):
        self.assertEqual(recover_observability_stack_cardinality_explosion({'operation': 'ingest telemetry', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'signal pipeline'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'signal pipeline'})

    def test_fails_permanent_cardinality_explosion(self):
        self.assertEqual(recover_observability_stack_cardinality_explosion({'operation': 'ingest telemetry', 'error': 'cardinality explosion', 'attempt': 1, 'max_attempts': 3, 'resource': 'signal pipeline'}), {'decision': 'fail', 'reason': 'cardinality explosion', 'resource': 'signal pipeline'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_observability_stack_cardinality_explosion({'operation': 'ingest telemetry', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'signal pipeline'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'signal pipeline'})


if __name__ == "__main__":
    unittest.main()
