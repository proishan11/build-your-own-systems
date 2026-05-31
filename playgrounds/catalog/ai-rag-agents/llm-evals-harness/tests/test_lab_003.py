import unittest

from lab_003 import plan_llm_evals_harness_score_answers


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_score_answer_operations(self):
        self.assertEqual(plan_llm_evals_harness_score_answers({'score-rubric-primary': 'ready', 'score-rubric-canary': 'ready'}, {'score-rubric-primary': 'stale', 'score-rubric-old': 'ready'}), [{'op': 'update', 'name': 'score-rubric-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'score-rubric-old', 'from': 'ready'}, {'op': 'create', 'name': 'score-rubric-canary', 'to': 'ready'}])

    def test_noops_when_score_rubric_already_matches(self):
        current = {'score-rubric-primary': 'ready'}
        self.assertEqual(plan_llm_evals_harness_score_answers(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_llm_evals_harness_score_answers({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
