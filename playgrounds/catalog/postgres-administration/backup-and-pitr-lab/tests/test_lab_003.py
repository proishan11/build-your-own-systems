import unittest

from lab_003 import plan_backup_and_pitr_lab_restore_targets


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_restore_target_operations(self):
        self.assertEqual(plan_backup_and_pitr_lab_restore_targets({'backup-catalog-primary': 'ready', 'backup-catalog-canary': 'ready'}, {'backup-catalog-primary': 'stale', 'backup-catalog-old': 'ready'}), [{'op': 'update', 'name': 'backup-catalog-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'backup-catalog-old', 'from': 'ready'}, {'op': 'create', 'name': 'backup-catalog-canary', 'to': 'ready'}])

    def test_noops_when_backup_catalog_already_matches(self):
        current = {'backup-catalog-primary': 'ready'}
        self.assertEqual(plan_backup_and_pitr_lab_restore_targets(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_backup_and_pitr_lab_restore_targets({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
