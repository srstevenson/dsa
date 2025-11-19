import unittest


# time:  O(n n!)
# space: O(n n!)
# where: n = len(items)
def permutations[T](items: list[T]) -> list[list[T]]:
    result: list[list[T]] = []
    current: list[T] = []
    used = [False for _ in items]

    def _backtrack() -> None:
        if len(current) == len(items):
            result.append(current[:])
            return

        for idx in range(len(items)):
            if used[idx]:
                continue
            current.append(items[idx])
            used[idx] = True
            _backtrack()
            current.pop()
            used[idx] = False

    _backtrack()
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertCountEqual(
            permutations(["a", "b", "c"]),
            [
                ["a", "b", "c"],
                ["b", "a", "c"],
                ["b", "c", "a"],
                ["a", "c", "b"],
                ["c", "a", "b"],
                ["c", "b", "a"],
            ],
        )

    def test_01(self) -> None:
        self.assertCountEqual(
            permutations(["red", "blue"]), [["red", "blue"], ["blue", "red"]]
        )

    def test_02(self) -> None:
        self.assertCountEqual(
            permutations([8, 2, 1, 4]),
            [
                [8, 2, 1, 4],
                [2, 8, 1, 4],
                [2, 1, 8, 4],
                [2, 1, 4, 8],
                [8, 1, 2, 4],
                [1, 8, 2, 4],
                [1, 2, 8, 4],
                [1, 2, 4, 8],
                [8, 1, 4, 2],
                [1, 8, 4, 2],
                [1, 4, 8, 2],
                [1, 4, 2, 8],
                [8, 2, 4, 1],
                [2, 8, 4, 1],
                [2, 4, 8, 1],
                [2, 4, 1, 8],
                [8, 4, 2, 1],
                [4, 8, 2, 1],
                [4, 2, 8, 1],
                [4, 2, 1, 8],
                [8, 4, 1, 2],
                [4, 8, 1, 2],
                [4, 1, 8, 2],
                [4, 1, 2, 8],
            ],
        )

    def test_03(self) -> None:
        self.assertEqual(permutations([]), [[]])


if __name__ == "__main__":
    unittest.main()
