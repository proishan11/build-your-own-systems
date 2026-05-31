import unittest

from lab_004 import recover_model_registry_missing_lineage


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_promote_model_failure(self):
        self.assertEqual(recover_model_registry_missing_lineage({'operation': 'promote model', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'registry version'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'registry version'})

    def test_fails_permanent_missing_lineage(self):
        self.assertEqual(recover_model_registry_missing_lineage({'operation': 'promote model', 'error': 'missing lineage', 'attempt': 1, 'max_attempts': 3, 'resource': 'registry version'}), {'decision': 'fail', 'reason': 'missing lineage', 'resource': 'registry version'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_model_registry_missing_lineage({'operation': 'promote model', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'registry version'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'registry version'})


if __name__ == "__main__":
    unittest.main()
