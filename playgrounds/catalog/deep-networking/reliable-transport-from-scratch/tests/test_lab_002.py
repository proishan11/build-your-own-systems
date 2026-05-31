import unittest

from lab_002 import apply_reliable_transport_from_scratch_transport_segment_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_transport_segment_events_idempotently(self):
        self.assertEqual(apply_reliable_transport_from_scratch_transport_segment_event([{'id': 'e1', 'resource': 'receive window', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'receive window', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'receive window', 'version': 2, 'state': 'committed'}]), {'resource': 'receive window', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_transport_segment_event(self):
        self.assertEqual(apply_reliable_transport_from_scratch_transport_segment_event([{'id': 'e1', 'resource': 'receive window', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'receive window', 'version': 1, 'state': 'old'}]), {'resource': 'receive window', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_reliable_transport_from_scratch_transport_segment_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
