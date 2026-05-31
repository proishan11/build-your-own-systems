import unittest

from lab_003 import plan_oci_image_builder_assemble_images


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_assemble_image_operations(self):
        self.assertEqual(plan_oci_image_builder_assemble_images({'image-manifest-primary': 'ready', 'image-manifest-canary': 'ready'}, {'image-manifest-primary': 'stale', 'image-manifest-old': 'ready'}), [{'op': 'update', 'name': 'image-manifest-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'image-manifest-old', 'from': 'ready'}, {'op': 'create', 'name': 'image-manifest-canary', 'to': 'ready'}])

    def test_noops_when_image_manifest_already_matches(self):
        current = {'image-manifest-primary': 'ready'}
        self.assertEqual(plan_oci_image_builder_assemble_images(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_oci_image_builder_assemble_images({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
