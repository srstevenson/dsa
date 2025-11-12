import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def binary_search_tree_includes(root: Node | None, target: int) -> bool:
    if not root:
        return False
    if target == root.val:
        return True
    if target < root.val:
        return binary_search_tree_includes(root.left, target)
    return binary_search_tree_includes(root.right, target)


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

        self.assertTrue(binary_search_tree_includes(a, 9))

    def test_01(self) -> None:
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

        self.assertFalse(binary_search_tree_includes(a, 15))

    def test_02(self) -> None:
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

        self.assertFalse(binary_search_tree_includes(a, 1))

    def test_03(self) -> None:
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

        self.assertTrue(binary_search_tree_includes(a, 12))

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

        self.assertFalse(binary_search_tree_includes(q, 55))

    def test_05(self) -> None:
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

        self.assertTrue(binary_search_tree_includes(q, 47))

    def test_06(self) -> None:
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

        self.assertFalse(binary_search_tree_includes(q, 49))

    def test_07(self) -> None:
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

        self.assertTrue(binary_search_tree_includes(q, 70))

    def test_08(self) -> None:
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

        self.assertFalse(binary_search_tree_includes(q, 100))


if __name__ == "__main__":
    unittest.main()
