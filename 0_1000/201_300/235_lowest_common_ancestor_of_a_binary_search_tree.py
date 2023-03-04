class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node is not None:
            if node.val in [p.val, q.val] or p.val < node.val < q.val or q.val < node.val < p.val:
                return node
            else:
                if p.val < node.val:
                    node = node.left
                else:
                    node = node.right
        return node
