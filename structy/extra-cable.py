import unittest


# time:  O(n + eα(n))
# space: O(n)
# where: e = len(cables), α is the inverse Ackermann function
def extra_cable(num_computers: int, cables: list[tuple[int, int]]) -> tuple[int, int]:
    roots = list(range(num_computers))
    sizes = [1] * num_computers

    def find(comp: int) -> int:
        if roots[comp] != comp:
            roots[comp] = find(roots[comp])
        return roots[comp]

    def union(comp_a: int, comp_b: int) -> bool:
        root_a = find(comp_a)
        root_b = find(comp_b)

        if root_a == root_b:
            return True

        if sizes[root_a] >= sizes[root_b]:
            roots[root_b] = root_a
            sizes[root_a] += sizes[root_b]
        else:
            roots[root_a] = root_b
            sizes[root_b] += sizes[root_a]

        return False

    for cable in cables:
        if union(*cable):
            return cable

    raise RuntimeError("Solution not found")


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            extra_cable(5, [(3, 2), (1, 2), (4, 2), (3, 1), (0, 1)]), (3, 1)
        )

    def test_01(self) -> None:
        self.assertEqual(
            extra_cable(6, [(0, 4), (4, 5), (3, 4), (5, 1), (1, 3), (2, 4)]), (1, 3)
        )

    def test_02(self) -> None:
        self.assertEqual(extra_cable(3, [(0, 1), (1, 2), (2, 0)]), (2, 0))


if __name__ == "__main__":
    unittest.main()
