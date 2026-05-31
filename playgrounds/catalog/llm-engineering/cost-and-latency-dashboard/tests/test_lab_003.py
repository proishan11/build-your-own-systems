import unittest

from lab_003 import plan_cost_and_latency_dashboard_aggregate_samples


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_aggregate_sample_operations(self):
        self.assertEqual(plan_cost_and_latency_dashboard_aggregate_samples({'metric-bucket-primary': 'ready', 'metric-bucket-canary': 'ready'}, {'metric-bucket-primary': 'stale', 'metric-bucket-old': 'ready'}), [{'op': 'update', 'name': 'metric-bucket-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'metric-bucket-old', 'from': 'ready'}, {'op': 'create', 'name': 'metric-bucket-canary', 'to': 'ready'}])

    def test_noops_when_metric_bucket_already_matches(self):
        current = {'metric-bucket-primary': 'ready'}
        self.assertEqual(plan_cost_and_latency_dashboard_aggregate_samples(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_cost_and_latency_dashboard_aggregate_samples({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
