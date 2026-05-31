import unittest

from lab_004 import recover_xv6_style_kernel_lab_invalid_trap_frame


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_enter_kernel_failure(self):
        self.assertEqual(recover_xv6_style_kernel_lab_invalid_trap_frame({'operation': 'enter kernel', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'process table'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'process table'})

    def test_fails_permanent_invalid_trap_frame(self):
        self.assertEqual(recover_xv6_style_kernel_lab_invalid_trap_frame({'operation': 'enter kernel', 'error': 'invalid trap frame', 'attempt': 1, 'max_attempts': 3, 'resource': 'process table'}), {'decision': 'fail', 'reason': 'invalid trap frame', 'resource': 'process table'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_xv6_style_kernel_lab_invalid_trap_frame({'operation': 'enter kernel', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'process table'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'process table'})


if __name__ == "__main__":
    unittest.main()
