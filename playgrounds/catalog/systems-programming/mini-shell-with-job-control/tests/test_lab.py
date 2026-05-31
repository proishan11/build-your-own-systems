import unittest

from lab import spawn_job_command_pipeline


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_command_pipeline_request(self):
        self.assertEqual(spawn_job_command_pipeline({'id': 'command-pipeline-001', 'kind': 'spawn job', 'target': 'process group', 'priority': 2, 'metadata': {'source': 'Mini Shell With Job Control', 'track': 'systems-programming'}}), {'id': 'command-pipeline-001', 'action': 'spawn job', 'target': 'process group', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_command_pipeline_request(self):
        self.assertEqual(spawn_job_command_pipeline({'id': 'bad', 'kind': '', 'target': 'process group', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'process group', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'command-pipeline-001', 'kind': 'spawn job', 'target': 'process group', 'priority': 2, 'metadata': {'source': 'Mini Shell With Job Control', 'track': 'systems-programming'}}
        original = dict(request)
        spawn_job_command_pipeline(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
