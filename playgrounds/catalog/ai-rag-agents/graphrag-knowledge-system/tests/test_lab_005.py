import unittest

from lab_005 import run_graphrag_knowledge_system_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_graphrag_knowledge_system_happy_path_scenario(self):
        self.assertEqual(run_graphrag_knowledge_system_scenario([{'type': 'apply', 'resource': 'knowledge graph', 'value': 'ready'}, {'type': 'metric', 'name': 'communities_found', 'value': 3}, {'type': 'fail', 'reason': 'duplicate entity'}, {'type': 'recover', 'reason': 'duplicate entity'}]), {'state': {'knowledge graph': 'ready'}, 'metrics': {'communities_found': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_graphrag_knowledge_system_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'communities_found': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_graphrag_knowledge_system_scenario([]),
            {'state': {}, 'metrics': {'communities_found': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
