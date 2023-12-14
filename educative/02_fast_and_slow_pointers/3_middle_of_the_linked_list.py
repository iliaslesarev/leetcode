def get_middle_node(head):
    if not head.next:
        return head
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
