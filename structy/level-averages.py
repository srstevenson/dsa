import unittest
from collections import defaultdict, deque
from statistics import mean


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def level_averages(root: Node | None) -> list[float]:
    if not root:
        return []

    result: defaultdict[int, list[int]] = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()
        result[level].append(node.val)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return [mean(level) for level in result.values()]


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

        self.assertEqual(level_averages(a), [3, 7.5, 1])

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

        self.assertEqual(level_averages(a), [5, 32.5, 17.5, 2])

    def test_02(self) -> None:
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(0)
        f = Node(45)
        g = Node(-1)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(level_averages(a), [-1, -5.5, 14, -1.5])

    def test_03(self) -> None:
        q = Node(13)
        r = Node(4)
        s = Node(2)
        t = Node(9)
        u = Node(2)
        v = Node(42)

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        self.assertEqual(level_averages(q), [13, 3, 9, 2, 42])

    def test_04(self) -> None:
        self.assertEqual(level_averages(None), [])


if __name__ == "__main__":
    unittest.main()
