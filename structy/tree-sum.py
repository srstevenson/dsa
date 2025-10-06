import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def tree_sum(root: Node | None) -> int:
    if not root:
        return 0

    total = 0
    stack = [root]
    while stack:
        current = stack.pop()
        total += current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return total


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

        self.assertEqual(tree_sum(a), 21)

    def test_01(self) -> None:
        a = Node(1)
        b = Node(6)
        c = Node(0)
        d = Node(3)
        e = Node(-6)
        f = Node(2)
        g = Node(2)
        h = Node(2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(tree_sum(a), 10)

    def test_02(self) -> None:
        self.assertEqual(tree_sum(None), 0)


if __name__ == "__main__":
    unittest.main()
