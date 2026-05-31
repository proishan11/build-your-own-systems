import unittest

from lab import transform_stream_file_stream


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_file_stream_request(self):
        self.assertEqual(transform_stream_file_stream({'id': 'file-stream-001', 'kind': 'transform stream', 'target': 'command input', 'priority': 2, 'metadata': {'source': 'Coreutils From Scratch', 'track': 'tooling-foundations'}}), {'id': 'file-stream-001', 'action': 'transform stream', 'target': 'command input', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_file_stream_request(self):
        self.assertEqual(transform_stream_file_stream({'id': 'bad', 'kind': '', 'target': 'command input', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'command input', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'file-stream-001', 'kind': 'transform stream', 'target': 'command input', 'priority': 2, 'metadata': {'source': 'Coreutils From Scratch', 'track': 'tooling-foundations'}}
        original = dict(request)
        transform_stream_file_stream(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
