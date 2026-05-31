import unittest

from lab_003 import plan_distributed_training_simulator_allreduce_shards


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_allreduce_shard_operations(self):
        self.assertEqual(plan_distributed_training_simulator_allreduce_shards({'worker-ring-primary': 'ready', 'worker-ring-canary': 'ready'}, {'worker-ring-primary': 'stale', 'worker-ring-old': 'ready'}), [{'op': 'update', 'name': 'worker-ring-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'worker-ring-old', 'from': 'ready'}, {'op': 'create', 'name': 'worker-ring-canary', 'to': 'ready'}])

    def test_noops_when_worker_ring_already_matches(self):
        current = {'worker-ring-primary': 'ready'}
        self.assertEqual(plan_distributed_training_simulator_allreduce_shards(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_distributed_training_simulator_allreduce_shards({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
