import unittest
from heapq import heappop, heappush


# time:  O(n log n)
# space: O(1)
# where: n = len(numbers)
def kth_largest_sort(numbers: list[int], k: int) -> int:
    numbers.sort()
    return numbers[-k]


# time:  O(n log k)
# space: O(k)
# where: n = len(numbers)
def kth_largest_heap(numbers: list[int], k: int) -> int:
    heap: list[int] = []
    for number in numbers:
        heappush(heap, number)
        if len(heap) > k:
            heappop(heap)
    return heappop(heap)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        for solution in [kth_largest_heap, kth_largest_sort]:
            self.assertEqual(solution([9, 2, 6, 6, 1, 5, 8, 7], 3), 7)

    def test_01(self) -> None:
        for solution in [kth_largest_heap, kth_largest_sort]:
            self.assertEqual(solution([9, 2, 6, 6, 1, 5, 8, 7], 4), 6)

    def test_02(self) -> None:
        for solution in [kth_largest_heap, kth_largest_sort]:
            self.assertEqual(solution([9, 2, 6, 6, 1, 5, 8, 7], 5), 6)

    def test_03(self) -> None:
        for solution in [kth_largest_heap, kth_largest_sort]:
            self.assertEqual(solution([10, 1, 8, 5, 2, 4], 2), 8)

    def test_04(self) -> None:
        numbers = [
            4,
            5,
            85,
            77,
            47,
            80,
            37,
            42,
            3,
            6,
            62,
            33,
            69,
            68,
            16,
            20,
            83,
            39,
            14,
            58,
            75,
            35,
            72,
            36,
            19,
            18,
            66,
            61,
            41,
            79,
            28,
            43,
            7,
            24,
            40,
            53,
            32,
            12,
        ]
        for solution in [kth_largest_heap, kth_largest_sort]:
            self.assertEqual(solution(numbers, 9), 68)

    def test_05(self) -> None:
        numbers = [
            4,
            5,
            85,
            77,
            47,
            80,
            37,
            42,
            3,
            6,
            62,
            33,
            69,
            68,
            16,
            20,
            83,
            39,
            14,
            58,
            75,
            35,
            72,
            36,
            19,
            18,
            66,
            61,
            41,
            79,
            28,
            43,
            7,
            24,
            40,
            53,
            32,
            12,
        ]
        for solution in [kth_largest_heap, kth_largest_sort]:
            self.assertEqual(solution(numbers, 5), 77)


if __name__ == "__main__":
    unittest.main()
