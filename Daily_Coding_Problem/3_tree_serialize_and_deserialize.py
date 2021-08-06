# Given the root to a binary tree, implement
# serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        

def serialize(tree):
    str_arr = []
    def serializer(node):
        if node == None:
            str_arr.append('None')
            return
        str_arr.append(node.val)
        serializer(node.left)
        serializer(node.right)
    serializer(tree)
    return ','.join(str_arr)


def deserialize(string):
    values = iter(string.split(','))
    def deserializer():
        val = next(values)
        if val == 'None':
            return None
        tree = Node(val)
        tree.left = deserializer()
        tree.right = deserializer()
        return tree
    return deserializer()

        
node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'