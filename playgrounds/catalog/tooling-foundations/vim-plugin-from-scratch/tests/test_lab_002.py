import unittest

from lab_002 import apply_vim_plugin_from_scratch_plugin_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_plugin_events_idempotently(self):
        self.assertEqual(apply_vim_plugin_from_scratch_plugin_event([{'id': 'e1', 'resource': 'editor state', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'editor state', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'editor state', 'version': 2, 'state': 'committed'}]), {'resource': 'editor state', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_plugin_event(self):
        self.assertEqual(apply_vim_plugin_from_scratch_plugin_event([{'id': 'e1', 'resource': 'editor state', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'editor state', 'version': 1, 'state': 'old'}]), {'resource': 'editor state', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_vim_plugin_from_scratch_plugin_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
