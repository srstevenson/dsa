import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def sum_list(head: Node | None) -> int:
    total = 0
    current = head
    while current:
        total += current.val
        current = current.next
    return total


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(2)
        b = Node(8)
        c = Node(3)
        d = Node(-1)
        e = Node(7)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertEqual(sum_list(a), 19)

    def test_01(self) -> None:
        x = Node(38)
        y = Node(4)

        x.next = y

        self.assertEqual(sum_list(x), 42)

    def test_02(self) -> None:
        z = Node(100)

        self.assertEqual(sum_list(z), 100)

    def test_03(self) -> None:
        self.assertEqual(sum_list(None), 0)


if __name__ == "__main__":
    unittest.main()
