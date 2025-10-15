import unittest


# time:  O(n)
# space: O(n)
# where: n = len(items)
def all_unique(items: list[str]) -> bool:
    return len(items) == len(set(items))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(all_unique(["q", "r", "s", "a"]))

    def test_01(self) -> None:
        self.assertFalse(all_unique(["q", "r", "s", "a", "r", "z"]))

    def test_02(self) -> None:
        self.assertTrue(all_unique(["red", "blue", "yellow", "green", "orange"]))

    def test_03(self) -> None:
        self.assertFalse(all_unique(["cat", "cat", "dog"]))

    def test_04(self) -> None:
        self.assertFalse(all_unique(["a", "u", "t", "u", "m", "n"]))


if __name__ == "__main__":
    unittest.main()
