import unittest


# time:  O(nw)
# space: O(w)
# where: n = len(values), w = weight_limit
def knapsack(values: list[int], weights: list[int], weight_limit: int) -> int:
    dp = [0] * (weight_limit + 1)

    for i in range(len(values)):
        for w in range(weight_limit, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[weight_limit]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(knapsack([5, 4, 9], [6, 1, 15], 20), 13)

    def test_01(self) -> None:
        self.assertEqual(knapsack([5, 1, 6], [4, 1, 5], 20), 12)

    def test_02(self) -> None:
        self.assertEqual(knapsack([5, 1, 7, 3], [4, 1, 5, 2], 8), 11)

    def test_03(self) -> None:
        self.assertEqual(knapsack([89, 45, 12, 50], [40, 20, 10, 15], 50), 107)

    def test_04(self) -> None:
        self.assertEqual(knapsack([3, 5, 8, 7], [2, 4, 8, 6], 15), 16)

    def test_05(self) -> None:
        self.assertEqual(
            knapsack(
                [
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                ],
                [
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                ],
                100,
            ),
            42,
        )


if __name__ == "__main__":
    unittest.main()
