import unittest
from itertools import combinations


# time:  O(n²)
# space: O(n²)
# where: n = len(elements)
def pairs(elements: list[str]) -> list[list[str]]:
    result: list[list[str]] = []
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            result.append([elements[i], elements[j]])  # noqa: PERF401
    return result


def pairs_itertools(elements: list[str]) -> list[list[str]]:
    return list(map(list, combinations(elements, r=2)))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        for solution in [pairs, pairs_itertools]:
            self.assertEqual(
                solution(["a", "b", "c"]), [["a", "b"], ["a", "c"], ["b", "c"]]
            )

    def test_01(self) -> None:
        for solution in [pairs, pairs_itertools]:
            self.assertEqual(
                solution(["a", "b", "c", "d"]),
                [
                    ["a", "b"],
                    ["a", "c"],
                    ["a", "d"],
                    ["b", "c"],
                    ["b", "d"],
                    ["c", "d"],
                ],
            )

    def test_02(self) -> None:
        for solution in [pairs, pairs_itertools]:
            self.assertEqual(
                solution(
                    ["cherry", "cranberry", "banana", "blueberry", "lime", "papaya"]
                ),
                [
                    ["cherry", "cranberry"],
                    ["cherry", "banana"],
                    ["cherry", "blueberry"],
                    ["cherry", "lime"],
                    ["cherry", "papaya"],
                    ["cranberry", "banana"],
                    ["cranberry", "blueberry"],
                    ["cranberry", "lime"],
                    ["cranberry", "papaya"],
                    ["banana", "blueberry"],
                    ["banana", "lime"],
                    ["banana", "papaya"],
                    ["blueberry", "lime"],
                    ["blueberry", "papaya"],
                    ["lime", "papaya"],
                ],
            )


if __name__ == "__main__":
    unittest.main()
