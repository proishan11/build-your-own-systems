import unittest

from lab import run_forward_pass_training_batch


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_training_batch_request(self):
        self.assertEqual(run_forward_pass_training_batch({'id': 'training-batch-001', 'kind': 'run forward pass', 'target': 'module graph', 'priority': 2, 'metadata': {'source': 'Mini Deep Learning Framework', 'track': 'ml-systems'}}), {'id': 'training-batch-001', 'action': 'run forward pass', 'target': 'module graph', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_training_batch_request(self):
        self.assertEqual(run_forward_pass_training_batch({'id': 'bad', 'kind': '', 'target': 'module graph', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'module graph', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'training-batch-001', 'kind': 'run forward pass', 'target': 'module graph', 'priority': 2, 'metadata': {'source': 'Mini Deep Learning Framework', 'track': 'ml-systems'}}
        original = dict(request)
        run_forward_pass_training_batch(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
