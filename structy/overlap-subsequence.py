import unittest
from functools import cache


# time:  O(nm)
# space: O(nm)
# where: n = len(string_1), m = len(string_2)
def overlap_subsequence(string_1: str, string_2: str) -> int:
    @cache
    def _overlap_subsequence(idx1: int, idx2: int) -> int:
        if idx1 == len(string_1) or idx2 == len(string_2):
            return 0
        if string_1[idx1] == string_2[idx2]:
            return 1 + _overlap_subsequence(idx1 + 1, idx2 + 1)
        return max(
            _overlap_subsequence(idx1 + 1, idx2), _overlap_subsequence(idx1, idx2 + 1)
        )

    return _overlap_subsequence(0, 0)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(overlap_subsequence("dogs", "daogt"), 3)

    def test_01(self) -> None:
        self.assertEqual(overlap_subsequence("xcyats", "criaotsi"), 4)

    def test_02(self) -> None:
        self.assertEqual(overlap_subsequence("xfeqortsver", "feeeuavoeqr"), 5)

    def test_03(self) -> None:
        self.assertEqual(
            overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave"), 11
        )

    def test_04(self) -> None:
        self.assertEqual(
            overlap_subsequence(
                "mumblecorebeardleggingsauthenticunicorn",
                "succulentspughumblemeditationlocavore",
            ),
            15,
        )


if __name__ == "__main__":
    unittest.main()
