import sys
import unittest
from functools import cache


# time:  O(nm)
# space: O(nm)
# where: n = number of plants, m = number of positions
def positioning_plants(costs: list[list[int]]) -> int:
    @cache
    def _positioning_plants(curr_idx: int, prev_idx: int) -> int:
        if curr_idx == len(costs):
            return 0

        min_cost = sys.maxsize
        for idx, cost in enumerate(costs[curr_idx]):
            if idx != prev_idx:
                min_cost = min(min_cost, cost + _positioning_plants(curr_idx + 1, idx))

        return min_cost

    return _positioning_plants(0, -1)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(positioning_plants([[4, 3, 7], [6, 1, 9], [2, 5, 3]]), 7)

    def test_01(self) -> None:
        self.assertEqual(positioning_plants([[12, 14, 5], [6, 3, 2]]), 8)

    def test_02(self) -> None:
        self.assertEqual(
            positioning_plants(
                [[12, 14, 5], [6, 3, 2], [4, 2, 7], [4, 8, 4], [1, 13, 5], [8, 6, 7]]
            ),
            23,
        )

    def test_03(self) -> None:
        self.assertEqual(
            positioning_plants(
                [
                    [12, 14, 5, 13],
                    [6, 3, 20, 3],
                    [24, 12, 7, 2],
                    [4, 80, 45, 3],
                    [104, 13, 5, 14],
                    [38, 19, 7, 6],
                    [12, 2, 1, 2],
                ]
            ),
            26,
        )

    def test_04(self) -> None:
        self.assertEqual(
            positioning_plants(
                [
                    [12, 14, 50, 12],
                    [6, 3, 20, 3],
                    [24, 12, 7, 2],
                    [4, 80, 45, 3],
                    [104, 13, 5, 14],
                    [38, 19, 7, 6],
                    [1, 20, 1, 2],
                    [13, 12, 5, 13],
                    [60, 32, 20, 3],
                    [24, 12, 7, 2],
                    [4, 80, 44, 1],
                    [104, 13, 5, 14],
                    [38, 19, 76, 6],
                    [12, 23, 12, 20],
                    [1, 3, 1, 1],
                    [1, 2, 12, 5],
                ]
            ),
            74,
        )

    def test_05(self) -> None:
        self.assertEqual(
            positioning_plants(
                [
                    [12, 14, 50, 12, 13],
                    [6, 3, 20, 3, 16],
                    [24, 12, 7, 2, 74],
                    [4, 80, 45, 3, 100],
                    [104, 13, 5, 14, 3],
                    [38, 19, 7, 6, 24],
                    [1, 20, 1, 2, 31],
                    [13, 12, 5, 13, 9],
                    [60, 32, 20, 3, 2],
                    [24, 12, 7, 2, 42],
                    [4, 80, 44, 1, 23],
                    [104, 13, 5, 14, 28],
                    [38, 19, 76, 6, 12],
                    [12, 23, 12, 20, 13],
                    [1, 3, 1, 1, 50],
                    [1, 2, 12, 5, 36],
                    [6, 2, 3, 12, 20],
                    [4, 6, 4, 11, 15],
                ]
            ),
            75,
        )


if __name__ == "__main__":
    unittest.main()
