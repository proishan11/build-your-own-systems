import unittest

from lab import authenticate_session_session_token


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_session_token_request(self):
        self.assertEqual(authenticate_session_session_token({'id': 'session-token-001', 'kind': 'authenticate session', 'target': 'session store', 'priority': 2, 'metadata': {'source': 'Auth and Session System', 'track': 'security-engineering'}}), {'id': 'session-token-001', 'action': 'authenticate session', 'target': 'session store', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_session_token_request(self):
        self.assertEqual(authenticate_session_session_token({'id': 'bad', 'kind': '', 'target': 'session store', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'session store', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'session-token-001', 'kind': 'authenticate session', 'target': 'session store', 'priority': 2, 'metadata': {'source': 'Auth and Session System', 'track': 'security-engineering'}}
        original = dict(request)
        authenticate_session_session_token(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
