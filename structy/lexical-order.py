import unittest


# time:  O(min(n, m) + p)
# space: O(p)
# where: n = len(word_1), m = len(word_2), p = len(alphabet)
def lexical_order(word_1: str, word_2: str, alphabet: str) -> bool:
    indices = {char: idx for idx, char in enumerate(alphabet)}
    idx_1 = idx_2 = 0
    while idx_1 < len(word_1) and idx_2 < len(word_2):
        if indices[word_1[idx_1]] < indices[word_2[idx_2]]:
            return True
        if indices[word_1[idx_1]] > indices[word_2[idx_2]]:
            return False
        idx_1 += 1
        idx_2 += 1
    return len(word_1) <= len(word_2)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(lexical_order("apple", "dock", alphabet))

    def test_01(self) -> None:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(lexical_order("apple", "ample", alphabet))

    def test_02(self) -> None:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(lexical_order("app", "application", alphabet))

    def test_03(self) -> None:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(lexical_order("backs", "backdoor", alphabet))

    def test_04(self) -> None:
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        self.assertTrue(lexical_order("zoo", "dinner", alphabet))

    def test_05(self) -> None:
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        self.assertFalse(lexical_order("leaper", "leap", alphabet))

    def test_06(self) -> None:
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        self.assertTrue(lexical_order("backs", "backdoor", alphabet))

    def test_07(self) -> None:
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        self.assertTrue(lexical_order("semper", "semper", alphabet))


if __name__ == "__main__":
    unittest.main()
