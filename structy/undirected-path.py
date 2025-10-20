import unittest
from collections import defaultdict, deque


# time:  O(n + e)
# space: O(n + e)
# where: n = number of nodes, e = number of edges
def undirected_path(edges: list[tuple[str, str]], node_A: str, node_B: str) -> bool:  # noqa: N803
    graph: dict[str, list[str]] = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited: set[str] = {node_A}
    queue = deque([node_A])
    while queue:
        current = queue.popleft()
        if current == node_B:
            return True
        for neighbour in graph[current]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            queue.append(neighbour)
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        self.assertTrue(undirected_path(edges, "j", "m"))

    def test_01(self) -> None:
        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        self.assertTrue(undirected_path(edges, "m", "j"))

    def test_02(self) -> None:
        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        self.assertTrue(undirected_path(edges, "l", "j"))

    def test_03(self) -> None:
        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        self.assertFalse(undirected_path(edges, "k", "o"))

    def test_04(self) -> None:
        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        self.assertFalse(undirected_path(edges, "i", "o"))

    def test_05(self) -> None:
        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        self.assertTrue(undirected_path(edges, "a", "b"))

    def test_06(self) -> None:
        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        self.assertTrue(undirected_path(edges, "a", "c"))

    def test_07(self) -> None:
        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        self.assertTrue(undirected_path(edges, "r", "t"))

    def test_08(self) -> None:
        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        self.assertFalse(undirected_path(edges, "r", "b"))

    def test_09(self) -> None:
        edges = [("s", "r"), ("t", "q"), ("q", "r")]

        self.assertTrue(undirected_path(edges, "r", "t"))


if __name__ == "__main__":
    unittest.main()
