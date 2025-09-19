import unittest


# time:  O(nm)
# space: O(nm)
# where: n = number of groups, m = maximum group size
def uncompress(s: str) -> str:
    result: list[str] = []
    i = j = 0

    while j < len(s):
        while s[j].isdigit():
            j += 1
        number = int(s[i:j])
        char = s[j]
        result.append(char * number)
        j += 1
        i = j

    return "".join(result)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(uncompress("2c3a1t"), "ccaaat")

    def test_01(self) -> None:
        self.assertEqual(uncompress("4s2b"), "ssssbb")

    def test_02(self) -> None:
        self.assertEqual(uncompress("2p1o5p"), "ppoppppp")

    def test_03(self) -> None:
        self.assertEqual(uncompress("3n12e2z"), "nnneeeeeeeeeeeezz")

    def test_04(self) -> None:
        self.assertEqual(
            uncompress("127y"),
            "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
        )


if __name__ == "__main__":
    unittest.main()
