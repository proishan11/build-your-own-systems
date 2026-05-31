import unittest

from lab import promote_model_model_artifact


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_model_artifact_request(self):
        self.assertEqual(promote_model_model_artifact({'id': 'model-artifact-001', 'kind': 'promote model', 'target': 'registry version', 'priority': 2, 'metadata': {'source': 'Model Registry', 'track': 'ml-systems'}}), {'id': 'model-artifact-001', 'action': 'promote model', 'target': 'registry version', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_model_artifact_request(self):
        self.assertEqual(promote_model_model_artifact({'id': 'bad', 'kind': '', 'target': 'registry version', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'registry version', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'model-artifact-001', 'kind': 'promote model', 'target': 'registry version', 'priority': 2, 'metadata': {'source': 'Model Registry', 'track': 'ml-systems'}}
        original = dict(request)
        promote_model_model_artifact(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
