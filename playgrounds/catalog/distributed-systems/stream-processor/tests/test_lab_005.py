import unittest

from lab_005 import run_stream_processor_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_stream_processor_happy_path_scenario(self):
        self.assertEqual(run_stream_processor_scenario([{'type': 'apply', 'resource': 'watermark state', 'value': 'ready'}, {'type': 'metric', 'name': 'windows_closed', 'value': 3}, {'type': 'fail', 'reason': 'late event'}, {'type': 'recover', 'reason': 'late event'}]), {'state': {'watermark state': 'ready'}, 'metrics': {'windows_closed': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_stream_processor_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'windows_closed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_stream_processor_scenario([]),
            {'state': {}, 'metrics': {'windows_closed': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
