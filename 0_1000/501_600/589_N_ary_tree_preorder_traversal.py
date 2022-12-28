from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []
        result: List[int] = []
        stack: List[Node] = [root]
        while len(stack) != 0:
            node: Node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
        return result


root: Node = Node(1, [Node(3, [Node(5, None), Node(6, None)]), Node(2, None), Node(4, None)])
print(Solution().preorder(root))
