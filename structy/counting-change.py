import unittest


# time:  O(amount * c)
# space: O(amount)
# where: c = len(coins)
def counting_change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(counting_change(4, [1, 2, 3]), 4)

    def test_01(self) -> None:
        self.assertEqual(counting_change(8, [1, 2, 3]), 10)

    def test_02(self) -> None:
        self.assertEqual(counting_change(24, [5, 7, 3]), 5)

    def test_03(self) -> None:
        self.assertEqual(counting_change(13, [2, 6, 12, 10]), 0)

    def test_04(self) -> None:
        self.assertEqual(counting_change(512, [1, 5, 10, 25]), 20119)

    def test_05(self) -> None:
        self.assertEqual(counting_change(1000, [1, 5, 10, 25]), 142511)

    def test_06(self) -> None:
        self.assertEqual(counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]), 1525987916)


if __name__ == "__main__":
    unittest.main()
