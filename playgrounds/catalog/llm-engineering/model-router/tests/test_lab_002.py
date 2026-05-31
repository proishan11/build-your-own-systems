import unittest

from lab_002 import apply_model_router_llm_request_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_llm_request_events_idempotently(self):
        self.assertEqual(apply_model_router_llm_request_event([{'id': 'e1', 'resource': 'model catalog', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'model catalog', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'model catalog', 'version': 2, 'state': 'committed'}]), {'resource': 'model catalog', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_llm_request_event(self):
        self.assertEqual(apply_model_router_llm_request_event([{'id': 'e1', 'resource': 'model catalog', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'model catalog', 'version': 1, 'state': 'old'}]), {'resource': 'model catalog', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_model_router_llm_request_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
