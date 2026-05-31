import unittest

from lab import schedule_task_map_task


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_map_task_request(self):
        self.assertEqual(schedule_task_map_task({'id': 'map-task-001', 'kind': 'schedule task', 'target': 'task tracker', 'priority': 2, 'metadata': {'source': 'MapReduce Runtime', 'track': 'distributed-systems'}}), {'id': 'map-task-001', 'action': 'schedule task', 'target': 'task tracker', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_map_task_request(self):
        self.assertEqual(schedule_task_map_task({'id': 'bad', 'kind': '', 'target': 'task tracker', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'task tracker', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'map-task-001', 'kind': 'schedule task', 'target': 'task tracker', 'priority': 2, 'metadata': {'source': 'MapReduce Runtime', 'track': 'distributed-systems'}}
        original = dict(request)
        schedule_task_map_task(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
