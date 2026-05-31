import unittest

from lab_003 import plan_operator_for_postgresql_backups_start_backups


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_start_backup_operations(self):
        self.assertEqual(plan_operator_for_postgresql_backups_start_backups({'backup-schedule-primary': 'ready', 'backup-schedule-canary': 'ready'}, {'backup-schedule-primary': 'stale', 'backup-schedule-old': 'ready'}), [{'op': 'update', 'name': 'backup-schedule-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'backup-schedule-old', 'from': 'ready'}, {'op': 'create', 'name': 'backup-schedule-canary', 'to': 'ready'}])

    def test_noops_when_backup_schedule_already_matches(self):
        current = {'backup-schedule-primary': 'ready'}
        self.assertEqual(plan_operator_for_postgresql_backups_start_backups(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_operator_for_postgresql_backups_start_backups({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
