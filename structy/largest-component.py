import unittest


# time:  O(n + e)
# space: O(n)
# where: n = number of nodes, e = number of edges
def largest_component(graph: dict[int, list[int]]) -> int:
    visited: set[int] = set()
    max_component_size = 0
    for node in graph:
        max_component_size = max(max_component_size, _dfs(graph, visited, node))
    return max_component_size


def _dfs(graph: dict[int, list[int]], visited: set[int], node: int) -> int:
    component_size = 0
    stack = [node]
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        component_size += 1
        stack.extend(
            neighbour for neighbour in graph[current] if neighbour not in visited
        )
    return component_size


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            largest_component(
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
            4,
        )

    def test_01(self) -> None:
        self.assertEqual(
            largest_component(
                {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}
            ),
            6,
        )

    def test_02(self) -> None:
        self.assertEqual(
            largest_component(
                {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}
            ),
            5,
        )

    def test_03(self) -> None:
        self.assertEqual(largest_component({}), 0)

    def test_04(self) -> None:
        self.assertEqual(
            largest_component(
                {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
