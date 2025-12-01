import unittest
from functools import cache


# time:  O(n²)
# space: O(n²)
# where: n = len(string)
def max_palin_subsequence(string: str) -> int:
    @cache
    def _max_palin_subsequence(left: int, right: int) -> int:
        if left > right:
            return 0
        if left == right:
            return 1
        if string[left] == string[right]:
            return 2 + _max_palin_subsequence(left + 1, right - 1)
        return max(
            _max_palin_subsequence(left + 1, right),
            _max_palin_subsequence(left, right - 1),
        )

    return _max_palin_subsequence(0, len(string) - 1)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(max_palin_subsequence("luwxult"), 5)

    def test_01(self) -> None:
        self.assertEqual(max_palin_subsequence("xyzaxxzy"), 6)

    def test_02(self) -> None:
        self.assertEqual(max_palin_subsequence("lol"), 3)

    def test_03(self) -> None:
        self.assertEqual(max_palin_subsequence("boabcdefop"), 3)

    def test_04(self) -> None:
        self.assertEqual(max_palin_subsequence("z"), 1)

    def test_05(self) -> None:
        self.assertEqual(max_palin_subsequence("chartreusepugvicefree"), 7)

    def test_06(self) -> None:
        self.assertEqual(
            max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty"), 15
        )

    def test_07(self) -> None:
        self.assertEqual(
            max_palin_subsequence(
                "enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe"
            ),
            31,
        )


if __name__ == "__main__":
    unittest.main()
