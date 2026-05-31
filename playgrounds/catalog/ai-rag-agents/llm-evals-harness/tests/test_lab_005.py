import unittest

from lab_005 import run_llm_evals_harness_scenario


class IntegrationScenarioTest(unittest.TestCase):
    def test_runs_llm_evals_harness_happy_path_scenario(self):
        self.assertEqual(run_llm_evals_harness_scenario([{'type': 'apply', 'resource': 'score rubric', 'value': 'ready'}, {'type': 'metric', 'name': 'cases_scored', 'value': 3}, {'type': 'fail', 'reason': 'flaky evaluator'}, {'type': 'recover', 'reason': 'flaky evaluator'}]), {'state': {'score rubric': 'ready'}, 'metrics': {'cases_scored': 3, 'failures': 1, 'recoveries': 1}, 'invariant_ok': True, 'violations': []})

    def test_reports_missing_resource_violation(self):
        self.assertEqual(run_llm_evals_harness_scenario([{'type': 'apply', 'resource': '', 'value': 'bad'}]), {'state': {}, 'metrics': {'cases_scored': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': False, 'violations': ['missing resource']})

    def test_empty_scenario_is_valid_and_zeroed(self):
        self.assertEqual(
            run_llm_evals_harness_scenario([]),
            {'state': {}, 'metrics': {'cases_scored': 0, 'failures': 0, 'recoveries': 0}, 'invariant_ok': True, 'violations': []},
        )


if __name__ == "__main__":
    unittest.main()
