import unittest

from lab_005 import run_xv6_style_kernel_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_xv6_style_kernel_lab_happy_path_scenario(self):
        self.assertEqual(run_xv6_style_kernel_lab_scenario([{'type': 'apply', 'resource': 'process table', 'value': 'ready'}, {'type': 'metric', 'name': 'syscalls_served', 'value': 3}, {'type': 'fail', 'reason': 'invalid trap frame'}, {'type': 'recover', 'reason': 'invalid trap frame'}]), {'state': {'process table': 'ready'}, 'metrics': {'syscalls_served': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_xv6_style_kernel_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'syscalls_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_xv6_style_kernel_lab_scenario([]),
            {'state': {}, 'metrics': {'syscalls_served': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
