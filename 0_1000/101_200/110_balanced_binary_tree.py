from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass


print(Solution().isBalanced(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)), TreeNode(3, TreeNode(6)))))

"""
    1
  2   3
 4 5 6 None
8
"""
