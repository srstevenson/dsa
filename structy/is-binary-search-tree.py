import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def is_binary_search_tree(root: Node) -> bool:
    left_is_bst = _is_bst(root.left, infimum=None, supremum=root.val)
    right_is_bst = _is_bst(root.right, infimum=root.val, supremum=None)
    return left_is_bst and right_is_bst


def _is_bst(root: Node | None, *, infimum: int | None, supremum: int | None) -> bool:
    if not root:
        return True
    if infimum is not None and root.val < infimum:
        return False
    if supremum is not None and root.val >= supremum:
        return False
    left_is_bst = _is_bst(root.left, infimum=infimum, supremum=root.val)
    right_is_bst = _is_bst(root.right, infimum=root.val, supremum=supremum)
    return left_is_bst and right_is_bst


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(12)
        b = Node(5)
        c = Node(18)
        d = Node(3)
        e = Node(9)
        f = Node(19)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertTrue(is_binary_search_tree(a))

    def test_01(self) -> None:
        a = Node(12)
        b = Node(5)
        c = Node(18)
        d = Node(3)
        e = Node(15)
        f = Node(19)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertFalse(is_binary_search_tree(a))

    def test_02(self) -> None:
        a = Node(12)
        b = Node(5)
        c = Node(15)
        d = Node(3)
        e = Node(9)
        f = Node(19)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertTrue(is_binary_search_tree(a))

    def test_03(self) -> None:
        a = Node(12)
        b = Node(5)
        c = Node(10)
        d = Node(3)
        e = Node(9)
        f = Node(19)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertFalse(is_binary_search_tree(a))

    def test_04(self) -> None:
        q = Node(54)
        r = Node(42)
        s = Node(70)
        t = Node(31)
        u = Node(50)
        v = Node(72)
        w = Node(47)
        x = Node(90)

        q.left = r
        q.right = s
        r.left = t
        r.right = u
        s.right = v
        u.left = w
        v.right = x

        self.assertTrue(is_binary_search_tree(q))


if __name__ == "__main__":
    unittest.main()
