import unittest


# time:  O(n + e)
# space: O(n)
# where: n = number of nodes, e = number of edges
def has_cycle(graph: dict[str, list[str]]) -> bool:
    visited: set[str] = set()
    visiting: set[str] = set()
    return any(_has_cycle(graph, node, visited, visiting) for node in graph)


def _has_cycle(
    graph: dict[str, list[str]], node: str, visited: set[str], visiting: set[str]
) -> bool:
    if node in visited:
        return False
    if node in visiting:
        return True
    visiting.add(node)
    for neighbour in graph[node]:
        if _has_cycle(graph, neighbour, visited, visiting):
            return True
    visiting.remove(node)
    visited.add(node)
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(has_cycle({"a": ["b"], "b": ["c"], "c": ["a"]}))

    def test_01(self) -> None:
        self.assertFalse(has_cycle({"a": ["b", "c"], "b": ["c"], "c": ["d"], "d": []}))

    def test_02(self) -> None:
        self.assertTrue(
            has_cycle({"a": ["b", "c"], "b": [], "c": [], "e": ["f"], "f": ["e"]})
        )

    def test_03(self) -> None:
        self.assertFalse(
            has_cycle(
                {
                    "q": ["r", "s"],
                    "r": ["t", "u"],
                    "s": [],
                    "t": [],
                    "u": [],
                    "v": ["w"],
                    "w": [],
                    "x": ["w"],
                }
            )
        )

    def test_04(self) -> None:
        self.assertTrue(has_cycle({"a": ["b"], "b": ["c"], "c": ["a"], "g": []}))

    def test_05(self) -> None:
        self.assertTrue(has_cycle({"a": ["b"], "b": ["c"], "c": ["d"], "d": ["b"]}))

    def test_06(self) -> None:
        self.assertFalse(
            has_cycle({"a": ["b", "c"], "b": ["c"], "c": ["d"], "d": [], "e": ["c"]})
        )


if __name__ == "__main__":
    unittest.main()
