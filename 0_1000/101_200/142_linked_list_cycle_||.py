# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional, Dict


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                break

        if hare is not None and hare.next is not None:
            tortoise = head
            while tortoise != hare:
                tortoise = tortoise.next
                hare = hare.next
            return tortoise
        return None


# first = ListNode(3)
# second = ListNode(2)
# first.next = second
# third = ListNode(0)
# second.next = third
# fourth = ListNode(-4)
# third.next = fourth
# fourth.next = second
node0 = ListNode(1)
node1 = ListNode(2)
node0.next = node1
node1.next = node0

a = Solution().detectCycle(ListNode(1))
