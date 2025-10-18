import unittest


class Node:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def leaf_list(root: Node | None) -> list[int | str]:
    if not root:
        return []

    leaves: list[int | str] = []
    stack = [root]
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            leaves.append(node.val)
        else:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return leaves


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
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

        self.assertEqual(leaf_list(a), ["d", "e", "f"])

    def test_01(self) -> None:
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
        f.right = h

        self.assertEqual(leaf_list(a), ["d", "g", "h"])

    def test_02(self) -> None:
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

        self.assertEqual(leaf_list(a), [20, 1, 3, 54])

    def test_03(self) -> None:
        x = Node("x")

        self.assertEqual(leaf_list(x), ["x"])

    def test_04(self) -> None:
        self.assertEqual(leaf_list(None), [])


if __name__ == "__main__":
    unittest.main()
