import unittest

from lab_003 import plan_actions, summarize_plan


class OperationPlannerTest(unittest.TestCase):
    def test_plans_create_update_and_delete_in_key_order(self):
        desired = {"api": 2, "worker": 1}
        observed = {"api": 1, "old": 1}
        self.assertEqual(
            plan_actions(desired, observed),
            [
                {"action": "update", "key": "api", "old": 1, "value": 2},
                {"action": "delete", "key": "old", "old": 1},
                {"action": "create", "key": "worker", "value": 1},
            ],
        )

    def test_equal_state_has_no_actions(self):
        self.assertEqual(plan_actions({"api": 1}, {"api": 1}), [])

    def test_summarizes_plan(self):
        actions = [
            {"action": "create", "key": "a"},
            {"action": "update", "key": "b"},
            {"action": "update", "key": "c"},
        ]
        self.assertEqual(summarize_plan(actions), {"create": 1, "update": 2, "delete": 0, "total": 3})


if __name__ == "__main__":
    unittest.main()
