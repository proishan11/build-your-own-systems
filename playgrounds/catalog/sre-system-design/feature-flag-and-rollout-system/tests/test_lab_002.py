import unittest

from lab_002 import apply_feature_flag_and_rollout_system_flag_evaluation_event


class StateInvariantTest(unittest.TestCase):
    def test_applies_ordered_flag_evaluation_events_idempotently(self):
        self.assertEqual(apply_feature_flag_and_rollout_system_flag_evaluation_event([{'id': 'e1', 'resource': 'rollout rule', 'version': 1, 'state': 'prepared'}, {'id': 'e1', 'resource': 'rollout rule', 'version': 1, 'state': 'prepared'}, {'id': 'e2', 'resource': 'rollout rule', 'version': 2, 'state': 'committed'}]), {'resource': 'rollout rule', 'version': 2, 'state': 'committed', 'accepted_events': ['e1', 'e2']})

    def test_rejects_stale_flag_evaluation_event(self):
        self.assertEqual(apply_feature_flag_and_rollout_system_flag_evaluation_event([{'id': 'e1', 'resource': 'rollout rule', 'version': 2, 'state': 'new'}, {'id': 'e2', 'resource': 'rollout rule', 'version': 1, 'state': 'old'}]), {'resource': 'rollout rule', 'version': 2, 'state': 'new', 'accepted_events': ['e1'], 'rejected_events': ['e2']})

    def test_empty_event_stream_has_empty_state(self):
        self.assertEqual(apply_feature_flag_and_rollout_system_flag_evaluation_event([]), {'resource': None, 'version': 0, 'state': None, 'accepted_events': []})


if __name__ == "__main__":
    unittest.main()
