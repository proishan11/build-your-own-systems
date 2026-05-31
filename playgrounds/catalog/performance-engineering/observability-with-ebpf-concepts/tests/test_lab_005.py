import unittest

from lab_005 import run_observability_with_ebpf_concepts_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_observability_with_ebpf_concepts_happy_path_scenario(self):
        self.assertEqual(run_observability_with_ebpf_concepts_scenario([{'type': 'apply', 'resource': 'probe registry', 'value': 'ready'}, {'type': 'metric', 'name': 'events_captured', 'value': 3}, {'type': 'fail', 'reason': 'unsafe probe'}, {'type': 'recover', 'reason': 'unsafe probe'}]), {'state': {'probe registry': 'ready'}, 'metrics': {'events_captured': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_observability_with_ebpf_concepts_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'events_captured': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_observability_with_ebpf_concepts_scenario([]),
            {'state': {}, 'metrics': {'events_captured': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
