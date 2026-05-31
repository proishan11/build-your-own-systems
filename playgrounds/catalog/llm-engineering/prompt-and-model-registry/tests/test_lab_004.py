import unittest

from lab_004 import recover_prompt_and_model_registry_unsafe_prompt_change


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_publish_prompt_failure(self):
        self.assertEqual(recover_prompt_and_model_registry_unsafe_prompt_change({'operation': 'publish prompt', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'model binding'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'model binding'})

    def test_fails_permanent_unsafe_prompt_change(self):
        self.assertEqual(recover_prompt_and_model_registry_unsafe_prompt_change({'operation': 'publish prompt', 'error': 'unsafe prompt change', 'attempt': 1, 'max_attempts': 3, 'resource': 'model binding'}), {'decision': 'fail', 'reason': 'unsafe prompt change', 'resource': 'model binding'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_prompt_and_model_registry_unsafe_prompt_change({'operation': 'publish prompt', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'model binding'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'model binding'})


if __name__ == "__main__":
    unittest.main()
