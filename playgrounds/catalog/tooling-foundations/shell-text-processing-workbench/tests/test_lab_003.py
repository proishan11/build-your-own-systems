import unittest

from lab_003 import plan_shell_text_processing_workbench_filter_records


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_filter_record_operations(self):
        self.assertEqual(plan_shell_text_processing_workbench_filter_records({'pipeline-stage-primary': 'ready', 'pipeline-stage-canary': 'ready'}, {'pipeline-stage-primary': 'stale', 'pipeline-stage-old': 'ready'}), [{'op': 'update', 'name': 'pipeline-stage-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'pipeline-stage-old', 'from': 'ready'}, {'op': 'create', 'name': 'pipeline-stage-canary', 'to': 'ready'}])

    def test_noops_when_pipeline_stage_already_matches(self):
        current = {'pipeline-stage-primary': 'ready'}
        self.assertEqual(plan_shell_text_processing_workbench_filter_records(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_shell_text_processing_workbench_filter_records({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
