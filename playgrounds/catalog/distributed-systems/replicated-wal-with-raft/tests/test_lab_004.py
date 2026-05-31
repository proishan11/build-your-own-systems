import unittest

from lab_004 import RetryPolicy


class RetryPolicyTest(unittest.TestCase):
    def test_retryable_errors_retry_until_budget_is_exhausted(self):
        policy = RetryPolicy(max_attempts=3, retryable_errors={"timeout", "unavailable"})
        self.assertEqual(policy.record_failure("op1", "timeout"), {"decision": "retry", "attempt": 1})
        self.assertEqual(policy.record_failure("op1", "timeout"), {"decision": "retry", "attempt": 2})
        self.assertEqual(policy.record_failure("op1", "timeout"), {"decision": "give_up", "attempt": 3})

    def test_non_retryable_error_fails_immediately(self):
        policy = RetryPolicy(max_attempts=3, retryable_errors={"timeout"})
        self.assertEqual(policy.record_failure("op2", "permission_denied"), {"decision": "fail", "attempt": 1})

    def test_success_is_sticky(self):
        policy = RetryPolicy(max_attempts=3, retryable_errors={"timeout"})
        self.assertEqual(policy.record_success("op3"), {"decision": "success", "attempt": 0})
        self.assertEqual(policy.record_failure("op3", "timeout"), {"decision": "success", "attempt": 0})


if __name__ == "__main__":
    unittest.main()
