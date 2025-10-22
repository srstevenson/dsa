import unittest
from collections import defaultdict, deque


# time:  O(n + e)
# space: O(n + e)
# where: n = number of nodes, e = number of edges
def shortest_path(edges: list[list[str]], node_A: str, node_B: str) -> int:  # noqa: N803
    graph: dict[str, list[str]] = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited: set[str] = {node_A}
    queue = deque([(node_A, 0)])
    while queue:
        current, num_edges = queue.popleft()
        if current == node_B:
            return num_edges
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, num_edges + 1))

    return -1


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
        self.assertEqual(shortest_path(edges, "w", "z"), 2)

    def test_01(self) -> None:
        edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
        self.assertEqual(shortest_path(edges, "y", "x"), 1)

    def test_02(self) -> None:
        edges = [
            ["a", "c"],
            ["a", "b"],
            ["c", "b"],
            ["c", "d"],
            ["b", "d"],
            ["e", "d"],
            ["g", "f"],
        ]
        self.assertEqual(shortest_path(edges, "a", "e"), 3)

    def test_03(self) -> None:
        edges = [
            ["a", "c"],
            ["a", "b"],
            ["c", "b"],
            ["c", "d"],
            ["b", "d"],
            ["e", "d"],
            ["g", "f"],
        ]
        self.assertEqual(shortest_path(edges, "e", "c"), 2)

    def test_04(self) -> None:
        edges = [
            ["a", "c"],
            ["a", "b"],
            ["c", "b"],
            ["c", "d"],
            ["b", "d"],
            ["e", "d"],
            ["g", "f"],
        ]
        self.assertEqual(shortest_path(edges, "b", "g"), -1)

    def test_05(self) -> None:
        edges = [["c", "n"], ["c", "e"], ["c", "s"], ["c", "w"], ["w", "e"]]
        self.assertEqual(shortest_path(edges, "w", "e"), 1)

    def test_06(self) -> None:
        edges = [["c", "n"], ["c", "e"], ["c", "s"], ["c", "w"], ["w", "e"]]
        self.assertEqual(shortest_path(edges, "n", "e"), 2)

    def test_07(self) -> None:
        edges = [
            ["m", "n"],
            ["n", "o"],
            ["o", "p"],
            ["p", "q"],
            ["t", "o"],
            ["r", "q"],
            ["r", "s"],
        ]
        self.assertEqual(shortest_path(edges, "m", "s"), 6)


if __name__ == "__main__":
    unittest.main()
