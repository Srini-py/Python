# Compute the running median of a sequence of numbers. 
# That is, given a stream of numbers, 
# print out the median of the list so far on each new element.
#               10
#         5            15
#        3  7      13       18
#                11  14   17  21

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, val):
        if not root:
            return Node(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance < -1 and val > root.right.val:
            return self.leftRotate(root)
        if balance < -1 and val < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        if balance > 1 and val < root.left.val:
            return self.rightRotate(root)
        if balance > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        return root
    
    def createAVLTree(self, array):
        root = None
        for key in array:
            root = self.insert(root, key)
        return root
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def leftRotate(self, root):
        right = root.right
        left_to_the_right = right.left
        right.left = root
        root.right = left_to_the_right
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        right.height = 1 + max(self.getHeight(right.left), self.getHeight(right.right))
        return right
    
    def rightRotate(self, root):
        left = root.left
        right_to_the_left = left.right
        left.right = root
        root.left = right_to_the_left
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        left.height = 1 + max(self.getHeight(left.left), self.getHeight(left.right))
        return left

    def inOrder(self, root, arr):
        if not root:
            return
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        return arr
    
    def findMedian(self, res):
        l = len(res)
        if l % 2:
            print(res[l//2])
        else:
            print(sum(res[l//2 - 1: l//2 + 1])/2)
                

stream = [int(i) for i in input("Enter a stream of space seperated numbers :").split()]

myTree = AVLTree()
root = None
root = myTree.createAVLTree(stream)

res_array = []
res = myTree.inOrder(root, res_array)
print(res)

myTree.findMedian(res)