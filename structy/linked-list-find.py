import unittest


class Node:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def linked_list_find(head: Node, target: int | str) -> bool:
    current = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertTrue(linked_list_find(a, "c"))

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertTrue(linked_list_find(a, "d"))

    def test_02(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertFalse(linked_list_find(a, "q"))

    def test_03(self) -> None:
        node1 = Node("jason")
        node2 = Node("leneli")

        node1.next = node2

        self.assertTrue(linked_list_find(node1, "jason"))

    def test_04(self) -> None:
        node1 = Node(42)

        self.assertTrue(linked_list_find(node1, 42))

    def test_05(self) -> None:
        node1 = Node(42)

        self.assertFalse(linked_list_find(node1, 100))


if __name__ == "__main__":
    unittest.main()
