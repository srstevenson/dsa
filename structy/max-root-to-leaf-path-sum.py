import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def max_path_sum(root: Node | None) -> float:
    if not root:
        return float("-inf")

    if not root.left and not root.right:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


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

        self.assertEqual(max_path_sum(a), 18)

    def test_01(self) -> None:
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

        self.assertEqual(max_path_sum(a), 59)

    def test_02(self) -> None:
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

        self.assertEqual(max_path_sum(a), -8)

    def test_03(self) -> None:
        a = Node(42)

        self.assertEqual(max_path_sum(a), 42)


if __name__ == "__main__":
    unittest.main()
