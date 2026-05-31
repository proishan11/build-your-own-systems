import unittest

from lab_005 import run_scenario


class IntegrationSimulationTest(unittest.TestCase):
    def test_apply_events_build_final_state(self):
        report = run_scenario([
            {"type": "apply", "key": "api", "value": 2},
            {"type": "apply", "key": "worker", "value": 1},
        ])
        self.assertEqual(report["state"], {"api": 2, "worker": 1})
        self.assertEqual(report["metrics"]["processed"], 2)
        self.assertTrue(report["invariant_ok"])

    def test_tracks_failures_and_recoveries(self):
        report = run_scenario([
            {"type": "fail", "component": "api"},
            {"type": "recover", "component": "api"},
        ])
        self.assertEqual(report["metrics"]["failed"], 1)
        self.assertEqual(report["metrics"]["recovered"], 1)
        self.assertEqual(report["failed_components"], [])

    def test_reports_invariant_violations(self):
        report = run_scenario([{"type": "apply", "key": "", "value": 1}])
        self.assertFalse(report["invariant_ok"])
        self.assertGreaterEqual(len(report["violations"]), 1)


if __name__ == "__main__":
    unittest.main()
