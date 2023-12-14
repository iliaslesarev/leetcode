def detect_cycle(head):
    if not head:
        return False
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
