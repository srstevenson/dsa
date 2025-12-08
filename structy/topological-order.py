import unittest


# time:  O(n + e)
# space: O(n)
# where: n = number of nodes, e = number of edges
def topological_order(graph: dict[str, list[str]]) -> list[str]:
    order: list[str] = []
    visited: set[str] = set()

    def _dfs(node: str) -> None:
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                _dfs(neighbour)
        order.append(node)

    for node in graph:
        if node not in visited:
            _dfs(node)

    return order[::-1]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            topological_order(
                {
                    "a": ["f"],
                    "b": ["d"],
                    "c": ["a", "f"],
                    "d": ["e"],
                    "e": [],
                    "f": ["b", "e"],
                }
            ),
            ["c", "a", "f", "b", "d", "e"],
        )

    def test_01(self) -> None:
        self.assertEqual(
            topological_order(
                {
                    "h": ["l", "m"],
                    "i": ["k"],
                    "j": ["k", "i"],
                    "k": ["h", "m"],
                    "l": ["m"],
                    "m": [],
                }
            ),
            ["j", "i", "k", "h", "l", "m"],
        )

    def test_02(self) -> None:
        self.assertEqual(
            topological_order({"q": [], "r": ["q"], "s": ["r"], "t": ["s"]}),
            ["t", "s", "r", "q"],
        )

    def test_03(self) -> None:
        self.assertEqual(
            topological_order(
                {"v": ["z", "w"], "w": [], "x": ["w", "v", "z"], "y": ["x"], "z": ["w"]}
            ),
            ["y", "x", "v", "z", "w"],
        )


if __name__ == "__main__":
    unittest.main()
