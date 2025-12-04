import unittest
from functools import cache


# time:  O(nm)
# space: O(n)
# where: n = len(compound), m = len(elements)
def count_compounds(compound: str, elements: list[str]) -> int:
    @cache
    def _count_compounds(idx: int) -> int:
        if idx == len(compound):
            return 1

        return sum(
            _count_compounds(idx + len(element))
            for element in elements
            if compound.startswith(element.lower(), idx)
        )

    return _count_compounds(0)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(
            count_compounds(
                "neco", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            ),
            2,
        )

    def test_01(self) -> None:
        self.assertEqual(
            count_compounds(
                "nerco", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            ),
            0,
        )

    def test_02(self) -> None:
        self.assertEqual(
            count_compounds(
                "sir", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            ),
            1,
        )

    def test_03(self) -> None:
        self.assertEqual(
            count_compounds("hocli", ["C", "Cl", "I", "Ho", "Li", "La", "H", "O"]), 4
        )

    def test_04(self) -> None:
        self.assertEqual(
            count_compounds(
                "noses", ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"]
            ),
            0,
        )

    def test_05(self) -> None:
        self.assertEqual(
            count_compounds(
                "onbeinos",
                ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"],
            ),
            2,
        )

    def test_06(self) -> None:
        self.assertEqual(
            count_compounds(
                "necoonbeinos",
                ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"],
            ),
            4,
        )

    def test_07(self) -> None:
        self.assertEqual(
            count_compounds(
                "cocococococococococococococococococococococococococococococox",
                ["Ne", "O", "Be", "I", "N", "Os", "Si", "S", "Co", "C", "Ir"],
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
