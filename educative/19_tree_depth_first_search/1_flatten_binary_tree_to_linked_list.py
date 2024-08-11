# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def flatten_tree(root):
    if not root:
        return None

    current = root

    while current:

        if current.left:
            last = current.left

            while last.right:
                last = last.right

            last.right = current.right
            current.right = current.left
            current.left = None

        current = current.right

    return root

tree = TreeNode(3)

first = TreeNode(2)
second = TreeNode(17)
tree.left = first
tree.right = second

first.left = TreeNode(1)
first.right = TreeNode(4)

second.left = TreeNode(19)
second.right = TreeNode(5)

flatten_tree(tree)
a = 4