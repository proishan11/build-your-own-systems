import unittest

from lab_003 import plan_profiler_from_scratch_aggregate_samples


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_aggregate_sample_operations(self):
        self.assertEqual(plan_profiler_from_scratch_aggregate_samples({'profile-tree-primary': 'ready', 'profile-tree-canary': 'ready'}, {'profile-tree-primary': 'stale', 'profile-tree-old': 'ready'}), [{'op': 'update', 'name': 'profile-tree-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'profile-tree-old', 'from': 'ready'}, {'op': 'create', 'name': 'profile-tree-canary', 'to': 'ready'}])

    def test_noops_when_profile_tree_already_matches(self):
        current = {'profile-tree-primary': 'ready'}
        self.assertEqual(plan_profiler_from_scratch_aggregate_samples(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_profiler_from_scratch_aggregate_samples({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
