class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


# 1 -> 5 -> 10 -> 4 -> 7 -> 18 -> 90 -> None
# N = 3
def remove_nth_last_node(head: LinkedListNode, n: int):
    a, b = head, head

    for i in range(n):
        b = b.next

    if b is None:
        return head.next

    while b.next is not None:
        b = b.next
        a = a.next
    a.next = a.next.next

    return head


ll = LinkedList()
ll.create_linked_list([69, 8, 49, 106, 116, 112])
bb = 6
qq = remove_nth_last_node(ll.head, 6)
print(qq)
ee = 5
