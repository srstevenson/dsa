import unittest
from collections import defaultdict


# time:  O(an)
# space: O(a)
# where: a = amount, n = len(numbers)
def sum_possible(amount: int, numbers: list[int]) -> bool:
    dp: defaultdict[int, bool] = defaultdict(bool)
    dp[0] = True

    for i in range(1, amount + 1):
        for number in numbers:
            if dp[i - number]:
                dp[i] = True
                break

    return dp[amount]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(sum_possible(8, [5, 12, 4]))

    def test_01(self) -> None:
        self.assertFalse(sum_possible(15, [6, 2, 10, 19]))

    def test_02(self) -> None:
        self.assertTrue(sum_possible(13, [6, 2, 1]))

    def test_03(self) -> None:
        self.assertTrue(sum_possible(103, [6, 20, 1]))

    def test_04(self) -> None:
        self.assertFalse(sum_possible(12, []))

    def test_05(self) -> None:
        self.assertTrue(sum_possible(12, [12]))

    def test_06(self) -> None:
        self.assertTrue(sum_possible(0, []))

    def test_07(self) -> None:
        self.assertFalse(sum_possible(271, [10, 8, 265, 24]))

    def test_08(self) -> None:
        self.assertFalse(sum_possible(2017, [4, 2, 10]))

    def test_09(self) -> None:
        self.assertTrue(sum_possible(13, [3, 5]))

    def test_10(self) -> None:
        self.assertTrue(sum_possible(10, [4, 5, 7]))

    def test_11(self) -> None:
        self.assertTrue(sum_possible(16, [7, 6, 3]))


if __name__ == "__main__":
    unittest.main()
