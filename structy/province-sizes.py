import unittest


# time:  O(n + eα(n))
# space: O(n)
# where: e = len(roads), α is the inverse Ackermann function
def province_sizes(n: int, roads: list[tuple[int, int]]) -> list[int]:
    roots = list(range(n))
    sizes = [1] * n

    def find(city: int) -> int:
        if roots[city] != city:
            roots[city] = find(roots[city])
        return roots[city]

    def union(city_a: int, city_b: int) -> None:
        root_a = find(city_a)
        root_b = find(city_b)

        if root_a == root_b:
            return

        if sizes[root_a] >= sizes[root_b]:
            roots[root_b] = root_a
            sizes[root_a] += sizes[root_b]
        else:
            roots[root_a] = root_b
            sizes[root_b] += sizes[root_a]

    for road in roads:
        union(*road)

    return [sizes[i] for i in range(n) if roots[i] == i]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertCountEqual(
            province_sizes(6, [(4, 5), (1, 0), (2, 3), (0, 5), (5, 1), (4, 0)]), [4, 2]
        )

    def test_01(self) -> None:
        self.assertCountEqual(province_sizes(5, [(4, 0), (3, 2)]), [1, 2, 2])

    def test_02(self) -> None:
        self.assertCountEqual(
            province_sizes(7, [(3, 2), (4, 1), (0, 2), (3, 0), (2, 5)]), [2, 4, 1]
        )

    def test_03(self) -> None:
        self.assertCountEqual(
            province_sizes(
                7, [(1, 6), (0, 2), (6, 3), (5, 1), (1, 2), (3, 4), (1, 4), (3, 0)]
            ),
            [7],
        )


if __name__ == "__main__":
    unittest.main()
