import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def has_path_sum(root: Node | None, target: int) -> bool:
    if not root:
        return False
    if root.left or root.right:
        return has_path_sum(root.left, target - root.val) or has_path_sum(
            root.right, target - root.val
        )
    return target == root.val


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertTrue(has_path_sum(a, 8))

    def test_01(self) -> None:
        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertTrue(has_path_sum(a, 12))

    def test_02(self) -> None:
        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertFalse(has_path_sum(a, 7))

    def test_03(self) -> None:
        a = Node(5)
        b = Node(11)
        c = Node(54)
        d = Node(20)
        e = Node(15)
        f = Node(1)
        g = Node(3)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = f
        e.right = g

        self.assertFalse(has_path_sum(a, 16))

    def test_04(self) -> None:
        a = Node(5)
        b = Node(11)
        c = Node(54)
        d = Node(20)
        e = Node(15)
        f = Node(1)
        g = Node(3)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = f
        e.right = g

        self.assertTrue(has_path_sum(a, 32))

    def test_05(self) -> None:
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(0)
        f = Node(-13)
        g = Node(-1)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertTrue(has_path_sum(a, -10))

    def test_06(self) -> None:
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(0)
        f = Node(-13)
        g = Node(-1)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertFalse(has_path_sum(a, -5))

    def test_07(self) -> None:
        a = Node(42)

        self.assertTrue(has_path_sum(a, 42))


if __name__ == "__main__":
    unittest.main()
