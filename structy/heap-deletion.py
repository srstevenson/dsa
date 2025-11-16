import unittest


class MinHeap:
    def __init__(self) -> None:
        self.values: list[int] = []

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

    # time:  O(log n)
    # space: O(1)
    # where: n = len(self.values)
    def extract_min(self) -> int | None:
        if not self.values:
            return None
        root_val = self.values[0]
        tail_val = self.values.pop()
        if len(self.values):
            self.values[0] = tail_val
            self._sift_down(0)
        return root_val

    def _sift_down(self, idx: int) -> None:
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            left_child_val = (
                self.values[left_child_idx]
                if left_child_idx < len(self.values)
                else float("inf")
            )
            right_child_val = (
                self.values[right_child_idx]
                if right_child_idx < len(self.values)
                else float("inf")
            )
            min_child_idx = (
                left_child_idx if left_child_val < right_child_val else right_child_idx
            )
            if (
                min_child_idx < len(self.values)
                and self.values[idx] > self.values[min_child_idx]
            ):
                self.values[idx], self.values[min_child_idx] = (
                    self.values[min_child_idx],
                    self.values[idx],
                )
                idx = min_child_idx
            else:
                break


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
        self.assertEqual(heap.extract_min(), 4)
        self.assertEqual(heap.extract_min(), 9)
        self.assertEqual(heap.extract_min(), 11)

    def test_01(self) -> None:
        heap = MinHeap()
        heap.insert(12)
        heap.insert(93)
        heap.insert(63)
        heap.insert(16)
        self.assertEqual(heap.extract_min(), 12)
        self.assertEqual(heap.extract_min(), 16)
        heap.insert(-500)
        heap.insert(21)
        heap.insert(11)
        heap.insert(43)
        heap.insert(-6)
        heap.insert(35)
        heap.insert(15)
        self.assertEqual(heap.extract_min(), -500)
        self.assertEqual(heap.extract_min(), -6)
        self.assertEqual(heap.extract_min(), 11)
        self.assertEqual(heap.extract_min(), 15)
        self.assertEqual(heap.extract_min(), 21)
        self.assertEqual(heap.extract_min(), 35)
        self.assertEqual(heap.extract_min(), 43)
        self.assertEqual(heap.extract_min(), 63)
        self.assertEqual(heap.extract_min(), 93)


if __name__ == "__main__":
    unittest.main()
