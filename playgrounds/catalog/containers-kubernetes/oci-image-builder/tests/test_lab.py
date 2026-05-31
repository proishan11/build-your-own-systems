import unittest

from lab import assemble_image_image_layer


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_image_layer_request(self):
        self.assertEqual(assemble_image_image_layer({'id': 'image-layer-001', 'kind': 'assemble image', 'target': 'image manifest', 'priority': 2, 'metadata': {'source': 'OCI Image Builder', 'track': 'containers-kubernetes'}}), {'id': 'image-layer-001', 'action': 'assemble image', 'target': 'image manifest', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_image_layer_request(self):
        self.assertEqual(assemble_image_image_layer({'id': 'bad', 'kind': '', 'target': 'image manifest', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'image manifest', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'image-layer-001', 'kind': 'assemble image', 'target': 'image manifest', 'priority': 2, 'metadata': {'source': 'OCI Image Builder', 'track': 'containers-kubernetes'}}
        original = dict(request)
        assemble_image_image_layer(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
