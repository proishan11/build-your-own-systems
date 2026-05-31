import unittest

from lab import dispatch_handler_http_request


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_http_request_request(self):
        self.assertEqual(dispatch_handler_http_request({'id': 'http-request-001', 'kind': 'dispatch handler', 'target': 'route table', 'priority': 2, 'metadata': {'source': 'HTTP Server From Scratch', 'track': 'networking'}}), {'id': 'http-request-001', 'action': 'dispatch handler', 'target': 'route table', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_http_request_request(self):
        self.assertEqual(dispatch_handler_http_request({'id': 'bad', 'kind': '', 'target': 'route table', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'route table', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'http-request-001', 'kind': 'dispatch handler', 'target': 'route table', 'priority': 2, 'metadata': {'source': 'HTTP Server From Scratch', 'track': 'networking'}}
        original = dict(request)
        dispatch_handler_http_request(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
