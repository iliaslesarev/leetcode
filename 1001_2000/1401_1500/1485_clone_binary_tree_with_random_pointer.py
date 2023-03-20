from typing import Dict, Optional


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    visited: Dict[Node, NodeCopy] = {}

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        if root is None:
            return None
        if self.visited.get(root) is not None:
            return self.visited.get(root)

        self.visited[root] = NodeCopy(root.val)
        self.visited[root].left = self.copyRandomBinaryTree(root.left)
        self.visited[root].right = self.copyRandomBinaryTree(root.right)
        self.visited[root].random = self.copyRandomBinaryTree(root.random)
        return self.visited[root]


first = Node(1)
second = Node(4)
third = Node(7)
first.right = second
second.left = third
second.random = third
third.random = first

res = Solution().copyRandomBinaryTree(first)
a = 4
