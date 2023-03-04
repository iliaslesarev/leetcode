# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode], low: int = -math.inf, high: int = math.inf) -> bool:
            if node is None:
                return True

            if not low < node.val < high:
                return False

            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root)

print(Solution().isValidBST(TreeNode(val=5, left=TreeNode(1), right=TreeNode(val=4, left=TreeNode(3), right=TreeNode(6)))))
print(Solution().isValidBST(TreeNode(val=2, left=TreeNode(1), right=TreeNode(val=3))))
print(Solution().isValidBST(TreeNode(val=5, left=TreeNode(4), right=TreeNode(val=6, left=TreeNode(3), right=TreeNode(7)))))
