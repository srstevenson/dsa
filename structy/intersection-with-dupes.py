import unittest
from collections import Counter


# time:  O(n+m)
# space: O(n+m)
# where: n = len(a), b = len(b)
def intersection_with_dupes(
    a: list[int] | list[str], b: list[int] | list[str]
) -> list[int | str]:
    result: list[int | str] = []
    b_counts = Counter(b)
    for char, a_count in Counter(a).items():
        result.extend(char for _ in range(min(a_count, b_counts[char])))
    return result


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            intersection_with_dupes(["a", "b", "c", "b"], ["x", "y", "b", "b"]),
            ["b", "b"],
        )

    def test_01(self) -> None:
        self.assertEqual(
            intersection_with_dupes(["q", "b", "m", "s", "s", "s"], ["s", "m", "s"]),
            ["m", "s", "s"],
        )

    def test_02(self) -> None:
        self.assertEqual(intersection_with_dupes(["p", "r", "r", "r"], ["r"]), ["r"])

    def test_03(self) -> None:
        self.assertEqual(intersection_with_dupes(["r"], ["p", "r", "r", "r"]), ["r"])

    def test_04(self) -> None:
        self.assertEqual(
            intersection_with_dupes(["t", "v", "u"], ["g", "e", "d", "f"]), []
        )

    def test_05(self) -> None:
        self.assertEqual(
            intersection_with_dupes(
                ["a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a"]
            ),
            ["a", "a", "a", "a"],
        )

    def test_06(self) -> None:
        a: list[int] = []
        b: list[int] = []
        for i in range(150000):
            a.append(i)
            b.append(i)

        result = intersection_with_dupes(a, b)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 149999)
        self.assertEqual(len(result), 150000)


if __name__ == "__main__":
    unittest.main()
