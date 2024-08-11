# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter_helper(node, diameter):
    if node is None:
        return 0, diameter

    lh, diameter = diameter_helper(node.left, diameter)
    rh, diameter = diameter_helper(node.right, diameter)

    diameter = max(diameter, lh + rh)

    return max(lh, rh) + 1, diameter


def diameter_of_binaryTree(root):
    diameter = 0
    if not root:
        return diameter

    _, diameter = diameter_helper(root, diameter)

    return diameter


tree = TreeNode(3)

first = TreeNode(2)
second = TreeNode(17)
tree.left = first
tree.right = second

first.left = TreeNode(1)
first.right = TreeNode(4)

second.left = TreeNode(19)
second.right = TreeNode(5)

diameter_of_binaryTree(tree)
a = 4
