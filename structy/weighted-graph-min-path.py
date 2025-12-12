import sys
import unittest
from heapq import heappop, heappush


# time:  O((n + e)log n)
# space: O(n)
# where: n = number of nodes, e = number of edges
def weighted_graph_min_path(
    graph: dict[str, dict[str, int]], src: str, dst: str
) -> int:
    costs = dict.fromkeys(graph, sys.maxsize)
    costs[src] = 0
    queue = [(0, src)]
    while queue:
        cost, current = heappop(queue)

        if cost > costs[current]:
            continue

        if current == dst:
            return cost

        for node in graph[current]:
            node_cost = cost + graph[current][node]
            if node_cost < costs[node]:
                costs[node] = node_cost
                heappush(queue, (node_cost, node))

    raise RuntimeError("Solution not found")


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        graph = {
            "a": {"b": 2, "d": 9, "c": 5},
            "b": {"a": 2, "d": 4, "e": 6},
            "c": {"a": 5, "e": 4},
            "d": {"a": 9, "b": 4, "e": 1},
            "e": {"b": 6, "c": 4, "d": 1},
        }
        self.assertEqual(weighted_graph_min_path(graph, "a", "e"), 7)

    def test_01(self) -> None:
        graph = {
            "a": {"b": 1, "c": 1},
            "b": {"c": 3, "a": 1},
            "c": {"b": 3, "d": 1, "a": 1},
            "d": {"c": 1, "b": 2},
        }
        self.assertEqual(weighted_graph_min_path(graph, "a", "d"), 2)

    def test_02(self) -> None:
        graph = {
            "q": {"r": 5, "s": 10},
            "r": {"q": 5, "s": 9, "u": 2},
            "s": {"q": 10, "r": 9, "t": 1, "v": 8},
            "t": {"s": 1},
            "u": {"r": 2, "s": 1},
            "v": {},
        }
        self.assertEqual(weighted_graph_min_path(graph, "q", "v"), 16)

    def test_03(self) -> None:
        graph = {
            "q": {"r": 5, "s": 10},
            "r": {"q": 5, "s": 9, "u": 2},
            "s": {"q": 10, "r": 9, "t": 1, "v": 8},
            "t": {"s": 1},
            "u": {"r": 2, "s": 1},
            "v": {},
        }
        self.assertEqual(weighted_graph_min_path(graph, "r", "v"), 11)

    def test_04(self) -> None:
        graph = {
            "x": {"q": 1, "e": 10},
            "b": {"e": 7, "q": 8},
            "q": {"x": 1, "b": 8},
            "e": {"b": 7, "x": 10},
        }
        self.assertEqual(weighted_graph_min_path(graph, "b", "x"), 9)


if __name__ == "__main__":
    unittest.main()
