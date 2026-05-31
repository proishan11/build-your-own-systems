import unittest

from lab_003 import plan_supply_chain_scanner_scan_artifacts


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_scan_artifact_operations(self):
        self.assertEqual(plan_supply_chain_scanner_scan_artifacts({'sbom-index-primary': 'ready', 'sbom-index-canary': 'ready'}, {'sbom-index-primary': 'stale', 'sbom-index-old': 'ready'}), [{'op': 'update', 'name': 'sbom-index-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'sbom-index-old', 'from': 'ready'}, {'op': 'create', 'name': 'sbom-index-canary', 'to': 'ready'}])

    def test_noops_when_sbom_index_already_matches(self):
        current = {'sbom-index-primary': 'ready'}
        self.assertEqual(plan_supply_chain_scanner_scan_artifacts(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_supply_chain_scanner_scan_artifacts({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
