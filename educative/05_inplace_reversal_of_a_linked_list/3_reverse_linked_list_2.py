class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_list(head, k):
    prev, curr, tail = None, head, None

    for _ in range(k):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev, curr


def reverse_between(head, left, right):
    result = LinkedListNode(0, head)

    curr = result

    for _ in range(left - 1):
        curr = curr.next

    pointer = curr
    reversed_list, tail = reverse_list(pointer.next, right - left + 1)

    end_of_reversed_list = curr.next
    end_of_reversed_list.next = tail
    curr.next = reversed_list

    return result.next


ll = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
ll2 = reverse_between(ll, 1, 3)
a = 4
