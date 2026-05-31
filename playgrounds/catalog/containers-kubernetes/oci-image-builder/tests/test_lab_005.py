import unittest

from lab_005 import run_oci_image_builder_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_oci_image_builder_happy_path_scenario(self):
        self.assertEqual(run_oci_image_builder_scenario([{'type': 'apply', 'resource': 'image manifest', 'value': 'ready'}, {'type': 'metric', 'name': 'layers_reused', 'value': 3}, {'type': 'fail', 'reason': 'non-reproducible layer'}, {'type': 'recover', 'reason': 'non-reproducible layer'}]), {'state': {'image manifest': 'ready'}, 'metrics': {'layers_reused': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_oci_image_builder_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'layers_reused': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_oci_image_builder_scenario([]),
            {'state': {}, 'metrics': {'layers_reused': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
