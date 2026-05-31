import unittest

from lab_003 import plan_tail_latency_lab_compute_percentiles


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_compute_percentile_operations(self):
        self.assertEqual(plan_tail_latency_lab_compute_percentiles({'histogram-bucket-primary': 'ready', 'histogram-bucket-canary': 'ready'}, {'histogram-bucket-primary': 'stale', 'histogram-bucket-old': 'ready'}), [{'op': 'update', 'name': 'histogram-bucket-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'histogram-bucket-old', 'from': 'ready'}, {'op': 'create', 'name': 'histogram-bucket-canary', 'to': 'ready'}])

    def test_noops_when_histogram_bucket_already_matches(self):
        current = {'histogram-bucket-primary': 'ready'}
        self.assertEqual(plan_tail_latency_lab_compute_percentiles(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_tail_latency_lab_compute_percentiles({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
