import unittest

from lab import classify_tool_call


class AgentSecurityTest(unittest.TestCase):
    def test_allows_read_only_tools(self):
        decision, reason = classify_tool_call("read_file", {"path": "README.md"})
        self.assertEqual(decision, "allow")
        self.assertGreater(len(reason), 10)

    def test_requires_approval_for_mutation(self):
        decision, reason = classify_tool_call("write_file", {"path": "README.md"})
        self.assertEqual(decision, "approval")
        self.assertIn("mutat", reason.lower())

    def test_denies_dangerous_tools(self):
        decision, reason = classify_tool_call("disable_audit_log", {})
        self.assertEqual(decision, "deny")
        self.assertGreater(len(reason), 10)


if __name__ == "__main__":
    unittest.main()
