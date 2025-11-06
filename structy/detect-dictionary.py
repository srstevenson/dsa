import unittest
from itertools import pairwise


# time:  O(nm + p)
# space: O(p)
# where: n = len(dictionary), m = max word length, p = len(alphabet)
def detect_dictionary(dictionary: list[str], alphabet: str) -> bool:
    indices = {char: idx for idx, char in enumerate(alphabet)}
    return all(
        _lexical_order(word_1, word_2, indices)
        for word_1, word_2 in pairwise(dictionary)
    )


def _lexical_order(word_1: str, word_2: str, indices: dict[str, int]) -> bool:
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
        dictionary = ["zoo", "tick", "tack", "door"]
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        self.assertTrue(detect_dictionary(dictionary, alphabet))

    def test_01(self) -> None:
        dictionary = ["zoo", "tack", "tick", "door"]
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        self.assertFalse(detect_dictionary(dictionary, alphabet))

    def test_02(self) -> None:
        dictionary = ["zoos", "zoo", "tick", "tack", "door"]
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        self.assertFalse(detect_dictionary(dictionary, alphabet))

    def test_03(self) -> None:
        dictionary = ["miles", "milestone", "proper", "process", "goal"]
        alphabet = "mnoijpqrshkltabcdefguvwzxy"
        self.assertTrue(detect_dictionary(dictionary, alphabet))

    def test_04(self) -> None:
        dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"]
        alphabet = "mnoijpqrshkltabcdefguvwzxy"
        self.assertTrue(detect_dictionary(dictionary, alphabet))

    def test_05(self) -> None:
        dictionary = [
            "miles",
            "milestone",
            "pint",
            "proper",
            "process",
            "goal",
            "apple",
        ]
        alphabet = "mnoijpqrshkltabcdefguvwzxy"
        self.assertFalse(detect_dictionary(dictionary, alphabet))


if __name__ == "__main__":
    unittest.main()
