import unittest

from lab_004 import recover_event_loop_and_async_runtime_stalled_timer


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_schedule_callback_failure(self):
        self.assertEqual(recover_event_loop_and_async_runtime_stalled_timer({'operation': 'schedule callback', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'ready queue'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'ready queue'})

    def test_fails_permanent_stalled_timer(self):
        self.assertEqual(recover_event_loop_and_async_runtime_stalled_timer({'operation': 'schedule callback', 'error': 'stalled timer', 'attempt': 1, 'max_attempts': 3, 'resource': 'ready queue'}), {'decision': 'fail', 'reason': 'stalled timer', 'resource': 'ready queue'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_event_loop_and_async_runtime_stalled_timer({'operation': 'schedule callback', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'ready queue'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'ready queue'})


if __name__ == "__main__":
    unittest.main()
