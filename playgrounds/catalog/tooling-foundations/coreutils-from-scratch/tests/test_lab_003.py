import unittest

from lab_003 import plan_coreutils_from_scratch_transform_streams


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_transform_stream_operations(self):
        self.assertEqual(plan_coreutils_from_scratch_transform_streams({'command-input-primary': 'ready', 'command-input-canary': 'ready'}, {'command-input-primary': 'stale', 'command-input-old': 'ready'}), [{'op': 'update', 'name': 'command-input-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'command-input-old', 'from': 'ready'}, {'op': 'create', 'name': 'command-input-canary', 'to': 'ready'}])

    def test_noops_when_command_input_already_matches(self):
        current = {'command-input-primary': 'ready'}
        self.assertEqual(plan_coreutils_from_scratch_transform_streams(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_coreutils_from_scratch_transform_streams({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
