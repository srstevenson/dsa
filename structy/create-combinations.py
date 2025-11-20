import unittest


# time:  O(n n! / ((n-k)! k!))
# space: O(n n! / ((n-k)! k!))
# where: n = len(items)
def create_combinations[T](items: list[T], k: int) -> list[list[T]]:
    result: list[list[T]] = []
    current: list[T] = []

    def _backtrack(idx: int) -> None:
        if len(current) + (len(items) - idx) < k:
            return

        if len(current) == k:
            result.append(current[:])
            return

        if idx == len(items):
            return

        _backtrack(idx + 1)

        current.append(items[idx])
        _backtrack(idx + 1)
        current.pop()

    _backtrack(0)
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertCountEqual(
            create_combinations(["a", "b", "c"], 2),
            [["a", "b"], ["a", "c"], ["b", "c"]],
        )

    def test_01(self) -> None:
        self.assertCountEqual(
            create_combinations(["q", "r", "s", "t"], 2),
            [["q", "r"], ["q", "s"], ["q", "t"], ["r", "s"], ["r", "t"], ["s", "t"]],
        )

    def test_02(self) -> None:
        self.assertCountEqual(
            create_combinations(["q", "r", "s", "t"], 3),
            [["q", "r", "s"], ["q", "r", "t"], ["q", "s", "t"], ["r", "s", "t"]],
        )

    def test_03(self) -> None:
        self.assertCountEqual(create_combinations([1, 28, 94], 3), [[1, 28, 94]])


if __name__ == "__main__":
    unittest.main()
