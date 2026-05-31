import unittest

from lab_003 import plan_feature_flag_and_rollout_system_evaluate_flags


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_evaluate_flag_operations(self):
        self.assertEqual(plan_feature_flag_and_rollout_system_evaluate_flags({'rollout-rule-primary': 'ready', 'rollout-rule-canary': 'ready'}, {'rollout-rule-primary': 'stale', 'rollout-rule-old': 'ready'}), [{'op': 'update', 'name': 'rollout-rule-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'rollout-rule-old', 'from': 'ready'}, {'op': 'create', 'name': 'rollout-rule-canary', 'to': 'ready'}])

    def test_noops_when_rollout_rule_already_matches(self):
        current = {'rollout-rule-primary': 'ready'}
        self.assertEqual(plan_feature_flag_and_rollout_system_evaluate_flags(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_feature_flag_and_rollout_system_evaluate_flags({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
