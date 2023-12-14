def palindrome(head):
    slow, fast = head, head
    while fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            break

    prev = None
    next = None
    curr = slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    slow = head
    while prev:
        if slow.data != prev.data:
            return False
        slow = slow.next
        prev = prev.next

    return True
