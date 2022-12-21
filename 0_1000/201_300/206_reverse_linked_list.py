from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None

        while head:
            tmp = head.next
            head.next = res
            res = head
            head = tmp

        return res


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list2 = Solution().reverseList(list1)
a = 5
