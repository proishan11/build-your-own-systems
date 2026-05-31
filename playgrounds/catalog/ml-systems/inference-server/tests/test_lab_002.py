import unittest

from lab_002 import apply_inference_server_inference_request_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_inference_request_events_idempotently(self):
        self.assertEqual(apply_inference_server_inference_request_event([{'id': 'e1', 'resource': 'batch queue', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'batch queue', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'batch queue', 'version': 2, 'state': 'committed'}]), {'resource': 'batch queue', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_inference_request_event(self):
        self.assertEqual(apply_inference_server_inference_request_event([{'id': 'e1', 'resource': 'batch queue', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'batch queue', 'version': 1, 'state': 'old'}]), {'resource': 'batch queue', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_inference_server_inference_request_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
