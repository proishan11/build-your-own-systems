import unittest

from lab_003 import plan_vim_kata_track_apply_motions


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_apply_motion_operations(self):
        self.assertEqual(plan_vim_kata_track_apply_motions({'buffer-state-primary': 'ready', 'buffer-state-canary': 'ready'}, {'buffer-state-primary': 'stale', 'buffer-state-old': 'ready'}), [{'op': 'update', 'name': 'buffer-state-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'buffer-state-old', 'from': 'ready'}, {'op': 'create', 'name': 'buffer-state-canary', 'to': 'ready'}])

    def test_noops_when_buffer_state_already_matches(self):
        current = {'buffer-state-primary': 'ready'}
        self.assertEqual(plan_vim_kata_track_apply_motions(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_vim_kata_track_apply_motions({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
