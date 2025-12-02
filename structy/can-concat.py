import unittest
from functools import cache


# time:  O(nm)
# space: O(n)
# where: n = len(s), m = len(words)
def can_concat(s: str, words: list[str]) -> bool:
    @cache
    def _can_concat(idx: int) -> bool:
        return idx == len(s) or any(
            s.startswith(w, idx) and _can_concat(idx + len(w)) for w in words
        )

    return _can_concat(0)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(can_concat("oneisnone", ["one", "none", "is"]))

    def test_01(self) -> None:
        self.assertFalse(can_concat("oneisnone", ["on", "e", "is"]))

    def test_02(self) -> None:
        self.assertTrue(can_concat("oneisnone", ["on", "e", "is", "n"]))

    def test_03(self) -> None:
        self.assertTrue(can_concat("foodisgood", ["is", "g", "ood", "f"]))

    def test_04(self) -> None:
        self.assertFalse(can_concat("santahat", ["santah", "hat"]))

    def test_05(self) -> None:
        self.assertTrue(can_concat("santahat", ["santah", "san", "hat", "tahat"]))

    def test_06(self) -> None:
        self.assertFalse(
            can_concat(
                "rrrrrrrrrrrrrrrrrrrrrrrrrrx",
                ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"],
            )
        )

    def test_07(self) -> None:
        self.assertTrue(can_concat("fooisgood", ["foo", "is", "g", "ood", "f"]))


if __name__ == "__main__":
    unittest.main()
