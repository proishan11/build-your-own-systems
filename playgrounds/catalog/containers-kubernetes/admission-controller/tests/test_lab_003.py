import unittest

from lab_003 import plan_admission_controller_admit_objects


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_admit_object_operations(self):
        self.assertEqual(plan_admission_controller_admit_objects({'policy-set-primary': 'ready', 'policy-set-canary': 'ready'}, {'policy-set-primary': 'stale', 'policy-set-old': 'ready'}), [{'op': 'update', 'name': 'policy-set-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'policy-set-old', 'from': 'ready'}, {'op': 'create', 'name': 'policy-set-canary', 'to': 'ready'}])

    def test_noops_when_policy_set_already_matches(self):
        current = {'policy-set-primary': 'ready'}
        self.assertEqual(plan_admission_controller_admit_objects(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_admission_controller_admit_objects({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
