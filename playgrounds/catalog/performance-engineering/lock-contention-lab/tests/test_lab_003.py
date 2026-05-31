import unittest

from lab_003 import plan_lock_contention_lab_attribute_waits


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_attribute_wait_operations(self):
        self.assertEqual(plan_lock_contention_lab_attribute_waits({'wait-graph-primary': 'ready', 'wait-graph-canary': 'ready'}, {'wait-graph-primary': 'stale', 'wait-graph-old': 'ready'}), [{'op': 'update', 'name': 'wait-graph-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'wait-graph-old', 'from': 'ready'}, {'op': 'create', 'name': 'wait-graph-canary', 'to': 'ready'}])

    def test_noops_when_wait_graph_already_matches(self):
        current = {'wait-graph-primary': 'ready'}
        self.assertEqual(plan_lock_contention_lab_attribute_waits(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_lock_contention_lab_attribute_waits({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
