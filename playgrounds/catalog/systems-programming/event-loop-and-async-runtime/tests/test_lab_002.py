import unittest

from lab_002 import apply_event_loop_and_async_runtime_async_task_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_async_task_events_idempotently(self):
        self.assertEqual(apply_event_loop_and_async_runtime_async_task_event([{'id': 'e1', 'resource': 'ready queue', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'ready queue', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'ready queue', 'version': 2, 'state': 'committed'}]), {'resource': 'ready queue', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_async_task_event(self):
        self.assertEqual(apply_event_loop_and_async_runtime_async_task_event([{'id': 'e1', 'resource': 'ready queue', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'ready queue', 'version': 1, 'state': 'old'}]), {'resource': 'ready queue', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_event_loop_and_async_runtime_async_task_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
