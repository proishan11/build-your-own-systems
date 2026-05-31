import unittest

from lab_004 import recover_llm_trace_store_missing_parent_span


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_record_span_failure(self):
        self.assertEqual(recover_llm_trace_store_missing_parent_span({'operation': 'record span', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'trace index'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'trace index'})

    def test_fails_permanent_missing_parent_span(self):
        self.assertEqual(recover_llm_trace_store_missing_parent_span({'operation': 'record span', 'error': 'missing parent span', 'attempt': 1, 'max_attempts': 3, 'resource': 'trace index'}), {'decision': 'fail', 'reason': 'missing parent span', 'resource': 'trace index'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_llm_trace_store_missing_parent_span({'operation': 'record span', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'trace index'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'trace index'})


if __name__ == "__main__":
    unittest.main()
