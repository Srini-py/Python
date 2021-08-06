# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

'''
def check_unival(root, val):
    if root is None:
        return True
    if root.val == val:
        return check_unival(root.left, val) and check_unival(root.right, val)
    return False


def is_unival(root):
    return check_unival(root, root.val)


def count_unival_trees(root):x
    if root is None:
        return 0
    left = count_unival_trees(root.left)
    right = count_unival_trees(root.right)
    return 1 + left + right if is_unival(root) else left + right
'''


def helper(root):
    if root is None:
        return 0, True
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
        if root.left is not None and root.val != root.left.val:
            return total_count, False
        if root.right is not None and root.val != root.right.val:
            return total_count, False
        return total_count + 1, True
    return total_count, False


def count_unival_trees(root):
    count, _ = helper(root)
    return count