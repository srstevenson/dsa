import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def linked_list_values(head: Node | None) -> list[str]:
    values: list[str] = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(linked_list_values(a), ["a", "b", "c", "d"])

    def test_01(self) -> None:
        x = Node("x")
        y = Node("y")

        x.next = y

        self.assertEqual(linked_list_values(x), ["x", "y"])

    def test_02(self) -> None:
        q = Node("q")

        self.assertEqual(linked_list_values(q), ["q"])

    def test_03(self) -> None:
        self.assertEqual(linked_list_values(None), [])


if __name__ == "__main__":
    unittest.main()
