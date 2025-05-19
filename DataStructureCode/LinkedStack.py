from DataStructureCode.SimpleLinkedList import *

class LinkedStack:
	def __init__(self):
		self.stack = SimpleLinkedList()

	def push(self, x):
		self.stack.insert(0, x)

	def pop(self):
		return self.stack.pop(0)

	def top(self):
		if self.isEmpty():
			return None
		else:
			return self.stack.get(0)

	def isEmpty(self) -> bool:
		return self.stack.isEmpty()

	def size(self):
		return self.stack.size()

	def printStack(self):
		print("Elements from top to bottom: ", end=" ")
		for i in range(self.stack.size()):
			print(self.stack.get(i), end=" ")

