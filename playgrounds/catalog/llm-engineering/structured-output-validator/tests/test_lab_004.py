import unittest

from lab_004 import recover_structured_output_validator_schema_violation


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_validate_output_failure(self):
        self.assertEqual(recover_structured_output_validator_schema_violation({'operation': 'validate output', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'json schema'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'json schema'})

    def test_fails_permanent_schema_violation(self):
        self.assertEqual(recover_structured_output_validator_schema_violation({'operation': 'validate output', 'error': 'schema violation', 'attempt': 1, 'max_attempts': 3, 'resource': 'json schema'}), {'decision': 'fail', 'reason': 'schema violation', 'resource': 'json schema'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_structured_output_validator_schema_violation({'operation': 'validate output', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'json schema'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'json schema'})


if __name__ == "__main__":
    unittest.main()
