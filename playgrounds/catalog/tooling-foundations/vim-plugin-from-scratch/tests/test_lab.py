import unittest

from lab import handle_autocmd_plugin_event


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_plugin_event_request(self):
        self.assertEqual(handle_autocmd_plugin_event({'id': 'plugin-event-001', 'kind': 'handle autocmd', 'target': 'editor state', 'priority': 2, 'metadata': {'source': 'Vim Plugin From Scratch', 'track': 'tooling-foundations'}}), {'id': 'plugin-event-001', 'action': 'handle autocmd', 'target': 'editor state', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_plugin_event_request(self):
        self.assertEqual(handle_autocmd_plugin_event({'id': 'bad', 'kind': '', 'target': 'editor state', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'editor state', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'plugin-event-001', 'kind': 'handle autocmd', 'target': 'editor state', 'priority': 2, 'metadata': {'source': 'Vim Plugin From Scratch', 'track': 'tooling-foundations'}}
        original = dict(request)
        handle_autocmd_plugin_event(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
