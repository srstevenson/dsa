import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def longest_streak(head: Node | None) -> int:
    longest_streak = 0
    current_streak = 0
    previous_val = None

    while head:
        if head.val == previous_val:
            current_streak += 1
        else:
            current_streak = 1
            previous_val = head.val
        longest_streak = max(current_streak, longest_streak)
        head = head.next

    return longest_streak


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(5)
        b = Node(5)
        c = Node(7)
        d = Node(7)
        e = Node(7)
        f = Node(6)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertEqual(longest_streak(a), 3)

    def test_01(self) -> None:
        a = Node(3)
        b = Node(3)
        c = Node(3)
        d = Node(3)
        e = Node(9)
        f = Node(9)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertEqual(longest_streak(a), 4)

    def test_02(self) -> None:
        a = Node(9)
        b = Node(9)
        c = Node(1)
        d = Node(9)
        e = Node(9)
        f = Node(9)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertEqual(longest_streak(a), 3)

    def test_03(self) -> None:
        a = Node(5)
        b = Node(5)

        a.next = b

        self.assertEqual(longest_streak(a), 2)

    def test_04(self) -> None:
        a = Node(4)

        self.assertEqual(longest_streak(a), 1)

    def test_05(self) -> None:
        self.assertEqual(longest_streak(None), 0)


if __name__ == "__main__":
    unittest.main()
