import unittest

from lab import record_span_llm_span


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_llm_span_request(self):
        self.assertEqual(record_span_llm_span({'id': 'llm-span-001', 'kind': 'record span', 'target': 'trace index', 'priority': 2, 'metadata': {'source': 'LLM Trace Store', 'track': 'llm-engineering'}}), {'id': 'llm-span-001', 'action': 'record span', 'target': 'trace index', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_llm_span_request(self):
        self.assertEqual(record_span_llm_span({'id': 'bad', 'kind': '', 'target': 'trace index', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'trace index', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'llm-span-001', 'kind': 'record span', 'target': 'trace index', 'priority': 2, 'metadata': {'source': 'LLM Trace Store', 'track': 'llm-engineering'}}
        original = dict(request)
        record_span_llm_span(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
