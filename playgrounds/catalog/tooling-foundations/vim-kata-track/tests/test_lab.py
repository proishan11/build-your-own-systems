import unittest

from lab import apply_motion_editor_command


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_editor_command_request(self):
        self.assertEqual(apply_motion_editor_command({'id': 'editor-command-001', 'kind': 'apply motion', 'target': 'buffer state', 'priority': 2, 'metadata': {'source': 'Vim Kata Track', 'track': 'tooling-foundations'}}), {'id': 'editor-command-001', 'action': 'apply motion', 'target': 'buffer state', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_editor_command_request(self):
        self.assertEqual(apply_motion_editor_command({'id': 'bad', 'kind': '', 'target': 'buffer state', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'buffer state', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'editor-command-001', 'kind': 'apply motion', 'target': 'buffer state', 'priority': 2, 'metadata': {'source': 'Vim Kata Track', 'track': 'tooling-foundations'}}
        original = dict(request)
        apply_motion_editor_command(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
