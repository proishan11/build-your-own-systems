import unittest

from lab import compare_runs_benchmark_sample


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_benchmark_sample_request(self):
        self.assertEqual(compare_runs_benchmark_sample({'id': 'benchmark-sample-001', 'kind': 'compare runs', 'target': 'run config', 'priority': 2, 'metadata': {'source': 'Benchmark Harness', 'track': 'performance-engineering'}}), {'id': 'benchmark-sample-001', 'action': 'compare runs', 'target': 'run config', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_benchmark_sample_request(self):
        self.assertEqual(compare_runs_benchmark_sample({'id': 'bad', 'kind': '', 'target': 'run config', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'run config', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'benchmark-sample-001', 'kind': 'compare runs', 'target': 'run config', 'priority': 2, 'metadata': {'source': 'Benchmark Harness', 'track': 'performance-engineering'}}
        original = dict(request)
        compare_runs_benchmark_sample(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
