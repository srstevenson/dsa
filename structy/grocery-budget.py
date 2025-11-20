import unittest


# time:  O(n 2ⁿ)
# space: O(n 2ⁿ)
# where: n = len(grocery_list)
def grocery_budget(grocery_list: list[tuple[str, int]], budget: int) -> list[list[str]]:
    result: list[list[str]] = []
    basket: list[str] = []

    def _backtrack(idx: int, budget: int) -> None:
        if idx == len(grocery_list):
            result.append(basket[:])
            return

        _backtrack(idx + 1, budget)

        item, price = grocery_list[idx]
        if budget < price:
            return

        basket.append(item)
        _backtrack(idx + 1, budget - price)
        basket.pop()

    _backtrack(0, budget)
    return result


class TestSolution(unittest.TestCase):
    def normalise(self, data: list[list[str]]) -> list[list[str]]:
        return [sorted(inner) for inner in data]

    def test_00(self) -> None:
        self.assertCountEqual(
            self.normalise(
                grocery_budget([("eggs", 5), ("milk", 3), ("butter", 3)], 7)
            ),
            self.normalise([["eggs"], ["butter", "milk"], ["milk"], ["butter"], []]),
        )

    def test_01(self) -> None:
        self.assertCountEqual(
            self.normalise(
                grocery_budget([("eggs", 5), ("milk", 3), ("butter", 3)], 20)
            ),
            self.normalise(
                [
                    ["butter", "milk", "eggs"],
                    ["milk", "eggs"],
                    ["butter", "eggs"],
                    ["eggs"],
                    ["butter", "milk"],
                    ["milk"],
                    ["butter"],
                    [],
                ]
            ),
        )

    def test_02(self) -> None:
        self.assertCountEqual(
            self.normalise(
                grocery_budget(
                    [("eggs", 5), ("milk", 3), ("butter", 3), ("garlic", 1)], 7
                )
            ),
            self.normalise(
                [
                    ["garlic", "eggs"],
                    ["eggs"],
                    ["garlic", "butter", "milk"],
                    ["butter", "milk"],
                    ["garlic", "milk"],
                    ["milk"],
                    ["garlic", "butter"],
                    ["butter"],
                    ["garlic"],
                    [],
                ]
            ),
        )

    def test_03(self) -> None:
        self.assertCountEqual(
            self.normalise(
                grocery_budget(
                    [
                        ("salt", 1),
                        ("apples", 5),
                        ("tofu", 7),
                        ("chicken", 4),
                        ("salmon", 10),
                    ],
                    9,
                )
            ),
            self.normalise(
                [
                    ["salt", "apples"],
                    ["chicken", "apples"],
                    ["apples"],
                    ["salt", "tofu"],
                    ["tofu"],
                    ["chicken", "salt"],
                    ["salt"],
                    ["chicken"],
                    [],
                ]
            ),
        )

    def test_04(self) -> None:
        self.assertCountEqual(
            self.normalise(
                grocery_budget(
                    [
                        ("apples", 5),
                        ("tofu", 7),
                        ("salt", 1),
                        ("chicken", 4),
                        ("salmon", 10),
                        ("thyme", 2),
                    ],
                    12,
                )
            ),
            self.normalise(
                [
                    ["tofu", "apples"],
                    ["thyme", "chicken", "salt", "apples"],
                    ["chicken", "salt", "apples"],
                    ["thyme", "salt", "apples"],
                    ["salt", "apples"],
                    ["thyme", "chicken", "apples"],
                    ["chicken", "apples"],
                    ["thyme", "apples"],
                    ["apples"],
                    ["chicken", "salt", "tofu"],
                    ["thyme", "salt", "tofu"],
                    ["salt", "tofu"],
                    ["chicken", "tofu"],
                    ["thyme", "tofu"],
                    ["tofu"],
                    ["thyme", "chicken", "salt"],
                    ["chicken", "salt"],
                    ["salmon", "salt"],
                    ["thyme", "salt"],
                    ["salt"],
                    ["thyme", "chicken"],
                    ["chicken"],
                    ["thyme", "salmon"],
                    ["salmon"],
                    ["thyme"],
                    [],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
