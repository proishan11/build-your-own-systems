import unittest

from lab_004 import recover_shell_text_processing_workbench_locale_mismatch


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_filter_record_failure(self):
        self.assertEqual(recover_shell_text_processing_workbench_locale_mismatch({'operation': 'filter record', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'pipeline stage'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'pipeline stage'})

    def test_fails_permanent_locale_mismatch(self):
        self.assertEqual(recover_shell_text_processing_workbench_locale_mismatch({'operation': 'filter record', 'error': 'locale mismatch', 'attempt': 1, 'max_attempts': 3, 'resource': 'pipeline stage'}), {'decision': 'fail', 'reason': 'locale mismatch', 'resource': 'pipeline stage'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_shell_text_processing_workbench_locale_mismatch({'operation': 'filter record', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'pipeline stage'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'pipeline stage'})


if __name__ == "__main__":
    unittest.main()
