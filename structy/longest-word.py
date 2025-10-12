import unittest


# time:  O(n)
# space: O(m)
# where: n = length of sentence, m = length of longest word
def longest_word(sentence: str) -> str:
    longest = ""
    start = 0

    for i, char in enumerate(sentence):
        if char == " ":
            if i - start >= len(longest):
                longest = sentence[start:i]
            start = i + 1

    if len(sentence) - start >= len(longest):
        longest = sentence[start:]
    return longest


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(longest_word("what a wonderful world"), "wonderful")

    def test_01(self) -> None:
        self.assertEqual(longest_word("have a nice day"), "nice")

    def test_02(self) -> None:
        self.assertEqual(
            longest_word("the quick brown fox jumped over the lazy dog"), "jumped"
        )

    def test_03(self) -> None:
        self.assertEqual(longest_word("who did eat the ham"), "ham")

    def test_04(self) -> None:
        self.assertEqual(longest_word("potato"), "potato")


if __name__ == "__main__":
    unittest.main()
