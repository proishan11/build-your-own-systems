import unittest

from lab_005 import run_mini_container_runtime_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_mini_container_runtime_happy_path_scenario(self):
        self.assertEqual(run_mini_container_runtime_scenario([{'type': 'apply', 'resource': 'namespace plan', 'value': 'ready'}, {'type': 'metric', 'name': 'containers_started', 'value': 3}, {'type': 'fail', 'reason': 'missing isolation'}, {'type': 'recover', 'reason': 'missing isolation'}]), {'state': {'namespace plan': 'ready'}, 'metrics': {'containers_started': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_mini_container_runtime_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'containers_started': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_mini_container_runtime_scenario([]),
            {'state': {}, 'metrics': {'containers_started': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
