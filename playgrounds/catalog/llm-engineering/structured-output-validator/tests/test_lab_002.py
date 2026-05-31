import unittest

from lab_002 import apply_structured_output_validator_model_output_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_model_output_events_idempotently(self):
        self.assertEqual(apply_structured_output_validator_model_output_event([{'id': 'e1', 'resource': 'json schema', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'json schema', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'json schema', 'version': 2, 'state': 'committed'}]), {'resource': 'json schema', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_model_output_event(self):
        self.assertEqual(apply_structured_output_validator_model_output_event([{'id': 'e1', 'resource': 'json schema', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'json schema', 'version': 1, 'state': 'old'}]), {'resource': 'json schema', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_structured_output_validator_model_output_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
