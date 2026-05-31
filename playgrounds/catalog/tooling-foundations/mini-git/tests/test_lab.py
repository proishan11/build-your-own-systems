import unittest

from lab import write_object_git_object


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_git_object_request(self):
        self.assertEqual(write_object_git_object({'id': 'git-object-001', 'kind': 'write object', 'target': 'object database', 'priority': 2, 'metadata': {'source': 'Mini Git', 'track': 'tooling-foundations'}}), {'id': 'git-object-001', 'action': 'write object', 'target': 'object database', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_git_object_request(self):
        self.assertEqual(write_object_git_object({'id': 'bad', 'kind': '', 'target': 'object database', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'object database', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'git-object-001', 'kind': 'write object', 'target': 'object database', 'priority': 2, 'metadata': {'source': 'Mini Git', 'track': 'tooling-foundations'}}
        original = dict(request)
        write_object_git_object(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
