import unittest

from lab_003 import plan_structured_output_validator_validate_outputs


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_validate_output_operations(self):
        self.assertEqual(plan_structured_output_validator_validate_outputs({'json-schema-primary': 'ready', 'json-schema-canary': 'ready'}, {'json-schema-primary': 'stale', 'json-schema-old': 'ready'}), [{'op': 'update', 'name': 'json-schema-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'json-schema-old', 'from': 'ready'}, {'op': 'create', 'name': 'json-schema-canary', 'to': 'ready'}])

    def test_noops_when_json_schema_already_matches(self):
        current = {'json-schema-primary': 'ready'}
        self.assertEqual(plan_structured_output_validator_validate_outputs(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_structured_output_validator_validate_outputs({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
