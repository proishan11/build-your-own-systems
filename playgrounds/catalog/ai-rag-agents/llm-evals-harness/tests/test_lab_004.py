import unittest

from lab_004 import recover_llm_evals_harness_flaky_evaluator


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_score_answer_failure(self):
        self.assertEqual(recover_llm_evals_harness_flaky_evaluator({'operation': 'score answer', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'score rubric'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'score rubric'})

    def test_fails_permanent_flaky_evaluator(self):
        self.assertEqual(recover_llm_evals_harness_flaky_evaluator({'operation': 'score answer', 'error': 'flaky evaluator', 'attempt': 1, 'max_attempts': 3, 'resource': 'score rubric'}), {'decision': 'fail', 'reason': 'flaky evaluator', 'resource': 'score rubric'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_llm_evals_harness_flaky_evaluator({'operation': 'score answer', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'score rubric'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'score rubric'})


if __name__ == "__main__":
    unittest.main()
