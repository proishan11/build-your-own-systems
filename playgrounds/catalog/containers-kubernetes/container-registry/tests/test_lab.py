import unittest

from lab import serve_manifest_image_blob


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_image_blob_request(self):
        self.assertEqual(serve_manifest_image_blob({'id': 'image-blob-001', 'kind': 'serve manifest', 'target': 'blob store', 'priority': 2, 'metadata': {'source': 'Container Registry', 'track': 'containers-kubernetes'}}), {'id': 'image-blob-001', 'action': 'serve manifest', 'target': 'blob store', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_image_blob_request(self):
        self.assertEqual(serve_manifest_image_blob({'id': 'bad', 'kind': '', 'target': 'blob store', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'blob store', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'image-blob-001', 'kind': 'serve manifest', 'target': 'blob store', 'priority': 2, 'metadata': {'source': 'Container Registry', 'track': 'containers-kubernetes'}}
        original = dict(request)
        serve_manifest_image_blob(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
