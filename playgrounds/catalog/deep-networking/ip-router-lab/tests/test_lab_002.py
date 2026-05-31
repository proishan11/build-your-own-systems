import unittest

from lab_002 import apply_ip_router_lab_ip_packet_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_ip_packet_events_idempotently(self):
        self.assertEqual(apply_ip_router_lab_ip_packet_event([{'id': 'e1', 'resource': 'routing table', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'routing table', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'routing table', 'version': 2, 'state': 'committed'}]), {'resource': 'routing table', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_ip_packet_event(self):
        self.assertEqual(apply_ip_router_lab_ip_packet_event([{'id': 'e1', 'resource': 'routing table', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'routing table', 'version': 1, 'state': 'old'}]), {'resource': 'routing table', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_ip_router_lab_ip_packet_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
