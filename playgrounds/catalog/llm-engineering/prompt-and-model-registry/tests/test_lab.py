import unittest

from lab import publish_prompt_prompt_template


class CoreMechanismTest(unittest.TestCase):
    def test_builds_valid_prompt_template_request(self):
        self.assertEqual(publish_prompt_prompt_template({'id': 'prompt-template-001', 'kind': 'publish prompt', 'target': 'model binding', 'priority': 2, 'metadata': {'source': 'Prompt and Model Registry', 'track': 'llm-engineering'}}), {'id': 'prompt-template-001', 'action': 'publish prompt', 'target': 'model binding', 'priority': 2, 'accepted': True})

    def test_rejects_malformed_prompt_template_request(self):
        self.assertEqual(publish_prompt_prompt_template({'id': 'bad', 'kind': '', 'target': 'model binding', 'priority': -1, 'metadata': {}}), {'id': 'bad', 'action': 'reject', 'target': 'model binding', 'reason': 'invalid request'})

    def test_does_not_mutate_input(self):
        request = {'id': 'prompt-template-001', 'kind': 'publish prompt', 'target': 'model binding', 'priority': 2, 'metadata': {'source': 'Prompt and Model Registry', 'track': 'llm-engineering'}}
        original = dict(request)
        publish_prompt_prompt_template(request)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
