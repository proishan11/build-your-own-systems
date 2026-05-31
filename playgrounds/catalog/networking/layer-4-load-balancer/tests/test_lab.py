import unittest

from lab import choose_backend_tcp_flow


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_tcp_flow_request(self):
        self.assertEqual(choose_backend_tcp_flow({'id': 'tcp-flow-001', 'kind': 'choose backend', 'target': 'backend pool', 'priority': 2, 'metadata': {'source': 'Layer 4 Load Balancer', 'track': 'networking'}}), {'id': 'tcp-flow-001', 'action': 'choose backend', 'target': 'backend pool', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_tcp_flow_request(self):
        self.assertEqual(choose_backend_tcp_flow({'id': 'bad', 'kind': '', 'target': 'backend pool', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'backend pool', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'tcp-flow-001', 'kind': 'choose backend', 'target': 'backend pool', 'priority': 2, 'metadata': {'source': 'Layer 4 Load Balancer', 'track': 'networking'}}
        original = dict(request)
        choose_backend_tcp_flow(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
