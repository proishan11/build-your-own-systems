import unittest

from lab_003 import plan_rag_from_scratch_retrieve_contexts


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_retrieve_context_operations(self):
        self.assertEqual(plan_rag_from_scratch_retrieve_contexts({'vector-index-primary': 'ready', 'vector-index-canary': 'ready'}, {'vector-index-primary': 'stale', 'vector-index-old': 'ready'}), [{'op': 'update', 'name': 'vector-index-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'vector-index-old', 'from': 'ready'}, {'op': 'create', 'name': 'vector-index-canary', 'to': 'ready'}])

    def test_noops_when_vector_index_already_matches(self):
        current = {'vector-index-primary': 'ready'}
        self.assertEqual(plan_rag_from_scratch_retrieve_contexts(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_rag_from_scratch_retrieve_contexts({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
