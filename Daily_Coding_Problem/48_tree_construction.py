# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def constructTree(preorder, inorder, h, root):
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    root = Node(preorder.pop(0))
    root_index = inorder.index(root.val)
    root.left = constructTree(preorder[:root_index - h], inorder[:root_index], root_index - 1, root.left)
    root.right = constructTree(preorder[root_index:], inorder[root_index + 1:], h - root_index - 1, root.right)
    return root


def preOrder(root):
    if not root:
        return
    print(root.val, end = ' ')
    preOrder(root.left)
    preOrder(root.right)


preorder = input('Enter the preorder traversal of tree: ').split()
inorder = input('Enter the inorder traversal of tree: ').split()
l = len(inorder)

root = constructTree(preorder, inorder, l - 1, None)
preOrder(root)