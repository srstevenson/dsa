import unittest


# time:  O(n + m)
# space: O(n + m)
# where: n = len(a), m = len(b)
def intersection(a: list[int], b: list[int]) -> list[int]:
    return list(set(a) & set(b))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertCountEqual(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]), [2, 6])

    def test_01(self) -> None:
        self.assertCountEqual(intersection([2, 4, 6], [4, 2]), [2, 4])

    def test_02(self) -> None:
        self.assertCountEqual(intersection([4, 2, 1], [1, 2, 4, 6]), [1, 2, 4])

    def test_03(self) -> None:
        self.assertCountEqual(intersection([0, 1, 2], [10, 11]), [])

    def test_04(self) -> None:
        a = list(range(50000))
        b = list(range(50000))
        self.assertCountEqual(intersection(a, b), list(range(50_000)))


if __name__ == "__main__":
    unittest.main()
