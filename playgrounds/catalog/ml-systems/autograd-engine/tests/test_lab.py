import unittest

from lab import backpropagate_gradient_tensor_operation


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_tensor_operation_request(self):
        self.assertEqual(backpropagate_gradient_tensor_operation({'id': 'tensor-operation-001', 'kind': 'backpropagate gradient', 'target': 'computation graph', 'priority': 2, 'metadata': {'source': 'Autograd Engine', 'track': 'ml-systems'}}), {'id': 'tensor-operation-001', 'action': 'backpropagate gradient', 'target': 'computation graph', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_tensor_operation_request(self):
        self.assertEqual(backpropagate_gradient_tensor_operation({'id': 'bad', 'kind': '', 'target': 'computation graph', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'computation graph', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'tensor-operation-001', 'kind': 'backpropagate gradient', 'target': 'computation graph', 'priority': 2, 'metadata': {'source': 'Autograd Engine', 'track': 'ml-systems'}}
        original = dict(request)
        backpropagate_gradient_tensor_operation(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
