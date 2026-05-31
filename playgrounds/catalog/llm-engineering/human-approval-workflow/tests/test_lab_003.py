import unittest

from lab_003 import plan_human_approval_workflow_route_approvals


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_route_approval_operations(self):
        self.assertEqual(plan_human_approval_workflow_route_approvals({'approval-queue-primary': 'ready', 'approval-queue-canary': 'ready'}, {'approval-queue-primary': 'stale', 'approval-queue-old': 'ready'}), [{'op': 'update', 'name': 'approval-queue-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'approval-queue-old', 'from': 'ready'}, {'op': 'create', 'name': 'approval-queue-canary', 'to': 'ready'}])

    def test_noops_when_approval_queue_already_matches(self):
        current = {'approval-queue-primary': 'ready'}
        self.assertEqual(plan_human_approval_workflow_route_approvals(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_human_approval_workflow_route_approvals({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
