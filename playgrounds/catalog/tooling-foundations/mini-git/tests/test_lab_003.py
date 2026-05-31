import unittest

from lab_003 import plan_mini_git_write_objects


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_write_object_operations(self):
        self.assertEqual(plan_mini_git_write_objects({'object-database-primary': 'ready', 'object-database-canary': 'ready'}, {'object-database-primary': 'stale', 'object-database-old': 'ready'}), [{'op': 'update', 'name': 'object-database-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'object-database-old', 'from': 'ready'}, {'op': 'create', 'name': 'object-database-canary', 'to': 'ready'}])

    def test_noops_when_object_database_already_matches(self):
        current = {'object-database-primary': 'ready'}
        self.assertEqual(plan_mini_git_write_objects(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_mini_git_write_objects({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
