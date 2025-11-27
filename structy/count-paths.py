import unittest


# time:  O(rc)
# space: O(rc)
# where: r = len(grid), c = len(grid[0])
def count_paths(grid: list[list[str]]) -> int:
    nrows = len(grid)
    ncols = len(grid[0])
    dp = [[0 for _ in range(ncols)] for _ in range(nrows)]

    for row in range(nrows - 1, -1, -1):
        for col in range(ncols - 1, -1, -1):
            if row == nrows - 1 and col == ncols - 1:
                dp[row][col] = 1
                continue
            if row + 1 < nrows and grid[row + 1][col] == "O":
                dp[row][col] += dp[row + 1][col]
            if col + 1 < ncols and grid[row][col + 1] == "O":
                dp[row][col] += dp[row][col + 1]

    return dp[0][0]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        grid = [["O", "O"], ["O", "O"]]
        self.assertEqual(count_paths(grid), 2)

    def test_01(self) -> None:
        grid = [["O", "O", "X"], ["O", "O", "O"], ["O", "O", "O"]]
        self.assertEqual(count_paths(grid), 5)

    def test_02(self) -> None:
        grid = [["O", "O", "O"], ["O", "O", "X"], ["O", "O", "O"]]
        self.assertEqual(count_paths(grid), 3)

    def test_03(self) -> None:
        grid = [["O", "O", "O"], ["O", "X", "X"], ["O", "O", "O"]]
        self.assertEqual(count_paths(grid), 1)

    def test_04(self) -> None:
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "X", "O", "O", "O"],
            ["X", "O", "X", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
        ]
        self.assertEqual(count_paths(grid), 0)

    def test_05(self) -> None:
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
            ["X", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
        ]
        self.assertEqual(count_paths(grid), 42)

    def test_06(self) -> None:
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
            ["X", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
        ]
        self.assertEqual(count_paths(grid), 0)

    def test_07(self) -> None:
        grid = [
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        self.assertEqual(count_paths(grid), 40116600)

    def test_08(self) -> None:
        grid = [
            ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
        ]
        self.assertEqual(count_paths(grid), 3190434)


if __name__ == "__main__":
    unittest.main()
