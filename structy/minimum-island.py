import sys
import unittest


# time:  O(n m)
# space: O(n m)
# where: n = len(grid), m = len(grid[0])
def minimum_island(grid: list[list[str]]) -> int:
    visited: set[tuple[int, int]] = set()
    min_island_size = sys.maxsize
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "L" or (y, x) in visited:
                continue
            min_island_size = min(min_island_size, _island_size(grid, visited, y, x))
    return min_island_size


def _island_size(
    grid: list[list[str]], visited: set[tuple[int, int]], y: int, x: int
) -> int:
    size = 0
    visited.add((y, x))
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        size += 1
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            yp, xp = y + dy, x + dx
            if (
                0 <= yp < len(grid)
                and 0 <= xp < len(grid[0])
                and grid[yp][xp] == "L"
                and (yp, xp) not in visited
            ):
                visited.add((yp, xp))
                stack.append((yp, xp))
    return size


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        grid = [
            ["W", "L", "W", "W", "W"],
            ["W", "L", "W", "W", "W"],
            ["W", "W", "W", "L", "W"],
            ["W", "W", "L", "L", "W"],
            ["L", "W", "W", "L", "L"],
            ["L", "L", "W", "W", "W"],
        ]

        self.assertEqual(minimum_island(grid), 2)

    def test_01(self) -> None:
        grid = [
            ["L", "W", "W", "L", "W"],
            ["L", "W", "W", "L", "L"],
            ["W", "L", "W", "L", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "W", "L", "L", "L"],
        ]

        self.assertEqual(minimum_island(grid), 1)

    def test_02(self) -> None:
        grid = [["L", "L", "L"], ["L", "L", "L"], ["L", "L", "L"]]

        self.assertEqual(minimum_island(grid), 9)

    def test_03(self) -> None:
        grid = [["W", "W"], ["L", "L"], ["W", "W"], ["W", "L"]]

        self.assertEqual(minimum_island(grid), 1)


if __name__ == "__main__":
    unittest.main()
