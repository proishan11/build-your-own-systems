import unittest

from lab import ingest_telemetry_trace_span


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_trace_span_request(self):
        self.assertEqual(ingest_telemetry_trace_span({'id': 'trace-span-001', 'kind': 'ingest telemetry', 'target': 'signal pipeline', 'priority': 2, 'metadata': {'source': 'Observability Stack', 'track': 'sre-system-design'}}), {'id': 'trace-span-001', 'action': 'ingest telemetry', 'target': 'signal pipeline', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_trace_span_request(self):
        self.assertEqual(ingest_telemetry_trace_span({'id': 'bad', 'kind': '', 'target': 'signal pipeline', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'signal pipeline', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'trace-span-001', 'kind': 'ingest telemetry', 'target': 'signal pipeline', 'priority': 2, 'metadata': {'source': 'Observability Stack', 'track': 'sre-system-design'}}
        original = dict(request)
        ingest_telemetry_trace_span(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
