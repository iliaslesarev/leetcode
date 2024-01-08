# Template for linked list node class

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_list(head, k):
    prev, curr, tail = None, head, None

    for i in range(k):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev, curr


def reverse_k_groups(head, k):
    result = LinkedListNode(0, head)
    pointer = result

    while pointer is not None:

        cursor = pointer
        for i in range(k):
            cursor = cursor.next
            if cursor is None:
                break

        if cursor is None:
            break

        reversed_list, tail = reverse_list(pointer.next, k)

        end_of_reversed_list = pointer.next
        end_of_reversed_list.next = tail
        pointer.next = reversed_list
        pointer = end_of_reversed_list

    return result.next


ll = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4))))
fl = reverse_k_groups(head=ll, k=2)
a = 4
