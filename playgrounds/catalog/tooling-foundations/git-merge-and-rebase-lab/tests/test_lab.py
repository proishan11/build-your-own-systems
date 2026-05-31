import unittest

from lab import resolve_merge_commit_change


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_commit_change_request(self):
        self.assertEqual(resolve_merge_commit_change({'id': 'commit-change-001', 'kind': 'resolve merge', 'target': 'merge graph', 'priority': 2, 'metadata': {'source': 'Git Merge and Rebase Lab', 'track': 'tooling-foundations'}}), {'id': 'commit-change-001', 'action': 'resolve merge', 'target': 'merge graph', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_commit_change_request(self):
        self.assertEqual(resolve_merge_commit_change({'id': 'bad', 'kind': '', 'target': 'merge graph', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'merge graph', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'commit-change-001', 'kind': 'resolve merge', 'target': 'merge graph', 'priority': 2, 'metadata': {'source': 'Git Merge and Rebase Lab', 'track': 'tooling-foundations'}}
        original = dict(request)
        resolve_merge_commit_change(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
