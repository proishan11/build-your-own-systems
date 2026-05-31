import unittest

from lab_003 import plan_tiny_journaling_file_system_commit_records


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_commit_record_operations(self):
        self.assertEqual(plan_tiny_journaling_file_system_commit_records({'inode-block-primary': 'ready', 'inode-block-canary': 'ready'}, {'inode-block-primary': 'stale', 'inode-block-old': 'ready'}), [{'op': 'update', 'name': 'inode-block-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'inode-block-old', 'from': 'ready'}, {'op': 'create', 'name': 'inode-block-canary', 'to': 'ready'}])

    def test_noops_when_inode_block_already_matches(self):
        current = {'inode-block-primary': 'ready'}
        self.assertEqual(plan_tiny_journaling_file_system_commit_records(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_tiny_journaling_file_system_commit_records({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
