import unittest

from lab import advance_watermark_stream_event


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_stream_event_request(self):
        self.assertEqual(advance_watermark_stream_event({'id': 'stream-event-001', 'kind': 'advance watermark', 'target': 'watermark state', 'priority': 2, 'metadata': {'source': 'Stream Processor', 'track': 'distributed-systems'}}), {'id': 'stream-event-001', 'action': 'advance watermark', 'target': 'watermark state', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_stream_event_request(self):
        self.assertEqual(advance_watermark_stream_event({'id': 'bad', 'kind': '', 'target': 'watermark state', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'watermark state', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'stream-event-001', 'kind': 'advance watermark', 'target': 'watermark state', 'priority': 2, 'metadata': {'source': 'Stream Processor', 'track': 'distributed-systems'}}
        original = dict(request)
        advance_watermark_stream_event(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
