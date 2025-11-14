import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def build_tree_in_pre(in_order: list[str], pre_order: list[str]) -> Node | None:
    in_value_map = {value: idx for idx, value in enumerate(in_order)}
    return _build_tree_in_pre(
        in_order, pre_order, in_value_map, 0, len(in_order) - 1, 0, len(pre_order) - 1
    )


def _build_tree_in_pre(  # noqa: PLR0913
    in_order: list[str],
    pre_order: list[str],
    in_value_map: dict[str, int],
    in_min_idx: int,
    in_max_idx: int,
    pre_min_idx: int,
    pre_max_idx: int,
) -> Node | None:
    if in_min_idx > in_max_idx:
        return None

    root = Node(root_val := pre_order[pre_min_idx])
    mid = in_value_map[root_val]
    left_size = mid - in_min_idx
    root.left = _build_tree_in_pre(
        in_order,
        pre_order,
        in_value_map,
        in_min_idx,
        mid - 1,
        pre_min_idx + 1,
        pre_min_idx + left_size,
    )
    root.right = _build_tree_in_pre(
        in_order,
        pre_order,
        in_value_map,
        mid + 1,
        in_max_idx,
        pre_min_idx + left_size + 1,
        pre_max_idx,
    )
    return root


class TestSolution(unittest.TestCase):
    def pre_order(self, root: Node | None) -> list[str]:
        values: list[str] = []

        def _pre_order(root: Node | None) -> None:
            if root:
                values.append(root.val)
                _pre_order(root.left)
                _pre_order(root.right)

        _pre_order(root)
        return values

    def test_00(self) -> None:
        self.assertEqual(
            self.pre_order(build_tree_in_pre(["z", "y", "x"], ["y", "z", "x"])),
            ["y", "z", "x"],
        )

    def test_01(self) -> None:
        self.assertEqual(
            self.pre_order(build_tree_in_pre(["y", "z", "x"], ["y", "x", "z"])),
            ["y", "x", "z"],
        )

    def test_02(self) -> None:
        self.assertEqual(
            self.pre_order(
                build_tree_in_pre(
                    ["d", "b", "g", "e", "h", "a", "c", "f"],
                    ["a", "b", "d", "e", "g", "h", "c", "f"],
                )
            ),
            ["a", "b", "d", "e", "g", "h", "c", "f"],
        )

    def test_03(self) -> None:
        self.assertEqual(
            self.pre_order(
                build_tree_in_pre(
                    ["t", "u", "s", "q", "r", "p"], ["u", "t", "s", "r", "q", "p"]
                )
            ),
            ["u", "t", "s", "r", "q", "p"],
        )

    def test_04(self) -> None:
        self.assertEqual(
            self.pre_order(
                build_tree_in_pre(
                    ["m", "l", "q", "o", "r", "n", "s", "p", "t"],
                    ["l", "m", "n", "o", "q", "r", "p", "s", "t"],
                )
            ),
            ["l", "m", "n", "o", "q", "r", "p", "s", "t"],
        )


if __name__ == "__main__":
    unittest.main()
