import unittest
from collections import deque


# time:  O(nm)
# space: O(nm)
# where: n = len(grid), m = len(grid[0])
def closest_carrot(grid: list[list[str]], starting_row: int, starting_col: int) -> int:
    visited = {(starting_row, starting_col)}
    queue = deque([(starting_row, starting_col, 0)])
    while queue:
        y, x, steps = queue.popleft()
        if grid[y][x] == "C":
            return steps
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            yp, xp = y + dy, x + dx
            if (
                0 <= yp < len(grid)
                and 0 <= xp < len(grid[0])
                and grid[yp][xp] != "X"
                and (yp, xp) not in visited
            ):
                visited.add((yp, xp))
                queue.append((yp, xp, steps + 1))

    return -1


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        grid = [
            ["O", "O", "O", "O", "O"],
            ["O", "X", "O", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["O", "X", "C", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["C", "O", "O", "O", "O"],
        ]

        self.assertEqual(closest_carrot(grid, 1, 2), 4)

    def test_01(self) -> None:
        grid = [
            ["O", "O", "O", "O", "O"],
            ["O", "X", "O", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["O", "X", "C", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["C", "O", "O", "O", "O"],
        ]

        self.assertEqual(closest_carrot(grid, 0, 0), 5)

    def test_02(self) -> None:
        grid = [
            ["O", "O", "X", "X", "X"],
            ["O", "X", "X", "X", "C"],
            ["O", "X", "O", "X", "X"],
            ["O", "O", "O", "O", "O"],
            ["O", "X", "X", "X", "X"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "C", "O", "O"],
            ["O", "O", "O", "O", "O"],
        ]

        self.assertEqual(closest_carrot(grid, 3, 4), 9)

    def test_03(self) -> None:
        grid = [
            ["O", "O", "X", "O", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "C", "C", "O"],
        ]

        self.assertEqual(closest_carrot(grid, 1, 4), 2)

    def test_04(self) -> None:
        grid = [
            ["O", "O", "X", "O", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "C", "C", "O"],
        ]

        self.assertEqual(closest_carrot(grid, 2, 0), -1)

    def test_05(self) -> None:
        grid = [
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "C"],
        ]

        self.assertEqual(closest_carrot(grid, 0, 0), -1)

    def test_06(self) -> None:
        grid = [
            ["O", "O", "X", "C", "O"],
            ["O", "X", "X", "X", "O"],
            ["C", "X", "O", "O", "O"],
        ]
        self.assertEqual(closest_carrot(grid, 2, 2), 5)


if __name__ == "__main__":
    unittest.main()
