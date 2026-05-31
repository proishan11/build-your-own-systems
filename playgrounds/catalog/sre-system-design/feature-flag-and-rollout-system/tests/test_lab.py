import unittest

from lab import evaluate_flag_flag_evaluation


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_flag_evaluation_request(self):
        self.assertEqual(evaluate_flag_flag_evaluation({'id': 'flag-evaluation-001', 'kind': 'evaluate flag', 'target': 'rollout rule', 'priority': 2, 'metadata': {'source': 'Feature Flag and Rollout System', 'track': 'sre-system-design'}}), {'id': 'flag-evaluation-001', 'action': 'evaluate flag', 'target': 'rollout rule', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_flag_evaluation_request(self):
        self.assertEqual(evaluate_flag_flag_evaluation({'id': 'bad', 'kind': '', 'target': 'rollout rule', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'rollout rule', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'flag-evaluation-001', 'kind': 'evaluate flag', 'target': 'rollout rule', 'priority': 2, 'metadata': {'source': 'Feature Flag and Rollout System', 'track': 'sre-system-design'}}
        original = dict(request)
        evaluate_flag_flag_evaluation(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
