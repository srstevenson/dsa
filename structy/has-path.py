import unittest
from collections import deque


# time:  O(n + e)
# space: O(n)
# where: n = number of nodes, e = number of edges
def has_path(graph: dict[str, list[str]], src: str, dst: str) -> bool:
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        self.assertTrue(has_path(graph, "f", "k"))

    def test_01(self) -> None:
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        self.assertFalse(has_path(graph, "f", "j"))

    def test_02(self) -> None:
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        self.assertTrue(has_path(graph, "i", "h"))

    def test_03(self) -> None:
        graph = {"v": ["x", "w"], "w": [], "x": [], "y": ["z"], "z": []}

        self.assertTrue(has_path(graph, "v", "w"))

    def test_04(self) -> None:
        graph = {"v": ["x", "w"], "w": [], "x": [], "y": ["z"], "z": []}

        self.assertFalse(has_path(graph, "v", "z"))


if __name__ == "__main__":
    unittest.main()
