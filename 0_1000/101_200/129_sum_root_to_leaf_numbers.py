from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    common_sum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], stack: List[str] = []):
            stack.append(str(node.val))
            if node.left is not None:
                dfs(node.left, stack)
            if node.right is not None:
                dfs(node.right, stack)

            if node.left is None and node.right is None:
                self.common_sum += int("".join(stack))
            stack.pop()

        dfs(root)
        return self.common_sum


print(Solution().sumNumbers(TreeNode(4, left=TreeNode(9, left=TreeNode(5), right=TreeNode(1)), right=TreeNode(0))))
