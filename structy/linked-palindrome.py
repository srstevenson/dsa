import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def linked_palindrome(head: Node | None) -> bool:
    values: list[int] = []
    while head:
        values.append(head.val)
        head = head.next

    left = 0
    right = len(values) - 1
    while left <= right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    return True


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(3)
        b = Node(2)
        c = Node(7)
        d = Node(7)
        e = Node(2)
        f = Node(3)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertTrue(linked_palindrome(a))

    def test_01(self) -> None:
        a = Node(3)
        b = Node(2)
        c = Node(4)

        a.next = b
        b.next = c

        self.assertFalse(linked_palindrome(a))

    def test_02(self) -> None:
        a = Node(3)
        b = Node(2)
        c = Node(3)

        a.next = b
        b.next = c

        self.assertTrue(linked_palindrome(a))

    def test_03(self) -> None:
        a = Node(0)
        b = Node(1)
        c = Node(0)
        d = Node(1)
        e = Node(0)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertTrue(linked_palindrome(a))

    def test_04(self) -> None:
        a = Node(0)
        b = Node(1)
        c = Node(0)
        d = Node(1)
        e = Node(1)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertFalse(linked_palindrome(a))

    def test_05(self) -> None:
        a = Node(5)

        self.assertTrue(linked_palindrome(a))

    def test_06(self) -> None:
        self.assertTrue(linked_palindrome(None))


if __name__ == "__main__":
    unittest.main()
