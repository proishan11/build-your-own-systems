import unittest

from lab_002 import apply_lock_contention_lab_lock_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_lock_events_idempotently(self):
        self.assertEqual(apply_lock_contention_lab_lock_event([{'id': 'e1', 'resource': 'wait graph', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'wait graph', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'wait graph', 'version': 2, 'state': 'committed'}]), {'resource': 'wait graph', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_lock_event(self):
        self.assertEqual(apply_lock_contention_lab_lock_event([{'id': 'e1', 'resource': 'wait graph', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'wait graph', 'version': 1, 'state': 'old'}]), {'resource': 'wait graph', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_lock_contention_lab_lock_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
