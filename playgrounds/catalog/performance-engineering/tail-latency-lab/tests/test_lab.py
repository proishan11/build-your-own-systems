import unittest

from lab import compute_percentile_latency_sample


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_latency_sample_request(self):
        self.assertEqual(compute_percentile_latency_sample({'id': 'latency-sample-001', 'kind': 'compute percentile', 'target': 'histogram bucket', 'priority': 2, 'metadata': {'source': 'Tail Latency Lab', 'track': 'performance-engineering'}}), {'id': 'latency-sample-001', 'action': 'compute percentile', 'target': 'histogram bucket', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_latency_sample_request(self):
        self.assertEqual(compute_percentile_latency_sample({'id': 'bad', 'kind': '', 'target': 'histogram bucket', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'histogram bucket', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'latency-sample-001', 'kind': 'compute percentile', 'target': 'histogram bucket', 'priority': 2, 'metadata': {'source': 'Tail Latency Lab', 'track': 'performance-engineering'}}
        original = dict(request)
        compute_percentile_latency_sample(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
