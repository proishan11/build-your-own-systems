import unittest

from lab_004 import recover_dynamic_routing_simulator_routing_loop


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_relax_route_failure(self):
        self.assertEqual(recover_dynamic_routing_simulator_routing_loop({'operation': 'relax route', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'neighbor table'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'neighbor table'})

    def test_fails_permanent_routing_loop(self):
        self.assertEqual(recover_dynamic_routing_simulator_routing_loop({'operation': 'relax route', 'error': 'routing loop', 'attempt': 1, 'max_attempts': 3, 'resource': 'neighbor table'}), {'decision': 'fail', 'reason': 'routing loop', 'resource': 'neighbor table'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_dynamic_routing_simulator_routing_loop({'operation': 'relax route', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'neighbor table'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'neighbor table'})


if __name__ == "__main__":
    unittest.main()
