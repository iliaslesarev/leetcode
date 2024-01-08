class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def swap_nodes(head, k):
    pointer1, pointer2 = head, None
    i = 1
    first = None

    while pointer1:
        if pointer2:
            pointer2 = pointer2.next
        if i == k:
            first = pointer1
            pointer2 = head
        pointer1 = pointer1.next
        i += 1

    tmp = first.data
    first.data = pointer2.data
    pointer2.data = tmp

    return head

ll = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
swap_nodes(ll, 2)
a = 4