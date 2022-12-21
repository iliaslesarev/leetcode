from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# list1 = ListNode(1, ListNode(2))
list2 = Solution().middleNode(list1)
a = 5
