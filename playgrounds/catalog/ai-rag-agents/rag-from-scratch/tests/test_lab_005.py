import unittest

from lab_005 import run_rag_from_scratch_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_rag_from_scratch_happy_path_scenario(self):
        self.assertEqual(run_rag_from_scratch_scenario([{'type': 'apply', 'resource': 'vector index', 'value': 'ready'}, {'type': 'metric', 'name': 'chunks_retrieved', 'value': 3}, {'type': 'fail', 'reason': 'lost citation'}, {'type': 'recover', 'reason': 'lost citation'}]), {'state': {'vector index': 'ready'}, 'metrics': {'chunks_retrieved': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_rag_from_scratch_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'chunks_retrieved': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_rag_from_scratch_scenario([]),
            {'state': {}, 'metrics': {'chunks_retrieved': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
