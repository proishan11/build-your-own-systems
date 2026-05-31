import unittest

from lab import score_answer_eval_case


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_eval_case_request(self):
        self.assertEqual(score_answer_eval_case({'id': 'eval-case-001', 'kind': 'score answer', 'target': 'score rubric', 'priority': 2, 'metadata': {'source': 'LLM Evals Harness', 'track': 'ai-rag-agents'}}), {'id': 'eval-case-001', 'action': 'score answer', 'target': 'score rubric', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_eval_case_request(self):
        self.assertEqual(score_answer_eval_case({'id': 'bad', 'kind': '', 'target': 'score rubric', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'score rubric', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'eval-case-001', 'kind': 'score answer', 'target': 'score rubric', 'priority': 2, 'metadata': {'source': 'LLM Evals Harness', 'track': 'ai-rag-agents'}}
        original = dict(request)
        score_answer_eval_case(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
