import unittest

from lab_003 import plan_kubernetes_controller_from_scratch_reconcile_objects


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_reconcile_object_operations(self):
        self.assertEqual(plan_kubernetes_controller_from_scratch_reconcile_objects({'reconcile-state-primary': 'ready', 'reconcile-state-canary': 'ready'}, {'reconcile-state-primary': 'stale', 'reconcile-state-old': 'ready'}), [{'op': 'update', 'name': 'reconcile-state-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'reconcile-state-old', 'from': 'ready'}, {'op': 'create', 'name': 'reconcile-state-canary', 'to': 'ready'}])

    def test_noops_when_reconcile_state_already_matches(self):
        current = {'reconcile-state-primary': 'ready'}
        self.assertEqual(plan_kubernetes_controller_from_scratch_reconcile_objects(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_kubernetes_controller_from_scratch_reconcile_objects({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
