import unittest

from lab_003 import plan_lsm_tree_kv_store_compact_runs


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_compact_run_operations(self):
        self.assertEqual(plan_lsm_tree_kv_store_compact_runs({'sstable-level-primary': 'ready', 'sstable-level-canary': 'ready'}, {'sstable-level-primary': 'stale', 'sstable-level-old': 'ready'}), [{'op': 'update', 'name': 'sstable-level-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'sstable-level-old', 'from': 'ready'}, {'op': 'create', 'name': 'sstable-level-canary', 'to': 'ready'}])

    def test_noops_when_sstable_level_already_matches(self):
        current = {'sstable-level-primary': 'ready'}
        self.assertEqual(plan_lsm_tree_kv_store_compact_runs(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_lsm_tree_kv_store_compact_runs({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
