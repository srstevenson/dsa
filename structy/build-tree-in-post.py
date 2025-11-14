import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def build_tree_in_post(in_order: list[str], post_order: list[str]) -> Node | None:
    in_value_map = {value: idx for idx, value in enumerate(in_order)}
    return _build_tree_in_post(
        in_order, post_order, in_value_map, 0, len(in_order) - 1, 0, len(post_order) - 1
    )


def _build_tree_in_post(  # noqa: PLR0913
    in_order: list[str],
    post_order: list[str],
    in_value_map: dict[str, int],
    in_min_idx: int,
    in_max_idx: int,
    post_min_idx: int,
    post_max_idx: int,
) -> Node | None:
    if in_min_idx > in_max_idx:
        return None

    root = Node(root_val := post_order[post_max_idx])
    mid = in_value_map[root_val]
    left_size = mid - in_min_idx
    root.left = _build_tree_in_post(
        in_order,
        post_order,
        in_value_map,
        in_min_idx,
        mid - 1,
        post_min_idx,
        post_min_idx + left_size - 1,
    )
    root.right = _build_tree_in_post(
        in_order,
        post_order,
        in_value_map,
        mid + 1,
        in_max_idx,
        post_min_idx + left_size,
        post_max_idx - 1,
    )
    return root


class TestSolution(unittest.TestCase):
    def post_order(self, root: Node | None) -> list[str]:
        values: list[str] = []

        def _post_order(root: Node | None) -> None:
            if root:
                _post_order(root.left)
                _post_order(root.right)
                values.append(root.val)

        _post_order(root)
        return values

    def test_00(self) -> None:
        self.assertEqual(
            self.post_order(build_tree_in_post(["y", "x", "z"], ["y", "z", "x"])),
            ["y", "z", "x"],
        )

    def test_01(self) -> None:
        self.assertEqual(
            self.post_order(
                build_tree_in_post(
                    ["d", "b", "e", "a", "f", "c", "g"],
                    ["d", "e", "b", "f", "g", "c", "a"],
                )
            ),
            ["d", "e", "b", "f", "g", "c", "a"],
        )

    def test_02(self) -> None:
        self.assertEqual(
            self.post_order(
                build_tree_in_post(
                    ["d", "b", "g", "e", "h", "a", "c", "f"],
                    ["d", "g", "h", "e", "b", "f", "c", "a"],
                )
            ),
            ["d", "g", "h", "e", "b", "f", "c", "a"],
        )

    def test_03(self) -> None:
        self.assertEqual(
            self.post_order(build_tree_in_post(["m", "n"], ["m", "n"])), ["m", "n"]
        )

    def test_04(self) -> None:
        self.assertEqual(
            self.post_order(build_tree_in_post(["n", "m"], ["m", "n"])), ["m", "n"]
        )


if __name__ == "__main__":
    unittest.main()
