import unittest

from lab import allreduce_shard_gradient_shard


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_gradient_shard_request(self):
        self.assertEqual(allreduce_shard_gradient_shard({'id': 'gradient-shard-001', 'kind': 'allreduce shard', 'target': 'worker ring', 'priority': 2, 'metadata': {'source': 'Distributed Training Simulator', 'track': 'ml-systems'}}), {'id': 'gradient-shard-001', 'action': 'allreduce shard', 'target': 'worker ring', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_gradient_shard_request(self):
        self.assertEqual(allreduce_shard_gradient_shard({'id': 'bad', 'kind': '', 'target': 'worker ring', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'worker ring', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'gradient-shard-001', 'kind': 'allreduce shard', 'target': 'worker ring', 'priority': 2, 'metadata': {'source': 'Distributed Training Simulator', 'track': 'ml-systems'}}
        original = dict(request)
        allreduce_shard_gradient_shard(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
