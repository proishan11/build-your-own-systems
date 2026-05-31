import unittest

from lab import aggregate_sample_stack_sample


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_stack_sample_request(self):
        self.assertEqual(aggregate_sample_stack_sample({'id': 'stack-sample-001', 'kind': 'aggregate sample', 'target': 'profile tree', 'priority': 2, 'metadata': {'source': 'Profiler From Scratch', 'track': 'performance-engineering'}}), {'id': 'stack-sample-001', 'action': 'aggregate sample', 'target': 'profile tree', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_stack_sample_request(self):
        self.assertEqual(aggregate_sample_stack_sample({'id': 'bad', 'kind': '', 'target': 'profile tree', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'profile tree', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'stack-sample-001', 'kind': 'aggregate sample', 'target': 'profile tree', 'priority': 2, 'metadata': {'source': 'Profiler From Scratch', 'track': 'performance-engineering'}}
        original = dict(request)
        aggregate_sample_stack_sample(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
