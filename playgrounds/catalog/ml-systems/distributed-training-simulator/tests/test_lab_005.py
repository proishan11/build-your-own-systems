import unittest

from lab_005 import run_distributed_training_simulator_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_distributed_training_simulator_happy_path_scenario(self):
        self.assertEqual(run_distributed_training_simulator_scenario([{'type': 'apply', 'resource': 'worker ring', 'value': 'ready'}, {'type': 'metric', 'name': 'steps_completed', 'value': 3}, {'type': 'fail', 'reason': 'straggler worker'}, {'type': 'recover', 'reason': 'straggler worker'}]), {'state': {'worker ring': 'ready'}, 'metrics': {'steps_completed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_distributed_training_simulator_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'steps_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_distributed_training_simulator_scenario([]),
            {'state': {}, 'metrics': {'steps_completed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
