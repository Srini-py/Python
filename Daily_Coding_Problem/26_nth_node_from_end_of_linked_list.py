# Given a singly linked list and an integer k, remove the kth last element from the list. 
# k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = newNode
            
    def print_node_from_last(self, n):
        ptr1 = self.head
        ptr2 = self.head
        i = 0
        while i < n:
            ptr1 = ptr1.next
            i += 1
        while ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        print(ptr2.val)
        

llist = LinkedList()

llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.insert(40)
llist.insert(50)
llist.insert(60)
llist.insert(70)

llist.print_node_from_last(3)
