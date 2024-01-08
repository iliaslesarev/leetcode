class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reorder_list(head):
    # find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    prev, curr = None, slow
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    # creating result
    first, second = head, prev

    while second.next:
        tmp = first.next
        first.next = second
        first = tmp

        tmp2 = second.next
        second.next = first
        second = tmp2

    return head


ll = LinkedListNode(1, LinkedListNode(1, LinkedListNode(2, LinkedListNode(2, LinkedListNode(3, LinkedListNode(-1, LinkedListNode(10, LinkedListNode(12))))))))
# ll = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
# ll = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4))))
l2 = reorder_list(ll)
a = 4
