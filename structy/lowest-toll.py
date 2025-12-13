import unittest
from collections import defaultdict
from heapq import heappop, heappush


# time:  O((n + e)log n)
# space: O(n + e)
# where: n = number of nodes, e = number of edges
def lowest_toll(
    highway_tolls: list[tuple[str, str, float]], start_city: str, end_city: str
) -> float:
    graph: defaultdict[str, dict[str, float]] = defaultdict(dict)
    for src, dst, cost in highway_tolls:
        graph[src][dst] = cost
        graph[dst][src] = cost

    costs = dict.fromkeys(graph, float("inf"))
    costs[start_city] = 0.0
    queue = [(0.0, start_city)]

    while queue:
        cost, current = heappop(queue)

        if cost > costs[current]:
            continue

        if current == end_city:
            return cost

        for city in graph[current]:
            city_cost = cost + graph[current][city]
            if city_cost >= costs[city]:
                continue
            costs[city] = city_cost
            heappush(queue, (city_cost, city))

    raise RuntimeError("Solution not found")


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        highway_tolls = [
            ("Hampton", "Fairfax", 7.50),
            ("Roanoake", "Alexandria", 4.20),
            ("Alexandria", "Hampton", 14.50),
            ("Hampton", "Roanoake", 8.90),
            ("Alexandria", "Fairfax", 5.90),
            ("Hampton", "Manassas", 3.50),
            ("Fairfax", "Manassas", 2.20),
        ]
        self.assertAlmostEqual(
            lowest_toll(highway_tolls, "Alexandria", "Hampton"), 11.60
        )

    def test_01(self) -> None:
        highway_tolls = [
            ("Hampton", "Fairfax", 7.50),
            ("Roanoake", "Alexandria", 4.20),
            ("Alexandria", "Hampton", 14.50),
            ("Hampton", "Roanoake", 8.90),
            ("Alexandria", "Fairfax", 5.90),
            ("Hampton", "Manassas", 3.50),
            ("Fairfax", "Manassas", 2.20),
        ]
        self.assertAlmostEqual(
            lowest_toll(highway_tolls, "Alexandria", "Fairfax"), 5.90
        )

    def test_02(self) -> None:
        highway_tolls = [
            ("Hampton", "Fairfax", 7.50),
            ("Roanoake", "Alexandria", 4.20),
            ("Alexandria", "Hampton", 14.50),
            ("Hampton", "Roanoake", 8.90),
            ("Alexandria", "Fairfax", 5.90),
            ("Hampton", "Manassas", 3.50),
            ("Fairfax", "Manassas", 2.20),
        ]
        self.assertAlmostEqual(lowest_toll(highway_tolls, "Hampton", "Fairfax"), 5.70)


if __name__ == "__main__":
    unittest.main()
