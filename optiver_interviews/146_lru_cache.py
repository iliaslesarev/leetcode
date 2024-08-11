from collections import OrderedDict
from typing import Dict


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache.get(key)

        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache.keys()) > self.capacity:
            self.cache.popitem(False)


class Node:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class MyOrderedDict:
    def __init__(self):
        self.cache: Dict[int, Node] = {}
        self.start = Node(-1, -1)
        self.end = Node(-1, -1)
        self.start.next = self.end
        self.end.prev = self.start

    def __str__(self):
        return str({f"{key}: {value.value}" for key, value in self.cache.items()})

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_end(key)
            return self.cache.get(key).value
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache[key].value = value
            self.move_to_end(key)
        else:
            new_node = Node(key, value, self.end.prev, self.end)
            self.cache[key] = new_node

            self.end.prev.next = self.cache[key]
            self.end.prev = self.cache[key]

    def move_to_end(self, key: int):
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev

        self.end.prev.next = self.cache[key]
        self.cache[key].prev = self.end.prev

        self.end.prev = self.cache[key]
        self.cache[key].next = self.end

    def pop_first(self):
        popping_node = self.start.next
        if popping_node.key in self.cache:
            del self.cache[popping_node.key]

            self.start.next = popping_node.next
            popping_node.next.prev = self.start

    def size(self):
        return len(self.cache.keys())


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: MyOrderedDict = MyOrderedDict()

    def get(self, key: int) -> int:
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        self.cache.put(key, value)
        if self.cache.size() > self.capacity:
            self.cache.pop_first()


commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

lru = None
for i in range(len(commands)):
    if commands[i] == "LRUCache":
        lru = LRUCache(values[i][0])
    elif commands[i] == "put":
        lru.put(values[i][0], values[i][1])
        print(lru.cache)
    elif commands[i] == "get":
        print(lru.get(values[i][0]))
