import unittest

from lab_005 import run_vim_plugin_from_scratch_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_vim_plugin_from_scratch_happy_path_scenario(self):
        self.assertEqual(run_vim_plugin_from_scratch_scenario([{'type': 'apply', 'resource': 'editor state', 'value': 'ready'}, {'type': 'metric', 'name': 'events_handled', 'value': 3}, {'type': 'fail', 'reason': 'recursive mapping'}, {'type': 'recover', 'reason': 'recursive mapping'}]), {'state': {'editor state': 'ready'}, 'metrics': {'events_handled': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_vim_plugin_from_scratch_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'events_handled': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_vim_plugin_from_scratch_scenario([]),
            {'state': {}, 'metrics': {'events_handled': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
