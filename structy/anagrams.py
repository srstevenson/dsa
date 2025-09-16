import unittest
from collections import Counter


# time:  O(n + m)
# space: O(n + m)
# where: n = len(s1), m = len(s2)
def anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(anagrams("restful", "fluster"))

    def test_01(self) -> None:
        self.assertFalse(anagrams("cats", "tocs"))

    def test_02(self) -> None:
        self.assertTrue(anagrams("monkeyswrite", "newyorktimes"))

    def test_03(self) -> None:
        self.assertFalse(anagrams("paper", "reapa"))

    def test_04(self) -> None:
        self.assertTrue(anagrams("elbow", "below"))

    def test_05(self) -> None:
        self.assertFalse(anagrams("tax", "taxi"))

    def test_06(self) -> None:
        self.assertFalse(anagrams("taxi", "tax"))

    def test_07(self) -> None:
        self.assertTrue(anagrams("night", "thing"))

    def test_08(self) -> None:
        self.assertFalse(anagrams("abbc", "aabc"))

    def test_09(self) -> None:
        self.assertFalse(anagrams("po", "popp"))

    def test_10(self) -> None:
        self.assertFalse(anagrams("pp", "oo"))


if __name__ == "__main__":
    unittest.main()
