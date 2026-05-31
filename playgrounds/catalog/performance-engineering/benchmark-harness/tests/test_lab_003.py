import unittest

from lab_003 import plan_benchmark_harness_compare_runss


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_compare_runs_operations(self):
        self.assertEqual(plan_benchmark_harness_compare_runss({'run-config-primary': 'ready', 'run-config-canary': 'ready'}, {'run-config-primary': 'stale', 'run-config-old': 'ready'}), [{'op': 'update', 'name': 'run-config-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'run-config-old', 'from': 'ready'}, {'op': 'create', 'name': 'run-config-canary', 'to': 'ready'}])

    def test_noops_when_run_config_already_matches(self):
        current = {'run-config-primary': 'ready'}
        self.assertEqual(plan_benchmark_harness_compare_runss(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_benchmark_harness_compare_runss({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
