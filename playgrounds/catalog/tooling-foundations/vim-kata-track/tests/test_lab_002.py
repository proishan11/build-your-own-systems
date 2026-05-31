import unittest

from lab_002 import apply_vim_kata_track_editor_command_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_editor_command_events_idempotently(self):
        self.assertEqual(apply_vim_kata_track_editor_command_event([{'id': 'e1', 'resource': 'buffer state', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'buffer state', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'buffer state', 'version': 2, 'state': 'committed'}]), {'resource': 'buffer state', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_editor_command_event(self):
        self.assertEqual(apply_vim_kata_track_editor_command_event([{'id': 'e1', 'resource': 'buffer state', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'buffer state', 'version': 1, 'state': 'old'}]), {'resource': 'buffer state', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_vim_kata_track_editor_command_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
