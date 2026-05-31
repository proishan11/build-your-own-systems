import unittest

from lab_005 import run_event_loop_and_async_runtime_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_event_loop_and_async_runtime_happy_path_scenario(self):
        self.assertEqual(run_event_loop_and_async_runtime_scenario([{'type': 'apply', 'resource': 'ready queue', 'value': 'ready'}, {'type': 'metric', 'name': 'ready_tasks', 'value': 3}, {'type': 'fail', 'reason': 'stalled timer'}, {'type': 'recover', 'reason': 'stalled timer'}]), {'state': {'ready queue': 'ready'}, 'metrics': {'ready_tasks': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_event_loop_and_async_runtime_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'ready_tasks': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_event_loop_and_async_runtime_scenario([]),
            {'state': {}, 'metrics': {'ready_tasks': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
