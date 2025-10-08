import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def tree_min_value(root: Node) -> int:
    min_value = root.val
    stack = [root]
    while stack:
        current = stack.pop()
        min_value = min(current.val, min_value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return min_value


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

        self.assertEqual(tree_min_value(a), -2)

    def test_01(self) -> None:
        a = Node(5)
        b = Node(11)
        c = Node(3)
        d = Node(4)
        e = Node(14)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertEqual(tree_min_value(a), 3)

    def test_02(self) -> None:
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(tree_min_value(a), -13)

    def test_03(self) -> None:
        a = Node(42)

        self.assertEqual(tree_min_value(a), 42)


if __name__ == "__main__":
    unittest.main()
