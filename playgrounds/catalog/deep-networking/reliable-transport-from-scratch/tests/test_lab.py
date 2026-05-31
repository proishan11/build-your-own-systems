import unittest

from lab import ack_segment_transport_segment


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_transport_segment_request(self):
        self.assertEqual(ack_segment_transport_segment({'id': 'transport-segment-001', 'kind': 'ack segment', 'target': 'receive window', 'priority': 2, 'metadata': {'source': 'Reliable Transport From Scratch', 'track': 'deep-networking'}}), {'id': 'transport-segment-001', 'action': 'ack segment', 'target': 'receive window', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_transport_segment_request(self):
        self.assertEqual(ack_segment_transport_segment({'id': 'bad', 'kind': '', 'target': 'receive window', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'receive window', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'transport-segment-001', 'kind': 'ack segment', 'target': 'receive window', 'priority': 2, 'metadata': {'source': 'Reliable Transport From Scratch', 'track': 'deep-networking'}}
        original = dict(request)
        ack_segment_transport_segment(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
