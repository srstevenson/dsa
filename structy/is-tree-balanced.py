import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def is_tree_balanced(root: Node | None) -> bool:
    return _balanced_height(root) is not None


def _balanced_height(root: Node | None) -> int | None:
    if not root:
        return 0
    if (left_height := _balanced_height(root.left)) is None:
        return None
    if (right_height := _balanced_height(root.right)) is None:
        return None
    if abs(left_height - right_height) > 1:
        return None
    return 1 + max(left_height, right_height)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")

        a.left = b
        a.right = c

        self.assertTrue(is_tree_balanced(a))

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.left = b
        a.right = c
        b.right = d

        self.assertTrue(is_tree_balanced(a))

    def test_02(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")

        a.right = b
        b.right = c

        self.assertFalse(is_tree_balanced(a))

    def test_03(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertTrue(is_tree_balanced(a))

    def test_04(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        self.assertTrue(is_tree_balanced(a))

    def test_05(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        c.right = e
        d.left = f

        self.assertFalse(is_tree_balanced(a))

    def test_06(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        g.right = h

        self.assertFalse(is_tree_balanced(a))

    def test_07(self) -> None:
        a = Node("a")

        self.assertTrue(is_tree_balanced(a))

    def test_08(self) -> None:
        self.assertTrue(is_tree_balanced(None))


if __name__ == "__main__":
    unittest.main()
