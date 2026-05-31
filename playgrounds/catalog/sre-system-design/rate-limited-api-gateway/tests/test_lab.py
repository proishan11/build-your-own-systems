import unittest

from lab import allow_request_api_request


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_api_request_request(self):
        self.assertEqual(allow_request_api_request({'id': 'api-request-001', 'kind': 'allow request', 'target': 'token bucket', 'priority': 2, 'metadata': {'source': 'Rate-Limited API Gateway', 'track': 'sre-system-design'}}), {'id': 'api-request-001', 'action': 'allow request', 'target': 'token bucket', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_api_request_request(self):
        self.assertEqual(allow_request_api_request({'id': 'bad', 'kind': '', 'target': 'token bucket', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'token bucket', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'api-request-001', 'kind': 'allow request', 'target': 'token bucket', 'priority': 2, 'metadata': {'source': 'Rate-Limited API Gateway', 'track': 'sre-system-design'}}
        original = dict(request)
        allow_request_api_request(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
