import unittest


# time:  O(n + m)
# space: O(n + m)
# where: n = len(a), m = len(b)
def exclusive_items(a: list[int], b: list[int]) -> list[int]:
    return list(set(a) ^ set(b))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertCountEqual(
            exclusive_items([4, 2, 1, 6], [3, 6, 9, 2, 10]), [4, 1, 3, 9, 10]
        )

    def test_01(self) -> None:
        self.assertCountEqual(exclusive_items([2, 4, 6], [4, 2]), [6])

    def test_02(self) -> None:
        self.assertCountEqual(exclusive_items([4, 2, 1], [1, 2, 4, 6]), [6])

    def test_03(self) -> None:
        self.assertCountEqual(exclusive_items([0, 1, 2], [10, 11]), [0, 1, 2, 10, 11])

    def test_04(self) -> None:
        a = list(range(50000))
        b = list(range(50000))
        self.assertCountEqual(exclusive_items(a, b), [])


if __name__ == "__main__":
    unittest.main()
