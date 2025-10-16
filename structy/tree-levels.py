import unittest
from collections import defaultdict, deque


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def tree_levels(root: Node | None) -> list[list[str]]:
    if not root:
        return []

    levels: defaultdict[int, list[str]] = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()
        levels[level].append(node.val)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return list(levels.values())


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def tree_levels_dfs(root: Node | None) -> list[list[str]]:
    if not root:
        return []

    levels: defaultdict[int, list[str]] = defaultdict(list)
    stack = [(root, 0)]
    while stack:
        node, level = stack.pop()
        levels[level].append(node.val)
        if node.right:
            stack.append((node.right, level + 1))
        if node.left:
            stack.append((node.left, level + 1))

    return list(levels.values())


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def tree_levels_recursive(root: Node | None) -> list[list[str]]:
    levels: defaultdict[int, list[str]] = defaultdict(list)

    def _tree_levels(root: Node | None, level: int) -> None:
        if root:
            levels[level].append(root.val)
            if root.left:
                _tree_levels(root.left, level + 1)
            if root.right:
                _tree_levels(root.right, level + 1)

    _tree_levels(root, 0)
    return list(levels.values())


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        for solution in [tree_levels, tree_levels_dfs, tree_levels_recursive]:
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

            self.assertEqual(solution(a), [["a"], ["b", "c"], ["d", "e", "f"]])

    def test_01(self) -> None:
        for solution in [tree_levels, tree_levels_dfs, tree_levels_recursive]:
            a = Node("a")
            b = Node("b")
            c = Node("c")
            d = Node("d")
            e = Node("e")
            f = Node("f")
            g = Node("g")
            h = Node("h")
            i = Node("i")

            a.left = b
            a.right = c
            b.left = d
            b.right = e
            c.right = f
            e.left = g
            e.right = h
            f.left = i

            self.assertEqual(
                solution(a), [["a"], ["b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
            )

    def test_02(self) -> None:
        for solution in [tree_levels, tree_levels_dfs, tree_levels_recursive]:
            q = Node("q")
            r = Node("r")
            s = Node("s")
            t = Node("t")
            u = Node("u")
            v = Node("v")

            q.left = r
            q.right = s
            r.right = t
            t.left = u
            u.right = v

            self.assertEqual(solution(q), [["q"], ["r", "s"], ["t"], ["u"], ["v"]])

    def test_03(self) -> None:
        for solution in [tree_levels, tree_levels_dfs, tree_levels_recursive]:
            self.assertEqual(solution(None), [])


if __name__ == "__main__":
    unittest.main()
