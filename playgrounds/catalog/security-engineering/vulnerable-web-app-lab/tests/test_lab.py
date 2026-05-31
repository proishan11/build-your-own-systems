import unittest

from lab import sanitize_request_http_input


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_http_input_request(self):
        self.assertEqual(sanitize_request_http_input({'id': 'http-input-001', 'kind': 'sanitize request', 'target': 'security policy', 'priority': 2, 'metadata': {'source': 'Vulnerable Web App Lab', 'track': 'security-engineering'}}), {'id': 'http-input-001', 'action': 'sanitize request', 'target': 'security policy', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_http_input_request(self):
        self.assertEqual(sanitize_request_http_input({'id': 'bad', 'kind': '', 'target': 'security policy', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'security policy', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'http-input-001', 'kind': 'sanitize request', 'target': 'security policy', 'priority': 2, 'metadata': {'source': 'Vulnerable Web App Lab', 'track': 'security-engineering'}}
        original = dict(request)
        sanitize_request_http_input(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
