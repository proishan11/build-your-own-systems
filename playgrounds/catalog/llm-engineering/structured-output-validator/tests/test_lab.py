import unittest

from lab import validate_output_model_output


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_model_output_request(self):
        self.assertEqual(validate_output_model_output({'id': 'model-output-001', 'kind': 'validate output', 'target': 'json schema', 'priority': 2, 'metadata': {'source': 'Structured Output Validator', 'track': 'llm-engineering'}}), {'id': 'model-output-001', 'action': 'validate output', 'target': 'json schema', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_model_output_request(self):
        self.assertEqual(validate_output_model_output({'id': 'bad', 'kind': '', 'target': 'json schema', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'json schema', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'model-output-001', 'kind': 'validate output', 'target': 'json schema', 'priority': 2, 'metadata': {'source': 'Structured Output Validator', 'track': 'llm-engineering'}}
        original = dict(request)
        validate_output_model_output(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
