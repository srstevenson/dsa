import unittest


# time:  O(n + e)
# space: O(n)
# where: n = number of nodes, e = number of edges
def connected_components_count(graph: dict[int, list[int]]) -> int:
    visited: set[int] = set()
    count = 0
    for node in graph:
        if node not in visited:
            count += 1
            _dfs(graph, visited, node)
    return count


def _dfs(graph: dict[int, list[int]], visited: set[int], node: int) -> None:
    stack: list[int] = [node]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(
                neighbour for neighbour in graph[current] if neighbour not in visited
            )


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            connected_components_count(
                {
                    0: [8, 1, 5],
                    1: [0],
                    5: [0, 8],
                    8: [0, 5],
                    2: [3, 4],
                    3: [2, 4],
                    4: [3, 2],
                }
            ),
            2,
        )

    def test_01(self) -> None:
        self.assertEqual(
            connected_components_count(
                {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}
            ),
            1,
        )

    def test_02(self) -> None:
        self.assertEqual(
            connected_components_count(
                {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}
            ),
            3,
        )

    def test_03(self) -> None:
        self.assertEqual(connected_components_count({}), 0)

    def test_04(self) -> None:
        self.assertEqual(
            connected_components_count(
                {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}
            ),
            5,
        )


if __name__ == "__main__":
    unittest.main()
