import unittest

from lab_005 import run_reliable_transport_from_scratch_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_reliable_transport_from_scratch_happy_path_scenario(self):
        self.assertEqual(run_reliable_transport_from_scratch_scenario([{'type': 'apply', 'resource': 'receive window', 'value': 'ready'}, {'type': 'metric', 'name': 'bytes_delivered', 'value': 3}, {'type': 'fail', 'reason': 'out-of-order segment'}, {'type': 'recover', 'reason': 'out-of-order segment'}]), {'state': {'receive window': 'ready'}, 'metrics': {'bytes_delivered': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_reliable_transport_from_scratch_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'bytes_delivered': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_reliable_transport_from_scratch_scenario([]),
            {'state': {}, 'metrics': {'bytes_delivered': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
