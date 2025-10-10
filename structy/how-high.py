import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def how_high(root: Node | None) -> int:
    if not root:
        return -1
    return 1 + max(how_high(root.left), how_high(root.right))


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

        self.assertEqual(how_high(a), 2)

    def test_01(self) -> None:
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

        self.assertEqual(how_high(a), 3)

    def test_02(self) -> None:
        a = Node("a")
        c = Node("c")

        a.right = c

        self.assertEqual(how_high(a), 1)

    def test_03(self) -> None:
        a = Node("a")

        self.assertEqual(how_high(a), 0)

    def test_04(self) -> None:
        self.assertEqual(how_high(None), -1)


if __name__ == "__main__":
    unittest.main()
