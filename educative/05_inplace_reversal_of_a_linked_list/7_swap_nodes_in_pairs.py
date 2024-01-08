class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def create_ll(arr):
    ll = LinkedListNode(arr[0])
    main_pointer = ll
    for el in arr[1:]:
        main_pointer.next = LinkedListNode(el)
        main_pointer = main_pointer.next
    return ll


def swap_nodes(head):
    head = LinkedListNode(0, head)
    curr = head

    while curr.next and curr.next.next:
        first = curr.next
        second = curr.next.next
        after = second.next

        curr.next = second
        second.next = first
        first.next = after

        curr = first

    return head.next


input_list = [1, 2, 3, 4, 5]
input_ll = create_ll(input_list)
output_ll = swap_nodes(input_ll)
a = 4
