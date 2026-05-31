import unittest

from lab_002 import StaleEvent, StateModel


class StateModelTest(unittest.TestCase):
    def test_apply_event_updates_state_and_audit(self):
        model = StateModel()
        result = model.apply({"id": "e1", "key": "alpha", "version": 1, "value": {"replicas": 2}})
        self.assertEqual(result, {"key": "alpha", "version": 1, "value": {"replicas": 2}})
        self.assertEqual(model.get("alpha"), {"replicas": 2})
        self.assertEqual(len(model.audit()), 1)

    def test_duplicate_event_is_idempotent(self):
        model = StateModel()
        event = {"id": "e1", "key": "alpha", "version": 1, "value": 10}
        self.assertEqual(model.apply(event), model.apply(dict(event)))
        self.assertEqual(len(model.audit()), 1)

    def test_stale_event_is_rejected(self):
        model = StateModel()
        model.apply({"id": "e1", "key": "alpha", "version": 2, "value": "new"})
        with self.assertRaises(StaleEvent):
            model.apply({"id": "e2", "key": "alpha", "version": 1, "value": "old"})


if __name__ == "__main__":
    unittest.main()
