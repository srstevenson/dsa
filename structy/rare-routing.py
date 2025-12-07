import unittest


# time:  O(n + r)
# space: O(n + r)
# where: r = len(roads)
def rare_routing(n: int, roads: list[tuple[int, int]]) -> bool:
    graph: dict[int, list[int]] = {node: [] for node in range(n)}
    for src, dst in roads:
        graph[src].append(dst)
        graph[dst].append(src)

    visited = {0}
    stack = [(0, -1)]

    while stack:
        current, parent = stack.pop()
        for neighbour in graph[current]:
            if neighbour != parent:
                if neighbour in visited:
                    return False
                visited.add(neighbour)
                stack.append((neighbour, current))

    return len(visited) == n


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(rare_routing(4, [(0, 1), (0, 2), (0, 3)]))

    def test_01(self) -> None:
        self.assertFalse(rare_routing(4, [(0, 1), (0, 2), (0, 3), (3, 2)]))

    def test_02(self) -> None:
        self.assertTrue(rare_routing(6, [(1, 2), (5, 4), (3, 0), (0, 1), (0, 4)]))

    def test_03(self) -> None:
        self.assertFalse(
            rare_routing(6, [(1, 2), (4, 1), (5, 4), (3, 0), (0, 1), (0, 4)])
        )

    def test_04(self) -> None:
        self.assertFalse(rare_routing(4, [(0, 1), (3, 2)]))

    def test_05(self) -> None:
        self.assertFalse(rare_routing(4, [(0, 1), (0, 2), (1, 2)]))

    def test_06(self) -> None:
        self.assertFalse(rare_routing(4, []))


if __name__ == "__main__":
    unittest.main()
