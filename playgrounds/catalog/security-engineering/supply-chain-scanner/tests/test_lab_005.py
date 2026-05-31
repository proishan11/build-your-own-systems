import unittest

from lab_005 import run_supply_chain_scanner_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_supply_chain_scanner_happy_path_scenario(self):
        self.assertEqual(run_supply_chain_scanner_scenario([{'type': 'apply', 'resource': 'sbom index', 'value': 'ready'}, {'type': 'metric', 'name': 'findings_reported', 'value': 3}, {'type': 'fail', 'reason': 'unsigned dependency'}, {'type': 'recover', 'reason': 'unsigned dependency'}]), {'state': {'sbom index': 'ready'}, 'metrics': {'findings_reported': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_supply_chain_scanner_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'findings_reported': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_supply_chain_scanner_scenario([]),
            {'state': {}, 'metrics': {'findings_reported': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
