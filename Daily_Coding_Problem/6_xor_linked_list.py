# An XOR linked list is a more memory efficient doubly linked list. 
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
# Implement an XOR linked list; 
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

import ctypes


class Node:
	def __init__(self, value):
		self.value = value
		self.npx = 0

		
class XorLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.__nodes = []

	def InsertAtStart(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.head.npx = id(node) ^ self.head.npx
			node.npx = id(self.head)
			self.head = node
		self.__nodes.append(node)

	def InsertAtEnd(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.npx = id(node) ^ self.tail.npx
			node.npx = id(self.tail)
			self.tail = node
		self.__nodes.append(node)

	def DeleteAtStart(self):
		if self.isEmpty():
			return "List is empty !"
		elif self.head == self.tail:
			self.head = self.tail = None
		elif (0 ^ self.head.npx) == id(self.tail):
			self.head = self.tail
			self.head.npx = self.tail.npx = 0
		else:
			res = self.head.value
			x = self.__type_cast(0 ^ self.head.npx)
			y = (id(self.head) ^ x.npx)
			self.head = x
			self.head.npx = 0 ^ y
			return res

	def DeleteAtEnd(self):
		if self.isEmpty():
			return "List is empty !"
		elif self.head == self.tail:
			self.head = self.tail = None
		elif self.__type_cast(0 ^ self.head.npx) == (self.tail):
			self.tail = self.head
			self.head.npx = self.tail.npx = 0
		else:
			prev_id = 0
			node = self.head
			next_id = 1
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
			res = node.value
			x = self.__type_cast(prev_id).npx ^ id(node)
			y = self.__type_cast(prev_id)
			y.npx = x ^ 0
			self.tail = y
			return res

	def Print(self):
		"""We are printing values rather than returning it bacause
		for returning we have to append all values in a list
		and it takes extra memory to save all values in a list."""

		if self.head != None:
			prev_id = 0
			node = self.head
			next_id = 1
			print(node.value, end=' ')
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					print(node.value, end=' ')
				else:
					return
		else:
			print("List is empty !")

	def ReversePrint(self):
		"""We are printing values rather than returning it bacause
		for returning we have to append all values in a list
		and it takes extra memory to save all values in a list."""

		if self.head != None:
			prev_id = 0
			node = self.tail
			next_id = 1
			print(node.value, end=' ')
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					print(node.value, end=' ')
				else:
					return
		else:
			print("List is empty !")

	def Length(self):
		if not self.isEmpty():
			prev_id = 0
			node = self.head
			next_id = 1
			count = 1
			while next_id:
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					count += 1
				else:
					return count
		else:
			return 0

	def PrintByIndex(self, index):
		prev_id = 0
		node = self.head
		for i in range(index):
			next_id = prev_id ^ node.npx

			if next_id:
				prev_id = id(node)
				node = self.__type_cast(next_id)
			else:
				return "Value dosn't found index out of range."
		return node.value

	def isEmpty(self):
		if self.head is None:
			return True
		return False

	def __type_cast(self, id):
		return ctypes.cast(id, ctypes.py_object).value


		

obj = XorLinkedList()

obj.InsertAtEnd(2)
obj.InsertAtEnd(3)
obj.InsertAtEnd(4)
obj.InsertAtStart(0)
obj.InsertAtStart(6)
obj.InsertAtEnd(55)

print("\nLength:", obj.Length())

print("\nTraverse linked list:")
obj.Print()

print("\nTraverse in reverse order:")
obj.ReversePrint()

print('\nNodes:')
for i in range(obj.Length()):
	print("Data value at index", i, 'is', obj.PrintByIndex(i))

print("\nDelete Last Node: ", obj.DeleteAtEnd())
print("\nDelete First Node: ", obj.DeleteAtStart())

print("\nUpdated length:", obj.Length())

print('\nNodes:')
for i in range(obj.Length()):
	print("Data value at index", i, 'is', obj.PrintByIndex(i))

print("\nTraverse linked list:")
obj.Print()

print("\nTraverse in reverse order:")
obj.ReversePrint()
