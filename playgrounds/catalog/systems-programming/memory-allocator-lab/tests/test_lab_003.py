import unittest

from lab_003 import plan_memory_allocator_lab_split_allocations


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_split_allocation_operations(self):
        self.assertEqual(plan_memory_allocator_lab_split_allocations({'free-block-primary': 'ready', 'free-block-canary': 'ready'}, {'free-block-primary': 'stale', 'free-block-old': 'ready'}), [{'op': 'update', 'name': 'free-block-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'free-block-old', 'from': 'ready'}, {'op': 'create', 'name': 'free-block-canary', 'to': 'ready'}])

    def test_noops_when_free_block_already_matches(self):
        current = {'free-block-primary': 'ready'}
        self.assertEqual(plan_memory_allocator_lab_split_allocations(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_memory_allocator_lab_split_allocations({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
