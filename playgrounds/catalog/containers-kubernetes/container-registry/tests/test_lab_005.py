import unittest

from lab_005 import run_container_registry_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_container_registry_happy_path_scenario(self):
        self.assertEqual(run_container_registry_scenario([{'type': 'apply', 'resource': 'blob store', 'value': 'ready'}, {'type': 'metric', 'name': 'bytes_served', 'value': 3}, {'type': 'fail', 'reason': 'digest mismatch'}, {'type': 'recover', 'reason': 'digest mismatch'}]), {'state': {'blob store': 'ready'}, 'metrics': {'bytes_served': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_container_registry_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'bytes_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_container_registry_scenario([]),
            {'state': {}, 'metrics': {'bytes_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
