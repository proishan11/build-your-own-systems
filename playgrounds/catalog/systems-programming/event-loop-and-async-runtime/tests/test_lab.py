import unittest

from lab import schedule_callback_async_task


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_async_task_request(self):
        self.assertEqual(schedule_callback_async_task({'id': 'async-task-001', 'kind': 'schedule callback', 'target': 'ready queue', 'priority': 2, 'metadata': {'source': 'Event Loop and Async Runtime', 'track': 'systems-programming'}}), {'id': 'async-task-001', 'action': 'schedule callback', 'target': 'ready queue', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_async_task_request(self):
        self.assertEqual(schedule_callback_async_task({'id': 'bad', 'kind': '', 'target': 'ready queue', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'ready queue', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'async-task-001', 'kind': 'schedule callback', 'target': 'ready queue', 'priority': 2, 'metadata': {'source': 'Event Loop and Async Runtime', 'track': 'systems-programming'}}
        original = dict(request)
        schedule_callback_async_task(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
