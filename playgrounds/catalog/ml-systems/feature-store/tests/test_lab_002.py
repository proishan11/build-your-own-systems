import unittest

from lab_002 import apply_feature_store_feature_row_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_feature_row_events_idempotently(self):
        self.assertEqual(apply_feature_store_feature_row_event([{'id': 'e1', 'resource': 'feature registry', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'feature registry', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'feature registry', 'version': 2, 'state': 'committed'}]), {'resource': 'feature registry', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_feature_row_event(self):
        self.assertEqual(apply_feature_store_feature_row_event([{'id': 'e1', 'resource': 'feature registry', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'feature registry', 'version': 1, 'state': 'old'}]), {'resource': 'feature registry', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_feature_store_feature_row_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
