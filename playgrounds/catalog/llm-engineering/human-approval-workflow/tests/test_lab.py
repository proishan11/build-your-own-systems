import unittest

from lab import route_approval_approval_request


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_approval_request_request(self):
        self.assertEqual(route_approval_approval_request({'id': 'approval-request-001', 'kind': 'route approval', 'target': 'approval queue', 'priority': 2, 'metadata': {'source': 'Human Approval Workflow', 'track': 'llm-engineering'}}), {'id': 'approval-request-001', 'action': 'route approval', 'target': 'approval queue', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_approval_request_request(self):
        self.assertEqual(route_approval_approval_request({'id': 'bad', 'kind': '', 'target': 'approval queue', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'approval queue', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'approval-request-001', 'kind': 'route approval', 'target': 'approval queue', 'priority': 2, 'metadata': {'source': 'Human Approval Workflow', 'track': 'llm-engineering'}}
        original = dict(request)
        route_approval_approval_request(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
