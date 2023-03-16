from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            root = TreeNode(val=postorder.pop())

            i = indexes[root.val]
            root.right = helper(i + 1, end)
            root.left = helper(start, i - 1)
            return root

        indexes = {v: i for i, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


a = Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
