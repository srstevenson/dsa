import unittest
from collections import defaultdict


# time:  O(n + e)
# space: O(n + e)
# where: n = length of codes, e = number of hints
def safe_cracking(hints: list[tuple[int, int]]) -> str:
    graph: defaultdict[int, list[int]] = defaultdict(list)
    for child, parent in hints:
        graph[parent].append(child)

    code: list[int] = []
    visited: set[int] = set()

    def _dfs(node: int) -> None:
        visited.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                _dfs(neighbour)
        code.append(node)

    for node in graph:
        if node not in visited:
            _dfs(node)

    return "".join(map(str, code))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(safe_cracking([(7, 1), (1, 8), (7, 8)]), "718")

    def test_01(self) -> None:
        self.assertEqual(
            safe_cracking([(3, 1), (4, 7), (5, 9), (4, 3), (7, 3), (3, 5), (9, 1)]),
            "473591",
        )

    def test_02(self) -> None:
        self.assertEqual(
            safe_cracking(
                [(2, 5), (8, 6), (0, 6), (6, 2), (0, 8), (2, 3), (3, 5), (6, 5)]
            ),
            "086235",
        )

    def test_03(self) -> None:
        self.assertEqual(safe_cracking([(0, 1), (6, 0), (1, 8)]), "6018")

    def test_04(self) -> None:
        self.assertEqual(
            safe_cracking([(8, 9), (4, 2), (8, 2), (3, 8), (2, 9), (4, 9), (8, 4)]),
            "38429",
        )


if __name__ == "__main__":
    unittest.main()
