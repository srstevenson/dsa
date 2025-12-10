import unittest


# time:  O(ne)
# space: O(n)
# where: e = len(edges)
def count_components(n: int, edges: list[tuple[int, int]]) -> int:
    roots = list(range(n))

    def find(node: int) -> int:
        while roots[node] != node:
            node = roots[node]
        return node

    def union(node_a: int, node_b: int) -> None:
        roots[find(node_b)] = find(node_a)

    for edge in edges:
        union(*edge)

    return sum(i == v for i, v in enumerate(roots))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            count_components(7, [(0, 2), (1, 0), (4, 3), (2, 5), (3, 6)]), 2
        )

    def test_01(self) -> None:
        self.assertEqual(count_components(6, [(0, 3), (5, 3), (4, 2)]), 3)

    def test_02(self) -> None:
        self.assertEqual(
            count_components(6, [(0, 3), (5, 3), (4, 2), (3, 2), (3, 1)]), 1
        )

    def test_03(self) -> None:
        self.assertEqual(count_components(100, [(50, 60), (80, 20)]), 98)


if __name__ == "__main__":
    unittest.main()
