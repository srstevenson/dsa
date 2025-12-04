import unittest
from functools import cache


# time:  O(nm)
# space: O(n)
# where: n = len(compound), m = len(elements)
def valid_compound(compound: str, elements: list[str]) -> bool:
    @cache
    def _valid_compound(idx: int) -> bool:
        return idx == len(compound) or any(
            compound.startswith(element.lower(), idx)
            and _valid_compound(idx + len(element))
            for element in elements
        )

    return _valid_compound(0)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertTrue(
            valid_compound(
                "neco", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            )
        )

    def test_01(self) -> None:
        self.assertFalse(
            valid_compound(
                "nerco", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            )
        )

    def test_02(self) -> None:
        self.assertTrue(
            valid_compound(
                "sir", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            )
        )

    def test_03(self) -> None:
        self.assertFalse(
            valid_compound(
                "noses", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            )
        )

    def test_04(self) -> None:
        self.assertTrue(
            valid_compound(
                "onbeinos",
                ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"],
            )
        )

    def test_05(self) -> None:
        self.assertFalse(
            valid_compound(
                "cocococococococococococococococococococococococococococococox",
                ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"],
            )
        )


if __name__ == "__main__":
    unittest.main()
