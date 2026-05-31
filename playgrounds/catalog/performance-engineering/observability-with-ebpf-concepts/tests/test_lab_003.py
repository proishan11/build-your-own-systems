import unittest

from lab_003 import plan_observability_with_ebpf_concepts_attach_probes


class PlanningTest(unittest.TestCase):
    def test_plans_deterministic_attach_probe_operations(self):
        self.assertEqual(plan_observability_with_ebpf_concepts_attach_probes({'probe-registry-primary': 'ready', 'probe-registry-canary': 'ready'}, {'probe-registry-primary': 'stale', 'probe-registry-old': 'ready'}), [{'op': 'update', 'name': 'probe-registry-primary', 'from': 'stale', 'to': 'ready'}, {'op': 'delete', 'name': 'probe-registry-old', 'from': 'ready'}, {'op': 'create', 'name': 'probe-registry-canary', 'to': 'ready'}])

    def test_noops_when_probe_registry_already_matches(self):
        current = {'probe-registry-primary': 'ready'}
        self.assertEqual(plan_observability_with_ebpf_concepts_attach_probes(current, dict(current)), [])

    def test_create_actions_are_sorted_by_name(self):
        self.assertEqual(
            plan_observability_with_ebpf_concepts_attach_probes({'b': 'ready', 'a': 'ready'}, {}),
            [{'op': 'create', 'name': 'a', 'to': 'ready'}, {'op': 'create', 'name': 'b', 'to': 'ready'}],
        )


if __name__ == "__main__":
    unittest.main()
