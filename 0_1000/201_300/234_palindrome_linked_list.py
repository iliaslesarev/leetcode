from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        previous = None
        while slow is not None:
            next_node = slow.next
            slow.next = previous
            previous = slow
            slow = next_node

        while previous is not None:
            if head.val != previous.val:
                return False
            head = head.next
            previous = previous.next

        return True


print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(Solution().isPalindrome(ListNode(1, ListNode(0, ListNode(1)))))
