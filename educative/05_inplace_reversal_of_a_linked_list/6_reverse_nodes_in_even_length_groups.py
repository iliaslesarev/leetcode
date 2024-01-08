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


def reverse_list(head, k):
    prev, curr, tail = None, head, None

    i = 0
    while i < k and curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
        i += 1

    tail = curr
    return prev, tail


def reverse_even_length_groups(head):
    counter = 2
    main_pointer = head
    while main_pointer.next:

        check_pointer = main_pointer
        i = 0
        while i < counter:
            if check_pointer.next is None:
                break
            check_pointer = check_pointer.next
            i += 1

        if i % 2 == 0:
            reversed_list, tail = reverse_list(main_pointer.next, counter)
            end_of_group = main_pointer.next
            end_of_group.next = tail
            main_pointer.next = reversed_list
            main_pointer = end_of_group
        else:
            main_pointer = check_pointer

        counter += 1

    return head


input_list = [1, 2, 3, 4, 5, 6, 7, 8]
input_ll = create_ll(input_list)
output_ll = reverse_even_length_groups(input_ll)
a = 4
