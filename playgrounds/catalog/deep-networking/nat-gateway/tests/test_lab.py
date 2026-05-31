import unittest

from lab import allocate_port_outbound_flow


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_outbound_flow_request(self):
        self.assertEqual(allocate_port_outbound_flow({'id': 'outbound-flow-001', 'kind': 'allocate port', 'target': 'translation table', 'priority': 2, 'metadata': {'source': 'NAT Gateway', 'track': 'deep-networking'}}), {'id': 'outbound-flow-001', 'action': 'allocate port', 'target': 'translation table', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_outbound_flow_request(self):
        self.assertEqual(allocate_port_outbound_flow({'id': 'bad', 'kind': '', 'target': 'translation table', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'translation table', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'outbound-flow-001', 'kind': 'allocate port', 'target': 'translation table', 'priority': 2, 'metadata': {'source': 'NAT Gateway', 'track': 'deep-networking'}}
        original = dict(request)
        allocate_port_outbound_flow(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
