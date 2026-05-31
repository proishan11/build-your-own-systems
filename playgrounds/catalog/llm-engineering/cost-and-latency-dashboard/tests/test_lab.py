import unittest

from lab import aggregate_sample_usage_sample


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_usage_sample_request(self):
        self.assertEqual(aggregate_sample_usage_sample({'id': 'usage-sample-001', 'kind': 'aggregate sample', 'target': 'metric bucket', 'priority': 2, 'metadata': {'source': 'Cost and Latency Dashboard', 'track': 'llm-engineering'}}), {'id': 'usage-sample-001', 'action': 'aggregate sample', 'target': 'metric bucket', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_usage_sample_request(self):
        self.assertEqual(aggregate_sample_usage_sample({'id': 'bad', 'kind': '', 'target': 'metric bucket', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'metric bucket', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'usage-sample-001', 'kind': 'aggregate sample', 'target': 'metric bucket', 'priority': 2, 'metadata': {'source': 'Cost and Latency Dashboard', 'track': 'llm-engineering'}}
        original = dict(request)
        aggregate_sample_usage_sample(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
