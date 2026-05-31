import unittest

from lab_003 import plan_prompt_and_model_registry_publish_prompts


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_publish_prompt_operations(self):
        self.assertEqual(plan_prompt_and_model_registry_publish_prompts({'model-binding-primary': 'ready', 'model-binding-canary': 'ready'}, {'model-binding-primary': 'stale', 'model-binding-old': 'ready'}), [{'op': 'update', 'name': 'model-binding-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'model-binding-old', 'from': 'ready'}, {'op': 'create', 'name': 'model-binding-canary', 'to': 'ready'}])

    def test_noops_when_model_binding_already_matches(self):
        current = {'model-binding-primary': 'ready'}
        self.assertEqual(plan_prompt_and_model_registry_publish_prompts(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_prompt_and_model_registry_publish_prompts({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
