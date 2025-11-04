import unittest

Interval = tuple[int, int]


# time:  O(n log n)
# space: O(n)
# where: n = len(intervals)
def combine_intervals(intervals: list[Interval]) -> list[Interval]:
    intervals.sort(key=lambda interval: interval[0])

    combined: list[Interval] = []
    idx = 0
    current = intervals[0]
    while idx < len(intervals):
        if intervals[idx][0] <= current[1]:
            current = (current[0], max(current[1], intervals[idx][1]))
        else:
            combined.append(current)
            current = intervals[idx]
        idx += 1
    combined.append(current)
    return combined


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        intervals = [(1, 4), (12, 15), (3, 7), (8, 13)]
        self.assertEqual(combine_intervals(intervals), [(1, 7), (8, 15)])

    def test_01(self) -> None:
        intervals = [(6, 8), (2, 9), (10, 12), (20, 24)]
        self.assertEqual(combine_intervals(intervals), [(2, 9), (10, 12), (20, 24)])

    def test_02(self) -> None:
        intervals = [(3, 7), (5, 8), (1, 5)]
        self.assertEqual(combine_intervals(intervals), [(1, 8)])

    def test_03(self) -> None:
        intervals = [(3, 7), (10, 13), (5, 8), (27, 31), (1, 5), (12, 16), (20, 22)]
        self.assertEqual(
            combine_intervals(intervals), [(1, 8), (10, 16), (20, 22), (27, 31)]
        )

    def test_04(self) -> None:
        intervals = [(3, 7), (10, 13), (5, 8), (27, 31), (1, 5), (12, 16), (20, 32)]
        self.assertEqual(combine_intervals(intervals), [(1, 8), (10, 16), (20, 32)])

    def test_05(self) -> None:
        intervals = [(64, 70), (50, 55), (62, 65), (12, 50), (72, 300000)]
        self.assertEqual(
            combine_intervals(intervals), [(12, 55), (62, 70), (72, 300000)]
        )


if __name__ == "__main__":
    unittest.main()
