import unittest

from lab_004 import recover_oci_image_builder_non_reproducible_layer


class RecoveryTest(unittest.TestCase):
    def test_retries_transient_assemble_image_failure(self):
        self.assertEqual(recover_oci_image_builder_non_reproducible_layer({'operation': 'assemble image', 'error': 'timeout', 'attempt': 1, 'max_attempts': 3, 'resource': 'image manifest'}), {'decision': 'retry', 'next_attempt': 2, 'resource': 'image manifest'})

    def test_fails_permanent_non_reproducible_layer(self):
        self.assertEqual(recover_oci_image_builder_non_reproducible_layer({'operation': 'assemble image', 'error': 'non-reproducible layer', 'attempt': 1, 'max_attempts': 3, 'resource': 'image manifest'}), {'decision': 'fail', 'reason': 'non-reproducible layer', 'resource': 'image manifest'})

    def test_gives_up_when_retry_budget_is_exhausted(self):
        self.assertEqual(recover_oci_image_builder_non_reproducible_layer({'operation': 'assemble image', 'error': 'timeout', 'attempt': 3, 'max_attempts': 3, 'resource': 'image manifest'}), {'decision': 'give_up', 'reason': 'retry budget exhausted', 'resource': 'image manifest'})


if __name__ == "__main__":
    unittest.main()
