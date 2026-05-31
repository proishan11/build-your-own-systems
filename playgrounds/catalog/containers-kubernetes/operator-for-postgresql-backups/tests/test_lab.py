import unittest

from lab import start_backup_backup_custom_resource


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_backup_custom_resource_request(self):
        self.assertEqual(start_backup_backup_custom_resource({'id': 'backup-custom-resource-001', 'kind': 'start backup', 'target': 'backup schedule', 'priority': 2, 'metadata': {'source': 'Operator for PostgreSQL Backups', 'track': 'containers-kubernetes'}}), {'id': 'backup-custom-resource-001', 'action': 'start backup', 'target': 'backup schedule', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_backup_custom_resource_request(self):
        self.assertEqual(start_backup_backup_custom_resource({'id': 'bad', 'kind': '', 'target': 'backup schedule', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'backup schedule', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'backup-custom-resource-001', 'kind': 'start backup', 'target': 'backup schedule', 'priority': 2, 'metadata': {'source': 'Operator for PostgreSQL Backups', 'track': 'containers-kubernetes'}}
        original = dict(request)
        start_backup_backup_custom_resource(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
