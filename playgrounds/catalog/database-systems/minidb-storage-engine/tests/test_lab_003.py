import unittest

from lab_003 import plan_minidb_storage_engine_write_records


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_write_record_operations(self):
        self.assertEqual(plan_minidb_storage_engine_write_records({'page-cache-primary': 'ready', 'page-cache-canary': 'ready'}, {'page-cache-primary': 'stale', 'page-cache-old': 'ready'}), [{'op': 'update', 'name': 'page-cache-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'page-cache-old', 'from': 'ready'}, {'op': 'create', 'name': 'page-cache-canary', 'to': 'ready'}])

    def test_noops_when_page_cache_already_matches(self):
        current = {'page-cache-primary': 'ready'}
        self.assertEqual(plan_minidb_storage_engine_write_records(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_minidb_storage_engine_write_records({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
