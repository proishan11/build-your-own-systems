import unittest

from lab_003 import plan_git_merge_and_rebase_lab_resolve_merges


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_resolve_merge_operations(self):
        self.assertEqual(plan_git_merge_and_rebase_lab_resolve_merges({'merge-graph-primary': 'ready', 'merge-graph-canary': 'ready'}, {'merge-graph-primary': 'stale', 'merge-graph-old': 'ready'}), [{'op': 'update', 'name': 'merge-graph-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'merge-graph-old', 'from': 'ready'}, {'op': 'create', 'name': 'merge-graph-canary', 'to': 'ready'}])

    def test_noops_when_merge_graph_already_matches(self):
        current = {'merge-graph-primary': 'ready'}
        self.assertEqual(plan_git_merge_and_rebase_lab_resolve_merges(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_git_merge_and_rebase_lab_resolve_merges({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
