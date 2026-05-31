import unittest

from lab import batch_request_inference_request


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_inference_request_request(self):
        self.assertEqual(batch_request_inference_request({'id': 'inference-request-001', 'kind': 'batch request', 'target': 'batch queue', 'priority': 2, 'metadata': {'source': 'Inference Server', 'track': 'ml-systems'}}), {'id': 'inference-request-001', 'action': 'batch request', 'target': 'batch queue', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_inference_request_request(self):
        self.assertEqual(batch_request_inference_request({'id': 'bad', 'kind': '', 'target': 'batch queue', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'batch queue', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'inference-request-001', 'kind': 'batch request', 'target': 'batch queue', 'priority': 2, 'metadata': {'source': 'Inference Server', 'track': 'ml-systems'}}
        original = dict(request)
        batch_request_inference_request(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
