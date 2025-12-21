import unittest
from functools import cache
from typing import Final

DIRECTIONS: Final = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# time:  O(nmk)
# space:  O(nmk)
def breaking_boundaries(m: int, n: int, k: int, r: int, c: int) -> int:
    @cache
    def _breaking_boundaries(k: int, r: int, c: int) -> int:
        if r < 0 or r >= m or c < 0 or c >= n:
            return 1

        if k == 0:
            return 0

        return sum(_breaking_boundaries(k - 1, r + dr, c + dc) for dr, dc in DIRECTIONS)

    return _breaking_boundaries(k, r, c)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(breaking_boundaries(3, 4, 2, 0, 0), 4)

    def test_01(self) -> None:
        self.assertEqual(breaking_boundaries(2, 2, 2, 1, 1), 6)

    def test_02(self) -> None:
        self.assertEqual(breaking_boundaries(3, 4, 3, 0, 0), 11)

    def test_03(self) -> None:
        self.assertEqual(breaking_boundaries(4, 4, 5, 2, 1), 160)

    def test_04(self) -> None:
        self.assertEqual(breaking_boundaries(5, 6, 9, 2, 5), 11635)

    def test_05(self) -> None:
        self.assertEqual(breaking_boundaries(6, 6, 12, 3, 4), 871065)

    def test_06(self) -> None:
        self.assertEqual(breaking_boundaries(6, 6, 15, 3, 4), 40787896)

    def test_07(self) -> None:
        self.assertEqual(breaking_boundaries(6, 8, 16, 2, 1), 137495089)


if __name__ == "__main__":
    unittest.main()
