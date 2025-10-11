import unittest
from collections import deque


class Node:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def bottom_right_value(root: Node) -> int | str:
    current = root
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return current.val


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(3)
        b = Node(11)
        c = Node(10)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertEqual(bottom_right_value(a), 1)

    def test_01(self) -> None:
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(6)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h

        self.assertEqual(bottom_right_value(a), 6)

    def test_02(self) -> None:
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(6)
        i = Node(7)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        self.assertEqual(bottom_right_value(a), 7)

    def test_03(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.right = d
        d.left = e
        e.right = f

        self.assertEqual(bottom_right_value(a), "f")

    def test_04(self) -> None:
        a = Node(42)

        self.assertEqual(bottom_right_value(a), 42)


if __name__ == "__main__":
    unittest.main()
