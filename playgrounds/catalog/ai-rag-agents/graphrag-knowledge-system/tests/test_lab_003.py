import unittest

from lab_003 import plan_graphrag_knowledge_system_link_entitys


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_link_entity_operations(self):
        self.assertEqual(plan_graphrag_knowledge_system_link_entitys({'knowledge-graph-primary': 'ready', 'knowledge-graph-canary': 'ready'}, {'knowledge-graph-primary': 'stale', 'knowledge-graph-old': 'ready'}), [{'op': 'update', 'name': 'knowledge-graph-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'knowledge-graph-old', 'from': 'ready'}, {'op': 'create', 'name': 'knowledge-graph-canary', 'to': 'ready'}])

    def test_noops_when_knowledge_graph_already_matches(self):
        current = {'knowledge-graph-primary': 'ready'}
        self.assertEqual(plan_graphrag_knowledge_system_link_entitys(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_graphrag_knowledge_system_link_entitys({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
