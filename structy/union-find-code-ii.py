import unittest


# time:  O(n + eα(n))
# space: O(n)
# where: e = len(edges), α is the inverse Ackermann function
def count_components(n: int, edges: list[tuple[int, int]]) -> int:
    roots = list(range(n))
    sizes = [1] * n

    def find(node: int) -> int:
        if roots[node] != node:
            roots[node] = find(roots[node])
        return roots[node]

    def union(node_a: int, node_b: int) -> bool:
        root_a = find(node_a)
        root_b = find(node_b)

        if root_a == root_b:
            return False

        if sizes[root_a] >= sizes[root_b]:
            roots[root_b] = root_a
            sizes[root_a] += sizes[root_b]
        else:
            roots[root_a] = root_b
            sizes[root_b] += sizes[root_a]

        return True

    components = n
    for edge in edges:
        if union(*edge):
            components -= 1
    return components


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            count_components(
                10, [(3, 2), (5, 4), (4, 3), (2, 1), (0, 1), (8, 9), (5, 6), (7, 8)]
            ),
            2,
        )

    def test_01(self) -> None:
        self.assertEqual(
            count_components(7, [(0, 2), (1, 0), (4, 3), (2, 5), (3, 6)]), 2
        )

    def test_02(self) -> None:
        self.assertEqual(count_components(6, [(0, 3), (5, 3), (4, 2)]), 3)

    def test_03(self) -> None:
        self.assertEqual(
            count_components(6, [(0, 3), (5, 3), (4, 2), (3, 2), (3, 1)]), 1
        )

    def test_04(self) -> None:
        self.assertEqual(count_components(100, [(50, 60), (80, 20)]), 98)


if __name__ == "__main__":
    unittest.main()
