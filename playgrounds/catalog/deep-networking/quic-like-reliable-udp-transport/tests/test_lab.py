import unittest

from lab import ack_range_quic_frame


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_quic_frame_request(self):
        self.assertEqual(ack_range_quic_frame({'id': 'quic-frame-001', 'kind': 'ack range', 'target': 'connection state', 'priority': 2, 'metadata': {'source': 'QUIC-Like Reliable UDP Transport', 'track': 'deep-networking'}}), {'id': 'quic-frame-001', 'action': 'ack range', 'target': 'connection state', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_quic_frame_request(self):
        self.assertEqual(ack_range_quic_frame({'id': 'bad', 'kind': '', 'target': 'connection state', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'connection state', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'quic-frame-001', 'kind': 'ack range', 'target': 'connection state', 'priority': 2, 'metadata': {'source': 'QUIC-Like Reliable UDP Transport', 'track': 'deep-networking'}}
        original = dict(request)
        ack_range_quic_frame(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
