import unittest

from lab import ModelRouter, NoModel


class ModelRouterTest(unittest.TestCase):
    def test_route_respects_cost_limit(self):
        router = ModelRouter()
        router.add("cheap", context=1000, cost=0.1, latency=100)
        router.add("fast", context=1000, cost=0.2, latency=20)
        self.assertEqual(router.route(tokens=500, max_cost=0.15), "cheap")

    def test_route_picks_lowest_latency_eligible_model(self):
        router = ModelRouter()
        router.add("slow", context=1000, cost=0.1, latency=100)
        router.add("fast", context=1000, cost=0.1, latency=20)
        self.assertEqual(router.route(tokens=500, max_cost=0.2), "fast")

    def test_no_eligible_model(self):
        router = ModelRouter()
        router.add("tiny", context=100, cost=0.1, latency=20)
        with self.assertRaises(NoModel):
            router.route(tokens=500, max_cost=0.2)


if __name__ == "__main__":
    unittest.main()
