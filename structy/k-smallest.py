import unittest
from heapq import heappop, heappush, nsmallest


# time:  O(n log n)†
# space: O(k)
# where: n = len(nums)
#
# † heapq.nsmallest uses a heap, giving O(n log k) complexity, when k << n, but
# otherwise sorts, giving O(n log n) worst case complexity.
def k_smallest_heapq(nums: list[int], k: int) -> list[int]:
    return nsmallest(k, nums)


# time:  O(n log k)
# space: O(k)
# where: n = len(nums)
def k_smallest(nums: list[int], k: int) -> list[int]:
    heap: list[int] = []
    for num in nums:
        heappush(heap, -num)
        if len(heap) > k:
            heappop(heap)
    return sorted(-num for num in heap)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        for solution in [k_smallest, k_smallest_heapq]:
            self.assertEqual(solution([8, 2, 7, -3, 5, 10], 3), [-3, 2, 5])

    def test_01(self) -> None:
        for solution in [k_smallest, k_smallest_heapq]:
            self.assertEqual(
                solution([84, 22, 52, 69, 71, 22, 88, 100, 13, 89, 79], 4),
                [13, 22, 22, 52],
            )

    def test_02(self) -> None:
        for solution in [k_smallest, k_smallest_heapq]:
            self.assertEqual(
                solution(
                    [
                        43,
                        35,
                        62,
                        31,
                        86,
                        81,
                        58,
                        80,
                        91,
                        13,
                        54,
                        78,
                        75,
                        69,
                        60,
                        8,
                        22,
                        12,
                        30,
                        79,
                        100,
                        2,
                        64,
                        57,
                        11,
                        55,
                        7,
                        68,
                        66,
                        14,
                        45,
                        26,
                        83,
                        24,
                        28,
                        76,
                        34,
                        89,
                        37,
                        32,
                        41,
                        88,
                        20,
                        82,
                        59,
                        4,
                        40,
                        9,
                        74,
                        23,
                    ],
                    5,
                ),
                [2, 4, 7, 8, 9],
            )


if __name__ == "__main__":
    unittest.main()
