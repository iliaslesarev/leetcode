from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        amount = 0
        tmp = head
        while tmp is not None:
            amount += 1
            tmp = tmp.next

        tmp = dummy
        for i in range(amount - n):
            tmp = tmp.next
        tmp.next = tmp.next.next

        return dummy.next


print(Solution().removeNthFromEnd(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), n=2))
print(Solution().removeNthFromEnd(ListNode(1), 1))
print(Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 2))
