import unittest

from lab_003 import plan_xv6_style_kernel_lab_enter_kernels


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_enter_kernel_operations(self):
        self.assertEqual(plan_xv6_style_kernel_lab_enter_kernels({'process-table-primary': 'ready', 'process-table-canary': 'ready'}, {'process-table-primary': 'stale', 'process-table-old': 'ready'}), [{'op': 'update', 'name': 'process-table-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'process-table-old', 'from': 'ready'}, {'op': 'create', 'name': 'process-table-canary', 'to': 'ready'}])

    def test_noops_when_process_table_already_matches(self):
        current = {'process-table-primary': 'ready'}
        self.assertEqual(plan_xv6_style_kernel_lab_enter_kernels(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_xv6_style_kernel_lab_enter_kernels({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
