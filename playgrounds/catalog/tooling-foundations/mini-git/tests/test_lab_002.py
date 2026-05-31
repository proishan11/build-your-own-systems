import unittest

from lab_002 import apply_mini_git_git_object_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_git_object_events_idempotently(self):
        self.assertEqual(apply_mini_git_git_object_event([{'id': 'e1', 'resource': 'object database', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'object database', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'object database', 'version': 2, 'state': 'committed'}]), {'resource': 'object database', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_git_object_event(self):
        self.assertEqual(apply_mini_git_git_object_event([{'id': 'e1', 'resource': 'object database', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'object database', 'version': 1, 'state': 'old'}]), {'resource': 'object database', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_mini_git_git_object_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
