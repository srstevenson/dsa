import unittest


class MinHeap:
    def __init__(self) -> None:
        self.values: list[int] = []

    # time:  O(log n)
    # space: O(1)
    # where: n = len(self.values)
    def insert(self, val: int) -> None:
        self.values.append(val)
        self._sift_up(len(self.values) - 1)

    def _sift_up(self, idx: int) -> None:
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.values[parent_idx] > self.values[idx]:
            self.values[parent_idx], self.values[idx] = (
                self.values[idx],
                self.values[parent_idx],
            )
            idx = parent_idx
            parent_idx = (idx - 1) // 2


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        heap = MinHeap()
        heap.insert(12)
        heap.insert(13)
        heap.insert(11)
        heap.insert(4)
        heap.insert(20)
        heap.insert(9)
        heap.insert(22)
        heap.insert(14)

        self.assertEqual(heap.values, [4, 11, 9, 13, 20, 12, 22, 14])

    def test_01(self) -> None:
        heap = MinHeap()
        heap.insert(12)
        heap.insert(93)
        heap.insert(63)
        heap.insert(16)
        heap.insert(-500)
        heap.insert(21)
        heap.insert(11)
        heap.insert(43)
        heap.insert(-6)
        heap.insert(35)
        heap.insert(15)
        heap.insert(37)
        heap.insert(29)
        heap.insert(-501)
        heap.insert(80)

        self.assertEqual(
            heap.values,
            [-501, -6, -500, 12, 15, 29, 11, 93, 43, 35, 16, 63, 37, 21, 80],
        )


if __name__ == "__main__":
    unittest.main()
