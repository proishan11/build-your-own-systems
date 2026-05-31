import unittest

from lab_004 import recover_quic_like_reliable_udp_transport_lost_packet


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_ack_range_failure(self):
        self.assertEqual(recover_quic_like_reliable_udp_transport_lost_packet({'operation': 'ack range', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'connection state'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'connection state'})

    def test_fails_permanent_lost_packet(self):
        self.assertEqual(recover_quic_like_reliable_udp_transport_lost_packet({'operation': 'ack range', 'error': 'lost packet', 'attempt': 1, 'max_attempts': 3, 'resource': 'connection state'}), {'decision': 'fail', 'reason': 'lost packet', 'resource': 'connection state'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_quic_like_reliable_udp_transport_lost_packet({'operation': 'ack range', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'connection state'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'connection state'})


if __name__ == "__main__":
    unittest.main()
