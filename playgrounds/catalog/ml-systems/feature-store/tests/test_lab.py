import unittest

from lab import materialize_feature_feature_row


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_feature_row_request(self):
        self.assertEqual(materialize_feature_feature_row({'id': 'feature-row-001', 'kind': 'materialize feature', 'target': 'feature registry', 'priority': 2, 'metadata': {'source': 'Feature Store', 'track': 'ml-systems'}}), {'id': 'feature-row-001', 'action': 'materialize feature', 'target': 'feature registry', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_feature_row_request(self):
        self.assertEqual(materialize_feature_feature_row({'id': 'bad', 'kind': '', 'target': 'feature registry', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'feature registry', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'feature-row-001', 'kind': 'materialize feature', 'target': 'feature registry', 'priority': 2, 'metadata': {'source': 'Feature Store', 'track': 'ml-systems'}}
        original = dict(request)
        materialize_feature_feature_row(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
