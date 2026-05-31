import unittest

from lab_002 import apply_secrets_manager_secret_version_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_secret_version_events_idempotently(self):
        self.assertEqual(apply_secrets_manager_secret_version_event([{'id': 'e1', 'resource': 'secret store', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'secret store', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'secret store', 'version': 2, 'state': 'committed'}]), {'resource': 'secret store', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_secret_version_event(self):
        self.assertEqual(apply_secrets_manager_secret_version_event([{'id': 'e1', 'resource': 'secret store', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'secret store', 'version': 1, 'state': 'old'}]), {'resource': 'secret store', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_secrets_manager_secret_version_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
