import unittest

from lab_003 import plan_observability_stack_ingest_telemetrys


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_ingest_telemetry_operations(self):
        self.assertEqual(plan_observability_stack_ingest_telemetrys({'signal-pipeline-primary': 'ready', 'signal-pipeline-canary': 'ready'}, {'signal-pipeline-primary': 'stale', 'signal-pipeline-old': 'ready'}), [{'op': 'update', 'name': 'signal-pipeline-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'signal-pipeline-old', 'from': 'ready'}, {'op': 'create', 'name': 'signal-pipeline-canary', 'to': 'ready'}])

    def test_noops_when_signal_pipeline_already_matches(self):
        current = {'signal-pipeline-primary': 'ready'}
        self.assertEqual(plan_observability_stack_ingest_telemetrys(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_observability_stack_ingest_telemetrys({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
