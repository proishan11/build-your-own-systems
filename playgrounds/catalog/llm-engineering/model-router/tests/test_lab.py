import unittest

from lab import route_model_llm_request


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_llm_request_request(self):
        self.assertEqual(route_model_llm_request({'id': 'llm-request-001', 'kind': 'route model', 'target': 'model catalog', 'priority': 2, 'metadata': {'source': 'Model Router', 'track': 'llm-engineering'}}), {'id': 'llm-request-001', 'action': 'route model', 'target': 'model catalog', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_llm_request_request(self):
        self.assertEqual(route_model_llm_request({'id': 'bad', 'kind': '', 'target': 'model catalog', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'model catalog', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'llm-request-001', 'kind': 'route model', 'target': 'model catalog', 'priority': 2, 'metadata': {'source': 'Model Router', 'track': 'llm-engineering'}}
        original = dict(request)
        route_model_llm_request(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
