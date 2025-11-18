import unittest
from itertools import combinations


# time:  O(2ⁿn)
# space: O(2ⁿn)
# where: n = len(elements)
def subsets(elements: list[str]) -> list[list[str]]:
    result: list[list[str]] = []
    current: list[str] = []

    def _backtrack(idx: int) -> None:
        if idx == len(elements):
            result.append(current[:])
            return

        _backtrack(idx + 1)

        current.append(elements[idx])
        _backtrack(idx + 1)
        current.pop()

    _backtrack(0)
    return result


# time:  O(2ⁿ)
# space: O(2ⁿ)
# where: n = len(elements)
def subsets_itertools(elements: list[str]) -> list[list[str]]:
    return [
        list(combination)
        for k in range(len(elements) + 1)
        for combination in combinations(elements, k)
    ]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        for solution in [subsets, subsets_itertools]:
            self.assertCountEqual(solution(["a", "b"]), [[], ["b"], ["a"], ["a", "b"]])

    def test_01(self) -> None:
        for solution in [subsets, subsets_itertools]:
            self.assertCountEqual(
                solution(["a", "b", "c"]),
                [
                    [],
                    ["c"],
                    ["b"],
                    ["b", "c"],
                    ["a"],
                    ["a", "c"],
                    ["a", "b"],
                    ["a", "b", "c"],
                ],
            )

    def test_02(self) -> None:
        for solution in [subsets, subsets_itertools]:
            self.assertCountEqual(solution(["x"]), [[], ["x"]])

    def test_03(self) -> None:
        for solution in [subsets, subsets_itertools]:
            self.assertCountEqual(solution([]), [[]])

    def test_04(self) -> None:
        for solution in [subsets, subsets_itertools]:
            self.assertCountEqual(
                solution(["q", "r", "s", "t"]),
                [
                    [],
                    ["t"],
                    ["s"],
                    ["s", "t"],
                    ["r"],
                    ["r", "t"],
                    ["r", "s"],
                    ["r", "s", "t"],
                    ["q"],
                    ["q", "t"],
                    ["q", "s"],
                    ["q", "s", "t"],
                    ["q", "r"],
                    ["q", "r", "t"],
                    ["q", "r", "s"],
                    ["q", "r", "s", "t"],
                ],
            )


if __name__ == "__main__":
    unittest.main()
