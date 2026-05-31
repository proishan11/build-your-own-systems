import unittest

from lab_003 import plan_inference_server_batch_requests


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_batch_request_operations(self):
        self.assertEqual(plan_inference_server_batch_requests({'batch-queue-primary': 'ready', 'batch-queue-canary': 'ready'}, {'batch-queue-primary': 'stale', 'batch-queue-old': 'ready'}), [{'op': 'update', 'name': 'batch-queue-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'batch-queue-old', 'from': 'ready'}, {'op': 'create', 'name': 'batch-queue-canary', 'to': 'ready'}])

    def test_noops_when_batch_queue_already_matches(self):
        current = {'batch-queue-primary': 'ready'}
        self.assertEqual(plan_inference_server_batch_requests(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_inference_server_batch_requests({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
