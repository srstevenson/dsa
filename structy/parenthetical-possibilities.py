import unittest


# time:  O(mᵏ n)
# space: O(mᵏ n)
# where: n = len(s), m = length of largest group, k = number of groups
def parenthetical_possibilities(s: str) -> list[str]:
    results: list[str] = []
    current: list[str] = []

    def _backtrack(idx: int) -> None:
        if idx == len(s):
            results.append("".join(current))
            return

        if s[idx] == "(":
            close_idx = s.find(")", idx)
            for j in range(idx + 1, close_idx):
                current.append(s[j])
                _backtrack(close_idx + 1)
                current.pop()
        else:
            current.append(s[idx])
            _backtrack(idx + 1)
            current.pop()

    _backtrack(0)
    return results


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(parenthetical_possibilities("x(mn)yz"), ["xmyz", "xnyz"])

    def test_01(self) -> None:
        self.assertEqual(
            parenthetical_possibilities("(qr)ab(stu)c"),
            ["qabsc", "qabtc", "qabuc", "rabsc", "rabtc", "rabuc"],
        )

    def test_02(self) -> None:
        self.assertEqual(parenthetical_possibilities("taco"), ["taco"])

    def test_03(self) -> None:
        self.assertEqual(parenthetical_possibilities(""), [""])

    def test_04(self) -> None:
        self.assertEqual(
            parenthetical_possibilities("(etc)(blvd)(cat)"),
            [
                "ebc",
                "eba",
                "ebt",
                "elc",
                "ela",
                "elt",
                "evc",
                "eva",
                "evt",
                "edc",
                "eda",
                "edt",
                "tbc",
                "tba",
                "tbt",
                "tlc",
                "tla",
                "tlt",
                "tvc",
                "tva",
                "tvt",
                "tdc",
                "tda",
                "tdt",
                "cbc",
                "cba",
                "cbt",
                "clc",
                "cla",
                "clt",
                "cvc",
                "cva",
                "cvt",
                "cdc",
                "cda",
                "cdt",
            ],
        )


if __name__ == "__main__":
    unittest.main()
