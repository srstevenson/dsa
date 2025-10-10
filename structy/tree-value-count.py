import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def tree_value_count(root: Node | None, target: int) -> int:
    count = 0
    if not root:
        return count

    stack = [root]
    while stack:
        current = stack.pop()
        if current.val == target:
            count += 1
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return count


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertEqual(tree_value_count(a, 6), 3)

    def test_01(self) -> None:
        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        self.assertEqual(tree_value_count(a, 12), 2)

    def test_02(self) -> None:
        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(tree_value_count(a, 1), 4)

    def test_03(self) -> None:
        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(tree_value_count(a, 9), 0)

    def test_04(self) -> None:
        self.assertEqual(tree_value_count(None, 42), 0)


if __name__ == "__main__":
    unittest.main()
