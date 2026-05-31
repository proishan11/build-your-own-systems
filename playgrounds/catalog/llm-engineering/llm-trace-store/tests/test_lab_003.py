import unittest

from lab_003 import plan_llm_trace_store_record_spans


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_record_span_operations(self):
        self.assertEqual(plan_llm_trace_store_record_spans({'trace-index-primary': 'ready', 'trace-index-canary': 'ready'}, {'trace-index-primary': 'stale', 'trace-index-old': 'ready'}), [{'op': 'update', 'name': 'trace-index-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'trace-index-old', 'from': 'ready'}, {'op': 'create', 'name': 'trace-index-canary', 'to': 'ready'}])

    def test_noops_when_trace_index_already_matches(self):
        current = {'trace-index-primary': 'ready'}
        self.assertEqual(plan_llm_trace_store_record_spans(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_llm_trace_store_record_spans({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
