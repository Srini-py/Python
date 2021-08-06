# Given the root to a binary search tree, find the second largest node in the tree.


def findSecondLargest(root, c = [0]):
    if (not root) or c[0] >= 2:
        return
    findSecondLargest(root.right, c)
    c[0] += 1
    if c[0] == 2:
        print(root.key)
        return
    findSecondLargest(root.left, c)


findSecondLargest(root)