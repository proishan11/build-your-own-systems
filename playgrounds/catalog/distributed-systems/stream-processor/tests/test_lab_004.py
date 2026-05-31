import unittest

from lab_004 import recover_stream_processor_late_event


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_advance_watermark_failure(self):
        self.assertEqual(recover_stream_processor_late_event({'operation': 'advance watermark', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'watermark state'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'watermark state'})

    def test_fails_permanent_late_event(self):
        self.assertEqual(recover_stream_processor_late_event({'operation': 'advance watermark', 'error': 'late event', 'attempt': 1, 'max_attempts': 3, 'resource': 'watermark state'}), {'decision': 'fail', 'reason': 'late event', 'resource': 'watermark state'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_stream_processor_late_event({'operation': 'advance watermark', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'watermark state'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'watermark state'})


if __name__ == "__main__":
    unittest.main()
