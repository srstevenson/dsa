import unittest


# time:  O(n)
# space: O(1)
# where: n = len(string_2)
def is_subsequence(string_1: str, string_2: str) -> bool:
    idx_1 = idx_2 = 0
    while idx_1 < len(string_1) and idx_2 < len(string_2):
        if string_2[idx_2] == string_1[idx_1]:
            idx_1 += 1
        idx_2 += 1

    return idx_1 == len(string_1)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(is_subsequence("bde", "abcdef"))

    def test_01(self) -> None:
        self.assertFalse(is_subsequence("bda", "abcdef"))

    def test_02(self) -> None:
        self.assertTrue(is_subsequence("ser", "super"))

    def test_03(self) -> None:
        self.assertFalse(is_subsequence("serr", "super"))

    def test_04(self) -> None:
        self.assertTrue(is_subsequence("ama", "camera"))

    def test_05(self) -> None:
        self.assertTrue(is_subsequence("unfun", "unfortunate"))

    def test_06(self) -> None:
        self.assertFalse(is_subsequence("riverbed", "river"))

    def test_07(self) -> None:
        self.assertTrue(is_subsequence("river", "riverbed"))


if __name__ == "__main__":
    unittest.main()
