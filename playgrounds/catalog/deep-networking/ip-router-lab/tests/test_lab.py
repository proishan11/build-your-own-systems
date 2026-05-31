import unittest

from lab import forward_packet_ip_packet


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_ip_packet_request(self):
        self.assertEqual(forward_packet_ip_packet({'id': 'ip-packet-001', 'kind': 'forward packet', 'target': 'routing table', 'priority': 2, 'metadata': {'source': 'IP Router Lab', 'track': 'deep-networking'}}), {'id': 'ip-packet-001', 'action': 'forward packet', 'target': 'routing table', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_ip_packet_request(self):
        self.assertEqual(forward_packet_ip_packet({'id': 'bad', 'kind': '', 'target': 'routing table', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'routing table', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'ip-packet-001', 'kind': 'forward packet', 'target': 'routing table', 'priority': 2, 'metadata': {'source': 'IP Router Lab', 'track': 'deep-networking'}}
        original = dict(request)
        forward_packet_ip_packet(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
