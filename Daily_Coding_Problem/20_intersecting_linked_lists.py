# Given two singly linked lists that intersect at some point, 
# find the intersecting node. The lists are non-cyclical.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, node_val):
        newNode = Node(node_val)
        if self.head == None:
            self.head = newNode
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = newNode
        
    def createLinkedList(self, array):
        for i in array:
            self.insert(i)
    

def findLength(llist):
    l = 1
    temp_list = llist.head
    while temp_list.next:
        l += 1
        temp_list = temp_list.next
    return l


def findIntersection(list1, list2):
    l1 = findLength(list1)
    l2 = findLength(list2)
    list1_ptr = list1.head
    list2_ptr = list2.head
    if l1 > l2:
        while l1 - l2 > 0:
            list1_ptr = list1_ptr.next
            l1 -= 1
    else:
        while l2 - l1 > 0:
            list2_ptr = list2_ptr.next
            l2 -= 1
    for i in range(l1):
        if list1_ptr.val == list2_ptr.val:
            print(list1_ptr.val)
            return
        else:
            list1_ptr = list1_ptr.next
            list2_ptr = list2_ptr.next
    print("No intersection nodes")
    return


llist1 = LinkedList()
nodes1 = [int(i) for i in input("Enter space seperated integer nodes for 1st list :").split()]
llist1.createLinkedList(nodes1)

llist2 = LinkedList()
nodes2 = [int(i) for i in input("Enter space seperated integer nodes for 2nd list :").split()]
llist2.createLinkedList(nodes2)

findIntersection(llist1, llist2)
