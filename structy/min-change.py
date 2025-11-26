import unittest


# time:  O(amount * c)
# space: O(amount)
# where: c = len(coins)
def min_change(amount: int, coins: list[int]) -> int:
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0

    for c in coins:
        for i in range(c, amount + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] <= amount else -1


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(min_change(8, [1, 5, 4, 12]), 2)

    def test_01(self) -> None:
        self.assertEqual(min_change(13, [1, 9, 5, 14, 30]), 5)

    def test_02(self) -> None:
        self.assertEqual(min_change(23, [2, 5, 7]), 4)

    def test_03(self) -> None:
        self.assertEqual(min_change(102, [1, 5, 10, 25]), 6)

    def test_04(self) -> None:
        self.assertEqual(min_change(200, [1, 5, 10, 25]), 8)

    def test_05(self) -> None:
        self.assertEqual(min_change(2017, [4, 2, 10]), -1)

    def test_06(self) -> None:
        self.assertEqual(min_change(271, [10, 8, 265, 24]), -1)

    def test_07(self) -> None:
        self.assertEqual(min_change(0, [4, 2, 10]), 0)

    def test_08(self) -> None:
        self.assertEqual(min_change(0, []), 0)


if __name__ == "__main__":
    unittest.main()
