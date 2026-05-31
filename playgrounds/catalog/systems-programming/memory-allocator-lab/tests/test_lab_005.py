import unittest

from lab_005 import run_memory_allocator_lab_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_memory_allocator_lab_happy_path_scenario(self):
        self.assertEqual(run_memory_allocator_lab_scenario([{'type': 'apply', 'resource': 'free block', 'value': 'ready'}, {'type': 'metric', 'name': 'fragmentation_ratio', 'value': 3}, {'type': 'fail', 'reason': 'double free'}, {'type': 'recover', 'reason': 'double free'}]), {'state': {'free block': 'ready'}, 'metrics': {'fragmentation_ratio': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_memory_allocator_lab_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'fragmentation_ratio': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_memory_allocator_lab_scenario([]),
            {'state': {}, 'metrics': {'fragmentation_ratio': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
