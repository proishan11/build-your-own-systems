import unittest

from lab_004 import recover_auth_and_session_system_session_fixation


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_authenticate_session_failure(self):
        self.assertEqual(recover_auth_and_session_system_session_fixation({'operation': 'authenticate session', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'session store'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'session store'})

    def test_fails_permanent_session_fixation(self):
        self.assertEqual(recover_auth_and_session_system_session_fixation({'operation': 'authenticate session', 'error': 'session fixation', 'attempt': 1, 'max_attempts': 3, 'resource': 'session store'}), {'decision': 'fail', 'reason': 'session fixation', 'resource': 'session store'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_auth_and_session_system_session_fixation({'operation': 'authenticate session', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'session store'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'session store'})


if __name__ == "__main__":
    unittest.main()
