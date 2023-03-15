from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        children = [root]
        none_founded: bool = False
        while len(children) != 0:
            node = children.pop(0)
            if node is None:
                none_founded = True
            else:
                if none_founded:
                    return False
                children.append(node.left)
                children.append(node.right)
        return True


print(Solution().isCompleteTree(TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3, left=TreeNode(6)))))
