import unittest

from lab_002 import apply_llm_trace_store_llm_span_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_llm_span_events_idempotently(self):
        self.assertEqual(apply_llm_trace_store_llm_span_event([{'id': 'e1', 'resource': 'trace index', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'trace index', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'trace index', 'version': 2, 'state': 'committed'}]), {'resource': 'trace index', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_llm_span_event(self):
        self.assertEqual(apply_llm_trace_store_llm_span_event([{'id': 'e1', 'resource': 'trace index', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'trace index', 'version': 1, 'state': 'old'}]), {'resource': 'trace index', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_llm_trace_store_llm_span_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
